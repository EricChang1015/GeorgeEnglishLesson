(function () {
  const L = window.LESSON;
  if (!L) return;

  const ASSET = L.asset;
  const STORAGE_KEY = L.storageKey;
  const ROLE_LABEL = L.roleLabel || {};
  const vocab = L.vocab || [];
  const story = L.story || [];
  const quizPool = L.quiz || [];
  const phrases = L.phrases || [];
  const videoPages = L.videoPages || null;
  const videoDir = L.videoDir || "video/";
  const LETTERS = ["A", "B", "C"];

  function shufflePick(items, n) {
    const idx = items.map((_, i) => i);
    for (let i = idx.length - 1; i > 0; i -= 1) {
      const j = Math.floor(Math.random() * (i + 1));
      const tmp = idx[i];
      idx[i] = idx[j];
      idx[j] = tmp;
    }
    const take = Math.min(Math.max(1, n), items.length);
    return idx.slice(0, take).map((poolIndex) => ({
      ...items[poolIndex],
      poolIndex
    }));
  }

  const quizPick = Number(L.quizPick);
  const quiz = (quizPick > 0 && quizPick < quizPool.length)
    ? shufflePick(quizPool, quizPick)
    : quizPool.map((item, poolIndex) => ({ ...item, poolIndex }));

  const screens = [...document.querySelectorAll(".screen")];
  let current = 0;
  let quizIndex = 0;
  const quizChosen = quiz.map(() => null);
  let autoMode = false;
  let audioPlayer = new Audio();
  let playToken = 0;
  let slideDir = "next";
  const preloaded = new Set();

  function esc(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));
  }

  function displayName(name) {
    return String(name || "").replace(/\.(png|webp)$/i, "");
  }

  function webpSrc(name) {
    return ASSET + displayName(name) + ".webp";
  }

  function imgTag(name, className, alt) {
    return `<img class="${className}" data-src="${esc(webpSrc(name))}" alt="${esc(alt || "")}" />`;
  }

  function hasVideoFor(name) {
    if (!videoPages) return false;
    const base = displayName(name);
    return videoPages.some((v) => displayName(v) === base);
  }

  function videoSrc(name) {
    return ASSET + videoDir + displayName(name) + ".mp4";
  }

  function videoTag(name, className, alt) {
    const poster = esc(webpSrc(name));
    const src = esc(videoSrc(name));
    return `<div class="video-wrap">
      <video class="${className}" muted loop playsinline poster="${poster}"
        data-video-base="${esc(displayName(name))}" data-fallback-alt="${esc(alt || "")}">
        <source src="${src}" type="video/mp4" />
      </video>
    </div>`;
  }

  function mediaTag(name, className, alt) {
    if (hasVideoFor(name)) return videoTag(name, className, alt);
    return imgTag(name, className, alt);
  }

  function hydrateImages(root) {
    if (!root) return;
    root.querySelectorAll("img[data-src]").forEach((img) => {
      if (img.dataset.hydrated === "1") return;
      img.dataset.hydrated = "1";
      img.classList.add("is-loading");
      img.onload = () => {
        img.classList.remove("is-loading");
        img.classList.add("loaded");
      };
      img.src = img.dataset.src;
    });
  }

  function fallbackVideoToImage(video) {
    if (video.dataset.fallbackDone === "1") return;
    video.dataset.fallbackDone = "1";
    const base = video.dataset.videoBase;
    const alt = video.dataset.fallbackAlt || "";
    const wrap = video.closest(".video-wrap");
    const img = document.createElement("img");
    img.className = "hero";
    img.dataset.src = ASSET + base + ".webp";
    img.alt = alt;
    if (wrap) wrap.replaceChildren(img);
    else video.replaceWith(img);
    hydrateImages(wrap || video.parentElement);
  }

  function hydrateVideos(root) {
    if (!root) return;
    root.querySelectorAll("video.hero[data-video-base]").forEach((video) => {
      if (video.dataset.hydrated === "1") return;
      video.dataset.hydrated = "1";
      video.addEventListener("error", () => fallbackVideoToImage(video), { once: true });
      const playAttempt = video.play();
      if (playAttempt && typeof playAttempt.catch === "function") {
        playAttempt.catch(() => { /* autoplay blocked until gesture */ });
      }
    });
  }

  function syncStoryVideos(root, playing) {
    if (!root) return;
    root.querySelectorAll("video.hero").forEach((video) => {
      if (playing) {
        const p = video.play();
        if (p && typeof p.catch === "function") p.catch(() => {});
      } else {
        video.pause();
      }
    });
  }

  function preloadSrc(src) {
    if (!src || preloaded.has(src)) return;
    preloaded.add(src);
    const probe = new Image();
    probe.src = src;
  }

  function preloadScreen(index) {
    const sec = screens[index];
    if (!sec) return;
    sec.querySelectorAll("img[data-src]").forEach((img) => preloadSrc(img.dataset.src));
    if (sec.dataset.story != null) {
      const page = story[Number(sec.dataset.story)];
      if (page) preloadSrc(webpSrc(page.img));
    }
  }

  function stopAudio() {
    playToken += 1;
    audioPlayer.pause();
    audioPlayer.removeAttribute("src");
    try { audioPlayer.load(); } catch (_) { /* ignore */ }
    document.querySelectorAll(".playing").forEach((el) => el.classList.remove("playing"));
  }

  function playSrc(src, onEnd, highlightEl) {
    const token = ++playToken;
    document.querySelectorAll(".playing").forEach((el) => el.classList.remove("playing"));
    if (highlightEl) highlightEl.classList.add("playing");
    audioPlayer.pause();
    audioPlayer.src = ASSET + src;
    const done = () => {
      if (token !== playToken) return;
      document.querySelectorAll(".playing").forEach((el) => el.classList.remove("playing"));
      if (onEnd) onEnd();
    };
    audioPlayer.onended = done;
    audioPlayer.onerror = done;
    return audioPlayer.play().catch(done);
  }

  function playSequence(srcs, highlightEl, onEnd) {
    stopAudio();
    if (highlightEl) highlightEl.classList.add("playing");
    let i = 0;
    const next = () => {
      if (i >= srcs.length) {
        if (highlightEl) highlightEl.classList.remove("playing");
        if (onEnd) onEnd();
        return;
      }
      const src = srcs[i++];
      playSrc(src, next, highlightEl);
    };
    next();
  }

  function playLineEl(lineEl) {
    stopAuto({ silent: true });
    stopAudio();
    const screenEl = lineEl.closest(".screen");
    syncStoryVideos(screenEl, true);
    playSrc(lineEl.dataset.audio, null, lineEl);
  }

  function readPage(screenEl, onEnd) {
    const lines = [...screenEl.querySelectorAll(".line")];
    if (!lines.length) {
      if (onEnd) onEnd();
      return;
    }
    stopAudio();
    syncStoryVideos(screenEl, true);
    let i = 0;
    const next = () => {
      if (i >= lines.length) {
        if (onEnd) onEnd();
        return;
      }
      const el = lines[i];
      document.querySelectorAll(".playing").forEach((n) => n.classList.remove("playing"));
      el.classList.add("playing");
      el.scrollIntoView({ behavior: "smooth", block: "nearest" });
      playSrc(el.dataset.audio, () => { i += 1; next(); }, el);
    };
    next();
  }

  function voiceKeyHtml() {
    return `<div class="voice-key">${
      Object.keys(ROLE_LABEL).map((role) =>
        `<span class="${esc(role)}">${esc(ROLE_LABEL[role])}</span>`
      ).join("")
    }</div>`;
  }

  function buildStoryScreens() {
    document.querySelectorAll("[data-story]").forEach((sec) => {
      const i = Number(sec.dataset.story);
      const page = story[i];
      if (!page) return;
      const linesHtml = page.lines.map((line) => `
        <button class="line ${esc(line.role)}" type="button" data-audio="${esc(line.audio)}">
          <span class="who">${esc(ROLE_LABEL[line.role] || line.role)}</span>
          ${esc(line.text)}
        </button>
      `).join("");
      sec.innerHTML = `
        <div class="page-meta">Story ${i + 1} / ${story.length}</div>
        ${mediaTag(page.img, "hero", page.alt)}
        ${voiceKeyHtml()}
        <div class="lines">${linesHtml}</div>
        <p class="hint">Tap a line for AI voice · or Read the page · swipe to turn</p>
        <div class="controls">
          <button class="btn-ghost" type="button" data-prev>◀ Back</button>
          <button class="btn-secondary" type="button" data-read-page>🔊 Read page</button>
          <button class="btn-primary" type="button" data-next>Next ▶</button>
        </div>
      `;
    });
  }

  function buildVocab() {
    const grid = document.getElementById("vocabGrid");
    if (!grid) return;
    grid.innerHTML = vocab.map((v, i) => `
      <button class="vocab-card" type="button" data-vocab-index="${i}">
        ${imgTag(v.img, "", v.alt)}
        <div class="label">${esc(v.word)}</div>
        <div class="example">${esc(v.example)}</div>
      </button>
    `).join("");
  }

  function quizAudio(index) {
    const poolIndex = quiz[index] && quiz[index].poolIndex != null ? quiz[index].poolIndex : index;
    const nn = String(poolIndex + 1).padStart(2, "0");
    return {
      q: `audio/quiz-${nn}.mp3`,
      opts: LETTERS.map((_, oi) => `audio/quiz-${nn}-${"abc"[oi]}.mp3`),
      choose: "audio/quiz-choose.mp3"
    };
  }

  function isQuizScreen(index) {
    const sec = screens[index];
    return !!(sec && sec.querySelector("#quizArea"));
  }

  function isVocabScreen(index) {
    const sec = screens[index];
    return !!(sec && sec.querySelector("#vocabGrid"));
  }

  function isPhrasesScreen(index) {
    const sec = screens[index];
    return !!(sec && sec.querySelector("#sightGrid"));
  }

  function isNotesScreen(index) {
    const sec = screens[index];
    return !!(sec && sec.querySelector("#notesForm"));
  }

  function isCoverScreen(index) {
    return index === 0;
  }

  function isStoryScreen(index) {
    const sec = screens[index];
    return !!(sec && sec.dataset.story != null);
  }

  function allQuizAnswered() {
    return quizChosen.every((v) => v != null);
  }

  function renderQuizQuestion() {
    const area = document.getElementById("quizArea");
    if (!area || !quiz.length) return;
    const item = quiz[quizIndex];
    const chosen = quizChosen[quizIndex];
    const locked = chosen != null;
    area.innerHTML = `
      <div class="quiz-item" data-qi="${quizIndex}">
        <div class="page-meta">Question ${quizIndex + 1} / ${quiz.length}</div>
        <h3>${esc(item.q)}</h3>
        <div class="controls" style="margin-bottom:8px;">
          <button class="btn-secondary" type="button" data-read-quiz>🔊 Read question</button>
        </div>
        <p class="hint">${locked ? "You already answered this one" : "Tap Read, then choose A, B or C"}</p>
        <div class="quiz-options">
          ${item.options.map((opt, oi) => `
            <button type="button" class="quiz-opt" data-oi="${oi}" disabled>
              <span class="opt-letter">${LETTERS[oi] || oi + 1}</span>
              <span>${esc(opt)}</span>
            </button>
          `).join("")}
        </div>
        <p class="feedback" id="quizFb"></p>
      </div>
    `;
    if (locked) {
      const wrap = area.querySelector(".quiz-item");
      wrap.querySelectorAll(".quiz-opt").forEach((btn) => {
        const oi = Number(btn.dataset.oi);
        btn.disabled = true;
        if (oi === item.answer) btn.classList.add("correct");
        if (oi === chosen && chosen !== item.answer) btn.classList.add("wrong");
      });
      const fb = document.getElementById("quizFb");
      if (chosen === item.answer) {
        fb.textContent = "Great job! ⭐";
        fb.className = "feedback good";
      } else {
        fb.textContent = "Nice try! Let's learn it.";
        fb.className = "feedback bad";
      }
    }
    updateQuizNextBtn();
  }

  function enableQuizOptions() {
    const area = document.getElementById("quizArea");
    if (!area || quizChosen[quizIndex] != null) return;
    area.querySelectorAll(".quiz-opt").forEach((btn) => { btn.disabled = false; });
  }

  function readQuiz(onEnd) {
    const item = quiz[quizIndex];
    if (!item) {
      if (onEnd) onEnd();
      return;
    }
    const files = quizAudio(quizIndex);
    stopAudio();
    const steps = [
      { src: files.q, el: document.querySelector(".quiz-item h3") },
      ...files.opts.map((src, oi) => ({
        src,
        el: document.querySelector(`.quiz-opt[data-oi="${oi}"]`)
      })),
      { src: files.choose, el: null }
    ];
    let i = 0;
    const next = () => {
      if (i >= steps.length) {
        enableQuizOptions();
        if (onEnd) onEnd();
        return;
      }
      const step = steps[i++];
      playSrc(step.src, next, step.el);
    };
    next();
  }

  function answerQuiz(oi) {
    if (quizChosen[quizIndex] != null) return;
    const item = quiz[quizIndex];
    const area = document.getElementById("quizArea");
    const wrap = area && area.querySelector(".quiz-item");
    if (!wrap) return;
    quizChosen[quizIndex] = oi;
    wrap.querySelectorAll(".quiz-opt").forEach((b) => { b.disabled = true; });
    const picked = wrap.querySelector(`.quiz-opt[data-oi="${oi}"]`);
    const correctBtn = wrap.querySelector(`.quiz-opt[data-oi="${item.answer}"]`);
    const fb = document.getElementById("quizFb");
    const good = oi === item.answer;
    if (picked) picked.classList.add(good ? "correct" : "wrong");
    if (!good && correctBtn) correctBtn.classList.add("correct");
    if (fb) {
      fb.textContent = good ? "Great job! ⭐" : "Nice try! Let's learn it.";
      fb.className = "feedback " + (good ? "good" : "bad");
    }
    updateQuizNextBtn();
    const praise = good ? "audio/praise-great.mp3" : "audio/praise-try.mp3";
    playSrc(praise, () => {
      if (!autoMode) return;
      afterQuizAnswerAuto();
    });
  }

  function afterQuizAnswerAuto() {
    if (!autoMode) return;
    if (quizIndex < quiz.length - 1) {
      quizIndex += 1;
      renderQuizQuestion();
      readQuiz();
      return;
    }
    autoAdvance();
  }

  function buildPhrases() {
    const grid = document.getElementById("sightGrid");
    const fb = document.getElementById("sightFeedback");
    if (!grid) return;
    let count = 0;
    grid.innerHTML = phrases.map((p) => `
      <button class="sight-word" type="button" data-audio="${esc(p.audio)}">${esc(p.text)}</button>
    `).join("");
    grid.querySelectorAll("[data-audio]").forEach((btn) => {
      btn.addEventListener("click", () => {
        stopAuto({ silent: true });
        stopAudio();
        btn.classList.add("playing");
        playSrc(btn.dataset.audio, () => btn.classList.remove("playing"), btn);
        if (!btn.classList.contains("done")) {
          btn.classList.add("done");
          count += 1;
          if (fb) {
            fb.textContent = count >= phrases.length ? "You did it! 🎉" : `Nice! ${count}/${phrases.length}`;
            fb.className = "feedback good";
          }
        }
      });
    });
  }

  function pageLabel(sec, i) {
    if (sec.dataset.story != null) return `Story ${Number(sec.dataset.story) + 1}`;
    if (sec.querySelector("#quizArea")) return "Quiz";
    if (sec.querySelector("#sightGrid")) return "Phrases";
    if (sec.querySelector("#notesForm")) return "Notes";
    if (sec.querySelector("#vocabGrid")) return "New Words";
    if (i === 0) return "Cover";
    return `Page ${i + 1}`;
  }

  function installChrome() {
    const header = document.querySelector("header.top");
    if (!header || document.getElementById("pageJump")) return;
    const nav = header.querySelector(".nav-links");
    const toolbar = document.createElement("div");
    toolbar.className = "toolbar";
    toolbar.innerHTML = `
      <label class="jump">Go to
        <select id="pageJump" aria-label="Jump to page"></select>
      </label>
      <button type="button" id="autoReadBtn" class="btn-auto">▶ Auto read</button>
    `;
    if (nav) header.insertBefore(toolbar, nav);
    else header.appendChild(toolbar);

    const jump = document.getElementById("pageJump");
    jump.innerHTML = screens.map((sec, i) =>
      `<option value="${i}">${esc(pageLabel(sec, i))}</option>`
    ).join("");
    jump.addEventListener("change", () => {
      showScreen(Number(jump.value));
    });
    document.getElementById("autoReadBtn").addEventListener("click", toggleAuto);

    const coverControls = document.querySelector('[data-screen="0"] .controls');
    if (coverControls && !coverControls.querySelector("[data-auto-start]")) {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "btn-good";
      btn.dataset.autoStart = "1";
      btn.textContent = "▶ Auto read";
      coverControls.appendChild(btn);
    }

    screens.forEach((sec) => {
      if (sec.querySelector(".swipe-hint") || sec.querySelector("#notesForm")) return;
      const hint = document.createElement("p");
      hint.className = "swipe-hint";
      hint.textContent = "Swipe or use Go to page";
      sec.appendChild(hint);
    });
  }

  function updateJump() {
    const jump = document.getElementById("pageJump");
    if (jump && Number(jump.value) !== current) jump.value = String(current);
  }

  function updateAutoBtn() {
    const btn = document.getElementById("autoReadBtn");
    if (!btn) return;
    btn.classList.toggle("on", autoMode);
    btn.textContent = autoMode ? "⏹ Stop auto" : "▶ Auto read";
  }

  function updateHash() {
    const sec = screens[current];
    let hash = `#p=${current}`;
    if (sec && sec.dataset.story != null) hash = `#story=${Number(sec.dataset.story) + 1}`;
    else if (isQuizScreen(current)) hash = "#quiz";
    else if (isVocabScreen(current)) hash = "#words";
    else if (isPhrasesScreen(current)) hash = "#phrases";
    else if (isNotesScreen(current)) hash = "#notes";
    else if (isCoverScreen(current)) hash = "#cover";
    if (location.hash !== hash) history.replaceState(null, "", hash);
  }

  function clampScreen(n) {
    if (Number.isNaN(n)) return 0;
    return Math.max(0, Math.min(screens.length - 1, n));
  }

  function parseStartPage() {
    const params = new URLSearchParams(location.search);
    const qPage = params.get("page");
    if (qPage != null && qPage !== "") {
      const n = Number(qPage);
      if (!Number.isNaN(n)) return clampScreen(n);
    }
    const hash = (location.hash || "").replace(/^#/, "").toLowerCase();
    if (!hash) return 0;
    const storyMatch = hash.match(/^story=(\d+)/);
    if (storyMatch) {
      const n = Number(storyMatch[1]) - 1;
      const idx = screens.findIndex((s) => s.dataset.story === String(n));
      return idx >= 0 ? idx : 0;
    }
    const pMatch = hash.match(/^p=(\d+)/) || hash.match(/^page=(\d+)/);
    if (pMatch) return clampScreen(Number(pMatch[1]));
    if (hash === "cover") return 0;
    if (hash === "words" || hash === "vocab") {
      const idx = screens.findIndex((s) => s.querySelector("#vocabGrid"));
      return idx >= 0 ? idx : 1;
    }
    if (hash === "quiz") {
      const idx = screens.findIndex((s) => s.querySelector("#quizArea"));
      return idx >= 0 ? idx : 10;
    }
    if (hash === "phrases") {
      const idx = screens.findIndex((s) => s.querySelector("#sightGrid"));
      return idx >= 0 ? idx : 11;
    }
    if (hash === "notes") {
      const idx = screens.findIndex((s) => s.querySelector("#notesForm"));
      return idx >= 0 ? idx : screens.length - 1;
    }
    return 0;
  }

  function updateProgress() {
    const bar = document.getElementById("progressBar");
    if (!bar) return;
    bar.style.width = ((current / Math.max(screens.length - 1, 1)) * 100) + "%";
  }

  function showScreen(index, opts) {
    opts = opts || {};
    const fromAuto = !!opts.fromAuto;
    if (!fromAuto) stopAuto({ silent: true });
    stopAudio();
    const next = Math.max(0, Math.min(screens.length - 1, index));
    if (next !== current) {
      slideDir = next > current ? "next" : "prev";
    }
    current = next;
    screens.forEach((s, i) => {
      const on = i === current;
      s.classList.toggle("active", on);
      s.hidden = !on;
      s.classList.remove("slide-next", "slide-prev");
    });
    const active = screens[current];
    active.classList.add(slideDir === "prev" ? "slide-prev" : "slide-next");
    hydrateImages(active);
    hydrateVideos(active);
    if (isStoryScreen(current)) syncStoryVideos(active, autoMode);
    preloadScreen(current + 1);
    updateProgress();
    updateJump();
    updateHash();
    window.scrollTo({ top: 0, behavior: "smooth" });
    if (isQuizScreen(current)) renderQuizQuestion();
  }

  function updateQuizNextBtn() {
    const nextBtn = document.getElementById("quizNext");
    if (!nextBtn) return;
    const answered = quizChosen[quizIndex] != null;
    nextBtn.disabled = !answered;
    nextBtn.textContent = (quizIndex < quiz.length - 1) ? "Next question ▶" : "Next ▶";
  }

  function canLeaveQuizForward() {
    if (!isQuizScreen(current)) return true;
    return quizChosen[quizIndex] != null;
  }

  function goNext() {
    stopAuto({ silent: true });
    if (isQuizScreen(current)) {
      if (quizChosen[quizIndex] == null) return;
      if (quizIndex < quiz.length - 1) {
        quizIndex += 1;
        renderQuizQuestion();
        return;
      }
      if (!allQuizAnswered()) return;
    }
    if (current >= screens.length - 1) return;
    showScreen(current + 1);
  }

  function goPrev() {
    stopAuto({ silent: true });
    if (isQuizScreen(current) && quizIndex > 0) {
      quizIndex -= 1;
      renderQuizQuestion();
      return;
    }
    if (current <= 0) return;
    showScreen(current - 1);
  }

  function stopAuto(opts) {
    opts = opts || {};
    if (!autoMode) return;
    autoMode = false;
    updateAutoBtn();
    if (!opts.silent) stopAudio();
  }

  function toggleAuto() {
    if (autoMode) {
      stopAuto();
      return;
    }
    startAuto();
  }

  function startAuto() {
    autoMode = true;
    updateAutoBtn();
    stopAudio();
    runAutoForCurrentScreen();
  }

  function autoAdvance() {
    if (!autoMode) return;
    if (current >= screens.length - 1 || isNotesScreen(current)) {
      stopAuto({ silent: true });
      return;
    }
    const nextIndex = current + 1;
    setTimeout(() => {
      if (!autoMode) return;
      showScreen(nextIndex, { fromAuto: true });
      runAutoForCurrentScreen();
    }, 450);
  }

  function runAutoForCurrentScreen() {
    if (!autoMode) return;
    if (isCoverScreen(current)) {
      playSrc("audio/title.mp3", () => { if (autoMode) autoAdvance(); });
      return;
    }
    if (isVocabScreen(current)) {
      hydrateImages(screens[current]);
      const cards = [...document.querySelectorAll("[data-vocab-index]")];
      let i = 0;
      const next = () => {
        if (!autoMode) return;
        if (i >= cards.length) {
          autoAdvance();
          return;
        }
        const card = cards[i++];
        const item = vocab[Number(card.dataset.vocabIndex)];
        card.scrollIntoView({ behavior: "smooth", block: "nearest" });
        playSequence([item.audio, item.exampleAudio], card, next);
      };
      next();
      return;
    }
    if (isStoryScreen(current)) {
      readPage(screens[current], () => { if (autoMode) autoAdvance(); });
      return;
    }
    if (isQuizScreen(current)) {
      quizIndex = quizChosen.findIndex((v) => v == null);
      if (quizIndex < 0) {
        autoAdvance();
        return;
      }
      renderQuizQuestion();
      readQuiz();
      return;
    }
    if (isPhrasesScreen(current)) {
      const btns = [...document.querySelectorAll("#sightGrid [data-audio]")];
      let i = 0;
      const next = () => {
        if (!autoMode) return;
        if (i >= btns.length) {
          autoAdvance();
          return;
        }
        const btn = btns[i++];
        btn.classList.add("done");
        playSrc(btn.dataset.audio, next, btn);
      };
      next();
      return;
    }
    stopAuto({ silent: true });
  }

  function loadNotes() {
    try {
      const data = JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
      document.querySelectorAll("[data-note]").forEach((cb) => {
        cb.checked = !!data[cb.dataset.note];
      });
      const comment = document.getElementById("noteComment");
      if (comment) comment.value = data.comment || "";
    } catch (_) { /* ignore */ }
  }

  function saveNotes() {
    const comment = document.getElementById("noteComment");
    const data = { comment: comment ? comment.value : "" };
    document.querySelectorAll("[data-note]").forEach((cb) => {
      data[cb.dataset.note] = cb.checked;
    });
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    const msg = document.getElementById("saveMsg");
    if (!msg) return;
    msg.textContent = "Saved on this device ✓";
    setTimeout(() => { msg.textContent = ""; }, 2500);
  }

  function bindNotes() {
    const saveBtn = document.getElementById("saveNotes");
    const clearBtn = document.getElementById("clearNotes");
    if (saveBtn) saveBtn.addEventListener("click", saveNotes);
    if (clearBtn) {
      clearBtn.addEventListener("click", () => {
        localStorage.removeItem(STORAGE_KEY);
        document.querySelectorAll("[data-note]").forEach((cb) => { cb.checked = false; });
        const comment = document.getElementById("noteComment");
        if (comment) comment.value = "";
        const msg = document.getElementById("saveMsg");
        if (msg) msg.textContent = "Cleared";
      });
    }
  }

  function bindClicks() {
    document.addEventListener("click", (e) => {
      const autoStart = e.target.closest("[data-auto-start]");
      if (autoStart) {
        startAuto();
        return;
      }

      const vocabCard = e.target.closest("[data-vocab-index]");
      if (vocabCard) {
        stopAuto({ silent: true });
        const item = vocab[Number(vocabCard.dataset.vocabIndex)];
        playSequence([item.audio, item.exampleAudio], vocabCard);
        return;
      }

      const quizOpt = e.target.closest(".quiz-opt");
      if (quizOpt && !quizOpt.disabled) {
        answerQuiz(Number(quizOpt.dataset.oi));
        return;
      }

      const t = e.target.closest("[data-next],[data-prev],[data-audio],[data-read-page],[data-read-quiz]");
      if (!t) return;
      if (t.matches("[data-next]")) {
        if (isQuizScreen(current) && !canLeaveQuizForward()) return;
        goNext();
        return;
      }
      if (t.matches("[data-prev]")) { goPrev(); return; }
      if (t.matches("[data-read-quiz]")) {
        stopAuto({ silent: true });
        readQuiz();
        return;
      }
      if (t.matches("[data-read-page]")) {
        stopAuto({ silent: true });
        readPage(t.closest(".screen"));
        return;
      }
      if (t.matches(".line")) { playLineEl(t); return; }
      if (t.matches("[data-audio]")) {
        if (t.matches(".sight-word")) return;
        stopAuto({ silent: true });
        stopAudio();
        playSrc(t.dataset.audio, null, t);
      }
    });
  }

  function bindSwipe() {
    let startX = 0;
    let startY = 0;
    let startT = 0;
    let tracking = false;

    const ignore = (target) =>
      target.closest("button, a, select, textarea, input, label, .line, .vocab-card, .quiz-opt");

    document.addEventListener("pointerdown", (e) => {
      if (e.pointerType === "mouse" && e.button !== 0) return;
      if (ignore(e.target)) return;
      tracking = true;
      startX = e.clientX;
      startY = e.clientY;
      startT = Date.now();
    }, { passive: true });

    document.addEventListener("pointerup", (e) => {
      if (!tracking) return;
      tracking = false;
      const dx = e.clientX - startX;
      const dy = e.clientY - startY;
      if (Math.abs(dx) < 56) return;
      if (Math.abs(dy) > Math.abs(dx) * 0.75) return;
      if (Date.now() - startT > 900) return;
      if (dx < 0) goNext();
      else goPrev();
    });

    document.addEventListener("pointercancel", () => { tracking = false; });

    document.addEventListener("keydown", (e) => {
      if (!(e.target instanceof Element)) return;
      if (e.target.closest("textarea, input, select")) return;
      if (e.key === "ArrowRight") { e.preventDefault(); goNext(); }
      if (e.key === "ArrowLeft") { e.preventDefault(); goPrev(); }
    });
  }

  function hydrateCoverNow() {
    const cover = screens[0];
    if (!cover) return;
    cover.querySelectorAll("img.hero").forEach((img) => {
      const src = img.getAttribute("src") || "";
      if (/\.png$/i.test(src)) img.src = src.replace(/\.png$/i, ".webp");
    });
  }

  if (videoPages) document.body.classList.add("video-mode");

  buildVocab();
  buildStoryScreens();
  renderQuizQuestion();
  buildPhrases();
  installChrome();
  bindClicks();
  bindSwipe();
  bindNotes();
  loadNotes();
  hydrateCoverNow();

  const start = parseStartPage();
  showScreen(start);

  window.addEventListener("hashchange", () => {
    const idx = parseStartPage();
    if (idx !== current) showScreen(idx);
  });
})();
