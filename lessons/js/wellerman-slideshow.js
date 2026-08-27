(function () {
  const L = window.LESSON;
  if (!L || !L.lyricFrames || !L.lyricFrames.length) return;

  const ASSET = L.asset || "assets/lesson-06/";
  const frames = L.lyricFrames;
  const SECTION = {
    verse1: "Verse 1",
    chorus: "Chorus",
    verse2: "Verse 2",
    verse3: "Verse 3",
    verse4: "Verse 4",
    chorus2: "Chorus"
  };

  const imgEl = document.getElementById("slideImg");
  const metaEl = document.getElementById("slideMeta");
  const lyricEl = document.getElementById("slideLyric");
  const jumpEl = document.getElementById("slideJump");
  const progressEl = document.getElementById("progressBar");
  const btnPrev = document.getElementById("btnPrev");
  const btnNext = document.getElementById("btnNext");
  const btnReplay = document.getElementById("btnReplay");
  const btnAuto = document.getElementById("btnAuto");
  const figure = document.getElementById("slideFigure");

  let index = 0;
  let autoplay = false;
  let playToken = 0;
  const audio = new Audio();
  const preloaded = new Set();

  function esc(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));
  }

  function webpSrc(name) {
    return ASSET + String(name || "").replace(/\.(png|webp)$/i, "") + ".webp";
  }

  function audioSrc(name) {
    const n = String(name || "");
    if (/^https?:/i.test(n)) return n;
    if (n.startsWith("audio/")) return ASSET + n;
    return ASSET + "audio/" + n;
  }

  function stopAudio() {
    playToken += 1;
    audio.pause();
    audio.removeAttribute("src");
    try { audio.load(); } catch (_) { /* ignore */ }
    if (lyricEl) lyricEl.classList.remove("playing");
  }

  function stopAutoplay() {
    autoplay = false;
    if (btnAuto) {
      btnAuto.classList.remove("on");
      btnAuto.textContent = "▶ Play from here";
    }
  }

  function preloadAround(i) {
    [i - 1, i, i + 1].forEach((n) => {
      if (n < 0 || n >= frames.length) return;
      const src = webpSrc(frames[n].img);
      if (preloaded.has(src)) return;
      preloaded.add(src);
      const img = new Image();
      img.src = src;
    });
  }

  function parseHash() {
    const h = location.hash || "";
    const m = h.match(/#(line|frame)=(\d+)/i);
    if (!m) return 0;
    const n = Number(m[2]) - 1;
    if (Number.isNaN(n) || n < 0) return 0;
    return Math.min(n, frames.length - 1);
  }

  function writeHash() {
    const want = `#line=${index + 1}`;
    if (location.hash !== want) history.replaceState(null, "", want);
  }

  function render() {
    const frame = frames[index];
    if (!frame) return;
    const section = SECTION[frame.section] || frame.section;
    metaEl.textContent = `Line ${index + 1} / ${frames.length} · ${section}`;
    lyricEl.textContent = frame.text;
    imgEl.alt = frame.alt || frame.action || frame.text;
    imgEl.src = webpSrc(frame.img);
    if (jumpEl && Number(jumpEl.value) !== index) jumpEl.value = String(index);
    if (progressEl) {
      progressEl.style.width = `${((index + 1) / frames.length) * 100}%`;
    }
    if (btnPrev) btnPrev.disabled = index === 0;
    if (btnNext) btnNext.disabled = false;
    if (btnNext) btnNext.textContent = index === frames.length - 1 ? "Whole song ▶" : "Next ▶";
    writeHash();
    preloadAround(index);
  }

  function go(next, opts) {
    const silent = opts && opts.silent;
    if (next < 0 || next >= frames.length) return;
    if (!silent) stopAutoplay();
    stopAudio();
    index = next;
    render();
  }

  function playCurrent(onEnd) {
    const frame = frames[index];
    if (!frame) {
      if (onEnd) onEnd();
      return;
    }
    const token = ++playToken;
    lyricEl.classList.add("playing");
    audio.src = audioSrc(frame.audio);
    const done = () => {
      if (token !== playToken) return;
      lyricEl.classList.remove("playing");
      if (onEnd) onEnd();
    };
    audio.onended = done;
    audio.onerror = done;
    audio.play().catch(done);
  }

  function playFromHere() {
    autoplay = true;
    if (btnAuto) {
      btnAuto.classList.add("on");
      btnAuto.textContent = "⏹ Stop";
    }
    const step = () => {
      if (!autoplay) return;
      playCurrent(() => {
        if (!autoplay) return;
        if (index >= frames.length - 1) {
          stopAutoplay();
          return;
        }
        stopAudio();
        index += 1;
        render();
        step();
      });
    };
    stopAudio();
    step();
  }

  function toggleAuto() {
    if (autoplay) {
      stopAutoplay();
      stopAudio();
      return;
    }
    playFromHere();
  }

  if (jumpEl) {
    jumpEl.innerHTML = frames.map((f, i) => {
      const label = `${i + 1}. ${esc(f.text)}`;
      return `<option value="${i}">${label}</option>`;
    }).join("");
    jumpEl.addEventListener("change", () => go(Number(jumpEl.value)));
  }

  if (btnPrev) btnPrev.addEventListener("click", () => go(index - 1));
  if (btnNext) btnNext.addEventListener("click", () => {
    if (index >= frames.length - 1) {
      stopAutoplay();
      stopAudio();
      location.href = "lesson-06.html#listen";
      return;
    }
    go(index + 1);
  });
  if (btnReplay) {
    btnReplay.addEventListener("click", () => {
      stopAutoplay();
      stopAudio();
      playCurrent();
    });
  }
  if (btnAuto) btnAuto.addEventListener("click", toggleAuto);

  if (figure) {
    let startX = 0;
    figure.addEventListener("touchstart", (e) => {
      if (!e.changedTouches[0]) return;
      startX = e.changedTouches[0].clientX;
    }, { passive: true });
    figure.addEventListener("touchend", (e) => {
      if (!e.changedTouches[0]) return;
      const dx = e.changedTouches[0].clientX - startX;
      if (Math.abs(dx) < 40) return;
      if (dx < 0) go(index + 1);
      else go(index - 1);
    }, { passive: true });
  }

  window.addEventListener("hashchange", () => {
    const next = parseHash();
    if (next !== index) go(next);
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight") go(index + 1);
    if (e.key === "ArrowLeft") go(index - 1);
  });

  index = parseHash();
  render();
}());
