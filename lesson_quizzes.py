"""Per-lesson quiz links (header pill + wrap-up card) for the English+ B2+/C1 course.

Each lesson has a 12-question self-practice quiz in the english-quiz Supabase
project (seed file: english-quiz/sql/seed-lesson-quizzes-english-plus-b2-c1.sql).
The quiz ids are fixed there, so the links below never change. Used by
gen_common.nav_header() and gen_lesson_template.build().
"""
import html

PRACTICE_URL = "https://englishvoiced.com/english-quiz/practice.html?quiz="


def quiz_pill(quiz_id):
    return ('\n      <a id="quiz-link" href="' + PRACTICE_URL + quiz_id + '" target="_blank" rel="noopener" class="pill" '
            'style="text-decoration:none;font-size:12.5px;border-radius:var(--radius-sm)">📝 Lesson quiz</a>')


def quiz_card(quiz_id, name):
    return f'''
    <div class="card" id="quiz-card">
      <h3 style="margin-bottom:6px">Lesson quiz — find out what stuck</h3>
      <p style="font-size:14px;color:var(--text-secondary);margin-bottom:14px">12 quick questions on {html.escape(name)}. It opens in a new tab, so this lesson stays exactly where you left it.</p>
      <a class="btn btn-primary" id="quiz-card-link" href="{PRACTICE_URL}{quiz_id}" target="_blank" rel="noopener" style="text-decoration:none;display:inline-block">📝 Take the lesson quiz →</a>
    </div>'''


# lesson number -> (quiz id, quiz name)
QUIZZES = {
    1: ('57273d25-7c48-5a14-ab82-d6847a06a21e', 'Narrative Tenses in Extended Storytelling'),
    2: ('b631d7bb-a1be-58bb-9f0b-fbc006b0e62c', 'Used To vs Would for Past Habits'),
    3: ('9e5aecae-5530-5b27-8e20-b751b9dd804e', 'Future in the Past + Future Perfect Continuous'),
    4: ('cba44022-25db-569b-b512-7d7b756dac14', 'Academic Hedging: Seem To, Appear To, Tend To, Be Likely To'),
    5: ('da1d95ab-fdc4-56f9-b930-eae750766d7b', "Needn't Have vs Didn't Need To"),
    6: ('d8211586-eb38-5ab9-9b8a-2f06dfbaf55c', 'Deduction With Continuous Aspect'),
    7: ('47b07a34-7987-5a62-bc02-f97dd5877cce', 'Inversion in Conditionals'),
    8: ('f9067777-2f4c-52b1-b72c-4e4b80bb4014', 'Conditional Alternatives to If'),
    9: ('b26366a9-c1d2-5311-b214-b946427d3281', 'Hypothetical Meaning Without If'),
    10: ('196f6c6f-2120-5e67-9d7a-31e5ff45a3e7', 'Advanced Wish / If Only'),
    11: ('d3b6781a-f70a-58c0-ac3b-7ff0747adacd', 'Passive With Combined Aspects'),
    12: ('0bfda39a-9007-50a5-95fb-b0a926ba4d82', 'Impersonal Passive & Get-Passive'),
    13: ('6e8ef29a-4d40-5f51-87fa-d3e9ebf81228', 'Nominalisation'),
    14: ('4d5f61a2-2ee0-518f-92b5-2bc03567123d', 'Advanced Articles & Quantifiers'),
    15: ('07f18556-b09e-5c98-80f7-dd6fe8b20275', 'Participle Clauses'),
    16: ('f486c18d-4468-51eb-9368-7d964bcd68a8', 'Advanced Relative Clauses'),
    17: ('c32dd943-c7e9-55a0-a35d-1fec5a3ae3de', 'Ellipsis & Substitution'),
    18: ('bb2574b4-a859-5770-ad29-b3fe3076f7af', 'Negative Inversion for Emphasis'),
    19: ('e22af0e2-f74a-57e1-b349-e538c4796369', 'Fronting & Information Structure'),
    20: ('b71e930a-d2d5-510a-92e7-434dfd91181c', 'Formal Connectors: Nonetheless, Notwithstanding, Whereas'),
}
