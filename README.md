# English+ B2+/C1 Companion Course

An English+ course by Kris Galezewski: 20 lessons and 4 tests. Content lives in `lessons_section*.py` and
`tests_data.py`; `python3 build.py` regenerates every page (source + standalone).

## Design (2026 redesign)

The look follows the Claude Design handoff "English+ course redesign", shared by all five English+ courses
(companion-course colours: wine / slate / forest / gold; no word chips on lesson tiles).

| What | Where |
|---|---|
| Colours, type, every component style | `shared/theme.css` (the course palette is the `body.theme-*` block near the top) |
| Lesson-page chrome (hero, sticky section menu, headings, reading popover, listening player, wrap-up cards) | the **REDESIGN CHROME** block at the end of `shared/course-engine.js` |
| Course overview | `overview.py` (layout + script), data from `build.py → build_index()` and `redesign_config.py` |

## Free preview on englishvoiced.com/courses/

    python3 build.py
    python3 build_preview.py ../krisgalezewski.github.io/courses/english-plus-b2-c1
    python3 ../krisgalezewski.github.io/_seo/seo.py

Lessons 1–2 are open; the rest are listed, faded and locked (`?locked=N` explains it's in the full course).
