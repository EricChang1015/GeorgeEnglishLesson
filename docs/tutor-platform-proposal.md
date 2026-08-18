# Tutor Platform Proposal

> **Status:** Draft · 2026-08-18  
> **Origin:** Extension of [GeorgeEnglishLesson](../README.md) (single-learner static site) into a multi-student / multi-tutor platform.  
> **Constraints:** Supabase + Vercel free tier; static assets and heavy traffic via Cloudflare.

---

## 1. Executive summary

GeorgeEnglishLesson validates the **lesson player** (vocab → story → quiz → sight words), AI voice pipeline, and picture-book UX for a ~5-year-old at ORT Level 6. The next step is a **modular tutor platform** where:

- Students book lessons online
- Tutors and admins manage learners and assign content
- Teachers or admins **author and publish** reading lessons (generic branding — not tied to one child name)
- Students continue learning **after class** with personalised vocabulary and progress

This document proposes **four top-level modules**, recommended sub-modules, a **Supabase + Vercel + Cloudflare** stack that stays on free tiers at small scale, and a **phased roadmap** that preserves today’s lesson JSON / player investment.

---

## 2. Goals and non-goals

### Goals

| Goal | Notes |
|------|--------|
| Multi-tenant | Many tutors, many students; strict data isolation |
| Personalisation | Per-student progress, weak words, tutor notes, optional review queue |
| Content authoring | Admin / tutor can create lessons without editing raw HTML |
| Cost-conscious | Free tier first; predictable upgrade path |
| Asset efficiency | Large media (WebP, MP3, future video) off Vercel — served via Cloudflare |

### Non-goals (initial phases)

- Full LMS (grades, certificates, payments at scale)
- Automated pronunciation scoring (Phase 4+; start with tutor manual flags)
- Public marketplace of tutors (can come later)
- Replacing George’s current static site before Phase 1 MVP is proven

---

## 3. Module map

Four products, each splittable into deployable sub-modules.

```
┌─────────────────────────────────────────────────────────────────┐
│                        Tutor Platform                           │
├──────────────┬──────────────┬──────────────────┬────────────────┤
│  M1 Booking  │ M2 Admin /   │ M3 Curriculum    │ M4 Student     │
│              │    Tutor     │    (Lesson       │    Learning    │
│              │    Portal    │     Engine)      │                │
└──────────────┴──────────────┴──────────────────┴────────────────┘
         │              │                │                 │
         └──────────────┴────────────────┴─────────────────┘
                              │
                    Supabase (auth, DB, storage)
                    Vercel (Next.js apps)
                    Cloudflare (CDN, DNS, optional R2)
```

---

### M1 — Online booking platform

**Purpose:** Schedule live lessons between tutor and student (or parent).

| Sub-module | Responsibility |
|------------|----------------|
| **M1a Public site** | Landing, tutor profiles, pricing (optional), FAQ |
| **M1b Availability** | Tutor working hours, blackout dates, timezone |
| **M1c Booking flow** | Pick slot → confirm → calendar invite (ICS / Google Calendar link) |
| **M1d Notifications** | Email (Supabase Auth email / Resend free tier) or LINE webhook (later) |
| **M1e Payments** (optional) | Stripe — defer until product-market fit |

**Key entities:** `tutor_profiles`, `availability_slots`, `bookings`, `booking_status`

**Free-tier notes:** Booking writes are low volume. Avoid polling; use Supabase Realtime only if needed for live “slot taken” UX.

---

### M2 — Admin / tutor backend

**Purpose:** Operate the business and see learner overview.

| Sub-module | Responsibility |
|------------|----------------|
| **M2a Auth & roles** | `admin`, `tutor`, `parent`, `student` (see §6) |
| **M2b Org / roster** | Tutor ↔ student assignments; optional `organization` for future schools |
| **M2c Dashboard** | Upcoming bookings, recent activity, at-risk students |
| **M2d Student 360** | Progress per lesson, quiz scores, flagged words, tutor notes |
| **M2e Assignments** | Assign lesson packs or single lessons with due dates |
| **M2f Messaging** | Async tutor → student/parent notes (replaces Follow-up Notes) |
| **M2g Admin CMS** | User management, content moderation, global settings |

**Key entities:** `profiles`, `tutor_students`, `assignments`, `tutor_notes`, `admin_audit_log`

**UI host:** `admin.{domain}` or `app.{domain}/tutor` on Vercel.

---

### M3 — Curriculum system (Lesson Engine)

**Purpose:** Generic evolution of GeorgeEnglishLesson — author, publish, and deliver interactive reading lessons.

**Working name:** **Lesson Engine** (product code name; marketing TBD).

| Sub-module | Responsibility |
|------------|----------------|
| **M3a Content schema** | Canonical JSON: vocab, story pages, quiz, sight words, voices (from `scripts/voices.json`) |
| **M3b Authoring UI** | Form / wizard for admin & authorised tutors: text, upload art, preview |
| **M3c Media pipeline** | PNG → WebP (`optimize_lesson_images.py`); TTS (`generate_lesson_audio.py`) — run as CI or Edge Function trigger |
| **M3d Player runtime** | Extract `lesson-player.js` → versioned npm package or shared `packages/player` |
| **M3e Publish** | Draft → review → published; immutable version per release |
| **M3f Catalogue** | Lesson packs, levels (ORT L6), tags (dragons, science), language |
| **M3g Asset CDN** | Published WebP/MP3 on Cloudflare R2 or Supabase Storage + Cloudflare proxy |

**Reuse from current repo:**

| Today | Future |
|-------|--------|
| `lessons/js/lesson-player.js` | Shared player package |
| `scripts/lessonXX_story.json` | DB row + exported JSON blob |
| `lessons/assets/lesson-XX/` | Storage prefix `published/{lesson_id}/v{n}/` |
| Per-lesson HTML | Single player route: `/learn/lesson/[id]` |

**Key entities:** `content_packages`, `lessons`, `lesson_versions`, `lesson_assets`, `publish_jobs`

---

### M4 — Student post-class learning

**Purpose:** Everything the learner (or parent) sees after and between live sessions.

| Sub-module | Responsibility |
|------------|----------------|
| **M4a Student home** | My assignments, continue last lesson, upcoming booking |
| **M4b Lesson player shell** | Embeds M3 player; records progress events |
| **M4c Progress sync** | Page views, quiz answers, completion — cloud not `localStorage` |
| **M4d Word bank** | Aggregated vocab from lessons + mastery score |
| **M4e Review drills** | Spaced repetition on weak / flagged words (flashcards + example audio) |
| **M4f Pronunciation practice** (later) | Tutor-flagged items; optional recording upload |
| **M4g Parent view** | Read-only progress for child profiles |

**Key entities:** `lesson_attempts`, `quiz_responses`, `word_mastery`, `review_queue`, `pronunciation_flags`

**Personalisation loop:**

```
Quiz miss / tutor flag / low mastery
        → word_mastery updated
        → review_queue schedules next drill
        → M4e surfaces “Today’s words” on student home
```

---

## 4. Recommended architecture

### 4.1 Stack

| Layer | Choice | Role |
|-------|--------|------|
| **Frontend apps** | Next.js (App Router) on **Vercel** Hobby | M1 public + booking, M2 dashboard, M4 student app; optional M3 authoring |
| **API** | Supabase PostgREST + **Edge Functions** | Complex writes, webhooks, publish pipeline, booking conflicts |
| **Database** | **Supabase Postgres** | All relational data, RLS for multi-tenancy |
| **Auth** | **Supabase Auth** | Magic link / Google; parent owns child profiles |
| **Static assets** | **Cloudflare R2** (or Supabase Storage + CF CDN) | WebP, MP3, video — **not** Vercel bandwidth |
| **DNS & CDN** | **Cloudflare** | Proxy custom domain; cache immutable lesson assets |
| **Background jobs** | GitHub Actions or Supabase Edge + queue table | TTS generation, WebP optimisation |

### 4.2 Traffic routing (free-tier friendly)

```
Browser
  │
  ├─ app.example.com        → Cloudflare → Vercel (HTML/JS, SSR, API routes)
  │
  ├─ cdn.example.com        → Cloudflare → R2 (lesson WebP/MP3, long cache)
  │     OR
  └─ {project}.supabase.co/storage/... → Cloudflare cache rule in front
```

**Principles:**

1. **Never bundle lesson media in Next.js `public/`** at scale.
2. Player fetches `lesson.json` + assets from CDN URLs stored in DB.
3. Set `Cache-Control: public, max-age=31536000, immutable` on versioned asset paths (`.../v3/story-01.webp`).
4. API calls (progress, booking) hit Supabase directly from client with RLS — minimises Vercel serverless invocations.

### 4.3 Monorepo vs multi-repo (recommendation)

**Phase 1–2:** Single monorepo `tutor-platform/` (new repo or rename later):

```
apps/
  web/          # M1 + M4 student-facing (or split later)
  dashboard/    # M2 tutor/admin
  studio/       # M3 authoring (can ship later)
packages/
  player/       # extracted lesson-player
  schema/       # Zod types shared with JSON import
  supabase/     # migrations, seed
scripts/        # migrate existing Python TTS / WebP tools
```

GeorgeEnglishLesson remains the **reference implementation** until player extraction is done.

### 4.4 Free tier budget (rough)

| Service | Free limit | Expected early usage |
|---------|------------|----------------------|
| Vercel Hobby | 100 GB bandwidth / mo | Low if media on R2 |
| Supabase Free | 500 MB DB, 5 GB egress, 1 GB storage | Plenty for <500 students |
| Cloudflare | Free CDN + R2 free tier (10 GB storage, 10M reads/mo class) | Primary media egress |
| Supabase pause | After 7 days idle | Cron ping weekly on free projects |

**Upgrade triggers:** Supabase Pro when RLS-heavy reporting slows, or >500 MB DB; Vercel Pro only if SSR traffic spikes.

---

## 5. Data model (core tables)

Simplified ERD for implementation planning.

```
organizations (optional)
profiles (id, role, display_name, parent_id?)
tutor_students (tutor_id, student_id, status)

bookings (tutor_id, student_id, starts_at, ends_at, status)
availability_rules (...)

content_packages (title, level, tags)
lessons (package_id, slug, title, status)
lesson_versions (lesson_id, version, json_blob_url, published_at)

assignments (tutor_id, student_id, lesson_id, due_at)
lesson_attempts (student_id, lesson_version_id, progress, score)
quiz_responses (attempt_id, question_idx, chosen, correct)

vocab_items (lesson_version_id, word, ...)
word_mastery (student_id, vocab_item_id, score, wrong_count, last_seen)
review_queue (student_id, vocab_item_id, due_at)
pronunciation_flags (student_id, vocab_item_id, source: tutor|ai, note)

tutor_notes (tutor_id, student_id, lesson_id?, body, created_at)
```

All student-facing tables include **RLS**: `student_id = auth.uid()` or parent’s linked child IDs; tutors see only assigned students.

---

## 6. Identity model (children)

Recommended for COPPA-friendly simplicity:

| Actor | Login | Access |
|-------|-------|--------|
| **Parent** | Supabase Auth (email / Google) | Manages child profiles, bookings, billing |
| **Student (young)** | No separate login initially | Parent selects child on shared device |
| **Student (older)** | Optional PIN or magic link | Direct M4 access |
| **Tutor** | Auth + `role = tutor` | M2 + assign content |
| **Admin** | Auth + `role = admin` | Full M2 + M3 publish |

---

## 7. Migration from GeorgeEnglishLesson

| Step | Action |
|------|--------|
| 1 | Document `window.LESSON` schema → Zod / JSON Schema in `packages/schema` |
| 2 | Import `lesson-01..03` JSON into `lesson_versions` seed |
| 3 | Upload assets to R2; rewrite URLs in published JSON |
| 4 | Wrap player in Next.js route; parity smoke test (see `.cursor/rules/delivery.mdc`) |
| 5 | Add progress POST to Supabase; deprecate `localStorage` notes |
| 6 | Keep `george.macau-tech.com` on GitHub Pages until student app reaches parity |

**Branding:** Runtime uses configurable `protagonistName` and ref images per **student profile** or **lesson metadata** — not hard-coded “George”.

---

## 8. Phased roadmap

### Phase 0 — Foundation (2–3 weeks)

- [ ] New monorepo skeleton: Next.js + Supabase project
- [ ] Auth, roles, `profiles`, `tutor_students`
- [ ] Cloudflare R2 bucket + CDN subdomain
- [ ] Extract player package; load lesson-01 from CDN JSON

### Phase 1 — MVP loop (4–6 weeks)

- [ ] **M2 minimal:** tutor assigns one lesson; view quiz score
- [ ] **M4 minimal:** student home + player + cloud progress
- [ ] **M3 read-only:** import existing 3 lessons; no authoring UI yet
- [ ] **M1 minimal:** manual booking or Cal.com embed (no custom M1 until needed)

**Success metric:** One tutor, two student profiles, assign lesson → complete → tutor sees result.

### Phase 2 — Booking + word bank (4–6 weeks)

- [ ] **M1:** availability + booking table + email confirm
- [ ] **M4d:** word bank from quiz misses
- [ ] **M4e:** simple review drill (5 words/day)
- [ ] Tutor notes replace Follow-up Notes

### Phase 3 — Authoring (6–8 weeks)

- [ ] **M3b:** lesson wizard (vocab, pages, quiz)
- [ ] **M3c:** publish job → TTS + WebP → R2
- [ ] Draft / publish workflow + version pinning on assignments

### Phase 4 — Personalisation & polish

- [ ] SRS algorithm tuning
- [ ] Pronunciation flags + optional recording
- [ ] Dashboard analytics (class weak words, completion rates)
- [ ] Payments (Stripe) if needed

---

## 9. API and integration sketch

| Client action | Path |
|---------------|------|
| Load lesson | `GET cdn.../lessons/{id}/v{n}/manifest.json` |
| Start attempt | `POST /rest/v1/lesson_attempts` (RLS) |
| Submit quiz answer | `POST /rest/v1/quiz_responses` |
| Complete lesson | `PATCH lesson_attempts` + trigger `word_mastery` upsert (Edge Function) |
| Tutor assign | `POST /rest/v1/assignments` |
| Book slot | Edge Function `book_slot` (transaction — prevent double book) |
| Publish lesson | Edge Function `publish_lesson` → queue TTS job |

---

## 10. Security and privacy

- **RLS on every table** containing PII or progress; no service role key in browser
- Child data minimisation: display name + age band; avoid unnecessary PII
- Tutor can only access assigned students (join through `tutor_students`)
- Published lesson assets are **public** CDN; manifest URLs can be signed or obfuscated if needed
- Separate Supabase projects for **dev** and **prod** (fits free tier’s 2 active projects)
- Weekly cron to prevent Supabase free-tier auto-pause on prod

---

## 11. Open decisions

| # | Question | Options |
|---|----------|---------|
| 1 | Product name | Lesson Engine / Reading Studio / TBD |
| 2 | Domain strategy | `learn.macau-tech.com`, `app.…`, keep George subdomain for legacy |
| 3 | M1 build vs embed | Custom booking vs Cal.com / Calendly embed for Phase 1 |
| 4 | Storage primary | R2 vs Supabase Storage (R2 cheaper egress at scale) |
| 5 | Authoring scope | Admin-only publish vs tutor-created drafts |
| 6 | Offline / iPad | Service worker cache for assigned lessons? |
| 7 | Video lessons | Separate asset type in M3 (lesson-03 video pilot) |

---

## 12. Success criteria (12-month horizon)

- ≥3 tutors, ≥20 student profiles on free / low-cost infra
- ≥10 published lessons in catalogue (including migrated George trilogy)
- Median tutor can assign lesson and see quiz results in <2 minutes
- Students receive personalised review list within 24 h of completing a lesson
- Monthly infra cost ≤ **$25** until deliberate upgrade

---

## 13. References (current repo)

| Doc / path | Relevance |
|------------|-----------|
| [lesson-player.md](./lesson-player.md) | Player behaviour to preserve |
| [character-voices.md](./character-voices.md) | Voice roles for M3 schema |
| [custom-domain.md](./custom-domain.md) | Cloudflare + static hosting pattern |
| `lessons/js/lesson-player.js` | Player extraction source |
| `scripts/lessonXX_story.json` | M3 content schema reference |
| `.cursor/rules/learner-profile.mdc` | UX / level targets for M4 |

---

## 14. Next actions

1. **Confirm** module split and Phase 0 scope on second machine review.
2. **Create** Supabase dev project + R2 bucket naming convention.
3. **Spike:** Next.js page loads lesson-01 manifest from R2 with existing player logic.
4. **Decide** product name and primary domain before public M1.

---

*Document owner: Eric · Generated from planning discussion 2026-08-18*
