# -*- coding: utf-8 -*-
"""2026 redesign (Claude Design handoff "English+ course redesign").

Course-overview copy and art, the word chips shown on lesson tiles and
lesson heroes, and the section colours. Used by build.py; the lesson-page
chrome reads its own copy of the chips from the REDESIGN CHROME block at
the end of shared/course-engine.js.

Chip kinds: s = solid cream, o = outlined, x = dashed, d = dim.
"""

OVERVIEW_TOP = "English+ B2+/C1 Companion Course · by Kris Galezewski"
OVERVIEW_LABELS = ["English+", "Companion Course", "B2+/C1"]
INDEX_HEADING = "Welcome to English+ B2+/C1 with Kris"
WELCOME_COPY = "This is the <b>B2+/C1 Companion Course</b> — the sequel to the original English+ B1+/B2 grammar course, picking up where that one left off with more nuanced aspect, sophisticated conditionals, advanced passive structures and discourse-level grammar."
OVERVIEW_ART = "<div style=\"display:flex;flex-direction:column;gap:10px;align-items:flex-end;font-family:'Archivo';font-weight:800\">\n          <div style=\"display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end\"><span style=\"padding:5px 12px;border-radius:9px;background:#F6EEDD;color:#5C2140;font-size:18px\">had left</span><span style=\"padding:5px 12px;border-radius:9px;background:rgba(0,0,0,.2);font-size:18px\">was raining</span></div>\n          <div style=\"display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end\"><span style=\"padding:5px 12px;border-radius:9px;background:#4A5D78;color:#F6EEDD;font-size:18px\">Had I known,</span></div>\n          <div style=\"display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end\"><span style=\"padding:5px 12px;border-radius:9px;background:#4F6E55;color:#F6EEDD;font-size:18px\">is being built</span></div>\n          <div style=\"display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end\"><span style=\"padding:5px 12px;border-radius:9px;background:#8A7631;color:#F6EEDD;font-size:18px\">whereby</span></div>\n        </div>"
LESSON_CHIPS = {}

# main / deep colour per section, in section order
SECTION_COLORS = [{"color": "#5C2140", "deep": "#3B1429"}, {"color": "#2F4058", "deep": "#1D2A3B"}, {"color": "#34503A", "deep": "#203324"}, {"color": "#6B5A1E", "deep": "#463A12"}]
