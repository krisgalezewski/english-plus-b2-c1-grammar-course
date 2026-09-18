# -*- coding: utf-8 -*-
"""Section 1 — Aspect & Modality, Refined (Lessons 1-6)."""
from gen_lesson_template import vocab, gram

SECTION_NAME = "Aspect & Modality, Refined"
THEME = "theme-aspect"

LESSONS = []

# ============================================================
# LESSON 1 — Narrative tenses in extended storytelling
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-01-narrative-tenses",
    "num": 1, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Narrative Tenses in Extended Storytelling",
    "subtitle": "Weaving past simple, continuous and perfect fluidly across a whole story.",
    "warmup_intro": "You already know past simple, past continuous and past perfect individually. Today is about weaving all three together across a longer stretch of narrative — the way real stories, reports and anecdotes actually work.",
    "warmup": [
        {"prompt": "In a story, the tense that carries the main sequence of events forward is usually…",
         "options": [{"label": "past simple", "value": "right", "correct": True}, {"label": "past continuous", "value": "wrong", "correct": False}]},
        {"prompt": "\"It was raining when the meeting started\" uses past continuous to describe…",
         "options": [{"label": "background scene-setting, already in progress", "value": "right", "correct": True}, {"label": "the next event in the sequence", "value": "wrong", "correct": False}]},
        {"prompt": "\"By the time she arrived, everyone had left\" uses past perfect because leaving happened…",
         "options": [{"label": "before the arrival, the reference point in the story", "value": "right", "correct": True}, {"label": "at exactly the same moment as the arrival", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "Think of past simple as the story's spine, past continuous as its scenery, and past perfect as flashbacks — that's the whole lesson in one sentence.",
    "diagnostic": [
        {"prompt": "While the CEO ___ her speech, the lights suddenly went out.", "options": [{"label": "was giving", "value": "right", "correct": True}, {"label": "gave", "value": "wrong", "correct": False}]},
        {"prompt": "By the time the investors arrived, the team ___ the whole presentation.", "options": [{"label": "had rehearsed", "value": "right", "correct": True}, {"label": "rehearsed", "value": "wrong", "correct": False}]},
        {"prompt": "She opened the email, read it twice, then ___ her manager.", "options": [{"label": "called", "value": "right", "correct": True}, {"label": "was calling", "value": "wrong", "correct": False}]},
        {"prompt": "He realised he ___ his badge at home, so he had to sign in as a visitor.", "options": [{"label": "had left", "value": "right", "correct": True}, {"label": "left", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Three tenses, three jobs in one story",
        "intro": "Past simple moves the story forward, event by event. Past continuous paints the background it happens against. Past perfect reaches back to something that was already finished before that point in the story. Browse each below, or test yourself with Quick check.",
        "tabs": [{"key": "simple", "label": "Past Simple"}, {"key": "continuous", "label": "Past Continuous"}, {"key": "perfect", "label": "Past Perfect"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "simple": [
                {"label": "the main sequence of events", "example": "She walked in, sat down, and opened her laptop."},
                {"label": "a completed single action", "example": "He finished the report just before midnight."},
            ],
            "continuous": [
                {"label": "background scene already in progress", "example": "Rain was falling steadily as the taxi pulled up."},
                {"label": "an interrupted action", "example": "She was reviewing the contract when her phone rang."},
            ],
            "perfect": [
                {"label": "something finished before the story's reference point", "example": "By the time he arrived, the client had already left."},
                {"label": "the cause behind a later result in the story", "example": "She was exhausted because she had worked all weekend."},
            ],
        },
        "quiz_labels": {"simple": "Past Simple", "continuous": "Past Continuous", "perfect": "Past Perfect"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Past Simple: <b>subject + verb-ed / irregular past</b> — moves the plot forward.</div>
          <div class="formula" style="border-left-color:var(--c-continuous)">✅ Past Continuous: <b>subject + was/were + verb-ing</b> — sets the scene, or gets interrupted.</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ Past Perfect: <b>subject + had + past participle</b> — a flashback to something already finished.</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> past perfect is only needed when the order of two past events would otherwise be ambiguous or worth emphasising — not every earlier action needs it.<br><br>
            ✅ "She left the office and went home." — simple sequence, order is obvious from word order alone, no past perfect needed.<br>
            ✅ "She left the office because she had finished early." — past perfect clarifies that finishing happened <i>before</i> leaving, not as part of the same moment.<br><br>
            Overusing past perfect ("had left, had gone, had arrived...") for a plain sequence makes a story sound clumsy — save it for genuine flashbacks or cause-before-effect.</span>
          </div>'''
    },
    "compare": {
        "title": "Same events, different framing",
        "instruction": "Hover over each version to see how the tense choice changes what the sentence emphasises.",
        "items": [
            {"key": "c1", "label": "Plain sequence", "text": "She finished the call and left the building.",
             "explain": "Past simple + past simple: a straightforward sequence, one thing after another."},
            {"key": "c2", "label": "With background", "text": "She was finishing the call when the fire alarm went off.",
             "explain": "Past continuous sets an in-progress scene that a past simple event interrupts."},
            {"key": "c3", "label": "With flashback", "text": "She left the building because the alarm had gone off minutes earlier.",
             "explain": "Past perfect signals the alarm happened first, explaining the cause of what came after."},
        ]
    },
    "reading": {
        "heading": "The Halo Effect in Performance Reviews",
        "passage_paragraphs": [
            f'''Elena {gram("g1","had already formed")} a strong impression of David long before his official review began. Back in spring, he {gram("g2","had delivered")} a {vocab("dazzling","dazzling")} presentation to the board, and the memory of that single afternoon {vocab("overshadowed","overshadowed")} nearly everything that came after. While she {gram("g3","was flicking through")} his file the night before the meeting, she realised she could barely recall a single other thing he had done since.''',
            f'''During the review itself, Elena {gram("g4","praised")} David's "consistent excellence" and {vocab("credited","credited")} him with initiative he had barely shown that quarter. She {vocab("glossed","glossed over")} two missed deadlines, because by then that one dazzling afternoon {gram("g5","had already convinced")} her he was reliable. Meanwhile, two desks away, a quieter colleague, Priya, {gram("g6","was quietly finishing")} a {vocab("meticulous","meticulous")} project that would go on to save the department real money — work that barely earned a mention in her own review.''',
            f'''Psychologists have a name for what {gram("g7","happened")} that afternoon: the halo effect, first described nearly a century ago by the psychologist Edward Thorndike, occurs when one striking quality {vocab("skewed","skewed")} judgement of everything else. David's rating that year came out noticeably {vocab("inflated","inflated")}, while Priya's looked oddly {vocab("distorted","distorted")} downward, for no clear reason at all. It was only when an external auditor compared the numbers months later that the mistake finally {vocab("backfired","backfired")}, forcing the company to rewrite its entire review process.''',
        ],
        "comprehension": [
            {"prompt": "What had already happened before David's official review even began?", "options": [
                {"label": "He had delivered a dazzling presentation to the board months earlier.", "value": "right", "correct": True},
                {"label": "He had already resigned from his position.", "value": "wrong", "correct": False}]},
            {"prompt": "What was Priya doing while Elena was praising David?", "options": [
                {"label": "She was quietly finishing a meticulous project.", "value": "right", "correct": True},
                {"label": "She was preparing a formal complaint to HR.", "value": "wrong", "correct": False}]},
            {"prompt": "What finally exposed the problem with David's rating?", "options": [
                {"label": "An external auditor comparing the numbers months later.", "value": "right", "correct": True},
                {"label": "David himself admitting he had exaggerated his work.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "dazzling": {"word": "dazzling", "ipa": "/ˈdæz.lɪŋ/", "meaning": "extremely impressive or attractive", "example": "His dazzling presentation won over the entire board."},
            "overshadowed": {"word": "overshadowed", "ipa": "/ˌəʊ.vəˈʃæd.əʊd/", "meaning": "made something else seem less important by comparison", "example": "That single afternoon overshadowed everything he did afterwards."},
            "credited": {"word": "credited", "ipa": "/ˈkred.ɪ.tɪd/", "meaning": "given recognition or acknowledgement for something", "example": "She credited him with initiative he had barely shown."},
            "glossed": {"word": "glossed over", "ipa": "/ɡlɒst ˈəʊ.vər/", "meaning": "dealt with something briefly or superficially to avoid discussing it properly", "example": "She glossed over two missed deadlines entirely."},
            "meticulous": {"word": "meticulous", "ipa": "/məˈtɪk.jʊ.ləs/", "meaning": "very careful and precise about details", "example": "Priya's meticulous project saved the department real money."},
            "skewed": {"word": "skewed", "ipa": "/skjuːd/", "meaning": "distorted or made biased in a particular direction", "example": "One striking quality skewed judgement of everything else."},
            "inflated": {"word": "inflated", "ipa": "/ɪnˈfleɪ.tɪd/", "meaning": "artificially increased or exaggerated beyond what is justified", "example": "His rating that year came out noticeably inflated."},
            "distorted": {"word": "distorted", "ipa": "/dɪˈstɔː.tɪd/", "meaning": "given a false or misleading impression", "example": "Her rating looked oddly distorted downward."},
            "backfired": {"word": "backfired", "ipa": "/ˌbækˈfaɪəd/", "meaning": "had the opposite effect to what was intended, causing harm", "example": "The mistake finally backfired once an auditor compared the numbers."},
        },
        "gram_explanations": {
            "g1": "Past perfect — a mental state that had already formed before the story's main reference point (the review), used here as background flashback.",
            "g2": "Past perfect — a specific flashback event (the spring presentation) that explains the later bias; it happened before the story's main timeline.",
            "g3": "Past continuous — a background action in progress the night before the meeting, setting the scene for what she noticed.",
            "g4": "Past simple — the main spine event of the story: the review itself taking place.",
            "g5": "Past perfect — reaches back to explain why she dismissed the missed deadlines; the cause was already complete before the review.",
            "g6": "Past continuous — a parallel background action happening at the same time as the review, used for contrast.",
            "g7": "Past simple — the narrative resumes with the main sequence, moving toward the story's explanation and conclusion."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "\"Dazzling\" means…", "options": [{"label": "extremely impressive or attractive", "value": "right", "correct": True}, {"label": "quietly disappointing", "value": "wrong", "correct": False}, {"label": "deliberately vague", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Meticulous\" means…", "options": [{"label": "very careful and precise about details", "value": "right", "correct": True}, {"label": "careless and rushed", "value": "wrong", "correct": False}, {"label": "loud and confident", "value": "wrong2", "correct": False}]},
            {"prompt": "If judgement is \"skewed\", it is…", "options": [{"label": "distorted or biased in a particular direction", "value": "right", "correct": True}, {"label": "completely fair and balanced", "value": "wrong", "correct": False}, {"label": "based purely on statistics", "value": "wrong2", "correct": False}]},
            {"prompt": "A rating that is \"inflated\" is…", "options": [{"label": "artificially increased beyond what's justified", "value": "right", "correct": True}, {"label": "unfairly reduced", "value": "wrong", "correct": False}, {"label": "kept exactly accurate", "value": "wrong2", "correct": False}]},
            {"prompt": "If a plan \"backfired\", it…", "options": [{"label": "had the opposite effect to what was intended", "value": "right", "correct": True}, {"label": "worked exactly as intended", "value": "wrong", "correct": False}, {"label": "was never actually attempted", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "That single afternoon", "after": "everything he did afterwards.", "answers": ["overshadowed"], "width": 130},
            {"before": "She", "after": "him with initiative he had barely shown.", "answers": ["credited"], "width": 100},
            {"before": "She simply", "after": "two missed deadlines that quarter.", "answers": ["glossed over"], "width": 130},
            {"before": "Her rating looked oddly", "after": "downward for no clear reason.", "answers": ["distorted"], "width": 110},
        ],
    },
    "practice": {
        "gapfill_focus": "past simple, past continuous, or past perfect?",
        "gapfill": [
            {"before": "While the technician", "after": "(replace) the cable, the lights flickered twice.", "answers": ["was replacing"]},
            {"before": "By the time the fire brigade arrived, the staff", "after": "(already/evacuate) the building.", "answers": ["had already evacuated"]},
            {"before": "She", "after": "(read) the report twice before she finally understood it.", "answers": ["read"]},
            {"before": "He realised he", "after": "(forget) his laptop charger at the hotel.", "answers": ["had forgotten"]},
            {"before": "They", "after": "(still/discuss) the merger when the news broke publicly.", "answers": ["were still discussing"]},
            {"before": "The moment she", "after": "(open) the door, everyone shouted \"surprise!\"", "answers": ["opened"]},
        ],
        "second": {
            "type": "categorise", "title": "Categorise the function",
            "instruction": "Each sentence uses one of the three narrative tenses. Tap which job it's doing.",
            "categories": ["Moves the story forward", "Sets the background scene", "Flashback / earlier cause"],
            "items": [
                {"prompt": "\"The rain was hammering against the windows as the meeting began.\"", "correct": "Sets the background scene"},
                {"prompt": "\"She grabbed her coat and ran for the last train.\"", "correct": "Moves the story forward"},
                {"prompt": "\"He was exhausted because he had barely slept in two days.\"", "correct": "Flashback / earlier cause"},
                {"prompt": "\"They had already signed the contract before the lawyers even arrived.\"", "correct": "Flashback / earlier cause"},
            ],
        },
        "builders": [
            {"words": ["By", "the", "time", "she", "arrived,", "the", "server", "had", "already", "crashed."]},
            {"words": ["Rain", "was", "falling", "steadily", "when", "the", "taxi", "pulled", "up."]},
            {"words": ["He", "opened", "the", "laptop", "and", "started", "typing", "immediately."]},
        ],
    },
    "speaking": {
        "solo_text": "Tell a short story (real or invented) about something going wrong at work. Use at least one past simple event, one past continuous background detail, and one past perfect flashback.",
        "group_questions": [
            "Describe a memorable emergency or crisis you witnessed at work or school — what was happening right before it, and what had already happened by the time it was resolved?",
            "Tell your group about a time you arrived somewhere and something had already happened without you.",
            "What's a story from your life where the order of events really mattered to understand what happened?",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing a case study about the halo effect in performance reviews.",
        "dialogue": [
            {"speaker": "Anna", "line": "Did you read that case study about the halo effect? The one with the manager and her star employee?"},
            {"speaker": "Tomasz", "line": "Yes — Elena, right? She'd already fallen for David's one dazzling presentation months before the actual review."},
            {"speaker": "Anna", "line": "Exactly. By the time she sat down to write it, she'd basically decided he was brilliant before looking at any real evidence."},
            {"speaker": "Tomasz", "line": "Meanwhile poor Priya was quietly doing all this meticulous work that nobody noticed."},
            {"speaker": "Anna", "line": "That's what got me — her rating came out distorted downward for no real reason."},
            {"speaker": "Tomasz", "line": "It only came out because an auditor happened to compare the numbers months later."},
            {"speaker": "Anna", "line": "Which forced the whole company to rewrite how they do reviews."},
            {"speaker": "Tomasz", "line": "A pretty expensive lesson for one dazzling afternoon."},
        ],
        "comprehension": [
            {"prompt": "What had Elena already decided before evaluating any real evidence?", "options": [{"label": "That David was brilliant, based on one earlier presentation.", "value": "right", "correct": True}, {"label": "That David needed additional training.", "value": "wrong", "correct": False}]},
            {"prompt": "What was Priya doing while David was being praised?", "options": [{"label": "She was doing meticulous work that went unnoticed.", "value": "right", "correct": True}, {"label": "She was leaving the company.", "value": "wrong", "correct": False}]},
            {"prompt": "What eventually exposed the problem with the review?", "options": [{"label": "An auditor comparing the numbers months later.", "value": "right", "correct": True}, {"label": "David admitting to exaggeration.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "While she ___ the report, the printer jammed.", "options": [{"label": "was printing", "value": "right", "correct": True}, {"label": "printed", "value": "wrong", "correct": False}]},
        {"prompt": "By the time we got there, the shop ___.", "options": [{"label": "had already closed", "value": "right", "correct": True}, {"label": "closed", "value": "wrong", "correct": False}]},
        {"prompt": "He walked in, sat down, and ___ his laptop.", "options": [{"label": "opened", "value": "right", "correct": True}, {"label": "was opening", "value": "wrong", "correct": False}]},
        {"prompt": "She was tired because she ___ all night.", "options": [{"label": "had worked", "value": "right", "correct": True}, {"label": "worked", "value": "wrong", "correct": False}]},
        {"prompt": "It ___ heavily when the plane finally landed.", "options": [{"label": "was raining", "value": "right", "correct": True}, {"label": "rained", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 2 — Used to vs. would for past habits
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-02-used-to-vs-would",
    "num": 2, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Used To vs. Would for Past Habits",
    "subtitle": "Two ways to talk about repeated past routines — and why one of them refuses to describe states.",
    "warmup_intro": "Both \"used to\" and \"would\" describe repeated past habits or routines that no longer happen. They overlap a lot — but not completely.",
    "warmup": [
        {"prompt": "\"I used to live in Kraków\" and \"I would live in Kraków\" — which is correct for describing a past state?", "options": [{"label": "only \"used to\"", "value": "right", "correct": True}, {"label": "either works equally well", "value": "wrong", "correct": False}]},
        {"prompt": "\"Every summer, we would visit my grandmother\" describes…", "options": [{"label": "a repeated past action, now finished", "value": "right", "correct": True}, {"label": "a single one-off event", "value": "wrong", "correct": False}]},
        {"prompt": "\"Used to\" can describe both repeated actions AND past states; \"would\" can only describe…", "options": [{"label": "repeated actions, not states", "value": "right", "correct": True}, {"label": "states, not repeated actions", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "If you can replace it with \"was/were\" (a state), only \"used to\" works. If it's a repeated action, either usually works.",
    "diagnostic": [
        {"prompt": "She ___ a lot of money before she changed careers. (state)", "options": [{"label": "used to earn", "value": "right", "correct": True}, {"label": "would earn", "value": "wrong", "correct": False}]},
        {"prompt": "Every Friday, my father ___ us to the cinema.", "options": [{"label": "would take", "value": "right", "correct": True}, {"label": "was taking", "value": "wrong", "correct": False}]},
        {"prompt": "I ___ believe in ghosts when I was a child. (state)", "options": [{"label": "used to", "value": "right", "correct": True}, {"label": "would", "value": "wrong", "correct": False}]},
        {"prompt": "We ___ spend hours just talking about nothing.", "options": [{"label": "would", "value": "right", "correct": True}, {"label": "are used to", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Repeated actions vs. states",
        "intro": "For repeated past actions, \"used to\" and \"would\" are interchangeable — either one works, and the choice is mostly stylistic (\"would\" often adds a storytelling feel). The real dividing line is states: \"would\" simply can't describe a past state (a feeling, belief, possession or ongoing condition) — only \"used to\" can.",
        "tabs": [{"key": "usedto", "label": "Used to"}, {"key": "would", "label": "Would"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "usedto": [
                {"label": "a past state (feeling, belief, possession)", "example": "She used to be terrified of public speaking."},
                {"label": "a past state that no longer holds", "example": "We used to own a much smaller flat."},
            ],
            "would": [
                {"label": "a repeated past action, often with a storytelling feel", "example": "Every winter, we would build a snowman in the garden."},
                {"label": "a routine within a specific remembered period", "example": "During his internship, he would arrive an hour early."},
            ],
        },
        "quiz_labels": {"usedto": "Used to (states — \"would\" can't do this)", "would": "Would (storytelling flavour)"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Used to: <b>used to + base verb</b> — repeated actions AND states. "I used to smoke." / "I used to hate coffee."</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ Would: <b>would + base verb</b> — repeated actions only, never states. "I would smoke a pack a day." ❌ "I would hate coffee."</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> stative verbs (believe, hate, own, know, be, live as a state, want) simply block "would" — no exceptions.<br><br>
            ✅ "I used to own a motorbike." — a past state (possession). <b>Only "used to" works.</b><br>
            ❌ "I would own a motorbike." — ungrammatical; ownership isn't a repeated event, it's a continuous state.<br><br>
            When in doubt, ask: is this something that happened repeatedly and separately (would OK), or a continuous condition (would blocked, used to only)?<br><br>
            For a plain repeated action like "I used to cycle to work every day," either form works — "I would cycle to work every day" is just as correct. "Would" is simply the more common choice when you're narrating a story about the past, rather than just stating the fact.</span>
          </div>'''
    },
    "compare": {
        "title": "Compare: repeated action vs. state",
        "instruction": "Hover to see why one allows \"would\" and the other doesn't.",
        "items": [
            {"key": "c1", "label": "Repeated action", "text": "We would play cards after dinner every night.", "explain": "A distinct, repeatable event — \"would\" works fine here. So does \"used to\" (\"We used to play cards after dinner every night\") — for a plain repeated action either one is correct; \"would\" is just preferred when you want that storytelling feel."},
            {"key": "c2", "label": "Past state", "text": "We used to live three streets away from the office.", "explain": "A continuous condition, not a repeatable event — \"would\" is blocked; only \"used to\" works."},
            {"key": "c3", "label": "Repeated action", "text": "She would call her sister every Sunday without fail.", "explain": "A habitual, separately-occurring action — \"would\" is natural here. \"Used to\" works too (\"She used to call her sister every Sunday without fail\"); \"would\" is simply the more typical pick for narrating it as a story."},
            {"key": "c4", "label": "Past state", "text": "She used to be quite shy around new people.", "explain": "A state (a personality trait at the time), not a repeated action — only \"used to\" works."},
        ]
    },
    "reading": {
        "heading": "Parkinson's Law and the Expansion of Work",
        "passage_paragraphs": [
            f'''Before the finance team tightened its deadlines, a single quarterly report {gram("g1","used to take")} nearly two weeks to finish, even though the actual writing {vocab("consumed","consumed")} barely two working days. According to Cyril Northcote Parkinson, the economist who first {vocab("articulated","articulated")} this idea, work simply {gram("g2","would expand")} to swallow whatever time was available for it — and nowhere was that clearer than in this one office.''',
            f'''Old-timers {gram("g3","would recall")} how staff meetings {gram("g4","would stretch")} on for two or three hours during quiet months, filling every free slot on the calendar. The office {gram("g5","used to feel")} {vocab("perpetually","perpetually")} busy, even when there was demonstrably little to do, and deadlines that {gram("g6","used to be")} vague and generous only encouraged the {vocab("drift","drift")}.''',
            f'''Everything changed when a new director {vocab("imposed","imposed")} strict weekly deadlines and insisted that meetings run no longer than thirty minutes. Productivity, remarkably, barely {vocab("suffered","suffered")}; the same reports that once occupied two weeks now got finished within days, seemingly {vocab("confirming","confirming")} Parkinson's original observation with startling precision. The lesson, old staff admit, is uncomfortable: most of that old {vocab("slack","slack")} {vocab("stemmed","stemmed")} not from the work itself, but from how much room it was given to expand into.''',
        ],
        "comprehension": [
            {"prompt": "According to the passage, why did a report needing only two days of actual writing take two weeks to finish?", "options": [
                {"label": "Work tended to expand to fill whatever time was available.", "value": "right", "correct": True},
                {"label": "The writers assigned to it were inexperienced.", "value": "wrong", "correct": False}]},
            {"prompt": "What used to happen to staff meetings during quiet months?", "options": [
                {"label": "They would stretch on for two or three hours.", "value": "right", "correct": True},
                {"label": "They were cancelled altogether.", "value": "wrong", "correct": False}]},
            {"prompt": "What happened after the new director imposed strict deadlines?", "options": [
                {"label": "Productivity barely suffered, and reports were finished much faster.", "value": "right", "correct": True},
                {"label": "Most of the finance staff resigned within weeks.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "consumed": {"word": "consumed", "ipa": "/kənˈsjuːmd/", "meaning": "used up an amount of time, resources or energy", "example": "The actual writing consumed barely two working days."},
            "articulated": {"word": "articulated", "ipa": "/ɑːˈtɪk.jʊ.leɪ.tɪd/", "meaning": "expressed an idea clearly in words", "example": "Parkinson first articulated this idea in an essay."},
            "perpetually": {"word": "perpetually", "ipa": "/pəˈpetʃ.u.ə.li/", "meaning": "constantly, in a way that never stops", "example": "The office used to feel perpetually busy."},
            "drift": {"word": "drift", "ipa": "/drɪft/", "meaning": "a slow, gradual movement away from an original state", "example": "Vague deadlines only encouraged the drift."},
            "imposed": {"word": "imposed", "ipa": "/ɪmˈpəʊzd/", "meaning": "officially introduced a rule or requirement", "example": "The new director imposed strict weekly deadlines."},
            "suffered": {"word": "suffered", "ipa": "/ˈsʌf.əd/", "meaning": "was negatively affected by something", "example": "Productivity barely suffered after the change."},
            "confirming": {"word": "confirming", "ipa": "/kənˈfɜːm.ɪŋ/", "meaning": "showing that something believed or suspected is true", "example": "The result ended up confirming the original theory."},
            "slack": {"word": "slack", "ipa": "/slæk/", "meaning": "unused capacity or looseness in a system", "example": "Most of that old slack disappeared overnight."},
            "stemmed": {"word": "stemmed", "ipa": "/stemd/", "meaning": "originated or resulted from something", "example": "The delay stemmed from how loose the deadlines were."},
        },
        "gram_explanations": {
            "g1": "\"Used to\" + take — a past state or general condition (how long the process typically took), not a discrete repeatable event, so \"would\" wouldn't fit as naturally.",
            "g2": "\"Would\" + expand — describes a repeated, observable pattern of behaviour, which \"would\" can express.",
            "g3": "\"Would\" + recall — a repeated action (retelling the story), a natural narrative use of \"would\".",
            "g4": "\"Would\" + stretch — a repeated, separate occurrence each time meetings happened.",
            "g5": "\"Used to\" + feel — a past state (the general atmosphere of the office), which blocks \"would\".",
            "g6": "\"Used to\" + be — another past state (how deadlines generally were), so only \"used to\" works here."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "If time is \"consumed\" by a task, it is…", "options": [{"label": "used up by that task", "value": "right", "correct": True}, {"label": "saved for later use", "value": "wrong", "correct": False}, {"label": "wasted on something unrelated", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Perpetually\" means…", "options": [{"label": "constantly, without stopping", "value": "right", "correct": True}, {"label": "occasionally, now and then", "value": "wrong", "correct": False}, {"label": "briefly, for a moment", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"impose\" a rule means to…", "options": [{"label": "officially introduce it", "value": "right", "correct": True}, {"label": "quietly remove it", "value": "wrong", "correct": False}, {"label": "suggest it informally", "value": "wrong2", "correct": False}]},
            {"prompt": "If something \"confirms\" a theory, it…", "options": [{"label": "shows that the theory is true", "value": "right", "correct": True}, {"label": "proves the theory false", "value": "wrong", "correct": False}, {"label": "has no relation to the theory", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Slack\" in a system refers to…", "options": [{"label": "unused capacity or looseness", "value": "right", "correct": True}, {"label": "a strict, rigid structure", "value": "wrong", "correct": False}, {"label": "a sudden shortage of resources", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "Parkinson first", "after": "this idea in a well-known essay.", "answers": ["articulated"], "width": 120},
            {"before": "Vague deadlines only encouraged the", "after": ".", "answers": ["drift"], "width": 90},
            {"before": "Productivity barely", "after": "after the new deadlines came in.", "answers": ["suffered"], "width": 100},
            {"before": "Most of that old slack", "after": "from how loose the deadlines used to be.", "answers": ["stemmed"], "width": 100},
        ],
    },
    "practice": {
        "gapfill_focus": "used to or would — pick the one that actually works.",
        "gapfill": [
            {"before": "She", "after": "(own) a small café near the station. (state)", "answers": ["used to own"]},
            {"before": "Every summer, they", "after": "(spend) two weeks by the lake.", "answers": ["would spend", "used to spend"]},
            {"before": "I", "after": "(believe) in luck more than I do now. (state)", "answers": ["used to believe"]},
            {"before": "He", "after": "(tell) the same joke at every family dinner.", "answers": ["would tell", "used to tell"]},
            {"before": "We", "after": "(live) in a much smaller apartment. (state)", "answers": ["used to live"]},
            {"before": "My grandmother", "after": "(knit) us a new scarf every winter.", "answers": ["would knit", "used to knit"]},
        ],
        "second": {
            "type": "categorise", "title": "Would, or used-to-only?",
            "instruction": "Decide whether \"would\" could also replace \"used to\" in each sentence, or whether it's a state that blocks \"would\" entirely.",
            "categories": ["Would also works", "Used to only (a state)"],
            "items": [
                {"prompt": "\"I used to hate mushrooms as a child.\"", "correct": "Used to only (a state)"},
                {"prompt": "\"We used to meet at the same café every Thursday.\"", "correct": "Would also works"},
                {"prompt": "\"She used to have really long hair.\"", "correct": "Used to only (a state)"},
                {"prompt": "\"He used to visit his grandparents every August.\"", "correct": "Would also works"},
            ],
        },
        "builders": [
            {"words": ["We", "would", "play", "cards", "after", "dinner", "every", "night."]},
            {"words": ["She", "used", "to", "own", "a", "small", "bakery", "downtown."]},
            {"words": ["He", "used", "to", "believe", "in", "ghosts", "as", "a", "child."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a routine from your childhood using both \"used to\" and \"would\" — include at least one past state (used to only) and one repeated action (would or used to).",
        "group_questions": [
            "What's something your family used to do regularly that they no longer do?",
            "Describe a place you used to live or a job you used to have that felt very different from now.",
            "Tell your group about a habit you would have as a child that seems strange to you now.",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing Parkinson's Law and how their old office used to run.",
        "dialogue": [
            {"speaker": "Anna", "line": "I read about Parkinson's Law today — the idea that work expands to fill whatever time you give it."},
            {"speaker": "Tomasz", "line": "That explains our old finance team perfectly. Reports used to take two weeks even though the writing itself barely consumed two days."},
            {"speaker": "Anna", "line": "Meetings would stretch on forever too, back before the new director came in."},
            {"speaker": "Tomasz", "line": "Right, the office used to feel busy all the time, even when there wasn't much real work."},
            {"speaker": "Anna", "line": "Then deadlines got tightened and somehow productivity barely suffered."},
            {"speaker": "Tomasz", "line": "Which just confirms Parkinson was onto something."},
            {"speaker": "Anna", "line": "Most of that old slack apparently stemmed from how loose the deadlines used to be."},
            {"speaker": "Tomasz", "line": "I guess we should be grateful for tighter deadlines, annoying as they are."},
        ],
        "comprehension": [
            {"prompt": "According to Tomasz, how long did reports used to take even though the actual writing needed only two days?", "options": [{"label": "About two weeks.", "value": "right", "correct": True}, {"label": "About two months.", "value": "wrong", "correct": False}]},
            {"prompt": "What changed when the new director came in?", "options": [{"label": "Deadlines got tightened and productivity barely suffered.", "value": "right", "correct": True}, {"label": "The finance team was disbanded entirely.", "value": "wrong", "correct": False}]},
            {"prompt": "Where does Anna say the old slack came from?", "options": [{"label": "How loose the deadlines used to be.", "value": "right", "correct": True}, {"label": "Poorly trained new staff.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "She ___ a lot of money in her twenties. (state)", "options": [{"label": "used to earn", "value": "right", "correct": True}, {"label": "would earn", "value": "wrong", "correct": False}]},
        {"prompt": "Every Sunday, we ___ a long walk together.", "options": [{"label": "would take", "value": "right", "correct": True}, {"label": "are taking", "value": "wrong", "correct": False}]},
        {"prompt": "He ___ terrified of dogs as a child. (state)", "options": [{"label": "used to be", "value": "right", "correct": True}, {"label": "would be", "value": "wrong", "correct": False}]},
        {"prompt": "My uncle ___ us the same story every Christmas.", "options": [{"label": "would tell", "value": "right", "correct": True}, {"label": "is telling", "value": "wrong", "correct": False}]},
        {"prompt": "I ___ three cats when I was younger. (state)", "options": [{"label": "used to have", "value": "right", "correct": True}, {"label": "would have", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 3 — Future in the past (was going to / would) + future perfect continuous
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-03-future-in-the-past",
    "num": 3, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Future in the Past + Future Perfect Continuous",
    "subtitle": "Talking about a future that never arrived, and a future duration measured from further ahead.",
    "warmup_intro": "\"Future in the past\" describes a plan or prediction made at some point in the past, about what would happen next — often one that didn't actually happen. Future perfect continuous, meanwhile, looks forward to how long something will have been going on.",
    "warmup": [
        {"prompt": "\"She was going to call you, but she forgot\" describes a plan that…", "options": [{"label": "was made in the past but never happened", "value": "right", "correct": True}, {"label": "will definitely happen tomorrow", "value": "wrong", "correct": False}]},
        {"prompt": "\"By next June, I will have been working here for ten years\" focuses on…", "options": [{"label": "the duration of an action up to a future point", "value": "right", "correct": True}, {"label": "a single completed action in the future", "value": "wrong", "correct": False}]},
        {"prompt": "\"He said he would call later\" is future-in-the-past because the future was viewed…", "options": [{"label": "from a point back in the past", "value": "right", "correct": True}, {"label": "from right now, in the present", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "Future-in-the-past is always about a future seen from an earlier vantage point — often one that got disrupted.",
    "diagnostic": [
        {"prompt": "We ___ have a picnic, but it started raining.", "options": [{"label": "were going to", "value": "right", "correct": True}, {"label": "are going to", "value": "wrong", "correct": False}]},
        {"prompt": "By 2027, she ___ this company for two decades.", "options": [{"label": "will have been running", "value": "right", "correct": True}, {"label": "will run", "value": "wrong", "correct": False}]},
        {"prompt": "He told us he ___ resign at the end of the year.", "options": [{"label": "would", "value": "right", "correct": True}, {"label": "will", "value": "wrong", "correct": False}]},
        {"prompt": "By the time you land, I ___ for you at the airport for an hour.", "options": [{"label": "will have been waiting", "value": "right", "correct": True}, {"label": "will wait", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "A future seen from the past, and a future measured backward",
        "intro": "\"Was/were going to\" and \"would\" describe a future as it looked from an earlier point — often one that was cancelled or changed. Future perfect continuous measures how long something will have continued by a future point.",
        "tabs": [{"key": "fitp", "label": "Future in the Past"}, {"key": "fpc", "label": "Future Perfect Continuous"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "fitp": [
                {"label": "a plan made in the past, often disrupted", "example": "We were going to launch in March, but the funding fell through."},
                {"label": "a prediction or promise reported in the past", "example": "She said the results would be ready by Friday."},
            ],
            "fpc": [
                {"label": "duration of an action up to a stated future point", "example": "By December, he will have been coding for exactly a year."},
                {"label": "emphasising an ongoing process leading up to a deadline", "example": "By the time the audit starts, we will have been preparing for months."},
            ],
        },
        "quiz_labels": {"fitp": "Future in the Past", "fpc": "Future Perfect Continuous"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-future)">✅ Future in the past: <b>was/were going to</b> or <b>would</b> + base verb — a future viewed from an earlier moment.</div>
          <div class="formula" style="border-left-color:var(--c-continuous);margin-bottom:20px">✅ Future perfect continuous: <b>will have been + verb-ing</b> — duration up to a future point.</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> "future in the past" almost always implies the plan changed, was cancelled, or simply never came to pass — that's usually the whole point of using it rather than a plain past tense.<br><br>
            ✅ "We were going to move to Berlin, but the job offer fell through." — a cancelled plan, viewed from the past.<br>
            ✅ Compare with future perfect continuous, which never implies cancellation — it's a confident projection forward, purely about duration: "By June, she will have been living here for five years."</span>
          </div>'''
    },
    "compare": {
        "title": "A disrupted plan vs. a confident projection",
        "instruction": "Hover over each to see the difference in what's being claimed.",
        "items": [
            {"key": "c1", "label": "Future in the past", "text": "He was going to apply for the promotion, but he changed his mind.", "explain": "A plan that existed in the past but didn't happen — future-in-the-past almost always signals disruption."},
            {"key": "c2", "label": "Future perfect continuous", "text": "By next month, he will have been working here for three years.", "explain": "A confident forward projection about duration — no disruption implied at all."},
        ]
    },
    "reading": {
        "heading": "The Sunk Cost Fallacy in Project Management",
        "passage_paragraphs": [
            f'''When Aurora kicked off, the roadmap {gram("g1","was going to launch")} the platform in under six months, and engineers promised migration {gram("g2","would be")} complete well before the holiday season. Everyone was confident; the {vocab("projected","projected")} timeline looked, if anything, generous.''',
            f'''Then costs began to {vocab("spiral","spiral")}. A mid-project {vocab("audit","audit")} revealed that the chosen database architecture couldn't handle Aurora's expected traffic, and switching now would mean {vocab("discarding","discarding")} eight months of work. Leadership had already assured the board that they {gram("g3","were not going to reconsider")} the architecture at this stage — too much had already been {vocab("sunk","sunk")} into it. Rather than cut losses, the steering committee insisted that by the following fiscal year, Aurora {gram("g4","would have been generating")} more than enough revenue to justify every delay.''',
            f'''That prediction never came true. Researchers who study the sunk cost fallacy — our tendency to keep {vocab("funnelling","funnelling")} resources into a failing effort simply because we've already committed so much — would recognise the pattern instantly: the more the company spent trying to save Aurora, the harder abandoning it became to {vocab("justify","justify")}. Analysts now estimate that by the time a genuine replacement finally ships, the company {gram("g5","will have been paying")} for Aurora's {vocab("upkeep","upkeep")} for nearly three years longer than the original plan ever intended — a {vocab("stark","stark")} reminder that a plan can quietly outlive the reasons anyone had for trusting it.''',
        ],
        "comprehension": [
            {"prompt": "What did the original roadmap promise about Aurora's migration?", "options": [
                {"label": "That it would be complete before the holiday season.", "value": "right", "correct": True},
                {"label": "That it would take at least two years.", "value": "wrong", "correct": False}]},
            {"prompt": "Why did leadership refuse to reconsider the database architecture mid-project?", "options": [
                {"label": "Too much had already been invested in it.", "value": "right", "correct": True},
                {"label": "The alternative architecture was more expensive to license.", "value": "wrong", "correct": False}]},
            {"prompt": "What do analysts now estimate about the company's future spending on Aurora?", "options": [
                {"label": "That it will have been paying for its upkeep for years longer than planned.", "value": "right", "correct": True},
                {"label": "That the platform will have been fully retired within a year.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "projected": {"word": "projected", "ipa": "/prəˈdʒek.tɪd/", "meaning": "estimated or forecast for the future", "example": "The projected timeline looked generous at first."},
            "spiral": {"word": "spiral", "ipa": "/ˈspaɪə.rəl/", "meaning": "to increase rapidly and uncontrollably", "example": "Costs began to spiral soon after the audit."},
            "audit": {"word": "audit", "ipa": "/ˈɔː.dɪt/", "meaning": "an official inspection or review of something", "example": "A mid-project audit revealed the architecture problem."},
            "discarding": {"word": "discarding", "ipa": "/dɪˈskɑːd.ɪŋ/", "meaning": "getting rid of or abandoning something no longer wanted", "example": "Switching now would mean discarding eight months of work."},
            "sunk": {"word": "sunk", "ipa": "/sʌŋk/", "meaning": "invested and unable to be recovered", "example": "Too much money had already been sunk into the project."},
            "funnelling": {"word": "funnelling", "ipa": "/ˈfʌn.əl.ɪŋ/", "meaning": "directing something continuously into a particular place", "example": "They kept funnelling resources into a failing effort."},
            "justify": {"word": "justify", "ipa": "/ˈdʒʌs.tɪ.faɪ/", "meaning": "to show or prove that something is reasonable", "example": "Abandoning the project became harder to justify each month."},
            "upkeep": {"word": "upkeep", "ipa": "/ˈʌp.kiːp/", "meaning": "the process and cost of keeping something in good condition", "example": "The upkeep costs kept climbing long after launch."},
            "stark": {"word": "stark", "ipa": "/stɑːk/", "meaning": "harsh, severe, or impossible to avoid noticing", "example": "It was a stark reminder of how plans can go wrong."},
        },
        "gram_explanations": {
            "g1": "\"Was going to launch\" — future in the past: the original plan, viewed from before the project unravelled.",
            "g2": "\"Would be\" — future in the past: a promise made early on, reported from that earlier vantage point, which ultimately didn't hold.",
            "g3": "\"Were not going to reconsider\" — future in the past (negated): a decision, reported from the past, about what leadership planned not to do going forward.",
            "g4": "\"Would have been generating\" — future-in-the-past perfect continuous: a projection about ongoing revenue, made from a past vantage point about what would supposedly be happening by a still-later point.",
            "g5": "\"Will have been paying\" — future perfect continuous: a genuine forward-looking projection from the present, measuring duration up to a future point."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "An \"audit\" is…", "options": [{"label": "an official inspection or review", "value": "right", "correct": True}, {"label": "a casual conversation", "value": "wrong", "correct": False}, {"label": "a public celebration", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Discarding\" something means…", "options": [{"label": "getting rid of or abandoning it", "value": "right", "correct": True}, {"label": "improving it significantly", "value": "wrong", "correct": False}, {"label": "storing it carefully", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Funnelling\" resources into something means…", "options": [{"label": "directing them continuously into it", "value": "right", "correct": True}, {"label": "withdrawing them gradually from it", "value": "wrong", "correct": False}, {"label": "dividing them equally elsewhere", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"stark\" reminder is one that is…", "options": [{"label": "harsh and impossible to ignore", "value": "right", "correct": True}, {"label": "gentle and easily forgotten", "value": "wrong", "correct": False}, {"label": "amusing and lighthearted", "value": "wrong2", "correct": False}]},
            {"prompt": "Money that is \"sunk\" into a project is…", "options": [{"label": "invested and unable to be recovered", "value": "right", "correct": True}, {"label": "set aside for future use", "value": "wrong", "correct": False}, {"label": "refunded in full", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "The", "after": "timeline looked generous, at least at first.", "answers": ["projected"], "width": 110},
            {"before": "Costs began to", "after": "soon after the audit.", "answers": ["spiral"], "width": 90},
            {"before": "Abandoning the project became harder to", "after": "each month.", "answers": ["justify"], "width": 110},
            {"before": "The company kept paying for Aurora's", "after": "long after launch.", "answers": ["upkeep"], "width": 100},
        ],
    },
    "practice": {
        "gapfill_focus": "future in the past, or future perfect continuous?",
        "gapfill": [
            {"before": "We", "after": "(go) camping, but the forecast changed our minds.", "answers": ["were going to go"]},
            {"before": "By next spring, she", "after": "(run) her own business for five years.", "answers": ["will have been running"]},
            {"before": "He promised he", "after": "(finish) it by Friday, but he didn't.", "answers": ["would finish"]},
            {"before": "By the time the guests arrive, we", "after": "(cook) for six hours straight.", "answers": ["will have been cooking"]},
            {"before": "They", "after": "(announce) it last week, but the deal collapsed.", "answers": ["were going to announce"]},
            {"before": "By midnight, the volunteers", "after": "(pack) boxes non-stop for ten hours.", "answers": ["will have been packing"]},
        ],
        "second": {
            "type": "categorise", "title": "Disrupted plan, or confident projection?",
            "instruction": "Tap which pattern each sentence belongs to.",
            "categories": ["Future in the past (often disrupted)", "Future perfect continuous (duration projection)"],
            "items": [
                {"prompt": "\"She was going to quit, but she got promoted instead.\"", "correct": "Future in the past (often disrupted)"},
                {"prompt": "\"By June, he will have been studying medicine for six years.\"", "correct": "Future perfect continuous (duration projection)"},
                {"prompt": "\"We were going to sell the house last year.\"", "correct": "Future in the past (often disrupted)"},
                {"prompt": "\"By the time she retires, she will have been teaching for thirty years.\"", "correct": "Future perfect continuous (duration projection)"},
            ],
        },
        "builders": [
            {"words": ["We", "were", "going", "to", "launch", "in", "March,", "but", "we", "delayed", "it."]},
            {"words": ["By", "June,", "she", "will", "have", "been", "running", "the", "team", "for", "a", "year."]},
            {"words": ["He", "said", "he", "would", "call", "later", "that", "evening."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a plan that fell through in your life (\"I was going to..., but...\"), then describe something you'll have been doing for a long time by a specific future date.",
        "group_questions": [
            "Tell the group about a plan you had that changed at the last minute.",
            "By the time you finish this course, how long will you have been studying English?",
            "What's something someone once promised you \"would\" happen, that never actually did?",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing the Aurora project and the sunk cost fallacy.",
        "dialogue": [
            {"speaker": "Anna", "line": "Remember Aurora? It was going to launch in six months, and now it's been what, three years?"},
            {"speaker": "Tomasz", "line": "Don't remind me. The database was wrong from day one, but leadership were not going to reconsider it once they'd sunk that much money in."},
            {"speaker": "Anna", "line": "Classic sunk cost fallacy. They kept funnelling resources into it instead of cutting their losses."},
            {"speaker": "Tomasz", "line": "The committee even promised the board Aurora would have been generating serious revenue by the following fiscal year."},
            {"speaker": "Anna", "line": "Did it?"},
            {"speaker": "Tomasz", "line": "Not even close. Analysts now think we'll have been paying for its upkeep for years longer than anyone planned."},
            {"speaker": "Anna", "line": "It's hard to justify walking away once you've spent that much, I suppose."},
            {"speaker": "Tomasz", "line": "Which is exactly the trap."},
        ],
        "comprehension": [
            {"prompt": "What was the original plan for Aurora?", "options": [{"label": "To launch within six months.", "value": "right", "correct": True}, {"label": "To launch within three years.", "value": "wrong", "correct": False}]},
            {"prompt": "Why didn't leadership reconsider the database architecture?", "options": [{"label": "They had already sunk too much money into it.", "value": "right", "correct": True}, {"label": "A better alternative wasn't available at the time.", "value": "wrong", "correct": False}]},
            {"prompt": "What do analysts now think about the company's future spending?", "options": [{"label": "That they'll have been paying for Aurora's upkeep for years longer than planned.", "value": "right", "correct": True}, {"label": "That all spending on Aurora will end within a month.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "We ___ go to the beach, but it rained all day.", "options": [{"label": "were going to", "value": "right", "correct": True}, {"label": "will", "value": "wrong", "correct": False}]},
        {"prompt": "By 2030, she ___ this business for fifteen years.", "options": [{"label": "will have been running", "value": "right", "correct": True}, {"label": "will run", "value": "wrong", "correct": False}]},
        {"prompt": "He told me he ___ finish it that same night.", "options": [{"label": "would", "value": "right", "correct": True}, {"label": "will", "value": "wrong", "correct": False}]},
        {"prompt": "By the time you arrive, I ___ for an hour already.", "options": [{"label": "will have been waiting", "value": "right", "correct": True}, {"label": "will wait", "value": "wrong", "correct": False}]},
        {"prompt": "They ___ move abroad, but the visa fell through.", "options": [{"label": "were going to", "value": "right", "correct": True}, {"label": "have gone to", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 4 — Academic hedging (seem to / appear to / tend to / be likely to)
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-04-academic-hedging",
    "num": 4, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Academic Hedging: Seem To, Appear To, Tend To, Be Likely To",
    "subtitle": "Sounding careful and precise instead of overconfident — a register skill, not a tense.",
    "warmup_intro": "At C1 level, sounding credible often means sounding appropriately cautious. Hedging language softens a claim without weakening its substance — a skill used constantly in reports, research and professional writing.",
    "warmup": [
        {"prompt": "\"The data seems to suggest a correlation\" is more cautious than…", "options": [{"label": "\"The data proves a correlation.\"", "value": "right", "correct": True}, {"label": "\"The data might suggest a correlation.\"", "value": "wrong", "correct": False}]},
        {"prompt": "Hedging language is used mainly to…", "options": [{"label": "avoid overstating a claim you can't fully prove", "value": "right", "correct": True}, {"label": "make a sentence grammatically correct", "value": "wrong", "correct": False}]},
        {"prompt": "\"Younger employees tend to prefer flexible hours\" is a claim about…", "options": [{"label": "a general pattern, not every single case", "value": "right", "correct": True}, {"label": "one specific employee's exact preference", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "Hedging isn't weakness — it's precision. It signals exactly how confident you are, rather than pretending to certainty you don't have.",
    "diagnostic": [
        {"prompt": "The results ___ support the original hypothesis.", "options": [{"label": "appear to", "value": "right", "correct": True}, {"label": "are appearing to", "value": "wrong", "correct": False}]},
        {"prompt": "Remote workers ___ report higher job satisfaction, though not universally.", "options": [{"label": "tend to", "value": "right", "correct": True}, {"label": "are tending to", "value": "wrong", "correct": False}]},
        {"prompt": "Given current trends, prices ___ rise further next quarter.", "options": [{"label": "are likely to", "value": "right", "correct": True}, {"label": "likely rise", "value": "wrong", "correct": False}]},
        {"prompt": "She ___ have misunderstood the instructions.", "options": [{"label": "seems to", "value": "right", "correct": True}, {"label": "is seeming to", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Four ways to hedge a claim",
        "intro": "Each hedging phrase softens a claim slightly differently — seem/appear to soften based on evidence, tend to signals a general pattern with exceptions, and be likely to signals probability about the future.",
        "tabs": [{"key": "seemappear", "label": "Seem to / Appear to"}, {"key": "tend", "label": "Tend to"}, {"key": "likely", "label": "Be likely to"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "seemappear": [
                {"label": "a cautious claim based on available evidence", "example": "The strategy seems to be working, based on early figures."},
                {"label": "appear to — slightly more formal, same function", "example": "The company appears to have underestimated demand."},
            ],
            "tend": [
                {"label": "a general pattern, with acknowledged exceptions", "example": "Smaller teams tend to communicate more directly."},
                {"label": "softening a generalisation about people or things", "example": "New managers tend to over-explain their decisions at first."},
            ],
            "likely": [
                {"label": "a probability judgement about the future", "example": "Demand is likely to increase over the holiday period."},
                {"label": "hedging a prediction without full certainty", "example": "The merger is likely to be finalised by spring."},
            ],
        },
        "quiz_labels": {"seemappear": "Seem to / Appear to", "tend": "Tend to", "likely": "Be likely to"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--accent)">✅ Seem to / Appear to + base verb — a cautious claim grounded in evidence: "The plan seems to be succeeding."</div>
          <div class="formula" style="border-left-color:var(--c-present)">✅ Tend to + base verb — a general pattern, not a universal rule: "Junior staff tend to ask more questions."</div>
          <div class="formula" style="border-left-color:var(--c-future);margin-bottom:20px">✅ Be likely to + base verb — a probability about the future: "Costs are likely to rise next year."</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> these aren't interchangeable — each hedges a different kind of claim.<br><br>
            ✅ "The results seem to confirm the theory." — evidence-based caution about something already observed.<br>
            ❌ "The results tend to confirm the theory." — wrong: "tend to" describes a repeated pattern across cases, not a one-off observation.<br>
            ✅ "Prices are likely to rise." — a forward-looking probability, not an observation about the present.</span>
          </div>'''
    },
    "compare": {
        "title": "Same idea, different confidence level",
        "instruction": "Hover to see how the hedge changes the strength of the claim.",
        "items": [
            {"key": "c1", "label": "Strong claim", "text": "The new policy has reduced turnover.", "explain": "A flat, unhedged claim — states it as established fact."},
            {"key": "c2", "label": "Hedged (evidence)", "text": "The new policy seems to have reduced turnover.", "explain": "Softer — based on evidence so far, but not stated as certain."},
            {"key": "c3", "label": "Hedged (pattern)", "text": "Policies like this tend to reduce turnover.", "explain": "A general pattern across many cases, not a specific claim about this one policy."},
            {"key": "c4", "label": "Hedged (forecast)", "text": "This policy is likely to reduce turnover further.", "explain": "A forward-looking probability, not a claim about what has already happened."},
        ]
    },
    "reading": {
        "heading": "The Dunning-Kruger Effect and Misplaced Confidence",
        "passage_paragraphs": [
            f'''People with limited competence in a given skill {gram("g1","tend to overestimate")} their own ability, according to research popularised by the psychologists David Dunning and Justin Kruger. Their studies {gram("g2","appear to reveal")} a curious pattern: the least skilled participants in a task consistently rate their own performance as {vocab("exceptional","exceptional")}, while genuinely skilled participants, if anything, rate themselves slightly too low.''',
            f'''Novices {gram("g3","seem to lack")} the very {vocab("expertise","expertise")} that would let them spot their own mistakes — a kind of double {vocab("handicap","handicap")} researchers describe as incompetence {vocab("compounding","compounding")} itself. Someone who barely understands a subject {gram("g4","is unlikely to")} notice the gaps in their own reasoning, since spotting a gap requires the same knowledge that person doesn't have. This {vocab("paradox","paradox")} may explain why the loudest voice in a meeting {gram("g5","is likely to")} sound far more certain than the facts alone would justify.''',
            f'''The effect {gram("g6","appears to fade")} once people gain genuine experience, at which point confidence usually {vocab("realigns","realigns")} with actual competence — sometimes dipping briefly below it, a dip researchers nickname the {vocab("trough","trough")} of despair, before climbing back toward something closer to accurate {vocab("calibration","calibration")}. None of this makes confidence untrustworthy in general; it simply means that confidence left {vocab("unchecked","unchecked")} by honest feedback {gram("g7","tends to drift")} away from reality, in either direction, and usually in the most confident direction of all.''',
        ],
        "comprehension": [
            {"prompt": "According to the passage, how do the least skilled participants typically rate their own performance?", "options": [
                {"label": "As exceptional, well above what the evidence supports.", "value": "right", "correct": True},
                {"label": "As below average, out of excessive modesty.", "value": "wrong", "correct": False}]},
            {"prompt": "Why does the passage say novices struggle to notice their own mistakes?", "options": [
                {"label": "Spotting a gap requires the same knowledge that's missing.", "value": "right", "correct": True},
                {"label": "They are too busy to check their work carefully.", "value": "wrong", "correct": False}]},
            {"prompt": "What tends to happen to confidence once people gain real experience?", "options": [
                {"label": "It usually realigns with actual competence, sometimes dipping first.", "value": "right", "correct": True},
                {"label": "It disappears completely and never returns.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "exceptional": {"word": "exceptional", "ipa": "/ɪkˈsep.ʃən.əl/", "meaning": "unusually good, well above average", "example": "They rated their own performance as exceptional."},
            "expertise": {"word": "expertise", "ipa": "/ˌek.spɜːˈtiːz/", "meaning": "specialist skill or knowledge in a particular area", "example": "They lacked the expertise to spot their own mistakes."},
            "handicap": {"word": "handicap", "ipa": "/ˈhæn.di.kæp/", "meaning": "a disadvantage that makes something more difficult", "example": "It's a kind of double handicap for the least skilled."},
            "compounding": {"word": "compounding", "ipa": "/kəmˈpaʊnd.ɪŋ/", "meaning": "making a problem worse by adding to it", "example": "Incompetence ends up compounding itself over time."},
            "paradox": {"word": "paradox", "ipa": "/ˈpær.ə.dɒks/", "meaning": "a situation that seems contradictory but may be true", "example": "This paradox explains a lot about overconfident colleagues."},
            "realigns": {"word": "realigns", "ipa": "/ˌriː.əˈlaɪnz/", "meaning": "adjusts to match a correct or intended position again", "example": "Confidence gradually realigns with real ability."},
            "trough": {"word": "trough", "ipa": "/trɒf/", "meaning": "a low point between two higher points", "example": "Researchers nickname it the trough of despair."},
            "calibration": {"word": "calibration", "ipa": "/ˌkæl.ɪˈbreɪ.ʃən/", "meaning": "the accurate matching of a judgement to reality", "example": "Confidence slowly moves toward accurate calibration."},
            "unchecked": {"word": "unchecked", "ipa": "/ʌnˈtʃekt/", "meaning": "not controlled or tested against evidence", "example": "Confidence left unchecked tends to drift from reality."},
        },
        "gram_explanations": {
            "g1": "\"Tend to\" + overestimate — a general pattern across many people, not a universal claim about every individual.",
            "g2": "\"Appear to\" + reveal — a formal, evidence-based way of reporting what research seems to show, without overstating certainty.",
            "g3": "\"Seem to\" + lack — a cautious inference drawn from behaviour, not a definitive diagnosis of any one person.",
            "g4": "\"Be unlikely to\" — a probability judgement, hedging the claim about spotting one's own gaps.",
            "g5": "\"Be likely to\" — a forward-looking probability about typical behaviour in meetings, not a guarantee.",
            "g6": "\"Appear to\" + fade — evidence-based caution about a general trend as people gain experience.",
            "g7": "\"Tend to\" + drift — a general pattern, not a claim that every case of overconfidence behaves identically."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "\"Expertise\" refers to…", "options": [{"label": "specialist skill or knowledge in an area", "value": "right", "correct": True}, {"label": "a formal certificate or diploma", "value": "wrong", "correct": False}, {"label": "a general lack of interest", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"paradox\" is…", "options": [{"label": "a situation that seems contradictory but may be true", "value": "right", "correct": True}, {"label": "a simple, obvious fact", "value": "wrong", "correct": False}, {"label": "a formal academic paper", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"trough\" is…", "options": [{"label": "a low point between two higher points", "value": "right", "correct": True}, {"label": "the highest point in a process", "value": "wrong", "correct": False}, {"label": "a steady, unchanging level", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Calibration\" means…", "options": [{"label": "the accurate matching of judgement to reality", "value": "right", "correct": True}, {"label": "a total rejection of evidence", "value": "wrong", "correct": False}, {"label": "a sudden, unexplained change", "value": "wrong2", "correct": False}]},
            {"prompt": "Something left \"unchecked\" is…", "options": [{"label": "not controlled or tested against evidence", "value": "right", "correct": True}, {"label": "carefully verified by an expert", "value": "wrong", "correct": False}, {"label": "officially approved", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "They rated their own performance as", "after": ", well above what the evidence showed.", "answers": ["exceptional"], "width": 110},
            {"before": "Being unaware of one's own gaps is a kind of double", "after": ".", "answers": ["handicap"], "width": 100},
            {"before": "Confidence gradually", "after": "with actual competence over time.", "answers": ["realigns"], "width": 100},
            {"before": "Incompetence ends up", "after": "itself, researchers argue.", "answers": ["compounding"], "width": 120},
        ],
    },
    "practice": {
        "gapfill_focus": "seem to, appear to, tend to, or be likely to?",
        "gapfill": [
            {"before": "The new policy", "after": "(seem) to have improved retention slightly.", "answers": ["seems"]},
            {"before": "Smaller teams", "after": "(tend) to communicate more directly.", "answers": ["tend"]},
            {"before": "Costs", "after": "(be likely) to rise again next quarter.", "answers": ["are likely"]},
            {"before": "The committee", "after": "(appear) to have overlooked one key detail.", "answers": ["appears"]},
            {"before": "Junior staff", "after": "(tend) to ask more questions during onboarding.", "answers": ["tend"]},
            {"before": "The merger", "after": "(be likely) to be finalised by spring.", "answers": ["is likely"]},
        ],
        "second": {
            "type": "categorise", "title": "Which hedge fits?",
            "instruction": "Read the claim, then tap the hedge that best matches its type of caution.",
            "categories": ["Seem to / Appear to (evidence)", "Tend to (general pattern)", "Be likely to (future probability)"],
            "items": [
                {"prompt": "\"Remote teams ___ report fewer scheduling conflicts overall.\"", "correct": "Tend to (general pattern)"},
                {"prompt": "\"Based on the early data, the campaign ___ have exceeded its targets.\"", "correct": "Seem to / Appear to (evidence)"},
                {"prompt": "\"Given current demand, the product ___ sell out within days.\"", "correct": "Be likely to (future probability)"},
                {"prompt": "\"The report ___ have underestimated the actual cost.\"", "correct": "Seem to / Appear to (evidence)"},
            ],
        },
        "builders": [
            {"words": ["The", "results", "seem", "to", "support", "the", "original", "hypothesis."]},
            {"words": ["Smaller", "companies", "tend", "to", "adapt", "more", "quickly", "to", "change."]},
            {"words": ["Prices", "are", "likely", "to", "increase", "over", "the", "holidays."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a trend or pattern you've noticed (at work, in the news, in your own habits), using at least two different hedging phrases from this lesson.",
        "group_questions": [
            "What's a claim you've heard recently that you think was overstated, and how would you rephrase it more cautiously?",
            "Discuss a general pattern you've noticed among a group of people (colleagues, classmates, family) using \"tend to\".",
            "Make a cautious prediction about something in your field using \"be likely to\" or \"seem to\".",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing the Dunning-Kruger effect and overconfidence.",
        "dialogue": [
            {"speaker": "Anna", "line": "Have you heard of the Dunning-Kruger effect? People with limited competence tend to overestimate their own ability."},
            {"speaker": "Tomasz", "line": "Definitely seen that in meetings. The least experienced person always seems to lack the awareness that they're missing something."},
            {"speaker": "Anna", "line": "Right, and that's the paradox — you need expertise to even notice your own gaps."},
            {"speaker": "Tomasz", "line": "Meanwhile the genuinely skilled people are likely to underrate themselves, from what I've read."},
            {"speaker": "Anna", "line": "It's such a strange handicap. Confidence and actual ability barely seem to line up."},
            {"speaker": "Tomasz", "line": "Apparently it fades with real experience, though — confidence eventually realigns with competence."},
            {"speaker": "Anna", "line": "Until then, the loudest voice in the room is likely to sound the most certain, not the most correct."},
            {"speaker": "Tomasz", "line": "Which is exactly why I've started listening more carefully to the quiet people."},
        ],
        "comprehension": [
            {"prompt": "According to Anna, what do people with limited competence tend to do?", "options": [{"label": "Overestimate their own ability.", "value": "right", "correct": True}, {"label": "Avoid speaking up in meetings entirely.", "value": "wrong", "correct": False}]},
            {"prompt": "Why does Anna call it a paradox?", "options": [{"label": "You need expertise to notice your own gaps.", "value": "right", "correct": True}, {"label": "Confident people are usually the most correct.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Tomasz say happens with real experience?", "options": [{"label": "Confidence eventually realigns with actual competence.", "value": "right", "correct": True}, {"label": "Confidence disappears completely and never returns.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "The data ___ support our initial theory.", "options": [{"label": "seems to", "value": "right", "correct": True}, {"label": "is seeming to", "value": "wrong", "correct": False}]},
        {"prompt": "New hires ___ ask more questions in their first month.", "options": [{"label": "tend to", "value": "right", "correct": True}, {"label": "are tending to", "value": "wrong", "correct": False}]},
        {"prompt": "Given the forecast, sales ___ rise sharply.", "options": [{"label": "are likely to", "value": "right", "correct": True}, {"label": "likely will", "value": "wrong", "correct": False}]},
        {"prompt": "He ___ have missed the point entirely.", "options": [{"label": "appears to", "value": "right", "correct": True}, {"label": "is appearing to", "value": "wrong", "correct": False}]},
        {"prompt": "Smaller firms ___ react faster to market shifts.", "options": [{"label": "tend to", "value": "right", "correct": True}, {"label": "seem", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 5 — Needn't Have vs. Didn't Need To
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-05-neednt-have",
    "num": 5, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Needn't Have vs. Didn't Need To",
    "subtitle": "Two ways to talk about unnecessary past actions — but only one tells you the action happened anyway.",
    "warmup_intro": "Both phrases describe an action that wasn't necessary, but they answer a different question: did the action actually happen, or was it simply skipped?",
    "warmup": [
        {"prompt": "\"I needn't have brought an umbrella\" tells us the speaker…", "options": [{"label": "brought one, but it turned out to be unnecessary", "value": "right", "correct": True}, {"label": "didn't bring one at all", "value": "wrong", "correct": False}]},
        {"prompt": "\"I didn't need to book a table\" tells us the speaker…", "options": [{"label": "simply didn't book one — it wasn't required", "value": "right", "correct": True}, {"label": "booked a table that turned out to be pointless", "value": "wrong", "correct": False}]},
        {"prompt": "Which phrase always implies the action DID happen?", "options": [{"label": "needn't have + past participle", "value": "right", "correct": True}, {"label": "didn't need to + base verb", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "Think of \"needn't have\" as hindsight regret about something you DID do. \"Didn't need to\" is just a neutral statement about what wasn't required.",
    "diagnostic": [
        {"prompt": "She ___ rushed — the meeting was cancelled, but she'd already left.", "options": [{"label": "needn't have", "value": "right", "correct": True}, {"label": "didn't need to", "value": "wrong", "correct": False}]},
        {"prompt": "We ___ apply for a visa — our stay was under 90 days.", "options": [{"label": "didn't need to", "value": "right", "correct": True}, {"label": "needn't have", "value": "wrong", "correct": False}]},
        {"prompt": "He ___ explained it twice — I understood the first time, but he did it anyway.", "options": [{"label": "needn't have", "value": "right", "correct": True}, {"label": "didn't need to", "value": "wrong", "correct": False}]},
        {"prompt": "They ___ change the schedule at all — everyone was already free.", "options": [{"label": "didn't need to", "value": "right", "correct": True}, {"label": "needn't have", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Did it happen, or was it just unnecessary?",
        "intro": "\"Needn't have + past participle\" always means the action happened, but with hindsight it wasn't necessary. \"Didn't need to + base verb\" is neutral — it just says the requirement wasn't there.",
        "tabs": [{"key": "neednthave", "label": "Needn't Have"}, {"key": "didntneed", "label": "Didn't Need To"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "neednthave": [
                {"label": "the action happened, but wasn't necessary (hindsight)", "example": "I needn't have printed the report — everyone had it digitally."},
                {"label": "often implies mild regret or wasted effort", "example": "We needn't have worried — the flight was delayed anyway."},
            ],
            "didntneed": [
                {"label": "a neutral statement about a requirement that didn't exist", "example": "I didn't need to print the report — it was already shared."},
                {"label": "doesn't tell us whether the action happened or not", "example": "We didn't need to worry, so we didn't."},
            ],
        },
        "quiz_labels": {"neednthave": "Needn't Have", "didntneed": "Didn't Need To"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--accent)">✅ Needn't have + past participle — the action HAPPENED, but hindsight shows it wasn't necessary: "I needn't have worried."</div>
          <div class="formula" style="border-left-color:var(--c-past);margin-bottom:20px">✅ Didn't need to + base verb — neutral; doesn't confirm whether the action happened: "I didn't need to worry."</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> "didn't need to" can sometimes describe an action that happened too, but only with extra context.<br><br>
            ✅ "I needn't have bought a gift — she'd already got one." — clearly happened, clearly regretted with hindsight.<br>
            ⚠️ "I didn't need to buy a gift, but I did anyway, just to be safe." — here the second clause is doing the work of confirming it happened; the phrase alone doesn't tell you.<br>
            ❌ Never use "needn't have" for something that never happened at all — that's simply "didn't need to."</span>
          </div>'''
    },
    "compare": {
        "title": "Same situation, different meaning",
        "instruction": "Hover to see exactly what each sentence confirms.",
        "items": [
            {"key": "c1", "label": "Needn't have", "text": "I needn't have booked a hotel — my cousin offered a room.", "explain": "Confirms: the speaker DID book a hotel. With hindsight, it wasn't necessary."},
            {"key": "c2", "label": "Didn't need to", "text": "I didn't need to book a hotel — my cousin offered a room.", "explain": "Doesn't confirm either way whether a hotel was booked — most naturally reads as: it wasn't required, so it wasn't done."},
        ]
    },
    "reading": {
        "heading": "Decision Fatigue and the Limits of Willpower",
        "passage_paragraphs": [
            f'''Looking back at the product's chaotic launch week, the operations team {gram("g1","needn't have scheduled")} four separate strategy meetings in a single day; each one further {vocab("depleted","depleted")} a {vocab("finite","finite")} reserve of mental energy that researchers call {vocab("willpower","willpower")}, leaving the final decisions of the day measurably worse than the first.''',
            f'''Employees, on the other hand, {gram("g2","didn't need to attend")} every single meeting — attendance for two of the four was entirely optional, though almost nobody realised it at the time. The {vocab("culprit","culprit")}, researchers point out, is not laziness but simple {vocab("cognitive","cognitive")} exhaustion: after a long run of decisions, however {vocab("routine","routine")}, judgement {vocab("deteriorates","deteriorates")}, and people increasingly default to whichever option requires the least {vocab("deliberation","deliberation")}.''',
            f'''One manager later admitted she {gram("g3","needn't have reviewed")} every single expense report personally that week — a junior colleague could easily have handled the routine ones — and that by insisting on doing it all herself, she'd simply {vocab("exhausted","exhausted")} the reserve she needed for harder calls later. The marketing lead, likewise, {gram("g4","needn't have drafted")} three alternate versions of the launch email, since the first was approved without a single change. Interns, meanwhile, {gram("g5","didn't need to submit")} formal daily reports at all; a quick verbal update would have done just as well, and the company {gram("g6","didn't need to redesign")} its entire approval process to fix any of this — a far simpler rule, capping decisions per person per day, turned out to be enough.''',
        ],
        "comprehension": [
            {"prompt": "What does the passage say about the four strategy meetings scheduled in one day?", "options": [
                {"label": "They weren't necessary, even though they did happen.", "value": "right", "correct": True},
                {"label": "They were required by official company policy.", "value": "wrong", "correct": False}]},
            {"prompt": "According to the passage, what is the real cause of worse decisions later in the day?", "options": [
                {"label": "Simple cognitive exhaustion, not laziness.", "value": "right", "correct": True},
                {"label": "A lack of proper training among staff.", "value": "wrong", "correct": False}]},
            {"prompt": "What did the company conclude about redesigning its approval process?", "options": [
                {"label": "That it was never actually necessary.", "value": "right", "correct": True},
                {"label": "That it should have been done years earlier.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "depleted": {"word": "depleted", "ipa": "/dɪˈpliː.tɪd/", "meaning": "reduced in quantity, especially a resource", "example": "Each meeting further depleted the same mental reserve."},
            "finite": {"word": "finite", "ipa": "/ˈfaɪ.naɪt/", "meaning": "having limits, not unlimited", "example": "Willpower draws on a finite reserve of mental energy."},
            "willpower": {"word": "willpower", "ipa": "/ˈwɪl.paʊər/", "meaning": "the ability to control oneself and make decisions", "example": "Researchers describe willpower as a limited resource."},
            "culprit": {"word": "culprit", "ipa": "/ˈkʌl.prɪt/", "meaning": "the cause of a problem, or a person responsible for it", "example": "The real culprit was exhaustion, not laziness."},
            "cognitive": {"word": "cognitive", "ipa": "/ˈkɒɡ.nɪ.tɪv/", "meaning": "relating to mental processes like thinking and deciding", "example": "Cognitive exhaustion sets in after too many decisions."},
            "routine": {"word": "routine", "ipa": "/ruːˈtiːn/", "meaning": "ordinary, done regularly as a fixed procedure", "example": "Even routine decisions add to the mental load."},
            "deteriorates": {"word": "deteriorates", "ipa": "/dɪˈtɪə.ri.ə.reɪts/", "meaning": "becomes progressively worse", "example": "Judgement deteriorates after a long run of decisions."},
            "deliberation": {"word": "deliberation", "ipa": "/dɪˌlɪb.əˈreɪ.ʃən/", "meaning": "careful thought and consideration before deciding", "example": "People default to whatever needs the least deliberation."},
            "exhausted": {"word": "exhausted", "ipa": "/ɪɡˈzɔː.stɪd/", "meaning": "completely used up, drained of energy or resources", "example": "She exhausted the reserve she needed for harder calls."},
        },
        "gram_explanations": {
            "g1": "\"Needn't have scheduled\" — the meetings DID happen, but with hindsight they weren't necessary.",
            "g2": "\"Didn't need to attend\" — neutral: attendance simply wasn't required for two of the four meetings.",
            "g3": "\"Needn't have reviewed\" — she DID review every report herself, but it wasn't necessary given available help.",
            "g4": "\"Needn't have drafted\" — the alternate email versions WERE written, but turned out to be unnecessary effort.",
            "g5": "\"Didn't need to submit\" — neutral: there was no requirement for interns to submit daily reports at all.",
            "g6": "\"Didn't need to redesign\" — neutral: a full process redesign was never actually required to solve the problem."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "\"Willpower\" refers to…", "options": [{"label": "the ability to control oneself and make decisions", "value": "right", "correct": True}, {"label": "physical strength and stamina", "value": "wrong", "correct": False}, {"label": "a formal company policy", "value": "wrong2", "correct": False}]},
            {"prompt": "The \"culprit\" behind a problem is…", "options": [{"label": "its cause or source", "value": "right", "correct": True}, {"label": "its eventual solution", "value": "wrong", "correct": False}, {"label": "a person who reports it", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Deliberation\" means…", "options": [{"label": "careful thought before deciding", "value": "right", "correct": True}, {"label": "an instant, thoughtless reaction", "value": "wrong", "correct": False}, {"label": "a formal written complaint", "value": "wrong2", "correct": False}]},
            {"prompt": "Something \"finite\" is…", "options": [{"label": "limited, not unlimited", "value": "right", "correct": True}, {"label": "endless and unlimited", "value": "wrong", "correct": False}, {"label": "extremely valuable", "value": "wrong2", "correct": False}]},
            {"prompt": "If judgement \"deteriorates\", it…", "options": [{"label": "becomes progressively worse", "value": "right", "correct": True}, {"label": "becomes noticeably sharper", "value": "wrong", "correct": False}, {"label": "stays exactly the same", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "Each extra meeting further", "after": "the team's mental reserve.", "answers": ["depleted"], "width": 110},
            {"before": "Even", "after": "decisions add to the mental load over a day.", "answers": ["routine"], "width": 100},
            {"before": "Researchers point to simple", "after": "exhaustion, not laziness.", "answers": ["cognitive"], "width": 100},
            {"before": "By evening, she'd completely", "after": "the reserve she needed for harder calls.", "answers": ["exhausted"], "width": 110},
        ],
    },
    "practice": {
        "gapfill_focus": "needn't have + past participle, or didn't need to + base verb?",
        "gapfill": [
            {"before": "We", "after": "(needn't / worry) — the flight was delayed anyway.", "answers": ["needn't have worried"]},
            {"before": "She", "after": "(not need / bring) her passport — it was a domestic flight.", "answers": ["didn't need to bring"]},
            {"before": "He", "after": "(needn't / apologise) — nobody was upset in the first place.", "answers": ["needn't have apologised"]},
            {"before": "They", "after": "(not need / book) early — there were plenty of seats left.", "answers": ["didn't need to book"]},
            {"before": "I", "after": "(needn't / rush) — the train was ten minutes late.", "answers": ["needn't have rushed"]},
            {"before": "You", "after": "(not need / call) — I already knew about the change.", "answers": ["didn't need to call"]},
        ],
        "second": {
            "type": "errorspot", "title": "Spot the mistake",
            "instruction": "One word is wrong in each sentence. Tap it, then check the correction.",
            "items": [
                {"words": ["She", "needn't", "have", "bring", "an", "umbrella", "—", "it", "didn't", "rain."], "error_indices": [3], "correction": "\"bring\" → \"brought\" (needn't have + past participle)"},
                {"words": ["We", "didn't", "need", "brought", "extra", "chairs", "—", "there", "were", "enough."], "error_indices": [3], "correction": "\"brought\" → \"to bring\" (didn't need to + base verb)"},
                {"words": ["He", "needn't", "has", "explained", "it", "twice", "—", "I", "understood", "immediately."], "error_indices": [2], "correction": "\"has\" → \"have\" (needn't have, not needn't has)"},
            ],
        },
        "builders": [
            {"words": ["I", "needn't", "have", "worried", "about", "the", "deadline", "at", "all."]},
            {"words": ["They", "didn't", "need", "to", "change", "the", "schedule", "this", "time."]},
            {"words": ["We", "needn't", "have", "left", "so", "early", "for", "the", "airport."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe something you did that turned out to be unnecessary (a purchase, a worry, an effort), using \"needn't have\".",
        "group_questions": [
            "Tell your partner about a time you needn't have worried about something — what happened?",
            "Discuss something at work or school that people generally don't need to do, even though many still do it.",
            "Was there ever a situation where you weren't sure if something was necessary, and it turned out it wasn't? Use \"didn't need to\".",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing decision fatigue after a chaotic work week.",
        "dialogue": [
            {"speaker": "Anna", "line": "I read something about decision fatigue today. Apparently we needn't have scheduled four strategy meetings on the same day last month."},
            {"speaker": "Tomasz", "line": "I remember that day. By the fourth meeting nobody could decide anything properly."},
            {"speaker": "Anna", "line": "Exactly — each one depleted the same finite reserve of willpower, according to the research."},
            {"speaker": "Tomasz", "line": "To be fair, we didn't need to attend all four. Two of them were actually optional."},
            {"speaker": "Anna", "line": "I didn't know that at the time. The real culprit apparently isn't laziness, it's plain cognitive exhaustion."},
            {"speaker": "Tomasz", "line": "Makes sense. Even Priya needn't have reviewed every single expense line herself that week."},
            {"speaker": "Anna", "line": "Right, a junior colleague could have handled the routine ones easily."},
            {"speaker": "Tomasz", "line": "Lesson learned — we didn't need to redesign the whole process, just cap how many decisions we make per day."},
        ],
        "comprehension": [
            {"prompt": "What does Anna say about the four strategy meetings held on the same day?", "options": [{"label": "They weren't necessary, even though they happened.", "value": "right", "correct": True}, {"label": "They were required by official company policy.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Anna say is the real culprit behind worse decisions later in the day?", "options": [{"label": "Plain cognitive exhaustion.", "value": "right", "correct": True}, {"label": "Poor training among staff.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Tomasz conclude at the end of the conversation?", "options": [{"label": "They didn't need to redesign the whole process.", "value": "right", "correct": True}, {"label": "They need to hire a completely new team.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "We ___ rushed — the train was delayed anyway.", "options": [{"label": "needn't have", "value": "right", "correct": True}, {"label": "didn't need to", "value": "wrong", "correct": False}]},
        {"prompt": "She ___ apply for the extra permit — it wasn't required for her case.", "options": [{"label": "didn't need to", "value": "right", "correct": True}, {"label": "needn't have", "value": "wrong", "correct": False}]},
        {"prompt": "They ___ booked a translator — everyone spoke English fluently.", "options": [{"label": "needn't have", "value": "right", "correct": True}, {"label": "didn't need to", "value": "wrong", "correct": False}]},
        {"prompt": "He ___ call ahead — walk-ins were welcome.", "options": [{"label": "didn't need to", "value": "right", "correct": True}, {"label": "needn't have", "value": "wrong", "correct": False}]},
        {"prompt": "I ___ worried about the exam — it was cancelled.", "options": [{"label": "needn't have", "value": "right", "correct": True}, {"label": "didn't need to", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 6 — Deduction With Continuous Aspect (must have been working, etc.)
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-06-deduction-continuous",
    "num": 6, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Deduction With Continuous Aspect",
    "subtitle": "Must have been working, can't have been sleeping — adding continuous aspect sharpens a deduction about an ongoing past action.",
    "warmup_intro": "You already know must have / can't have / might have for deductions about the past. Adding continuous aspect lets you deduce about an action that was IN PROGRESS at a specific moment, not simply completed.",
    "warmup": [
        {"prompt": "\"He must have been sleeping when we called\" suggests…", "options": [{"label": "sleeping was in progress at that moment", "value": "right", "correct": True}, {"label": "he slept once, at some point, and finished", "value": "wrong", "correct": False}]},
        {"prompt": "\"She can't have finished the report\" (no continuous) focuses on…", "options": [{"label": "a completed action, not an ongoing one", "value": "right", "correct": True}, {"label": "an action in progress at a specific moment", "value": "wrong", "correct": False}]},
        {"prompt": "Continuous deduction forms are built with…", "options": [{"label": "modal + have been + -ing", "value": "right", "correct": True}, {"label": "modal + being + past participle", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "Ask yourself: am I deducing about a finished action, or about something that was happening at a particular moment? That decides whether you need the continuous form.",
    "diagnostic": [
        {"prompt": "The lights were on — someone ___ working late.", "options": [{"label": "must have been", "value": "right", "correct": True}, {"label": "must be", "value": "wrong", "correct": False}]},
        {"prompt": "He's out of breath — he ___ running.", "options": [{"label": "must have been", "value": "right", "correct": True}, {"label": "must have", "value": "wrong", "correct": False}]},
        {"prompt": "She can't have been sleeping — the light was still on and music was playing.", "options": [{"label": "correct as written", "value": "right", "correct": True}, {"label": "should be \"can't sleep\"", "value": "wrong", "correct": False}]},
        {"prompt": "They ___ arguing — I could hear raised voices through the wall.", "options": [{"label": "must have been", "value": "right", "correct": True}, {"label": "must have", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Simple deduction vs. continuous deduction",
        "intro": "Modal + have + past participle deduces about a completed action. Modal + have been + -ing deduces about an action that was in progress at a specific past moment.",
        "tabs": [{"key": "simple", "label": "Simple: modal + have + V3"}, {"key": "continuous", "label": "Continuous: modal + have been + -ing"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "simple": [
                {"label": "a deduction about a completed action", "example": "She must have finished the report by now."},
                {"label": "focuses on the result, not the process", "example": "He can't have eaten yet — the food's still here."},
            ],
            "continuous": [
                {"label": "a deduction about an action in progress at a moment", "example": "They must have been arguing when I walked in."},
                {"label": "focuses on the ongoing process, not the result", "example": "She must have been driving when he called — she didn't pick up."},
            ],
        },
        "quiz_labels": {"simple": "Simple: modal + have + V3", "continuous": "Continuous: modal + have been + -ing"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--accent)">✅ Must/can't/might + have + past participle — deduction about a completed action: "She must have left already."</div>
          <div class="formula" style="border-left-color:var(--c-continuous);margin-bottom:20px">✅ Must/can't/might + have been + -ing — deduction about an action in progress at a specific moment: "She must have been leaving when you called."</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> stative verbs (know, believe, want, seem, own) resist the continuous form here too — just as they resist ordinary continuous tenses.<br><br>
            ✅ "He must have known about the change." — correct; "know" is stative.<br>
            ❌ "He must have been knowing about the change." — wrong; stative verbs don't take continuous forms, even in deductions.<br>
            ✅ "They must have been discussing the plan for hours." — correct; "discuss" is a normal action verb.</span>
          </div>'''
    },
    "compare": {
        "title": "Completed action vs. action in progress",
        "instruction": "Hover to see what each deduction actually claims.",
        "items": [
            {"key": "c1", "label": "Simple deduction", "text": "He must have cooked dinner.", "explain": "A deduction that the cooking is finished — the result (dinner) exists."},
            {"key": "c2", "label": "Continuous deduction", "text": "He must have been cooking when the fire alarm went off.", "explain": "A deduction about what was happening at that specific moment — the process, not the result."},
            {"key": "c3", "label": "Negative simple", "text": "She can't have called — my phone shows no missed calls.", "explain": "A deduction that a completed action (the call) did not happen."},
            {"key": "c4", "label": "Negative continuous", "text": "She can't have been calling — the line was busy with someone else.", "explain": "A deduction that an ongoing action wasn't happening at that moment."},
        ]
    },
    "reading": {
        "heading": "Hindsight Bias: \"I Knew It All Along\"",
        "passage_paragraphs": [
            f'''When the startup's {vocab("flagship","flagship")} app collapsed within a month of launch, everyone suddenly had a theory. The investors {gram("g1","must have been ignoring")} clear warning signs, some said; the marketing team {gram("g2","can't have been testing")} the onboarding flow properly, others insisted, pointing to the flood of one-star reviews.''',
            f'''In reality, the team had {vocab("internally","internally")} flagged the same risks for weeks. Engineers {gram("g3","must have been raising")} concerns for months — internal messages later showed dozens of warnings about server capacity that leadership {vocab("brushed","brushed")} aside. Whoever approved the final launch date {gram("g4","can't have been reading")} those messages carefully, critics {vocab("concluded","concluded")}, though in truth several executives had read every single one.''',
            f'''This is hindsight bias at work: once an outcome is known, people {vocab("reconstruct","reconstruct")} the past so that failure looks {vocab("inevitable","inevitable")} and their own foresight looks sharper than it really was. Psychologists who study the {vocab("phenomenon","phenomenon")} note that almost everyone, after the fact, insists they {gram("g5","must have been suspecting")} trouble all along, even when contemporary records show they {vocab("endorsed","endorsed")} the launch enthusiastically at the time. The comforting phrase "I knew it all along" is, more often than not, a {vocab("retrospective","retrospective")} illusion rather than an honest memory.''',
        ],
        "comprehension": [
            {"prompt": "What did some people initially claim about the investors?", "options": [
                {"label": "That they must have been ignoring clear warning signs.", "value": "right", "correct": True},
                {"label": "That they had personally caused the server outage.", "value": "wrong", "correct": False}]},
            {"prompt": "What did internal messages actually reveal about the engineers?", "options": [
                {"label": "They had been raising concerns about server capacity for months.", "value": "right", "correct": True},
                {"label": "They had never mentioned any risks at all.", "value": "wrong", "correct": False}]},
            {"prompt": "According to the passage, what does hindsight bias make people believe about themselves?", "options": [
                {"label": "That they must have been suspecting trouble all along.", "value": "right", "correct": True},
                {"label": "That they were solely responsible for the failure.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "flagship": {"word": "flagship", "ipa": "/ˈflæg.ʃɪp/", "meaning": "the most important product or example of a company's work", "example": "The company's flagship app collapsed within a month."},
            "internally": {"word": "internally", "ipa": "/ɪnˈtɜː.nəl.i/", "meaning": "within an organisation, not publicly", "example": "The risks had been flagged internally for weeks."},
            "brushed": {"word": "brushed", "ipa": "/brʌʃt/", "meaning": "dismissed something without proper consideration", "example": "Leadership brushed the warnings aside."},
            "concluded": {"word": "concluded", "ipa": "/kənˈkluː.dɪd/", "meaning": "decided something after considering the evidence", "example": "Critics concluded that nobody had read the warnings."},
            "reconstruct": {"word": "reconstruct", "ipa": "/ˌriː.kənˈstrʌkt/", "meaning": "to build up a picture of past events again in the mind", "example": "People reconstruct the past once the outcome is known."},
            "inevitable": {"word": "inevitable", "ipa": "/ɪˈnev.ɪ.tə.bəl/", "meaning": "certain to happen, impossible to avoid", "example": "In hindsight, the failure looks entirely inevitable."},
            "phenomenon": {"word": "phenomenon", "ipa": "/fəˈnɒm.ɪ.nən/", "meaning": "a fact or occurrence that is observed to happen", "example": "Psychologists have studied this phenomenon for decades."},
            "endorsed": {"word": "endorsed", "ipa": "/ɪnˈdɔːsd/", "meaning": "publicly supported or approved of something", "example": "Several executives had endorsed the launch enthusiastically."},
            "retrospective": {"word": "retrospective", "ipa": "/ˌret.rəˈspek.tɪv/", "meaning": "looking back on past events, from a later point in time", "example": "That certainty is often just a retrospective illusion."},
        },
        "gram_explanations": {
            "g1": "\"Must have been ignoring\" — a continuous deduction about an action assumed to be ongoing (ignoring warnings) at the relevant time.",
            "g2": "\"Can't have been testing\" — a negative continuous deduction, doubting that an ongoing process (testing) actually happened properly.",
            "g3": "\"Must have been raising\" — a continuous deduction about an extended, ongoing action (raising concerns over months), later confirmed as fact.",
            "g4": "\"Can't have been reading\" — a negative continuous deduction that, ironically, turns out to be wrong once the truth comes out.",
            "g5": "\"Must have been suspecting\" — a continuous deduction about an ongoing mental state, used here to show how hindsight bias distorts memory of what people actually believed at the time."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "A company's \"flagship\" product is…", "options": [{"label": "its most important product or example", "value": "right", "correct": True}, {"label": "its cheapest, entry-level product", "value": "wrong", "correct": False}, {"label": "a discontinued old product", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"phenomenon\" is…", "options": [{"label": "a fact or occurrence that is observed to happen", "value": "right", "correct": True}, {"label": "a proven mathematical formula", "value": "wrong", "correct": False}, {"label": "a type of legal document", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"reconstruct\" the past means to…", "options": [{"label": "build up a picture of it again in the mind", "value": "right", "correct": True}, {"label": "destroy all evidence of it", "value": "wrong", "correct": False}, {"label": "predict what will happen next", "value": "wrong2", "correct": False}]},
            {"prompt": "Something \"inevitable\" is…", "options": [{"label": "certain to happen, impossible to avoid", "value": "right", "correct": True}, {"label": "extremely unlikely to happen", "value": "wrong", "correct": False}, {"label": "already cancelled", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"retrospective\" view is one that…", "options": [{"label": "looks back on past events", "value": "right", "correct": True}, {"label": "predicts distant future events", "value": "wrong", "correct": False}, {"label": "ignores time altogether", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "Leadership simply", "after": "the warnings aside without discussion.", "answers": ["brushed"], "width": 100},
            {"before": "Critics", "after": "that nobody had read the messages carefully.", "answers": ["concluded"], "width": 110},
            {"before": "Several executives had", "after": "the launch enthusiastically at the time.", "answers": ["endorsed"], "width": 110},
            {"before": "The risks had been flagged", "after": "for weeks before launch.", "answers": ["internally"], "width": 100},
        ],
    },
    "practice": {
        "gapfill_focus": "modal + have been + -ing, or modal + have + past participle?",
        "gapfill": [
            {"before": "The lights were on all night — someone", "after": "(must / work) late.", "answers": ["must have been working"]},
            {"before": "She's covered in paint — she", "after": "(must / paint) the fence.", "answers": ["must have been painting"]},
            {"before": "He", "after": "(can't / finish) already — he only started ten minutes ago.", "answers": ["can't have finished"]},
            {"before": "They", "after": "(must / argue) — I heard raised voices through the wall.", "answers": ["must have been arguing"]},
            {"before": "The report", "after": "(must / send) by now — the deadline passed hours ago.", "answers": ["must have been sent"]},
            {"before": "She", "after": "(can't / sleep) — the light was on and music was playing.", "answers": ["can't have been sleeping"]},
        ],
        "second": {
            "type": "categorise", "title": "Completed or in-progress?",
            "instruction": "Decide whether each deduction is about a completed action or one in progress at a specific moment.",
            "categories": ["Completed action", "Action in progress"],
            "items": [
                {"prompt": "\"He must have left already — his coat is gone.\"", "correct": "Completed action"},
                {"prompt": "\"They must have been discussing the merger for hours.\"", "correct": "Action in progress"},
                {"prompt": "\"She can't have been driving — she doesn't have a licence.\"", "correct": "Action in progress"},
                {"prompt": "\"The parcel must have arrived yesterday.\"", "correct": "Completed action"},
            ],
        },
        "builders": [
            {"words": ["Someone", "must", "have", "been", "working", "late", "last", "night."]},
            {"words": ["She", "can't", "have", "been", "sleeping", "with", "the", "music", "on."]},
            {"words": ["They", "must", "have", "been", "arguing", "about", "the", "budget."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a small mystery from your own life (a strange noise, a missing item, a message you couldn't explain) and offer two competing deductions using \"must have been -ing\" and \"can't have been -ing\".",
        "group_questions": [
            "Look around the room (or think of your workplace) — what evidence would let you deduce what someone \"must have been doing\" recently?",
            "Discuss a time you misjudged a situation because your deduction turned out to be wrong.",
            "Practise making a deduction about a friend's mood or behaviour using continuous aspect: \"She must have been feeling...\"",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing a failed app launch and the hindsight bias surrounding it.",
        "dialogue": [
            {"speaker": "Anna", "line": "Did you hear everyone suddenly has a theory about why the flagship app failed?"},
            {"speaker": "Tomasz", "line": "Yeah, someone told me the investors must have been ignoring obvious warning signs."},
            {"speaker": "Anna", "line": "Turns out the engineers must have been raising concerns for months. It was all in the internal messages."},
            {"speaker": "Tomasz", "line": "So whoever approved the launch date can't have been reading those messages carefully?"},
            {"speaker": "Anna", "line": "Apparently they did read them — several executives had, actually."},
            {"speaker": "Tomasz", "line": "That's classic hindsight bias, isn't it? Everyone now insists they must have been suspecting trouble all along."},
            {"speaker": "Anna", "line": "Exactly, even though most of them enthusiastically endorsed the launch at the time."},
            {"speaker": "Tomasz", "line": "\"I knew it all along\" is a pretty comforting phrase to reach for after the fact."},
        ],
        "comprehension": [
            {"prompt": "What did some people claim about the investors after the app failed?", "options": [{"label": "That they must have been ignoring clear warning signs.", "value": "right", "correct": True}, {"label": "That they had secretly sabotaged the launch.", "value": "wrong", "correct": False}]},
            {"prompt": "What did the internal messages actually show about the engineers?", "options": [{"label": "They had been raising concerns for months.", "value": "right", "correct": True}, {"label": "They had personally approved the launch.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Tomasz say about people's claims after the fact?", "options": [{"label": "They insist they must have been suspecting trouble all along.", "value": "right", "correct": True}, {"label": "They admit they were completely blindsided.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "The kitchen's a mess — someone ___ cooking.", "options": [{"label": "must have been", "value": "right", "correct": True}, {"label": "must be", "value": "wrong", "correct": False}]},
        {"prompt": "She can't ___ studying all night — she looks well-rested.", "options": [{"label": "have been", "value": "right", "correct": True}, {"label": "been", "value": "wrong", "correct": False}]},
        {"prompt": "He's soaking wet — he ___ caught in the rain.", "options": [{"label": "must have been", "value": "right", "correct": True}, {"label": "must have", "value": "wrong", "correct": False}]},
        {"prompt": "They ___ arguing — the neighbours heard shouting.", "options": [{"label": "must have been", "value": "right", "correct": True}, {"label": "must been", "value": "wrong", "correct": False}]},
        {"prompt": "He ___ known — he never mentioned it once. (stative verb)", "options": [{"label": "can't have", "value": "right", "correct": True}, {"label": "can't have been", "value": "wrong", "correct": False}]},
    ],
})
