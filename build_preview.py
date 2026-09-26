#!/usr/bin/env python3
"""Public preview of this course for englishvoiced.com/courses/<REPO>/.

    python3 build.py                     # rebuild the full course first
    python3 build_preview.py ../krisgalezewski.github.io/courses/english-plus-b2-c1
    python3 ../krisgalezewski.github.io/_seo/seo.py   # restore the SEO tags

Takes the built *-standalone.html files and writes a preview copy:
  * only the first PREVIEW_OPEN_LESSONS lessons ship (fully working); every
    other lesson and test is listed on the course page, faded and locked
  * clicking a locked row, or arriving with ?locked=N (N = lesson number, as
    the english-quiz "Want to go further?" links do), shows a note that the
    lesson is part of the full course, with a link to contact Kris
  * no Supabase backend (progress stays in the browser), an "All courses"
    link back to /courses/, and a free-preview banner
"""
import importlib, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

class C:  # this course has no course_config.py
    PREFIX = "b2c1"
    COURSE_NAME = "English+ B2+/C1 Companion"  # "… is part of the full <COURSE_NAME> course"
    ATTRIBUTION = "English+ B2+/C1 Companion Course · by Kris Galezewski"
    SECTION_FILES = ["lessons_section1", "lessons_section2", "lessons_section3", "lessons_section4"]
from extract_audio_manifest import slugify_for_audio

PREVIEW_OPEN_LESSONS = 2
CONTACT = "https://englishvoiced.com/contact/"

MODS = [importlib.import_module(n) for n in C.SECTION_FILES]
ALL_LESSONS = [l for m in MODS for l in m.LESSONS]


def short_prefix(lesson_id):
    return re.match(rf"^{C.PREFIX}-(lesson-\d+|test-\d+)", lesson_id).group(1)


def sub_once(html, old, new, what):
    assert html.count(old) >= 1, f"preview: anchor not found ({what})"
    return html.replace(old, new, 1)


BACK_CSS = """<style>
.course-attribution{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;max-width:1060px;margin:0 auto;text-align:left}
.course-attribution .back-to-courses{
  text-transform:none;letter-spacing:0;font-family:var(--font-sans);font-size:13px;font-weight:600;color:var(--accent);
  text-decoration:none;border:1.5px solid var(--border-strong);border-radius:999px;padding:5px 12px;background:#fff;
}
.course-attribution .back-to-courses:hover{background:var(--surface-alt)}
</style>
"""


def common_fixups(html):
    html = re.sub(r"window\.SUPABASE_URL = '[^']*';", "window.SUPABASE_URL = ''; // preview copy: no backend — localStorage only", html)
    html = re.sub(r"window\.SUPABASE_ANON_KEY = '[^']*';", "window.SUPABASE_ANON_KEY = ''; // preview copy: no backend — localStorage only", html)
    html = html.replace("index-standalone.html", "index.html")
    # The overview and the lesson chrome read these: the overview locks every
    # lesson after the first PREVIEW_OPEN_LESSONS and shows the preview banner;
    # lesson pages get an "All courses" link.
    html = re.sub(r"(?m)^<body(\s|>)",
                  f'<body data-preview-open="{PREVIEW_OPEN_LESSONS}" data-preview-contact="{CONTACT}" '
                  f'data-preview-course="{C.COURSE_NAME}"\\1', html, count=1)
    html = sub_once(html, "</head>", BACK_CSS + "</head>", "head")
    html = sub_once(html, f'<div class="course-attribution">{C.ATTRIBUTION}</div>',
                    f'<div class="course-attribution"><a class="back-to-courses" href="/courses/">&larr; All courses</a>'
                    f'<span>{C.ATTRIBUTION}</span></div>', "attribution")
    return html


def index_fixups(html):
    # Everything the preview needs is built into the overview (overview.py),
    # switched on by the data-preview-* attributes common_fixups() adds.
    return common_fixups(html)


def build(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    pages = {"index.html": index_fixups(open(os.path.join(ROOT, "index-standalone.html"), encoding="utf-8").read())}
    open_lessons = ALL_LESSONS[:PREVIEW_OPEN_LESSONS]
    for name in [short_prefix(l["id"]) + "-preview-standalone.html" for l in open_lessons] + ["glossary-standalone.html"]:
        pages[name] = common_fixups(open(os.path.join(ROOT, name), encoding="utf-8").read())
    for name, html in pages.items():
        path = os.path.join(out_dir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
    os.makedirs(os.path.join(out_dir, "assets"), exist_ok=True)
    for a in ("favicon-16.png", "favicon-32.png", "favicon-180.png"):
        src = os.path.join(ROOT, "assets", a)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(out_dir, "assets", a))
    audio = os.path.join(ROOT, "audio")
    for l in open_lessons:
        p = short_prefix(l["id"])
        for ext in ("mp3", "json"):
            src = os.path.join(audio, f"{p}-listening.{ext}")
            if os.path.exists(src):
                os.makedirs(os.path.join(out_dir, "audio"), exist_ok=True)
                shutil.copy(src, os.path.join(out_dir, "audio"))
        for entry in l["reading"]["vocab_data"].values():
            src = os.path.join(audio, "vocab", slugify_for_audio(entry["word"]) + ".mp3")
            if os.path.exists(src):
                os.makedirs(os.path.join(out_dir, "audio", "vocab"), exist_ok=True)
                shutil.copy(src, os.path.join(out_dir, "audio", "vocab"))
    print(f"Preview written to {out_dir} ({len(pages)} pages, {PREVIEW_OPEN_LESSONS} open lesson(s)).")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    build(sys.argv[1])
