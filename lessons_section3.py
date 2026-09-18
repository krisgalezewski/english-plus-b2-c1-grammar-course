# -*- coding: utf-8 -*-
"""Section 3 — Advanced Passive & Noun Phrases (Lessons 11-14)."""
from gen_lesson_template import vocab, gram

SECTION_NAME = "Advanced Passive & Noun Phrases"
THEME = "theme-passive"

LESSONS = []

# ============================================================
# LESSON 11 — Passive with combined aspects (being + p.p. / having been + p.p.)
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-11-passive-combined-aspects",
    "num": 11, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Passive With Combined Aspects",
    "subtitle": "\"Being reviewed\" and \"having been reviewed\" — passive forms that carry continuous and perfect meaning at once.",
    "warmup_intro": "You already know the basic passive (\"the report is reviewed\"). Today we combine it with continuous and perfect aspect, so the passive can also say something is in progress right now, or was already finished before something else happened.",
    "warmup": [
        {"prompt": "\"The contract is being reviewed by legal\" tells us the review is…",
         "options": [{"label": "in progress right now", "value": "right", "correct": True}, {"label": "completed and filed away", "value": "wrong", "correct": False}]},
        {"prompt": "\"Having been approved, the budget was released to the team\" tells us the approval happened…",
         "options": [{"label": "before the release, as a completed step", "value": "right", "correct": True}, {"label": "at the same moment as the release", "value": "wrong", "correct": False}]},
        {"prompt": "Which pattern combines passive with continuous aspect?",
         "options": [{"label": "being + past participle", "value": "right", "correct": True}, {"label": "to be + past participle", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "\"Being + p.p.\" = an ongoing passive process right now. \"Having been + p.p.\" = a finished passive step, usually explaining what came before the main event.",
    "diagnostic": [
        {"prompt": "The proposal ___ discussed in the boardroom as we speak.", "options": [{"label": "is being", "value": "right", "correct": True}, {"label": "is", "value": "wrong", "correct": False}]},
        {"prompt": "___ signed by both parties, the agreement finally took effect.", "options": [{"label": "Having been", "value": "right", "correct": True}, {"label": "Being", "value": "wrong", "correct": False}]},
        {"prompt": "The new servers ___ installed while the office is closed for the weekend.", "options": [{"label": "are being", "value": "right", "correct": True}, {"label": "have been", "value": "wrong", "correct": False}]},
        {"prompt": "___ delayed twice already, the launch was finally rescheduled for March.", "options": [{"label": "Having been", "value": "right", "correct": True}, {"label": "Being", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Two ways to combine passive with aspect",
        "intro": "\"Being + past participle\" adds continuous meaning to the passive — something is happening right now, done to someone or something. \"Having been + past participle\" adds perfect meaning — a passive step already finished before the next part of the sentence.",
        "tabs": [{"key": "being", "label": "Being + p.p."}, {"key": "havingbeen", "label": "Having been + p.p."}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "being": [
                {"label": "an action happening to someone/something right now", "example": "The candidates are being interviewed one by one this afternoon."},
                {"label": "an ongoing process someone notices mid-way", "example": "She realised her proposal was being rewritten without her input."},
            ],
            "havingbeen": [
                {"label": "a finished passive step, explaining what came before", "example": "Having been warned twice, he finally changed his approach."},
                {"label": "a cause or condition completed earlier in formal writing", "example": "Having been reviewed by three departments, the plan was finally approved."},
            ],
        },
        "quiz_labels": {"being": "Being + past participle", "havingbeen": "Having been + past participle"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Passive continuous: <b>is/are/was/were + being + past participle</b> — an action in progress, done to the subject.</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ Passive perfect participle: <b>having been + past participle</b> — a completed passive step before the main clause, often at the start of a sentence.</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> "having been + p.p." is a reduced clause, not a full sentence — it always needs a main clause with its own subject right after it.<br><br>
            ✅ "Having been reviewed, the report was approved." — the report is the subject of both parts.<br>
            ❌ "Having been reviewed, we approved the report." — this wrongly suggests <i>we</i> were reviewed, not the report. The reduced clause's implied subject must match the main clause's subject.<br><br>
            Meanwhile, "being + p.p." simply slots into any passive tense the way "-ing" slots into any active continuous tense — no such subject trap there.</span>
          </div>'''
    },
    "compare": {
        "title": "In progress vs. already finished",
        "instruction": "Hover over each version to see what the combined passive form adds.",
        "items": [
            {"key": "c1", "label": "Simple passive", "text": "The report is reviewed every quarter.", "explain": "A routine, repeated passive action — no sense of \"right now\" or sequence."},
            {"key": "c2", "label": "Passive + continuous", "text": "The report is being reviewed right now.", "explain": "\"Being + p.p.\" shows the review is actively in progress at this moment."},
            {"key": "c3", "label": "Passive + perfect (reduced clause)", "text": "Having been reviewed, the report was sent to the board.", "explain": "\"Having been + p.p.\" shows the review was already finished before the next step happened."},
        ]
    },
    "reading": {
        "heading": "The Bystander Effect in Office Culture",
        "passage_paragraphs": [
            f'''Social psychologists have long been fascinated by a puzzling pattern: when many people are capable of helping, each individual often ends up doing nothing. This is known as the bystander effect, and it shows up constantly in office culture, not only in emergencies. A flagged security alert {gram("g1","is being watched")} by six different inboxes at once, yet nobody clicks "resolved", because each recipient quietly assumes that someone else, {vocab("presumed","presumed")} to be more senior or more responsible, will step in.''',
            f'''The underlying mechanism is simple: responsibility becomes {vocab("diffuse","diffuse")}, spread thinly across a group instead of assigned to one person. {gram("g2","Having been copied")} on the original message, most employees feel their own {vocab("obligation","obligation")} has already been discharged, even though nothing has actually been done. An {vocab("ambiguous","ambiguous")} instruction — "someone should look into this" — only makes the diffusion worse, because no single name is ever attached to it, and the task {gram("g3","is being silently reassigned")}, again and again, to nobody in particular.''',
            f'''By the time the issue finally {gram("g4","is being escalated")} to a manager, days or even weeks may have passed. {gram("g5","Having been ignored")} by a dozen {vocab("onlookers","onlookers")}, the original complaint has usually grown into a far bigger problem than it needed to be. Researchers argue that the real fix is not to shame individuals for their {vocab("apathy","apathy")}, but to build clear {vocab("accountability","accountability")} into the system itself, so that a task is never simply {gram("g6","being left")} to whoever happens to notice it first. Without that structural change, the same {vocab("oversight","oversight")} keeps recurring, month after month, each time {gram("g7","having been quietly assumed")} — wrongly — to be someone else's job.''',
        ],
        "comprehension": [
            {"prompt": "According to the passage, why does responsibility often fail to get handled in offices, even when many people are aware of a problem?", "options": [
                {"label": "Because it becomes spread thinly across everyone, so no one person owns it.", "value": "right", "correct": True},
                {"label": "Because managers deliberately ignore all complaints they receive.", "value": "wrong", "correct": False}]},
            {"prompt": "What does an ambiguous instruction like \"someone should look into this\" tend to cause?", "options": [
                {"label": "It gets silently passed from person to person without ever being resolved.", "value": "right", "correct": True},
                {"label": "It gets immediately escalated to senior management.", "value": "wrong", "correct": False}]},
            {"prompt": "What solution do researchers suggest, according to the final paragraph?", "options": [
                {"label": "Building clear accountability with a single named owner for each task.", "value": "right", "correct": True},
                {"label": "Publicly shaming employees who ignore problems.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "presumed": {"word": "presumed", "ipa": "/prɪˈzjuːmd/", "meaning": "assumed to be true without proof", "example": "Each reader presumed someone more senior would handle it."},
            "diffuse": {"word": "diffuse", "ipa": "/dɪˈfjuːs/", "meaning": "spread out over a wide area, not concentrated", "example": "Responsibility becomes diffuse, spread thinly across a group."},
            "obligation": {"word": "obligation", "ipa": "/ˌɒb.lɪˈɡeɪ.ʃən/", "meaning": "a duty to do something", "example": "Most employees feel their obligation has already been discharged."},
            "ambiguous": {"word": "ambiguous", "ipa": "/æmˈbɪɡ.ju.əs/", "meaning": "unclear, open to more than one interpretation", "example": "An ambiguous instruction makes the diffusion worse."},
            "onlookers": {"word": "onlookers", "ipa": "/ˈɒnˌlʊk.əz/", "meaning": "people who watch an event without taking part", "example": "The complaint had been ignored by a dozen onlookers."},
            "apathy": {"word": "apathy", "ipa": "/ˈæp.ə.θi/", "meaning": "lack of interest or concern", "example": "The fix is not to shame individuals for their apathy."},
            "accountability": {"word": "accountability", "ipa": "/əˌkaʊn.təˈbɪl.ɪ.ti/", "meaning": "being responsible and answerable for one's actions", "example": "Organisations need to build clear accountability into the system."},
            "oversight": {"word": "oversight", "ipa": "/ˈəʊ.və.saɪt/", "meaning": "an unintentional failure to notice or do something", "example": "The same oversight keeps recurring month after month."},
        },
        "gram_explanations": {
            "g1": "Passive continuous (\"is being + p.p.\") — shows the watching is happening right now, by several inboxes at once.",
            "g2": "\"Having been + p.p.\" — a finished passive step (being copied) that explains why obligation feels already discharged.",
            "g3": "Passive continuous — an ongoing, repeated process of reassignment happening over time.",
            "g4": "Passive continuous — the escalation is shown as a gradual, in-progress action as days pass.",
            "g5": "\"Having been + p.p.\" — the ignoring was already complete before the complaint grew into a bigger problem.",
            "g6": "Passive continuous (negated) — \"is never simply being left\" shows an ongoing lack of ownership, not a single completed act.",
            "g7": "\"Having been + p.p.\" — each recurrence is preceded by a completed, incorrect assumption about whose job it was."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "If responsibility for a task is described as \"diffuse\", it means it is…", "options": [{"label": "spread thinly across many people rather than owned by one", "value": "right", "correct": True}, {"label": "assigned very clearly to a single person", "value": "wrong", "correct": False}, {"label": "written down in an official policy", "value": "wrong2", "correct": False}]},
            {"prompt": "An \"ambiguous\" instruction is one that…", "options": [{"label": "can be understood in more than one way", "value": "right", "correct": True}, {"label": "is extremely detailed and precise", "value": "wrong", "correct": False}, {"label": "has already been carried out", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Onlookers\" are people who…", "options": [{"label": "watch something happen without taking part", "value": "right", "correct": True}, {"label": "are directly and actively involved in solving a problem", "value": "wrong", "correct": False}, {"label": "manage a team of employees", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Apathy\" describes a feeling of…", "options": [{"label": "lack of interest or concern", "value": "right", "correct": True}, {"label": "intense enthusiasm", "value": "wrong", "correct": False}, {"label": "deep anxiety", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Accountability\" means…", "options": [{"label": "being responsible and answerable for one's actions", "value": "right", "correct": True}, {"label": "having no responsibility at all", "value": "wrong", "correct": False}, {"label": "receiving credit without doing any work", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "Everyone", "after": "someone else would deal with the complaint.", "answers": ["presumed"], "width": 110},
            {"before": "He felt his", "after": "ended the moment he forwarded the email.", "answers": ["obligation"], "width": 110},
            {"before": "The same", "after": "kept happening every single month.", "answers": ["oversight"], "width": 100},
            {"before": "A dozen", "after": "noticed the problem but did nothing about it.", "answers": ["onlookers"], "width": 100},
        ],
    },
    "practice": {
        "gapfill_focus": "passive continuous (being + p.p.) or passive perfect participle (having been + p.p.)?",
        "gapfill": [
            {"before": "The building", "after": "(renovate) while the staff work remotely.", "answers": ["is being renovated"]},
            {"before": "", "after": "(warn) three times, the contractor finally fixed the leak. (Having...)", "answers": ["Having been warned"]},
            {"before": "The invoices", "after": "(process) as we speak, so please be patient.", "answers": ["are being processed"]},
            {"before": "", "after": "(reject) once already, the proposal was rewritten from scratch. (Having...)", "answers": ["Having been rejected"]},
            {"before": "The candidates", "after": "(interview) one after another this morning.", "answers": ["are being interviewed"]},
            {"before": "", "after": "(approve) by the board, the merger finally went ahead. (Having...)", "answers": ["Having been approved"]},
        ],
        "second": {
            "type": "errorspot", "title": "Spot the mistake",
            "instruction": "One word is wrong in each sentence. Tap it, then check the correction.",
            "items": [
                {"words": ["The", "contract", "is", "being", "sign", "by", "both", "sides", "today."], "error_indices": [4], "correction": "\"sign\" → \"signed\" (is being + past participle)"},
                {"words": ["Have", "been", "approved,", "the", "budget", "was", "released", "immediately."], "error_indices": [0], "correction": "\"Have\" → \"Having\" (Having been + past participle)"},
                {"words": ["The", "servers", "was", "being", "upgraded", "over", "the", "weekend."], "error_indices": [2], "correction": "\"was\" → \"were\" (plural subject needs \"were being\")"},
            ],
        },
        "builders": [
            {"words": ["The", "report", "is", "being", "reviewed", "by", "legal", "right", "now."]},
            {"words": ["Having", "been", "approved,", "the", "budget", "was", "released."]},
            {"words": ["The", "candidates", "were", "being", "interviewed", "all", "morning."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a process at your workplace or in your studies that is currently \"being done\" (e.g. being reviewed, being redesigned, being tested), then describe a step that had to happen first, using \"having been...\".",
        "group_questions": [
            "Describe something at your workplace that is currently being changed, upgraded or reviewed.",
            "Tell your group about a decision that could only be made after something else had been checked or approved first.",
            "Have you ever waited for something \"being processed\" for far longer than expected? What happened?",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing an article about the bystander effect in office culture.",
        "dialogue": [
            {"speaker": "Anna", "line": "I just read this article about the bystander effect — apparently it happens in offices just as much as in emergencies."},
            {"speaker": "Tomasz", "line": "Oh, like when an alert is being watched by five different inboxes and nobody actually clicks resolve?"},
            {"speaker": "Anna", "line": "Exactly that. Everyone presumed someone more senior would handle it."},
            {"speaker": "Tomasz", "line": "That explains so much. Having been copied on an email, I always assume my part is basically done."},
            {"speaker": "Anna", "line": "Right, and that's exactly the problem — responsibility becomes so diffuse that nobody actually owns it."},
            {"speaker": "Tomasz", "line": "So what's the fix? Just tell people to care more?"},
            {"speaker": "Anna", "line": "No, apparently that doesn't work. The article says you need real accountability — one named person responsible for each task."},
            {"speaker": "Tomasz", "line": "Makes sense. Otherwise the same oversight just keeps repeating, month after month."},
        ],
        "comprehension": [
            {"prompt": "What does Tomasz compare to the bystander effect example from the article?", "options": [{"label": "A security alert being watched by many inboxes without anyone resolving it.", "value": "right", "correct": True}, {"label": "A fire alarm going off in an empty building.", "value": "wrong", "correct": False}]},
            {"prompt": "According to Anna, why doesn't simply telling people to \"care more\" fix the problem?", "options": [{"label": "Because real accountability, not just concern, is what's actually needed.", "value": "right", "correct": True}, {"label": "Because most employees already care too much.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Tomasz say happens without a fix?", "options": [{"label": "The same oversight keeps repeating month after month.", "value": "right", "correct": True}, {"label": "The company loses money every single day.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "The kitchen ___ renovated while the restaurant is closed.", "options": [{"label": "is being", "value": "right", "correct": True}, {"label": "is", "value": "wrong", "correct": False}]},
        {"prompt": "___ tested twice already, the app was finally released.", "options": [{"label": "Having been", "value": "right", "correct": True}, {"label": "Being", "value": "wrong", "correct": False}]},
        {"prompt": "The applications ___ reviewed one by one this week.", "options": [{"label": "are being", "value": "right", "correct": True}, {"label": "have been", "value": "wrong", "correct": False}]},
        {"prompt": "___ delayed by the strike, the shipment finally arrived on Friday.", "options": [{"label": "Having been", "value": "right", "correct": True}, {"label": "Being", "value": "wrong", "correct": False}]},
        {"prompt": "The new policy ___ rolled out to every branch this month.", "options": [{"label": "is being", "value": "right", "correct": True}, {"label": "was", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 12 — Impersonal passive & get-passive together
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-12-impersonal-get-passive",
    "num": 12, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Impersonal Passive & Get-Passive Together",
    "subtitle": "\"It is said that...\", \"he is believed to have...\", and when \"get\" beats \"be\" in the passive.",
    "warmup_intro": "The impersonal passive (\"it is said that...\", \"he is believed to have...\") lets us report opinions or rumours without naming who holds them. The get-passive (\"got fired\", \"got promoted\") is a more informal alternative to \"be\", often used for sudden or unwelcome changes.",
    "warmup": [
        {"prompt": "\"It is believed that the merger will go ahead\" avoids naming…",
         "options": [{"label": "who exactly believes this", "value": "right", "correct": True}, {"label": "what the merger involves", "value": "wrong", "correct": False}]},
        {"prompt": "\"He is thought to have resigned voluntarily\" is a more formal way of saying…",
         "options": [{"label": "people think he resigned voluntarily", "value": "right", "correct": True}, {"label": "he definitely resigned voluntarily", "value": "wrong", "correct": False}]},
        {"prompt": "\"She got promoted last month\" sounds more…",
         "options": [{"label": "informal and conversational than \"was promoted\"", "value": "right", "correct": True}, {"label": "official and legally binding than \"was promoted\"", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "Impersonal passive = formal, source hidden on purpose. Get-passive = informal, often for changes of state, especially unwelcome or sudden ones.",
    "diagnostic": [
        {"prompt": "___ that the company is planning layoffs.", "options": [{"label": "It is rumoured", "value": "right", "correct": True}, {"label": "It rumours", "value": "wrong", "correct": False}]},
        {"prompt": "The manager ___ have approved the request without checking the budget.", "options": [{"label": "is thought to", "value": "right", "correct": True}, {"label": "is thinking to", "value": "wrong", "correct": False}]},
        {"prompt": "He ___ fired after the scandal broke.", "options": [{"label": "got", "value": "right", "correct": True}, {"label": "got to", "value": "wrong", "correct": False}]},
        {"prompt": "___ that the negotiations collapsed over pricing, not delivery.", "options": [{"label": "It is understood", "value": "right", "correct": True}, {"label": "It understands", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Hiding the source vs. choosing an informal tone",
        "intro": "The impersonal passive reports beliefs, rumours or claims without naming a source — useful in news and formal writing. The get-passive is an informal alternative to \"be + p.p.\", often implying something sudden, unexpected, or affecting the subject personally.",
        "tabs": [{"key": "impersonal", "label": "Impersonal Passive"}, {"key": "get", "label": "Get-Passive"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "impersonal": [
                {"label": "it is + past participle + that-clause", "example": "It is understood that talks will resume next week."},
                {"label": "subject + is/are + past participle + to-infinitive", "example": "The CEO is said to be considering early retirement."},
            ],
            "get": [
                {"label": "an informal, often sudden change of state", "example": "Two managers got promoted in the same week."},
                {"label": "something unwelcome happening to the subject", "example": "The whole department got restructured overnight."},
            ],
        },
        "quiz_labels": {"impersonal": "Impersonal passive", "get": "Get-passive"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Impersonal passive: <b>It is + p.p. + that...</b> or <b>subject + is/are + p.p. + to-infinitive</b> — reports a claim, belief or rumour with no named source.</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ Get-passive: <b>get/got + past participle</b> — an informal alternative to \"be\", often for sudden, unwelcome or dynamic changes.</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> get-passive doesn't work with every verb, and it sounds distinctly informal — never use it in a formal report or academic writing.<br><br>
            ✅ "She got promoted." — natural, informal, common in spoken English.<br>
            ✅ "She was promoted." — the neutral, formal equivalent, used in reports and official announcements.<br>
            ❌ "It is got said that..." — get-passive never combines with impersonal "it" constructions; those stay strictly with "be".<br><br>
            Rule of thumb: reach for "get" in casual speech about personal change, and "be" (plain or impersonal) everywhere formal.</span>
          </div>'''
    },
    "compare": {
        "title": "Formal claim vs. informal change",
        "instruction": "Hover over each to see the difference in register and meaning.",
        "items": [
            {"key": "c1", "label": "Impersonal passive", "text": "It is believed that the CFO will step down by June.", "explain": "Formal, source deliberately unnamed — typical of news reporting."},
            {"key": "c2", "label": "Be-passive (neutral)", "text": "The proposal was rejected by the board.", "explain": "Neutral, standard passive — no particular emotional colouring."},
            {"key": "c3", "label": "Get-passive (informal)", "text": "The proposal got rejected by the board.", "explain": "Same event, but more informal and conversational, sometimes implying frustration or surprise."},
        ]
    },
    "reading": {
        "heading": "Confirmation Bias in Hiring Decisions",
        "passage_paragraphs": [
            f'''{gram("g1","It is widely believed")} that hiring decisions are the product of careful, objective comparison, but researchers who study interviews describe something far less rational. An interviewer typically forms a strong {vocab("impression","impression")} of a candidate within the first few minutes, often {vocab("unconsciously","unconsciously")}, and everything that follows tends to be read through that initial {vocab("lens","lens")}.''',
            f'''This pattern is known as confirmation bias, and once it takes hold, the rest of the interview quietly becomes a search for evidence supporting the first impression rather than a genuine test of it. A candidate who built early {vocab("rapport","rapport")} with the interviewer {gram("g2","is said to")} handle pressure well and think on their feet, even when the actual answers are fairly ordinary. A candidate who struck the interviewer badly, by contrast, {gram("g3","is believed to have")} performed poorly overall, regardless of how strong the individual answers actually were. Small, ambiguous moments in the conversation — a pause, a nervous laugh — {gram("g4","get interpreted")} in whichever direction the first impression has already {vocab("skewed","skewed")} the interviewer's judgement.''',
            f'''A related phenomenon, the {vocab("halo","halo")} effect, makes the bias even stronger: an interviewer who is impressed by one strong quality — confidence, a firm handshake, a shared hobby — tends to assume every other quality is equally impressive. As a result, some genuinely strong candidates {gram("g5","get overlooked")} simply because they made a flat first impression, while a confident but underqualified candidate sometimes {gram("g6","gets hired")} instead. {gram("g7","It is now recommended")} by most hiring specialists that interviewers use structured scoring sheets and delay their overall judgement until every candidate's {vocab("credentials","credentials")} have been reviewed side by side, precisely to stop the first few minutes from {vocab("overshadowing","overshadowing")} everything that comes after.''',
        ],
        "comprehension": [
            {"prompt": "According to researchers described in the passage, what actually drives many interview decisions, despite common belief?", "options": [
                {"label": "An early, often unconscious first impression that later evidence is read through.", "value": "right", "correct": True},
                {"label": "A completely objective, checklist-based comparison of every candidate.", "value": "wrong", "correct": False}]},
            {"prompt": "What tends to happen to a candidate who makes a strong early impression, according to the passage?", "options": [
                {"label": "Their ordinary answers tend to get reinterpreted more favourably.", "value": "right", "correct": True},
                {"label": "Their application is automatically rejected without review.", "value": "wrong", "correct": False}]},
            {"prompt": "What do hiring specialists now recommend, according to the final paragraph?", "options": [
                {"label": "Using structured scoring sheets and delaying overall judgement.", "value": "right", "correct": True},
                {"label": "Relying more heavily on a candidate's handshake and confidence.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "impression": {"word": "impression", "ipa": "/ɪmˈpreʃ.ən/", "meaning": "an idea or opinion formed quickly about someone", "example": "The interviewer formed a strong impression within minutes."},
            "unconsciously": {"word": "unconsciously", "ipa": "/ʌnˈkɒn.ʃəs.li/", "meaning": "without being aware of it", "example": "Most interviewers do this completely unconsciously."},
            "lens": {"word": "lens", "ipa": "/lenz/", "meaning": "a particular way of viewing or interpreting something", "example": "Everything afterward is read through that same lens."},
            "rapport": {"word": "rapport", "ipa": "/ræˈpɔːr/", "meaning": "a friendly relationship built on mutual understanding", "example": "The candidate built early rapport with the interviewer."},
            "skewed": {"word": "skewed", "ipa": "/skjuːd/", "meaning": "distorted or biased in a particular direction", "example": "The first impression had already skewed the interviewer's judgement."},
            "halo": {"word": "halo", "ipa": "/ˈheɪ.ləʊ/", "meaning": "(in \"the halo effect\") a tendency for one positive quality to influence overall judgement", "example": "The halo effect makes the bias even stronger."},
            "credentials": {"word": "credentials", "ipa": "/krɪˈden.ʃəlz/", "meaning": "qualifications or experience that prove someone's suitability", "example": "Every candidate's credentials should be reviewed side by side."},
            "overshadowing": {"word": "overshadowing", "ipa": "/ˌəʊ.vəˈʃæd.əʊ.ɪŋ/", "meaning": "making something seem less important by comparison", "example": "Structured scoring stops the first minutes from overshadowing everything else."},
        },
        "gram_explanations": {
            "g1": "Impersonal passive — \"It is widely believed that...\" reports a common assumption without naming who holds it.",
            "g2": "Impersonal passive — \"subject + is said to + infinitive\" reports an assumed quality without naming a source.",
            "g3": "Impersonal passive — \"subject + is believed to have + p.p.\" reports a belief about something in the past.",
            "g4": "Get-passive — informal, dynamic, highlights the moment ambiguous behaviour gets (mis)read.",
            "g5": "Get-passive — informal, implies an unwelcome, often unfair outcome for strong candidates.",
            "g6": "Get-passive — informal, parallel to \"get overlooked\", showing the flip side of the same bias.",
            "g7": "Impersonal passive — \"It is now recommended that...\" reports a shared professional recommendation with no single named source."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "\"Rapport\" refers to…", "options": [{"label": "a friendly relationship built on mutual understanding", "value": "right", "correct": True}, {"label": "a formal written contract", "value": "wrong", "correct": False}, {"label": "a scheduled follow-up interview", "value": "wrong2", "correct": False}]},
            {"prompt": "The \"halo\" effect describes how…", "options": [{"label": "one positive quality can make someone assume everything else about a person is also positive", "value": "right", "correct": True}, {"label": "a bad first impression is always accurate", "value": "wrong", "correct": False}, {"label": "interviews are recorded for staff training", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Credentials\" are…", "options": [{"label": "qualifications or experience that prove someone is suitable", "value": "right", "correct": True}, {"label": "personal opinions with no evidence behind them", "value": "wrong", "correct": False}, {"label": "informal notes taken during a meeting", "value": "wrong2", "correct": False}]},
            {"prompt": "If one factor is \"overshadowing\" everything else, it is…", "options": [{"label": "making everything else seem less important by comparison", "value": "right", "correct": True}, {"label": "being completely ignored by everyone", "value": "wrong", "correct": False}, {"label": "being carefully measured and scored", "value": "wrong2", "correct": False}]},
            {"prompt": "If a judgement has been \"skewed\", it has been…", "options": [{"label": "distorted or pulled in a particular direction", "value": "right", "correct": True}, {"label": "checked and confirmed as accurate", "value": "wrong", "correct": False}, {"label": "delayed until more evidence arrives", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "The interviewer formed a strong", "after": "within the first two minutes.", "answers": ["impression"], "width": 110},
            {"before": "Most interviewers do this completely", "after": ", without even realising it.", "answers": ["unconsciously"], "width": 130},
            {"before": "Everything afterward gets read through that same", "after": ".", "answers": ["lens"], "width": 80},
            {"before": "A firm handshake ended up", "after": "the rest of the interview.", "answers": ["overshadowing"], "width": 130},
        ],
    },
    "practice": {
        "gapfill_focus": "impersonal passive or get-passive?",
        "gapfill": [
            {"before": "", "after": "(believe) that the company will announce layoffs soon. (It...)", "answers": ["It is believed"]},
            {"before": "She", "after": "(get/fire) without any warning at all.", "answers": ["got fired"]},
            {"before": "The director", "after": "(think) to have known about the plan for months.", "answers": ["is thought"]},
            {"before": "He", "after": "(get/promote) twice in a single year.", "answers": ["got promoted"]},
            {"before": "", "after": "(understand) that the talks broke down over pricing. (It...)", "answers": ["It is understood"]},
            {"before": "The whole team", "after": "(get/reorganise) after the merger.", "answers": ["got reorganised"]},
        ],
        "second": {
            "type": "categorise", "title": "Impersonal passive or get-passive?",
            "instruction": "Decide which pattern each sentence uses.",
            "categories": ["Impersonal passive (formal, hides the source)", "Get-passive (informal, dynamic change)"],
            "items": [
                {"prompt": "\"It is said that the CEO will resign by summer.\"", "correct": "Impersonal passive (formal, hides the source)"},
                {"prompt": "\"He got moved to a completely different team overnight.\"", "correct": "Get-passive (informal, dynamic change)"},
                {"prompt": "\"She is believed to have leaked the information.\"", "correct": "Impersonal passive (formal, hides the source)"},
                {"prompt": "\"The whole office got soaked when the pipe burst.\"", "correct": "Get-passive (informal, dynamic change)"},
            ],
        },
        "builders": [
            {"words": ["It", "is", "rumoured", "that", "layoffs", "are", "coming."]},
            {"words": ["He", "is", "believed", "to", "have", "resigned", "voluntarily."]},
            {"words": ["She", "got", "promoted", "twice", "in", "one", "year."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a rumour or piece of office gossip you've heard (real or invented), using at least one impersonal passive construction (\"it is said/believed/rumoured that...\") and one get-passive.",
        "group_questions": [
            "Have you ever heard a workplace rumour that turned out to be true? What was it?",
            "Tell your group about someone who \"got promoted\" or \"got moved\" unexpectedly.",
            "Why might a company prefer to say \"it is believed that...\" rather than naming exactly who believes something?",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are comparing notes after sitting in on the same round of job interviews.",
        "dialogue": [
            {"speaker": "Anna", "line": "So what did you think of the candidate this morning? Everyone in the room seemed to love her instantly."},
            {"speaker": "Tomasz", "line": "Yeah, it's said that first impressions form within the first few minutes, and honestly that's exactly what happened."},
            {"speaker": "Anna", "line": "True. After that, every slightly awkward pause got interpreted as thoughtfulness instead of nerves."},
            {"speaker": "Tomasz", "line": "Meanwhile the candidate before her got overlooked completely, even though his answers were arguably stronger."},
            {"speaker": "Anna", "line": "He's believed to have frozen a little at the start, and nobody really recovered from that impression of him."},
            {"speaker": "Tomasz", "line": "It's a textbook halo effect, isn't it? One good moment and suddenly everything else looks impressive too."},
            {"speaker": "Anna", "line": "It is now recommended we use a proper scoring sheet next time, so it's less about gut feeling."},
            {"speaker": "Tomasz", "line": "Agreed. Otherwise a strong candidate keeps getting hired for the wrong reasons, or not hired at all."},
        ],
        "comprehension": [
            {"prompt": "What does Tomasz say happened to the candidate interviewed before the one everyone loved?", "options": [{"label": "He got overlooked, even though his answers were arguably stronger.", "value": "right", "correct": True}, {"label": "He was hired immediately after his interview.", "value": "wrong", "correct": False}]},
            {"prompt": "According to Anna, how did the panel interpret the successful candidate's awkward pauses?", "options": [{"label": "As thoughtfulness rather than nerves.", "value": "right", "correct": True}, {"label": "As a clear sign she wasn't prepared.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Anna suggest doing differently next time?", "options": [{"label": "Using a proper scoring sheet instead of relying on gut feeling.", "value": "right", "correct": True}, {"label": "Interviewing every candidate twice.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "___ that the merger will be announced next week.", "options": [{"label": "It is rumoured", "value": "right", "correct": True}, {"label": "It rumours", "value": "wrong", "correct": False}]},
        {"prompt": "The manager ___ have known about the leak beforehand.", "options": [{"label": "is thought to", "value": "right", "correct": True}, {"label": "is thinking to", "value": "wrong", "correct": False}]},
        {"prompt": "She ___ promoted twice within a year.", "options": [{"label": "got", "value": "right", "correct": True}, {"label": "got to", "value": "wrong", "correct": False}]},
        {"prompt": "___ that the two companies will merge by autumn.", "options": [{"label": "It is understood", "value": "right", "correct": True}, {"label": "It understands", "value": "wrong", "correct": False}]},
        {"prompt": "He ___ fired after the audit revealed the errors.", "options": [{"label": "got", "value": "right", "correct": True}, {"label": "was got", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 13 — Nominalisation
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-13-nominalisation",
    "num": 13, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Nominalisation",
    "subtitle": "Turning verbs and adjectives into nouns for a more formal, impersonal, report-like style.",
    "warmup_intro": "Nominalisation means turning a verb or adjective into a noun — \"they decided\" becomes \"the decision was made\", \"implement\" becomes \"implementation\". It's one of the biggest markers of formal, academic and business writing.",
    "warmup": [
        {"prompt": "\"They decided to expand the team\" nominalised becomes…",
         "options": [{"label": "\"A decision was made to expand the team.\"", "value": "right", "correct": True}, {"label": "\"They will decide to expand the team.\"", "value": "wrong", "correct": False}]},
        {"prompt": "Nominalisation tends to make writing sound more…",
         "options": [{"label": "formal and impersonal", "value": "right", "correct": True}, {"label": "casual and conversational", "value": "wrong", "correct": False}]},
        {"prompt": "The noun form of \"implement\" (a verb) is…",
         "options": [{"label": "implementation", "value": "right", "correct": True}, {"label": "implementing-ness", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "If you can replace a verb or adjective with an -ion/-ment/-ness/-ity noun and add a supporting verb like \"make\", \"reach\" or \"undergo\", you're nominalising.",
    "diagnostic": [
        {"prompt": "\"We will assess the risks\" nominalised: \"An assessment of the risks ___ conducted.\"", "options": [{"label": "will be", "value": "right", "correct": True}, {"label": "will has", "value": "wrong", "correct": False}]},
        {"prompt": "The noun form of \"analyse\" is…", "options": [{"label": "analysis", "value": "right", "correct": True}, {"label": "analysement", "value": "wrong", "correct": False}]},
        {"prompt": "The noun form of \"significant\" (adjective) is…", "options": [{"label": "significance", "value": "right", "correct": True}, {"label": "significantness", "value": "wrong", "correct": False}]},
        {"prompt": "\"They failed to meet the deadline\" nominalised: \"There was a ___ to meet the deadline.\"", "options": [{"label": "failure", "value": "right", "correct": True}, {"label": "failing", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Verbs and adjectives packed into nouns",
        "intro": "Formal reports often turn actions and qualities into noun phrases, then attach a light supporting verb (make, reach, undergo, conduct, carry out). This shifts focus from who did what to the process or result itself.",
        "tabs": [{"key": "verb", "label": "Verb → Noun"}, {"key": "adj", "label": "Adjective → Noun"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "verb": [
                {"label": "decide → decision", "example": "A decision was reached after three hours of debate."},
                {"label": "implement → implementation", "example": "Implementation of the new system began in April."},
                {"label": "analyse → analysis", "example": "A detailed analysis of the figures followed."},
            ],
            "adj": [
                {"label": "significant → significance", "example": "The significance of the finding was discussed at length."},
                {"label": "efficient → efficiency", "example": "Efficiency improved noticeably after the restructuring."},
                {"label": "aware → awareness", "example": "Awareness of the new policy is now widespread."},
            ],
        },
        "quiz_labels": {"verb": "Verb → noun", "adj": "Adjective → noun"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Verb → noun: <b>-ion, -ment, -al, -ure</b> (decide→decision, implement→implementation, arrive→arrival, fail→failure).</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ Adjective → noun: <b>-ity, -ness, -ance/-ence</b> (significant→significance, aware→awareness, efficient→efficiency).</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> nominalisation isn't just a vocabulary swap — it also changes the sentence's grammar, usually shifting from an active subject-verb-object to a passive or "there was/is a..." structure with a light verb.<br><br>
            ✅ "They implemented the policy quickly." → "The implementation of the policy was swift." (subject shifts from "they" to the process itself)<br>
            ✅ Overusing nominalisation makes writing feel dense and impersonal — perfect for a formal report, wrong for a friendly email.<br><br>
            Use it deliberately: when you want to sound objective and process-focused, not when you're just trying to sound smart.</span>
          </div>'''
    },
    "compare": {
        "title": "Active verb vs. nominalised noun phrase",
        "instruction": "Hover over each to see the shift in focus and formality.",
        "items": [
            {"key": "c1", "label": "Active, personal", "text": "The board decided to approve the merger.", "explain": "Direct, active, names the agent (\"the board\") clearly."},
            {"key": "c2", "label": "Nominalised, formal", "text": "The decision to approve the merger was made by the board.", "explain": "The noun phrase \"the decision\" becomes the focus; more formal, slightly more distant."},
            {"key": "c3", "label": "Fully impersonal", "text": "A decision was made to approve the merger.", "explain": "The agent disappears entirely — common in minutes, reports and official statements."},
        ]
    },
    "reading": {
        "heading": "The Peter Principle: Promoted Beyond Competence",
        "passage_paragraphs": [
            f'''In many organisations, an employee's {gram("g1","promotion")} is treated as straightforward proof of merit: strong performance in one role is assumed to guarantee success in the next. The Peter Principle, first proposed decades ago, challenges that assumption directly. Following extended {gram("g2","observation")} of {vocab("hierarchical","hierarchical")} companies, the theory concludes that employees tend to rise until they reach a position in which they are no longer competent, and then remain there indefinitely, since further advancement effectively stops.''',
            f'''The logic behind this pattern is simple, if uncomfortable. {gram("g3","Selection")} for a new role is based almost entirely on {vocab("proficiency","proficiency")} in the current one, even though the two positions often demand entirely different skills. A brilliant {vocab("technician","technician")} may show excellent attention to detail, qualities that lead naturally to a move into management — a role that instead requires {gram("g4","delegation")}, negotiation and {vocab("interpersonal","interpersonal")} judgement, skills the technician was never actually tested on. The {gram("g5","assessment")} behind that move, in other words, measured entirely the wrong thing.''',
            f'''Once {vocab("installed","installed")} in a role beyond their competence, the newly promoted employee typically produces weaker results than before, yet organisations rarely reverse the {gram("g6","decision")}. A formal {vocab("demotion","demotion")} is administratively awkward and can look like a public admission of failure, so the underperforming manager is usually left exactly where they are, contributing to a slow {gram("g7","stagnation")} across the whole {vocab("workforce","workforce")}, as talented staff below them wait indefinitely for a vacancy that never opens. The {vocab("incompetence","incompetence")} the theory describes, then, is less an individual failing than a structural one, built into how promotions are decided in the first place.''',
        ],
        "comprehension": [
            {"prompt": "According to the Peter Principle, what determines whether someone gets promoted?", "options": [
                {"label": "Performance in their current role, even if the new role needs different skills.", "value": "right", "correct": True},
                {"label": "A formal test of the skills the new position actually requires.", "value": "wrong", "correct": False}]},
            {"prompt": "Why does the passage say organisations rarely reverse a bad promotion?", "options": [
                {"label": "A formal demotion looks like a public admission of failure.", "value": "right", "correct": True},
                {"label": "It is against the law to demote an employee once promoted.", "value": "wrong", "correct": False}]},
            {"prompt": "What does the passage say the resulting stagnation affects?", "options": [
                {"label": "Talented staff below who wait indefinitely for a vacancy.", "value": "right", "correct": True},
                {"label": "Only the company's overall profits.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "hierarchical": {"word": "hierarchical", "ipa": "/ˌhaɪ.əˈrɑː.kɪ.kəl/", "meaning": "organised into ranks or levels of authority", "example": "The theory was developed by observing hierarchical companies."},
            "proficiency": {"word": "proficiency", "ipa": "/prəˈfɪʃ.ən.si/", "meaning": "a high level of skill or competence", "example": "Selection is based almost entirely on proficiency in the current role."},
            "technician": {"word": "technician", "ipa": "/tekˈnɪʃ.ən/", "meaning": "someone skilled in the practical or mechanical side of a job", "example": "A brilliant technician may struggle in a management role."},
            "interpersonal": {"word": "interpersonal", "ipa": "/ˌɪn.təˈpɜː.sən.əl/", "meaning": "relating to relationships and interaction between people", "example": "Management requires delegation and interpersonal judgement."},
            "installed": {"word": "installed", "ipa": "/ɪnˈstɔːld/", "meaning": "placed or fixed into a position", "example": "Once installed in the role, results usually got worse."},
            "demotion": {"word": "demotion", "ipa": "/dɪˈməʊ.ʃən/", "meaning": "a move to a lower rank or position", "example": "A formal demotion is administratively awkward."},
            "workforce": {"word": "workforce", "ipa": "/ˈwɜːk.fɔːs/", "meaning": "all the people who work for an organisation", "example": "Stagnation spreads slowly across the whole workforce."},
            "incompetence": {"word": "incompetence", "ipa": "/ɪnˈkɒm.pɪ.təns/", "meaning": "lack of the skill needed to do something well", "example": "The incompetence the theory describes is structural, not personal."},
        },
        "gram_explanations": {
            "g1": "Nominalisation of \"promote\" → \"promotion\" — shifts focus from an active decision-maker to the process/event itself, typical of report-register writing.",
            "g2": "Nominalisation of \"observe\" → \"observation\" — turns the act of observing into an abstract noun, paired with \"following\".",
            "g3": "Nominalisation of \"select\" → \"selection\" — heads the sentence as an abstract process, removing any named decision-maker.",
            "g4": "Nominalisation of \"delegate\" → \"delegation\" — a formal noun naming a required skill, instead of describing someone delegating.",
            "g5": "Nominalisation of \"assess\" → \"assessment\" — the evaluative act becomes a noun that itself \"measured\" something, a hallmark of impersonal report style.",
            "g6": "Nominalisation of \"decide\" → \"decision\", paired with the light verb \"reverse\" — a noun standing in for an active choice.",
            "g7": "Nominalisation of \"stagnate\" → \"stagnation\" — turns a gradual process into an abstract noun functioning as the sentence's object."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "A \"hierarchical\" organisation is one that is…", "options": [{"label": "organised into ranks or levels of authority", "value": "right", "correct": True}, {"label": "run entirely without any managers", "value": "wrong", "correct": False}, {"label": "focused only on remote work", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Proficiency\" means…", "options": [{"label": "a high level of skill or competence", "value": "right", "correct": True}, {"label": "a complete lack of experience", "value": "wrong", "correct": False}, {"label": "a formal job title", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Interpersonal\" skills relate to…", "options": [{"label": "relationships and interaction between people", "value": "right", "correct": True}, {"label": "technical knowledge of machinery", "value": "wrong", "correct": False}, {"label": "financial planning and budgeting", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"demotion\" is…", "options": [{"label": "a move to a lower rank or position", "value": "right", "correct": True}, {"label": "a move to a higher rank or position", "value": "wrong", "correct": False}, {"label": "a temporary period of leave", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Incompetence\" means…", "options": [{"label": "a lack of the skill needed to do something well", "value": "right", "correct": True}, {"label": "an unusually high level of skill", "value": "wrong", "correct": False}, {"label": "a formal complaint procedure", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "The promotion was based purely on his", "after": "in the previous role.", "answers": ["proficiency"], "width": 110},
            {"before": "A skilled", "after": "was promoted into a management role he wasn't suited for.", "answers": ["technician"], "width": 100},
            {"before": "Talented staff across the", "after": "waited years for a vacancy.", "answers": ["workforce"], "width": 100},
            {"before": "Once", "after": "in the role, he was rarely moved again.", "answers": ["installed"], "width": 90},
        ],
    },
    "practice": {
        "gapfill_focus": "nominalisation — turn the verb/adjective in brackets into its noun form.",
        "gapfill": [
            {"before": "The", "after": "(analyse) of the data took nearly a week.", "answers": ["analysis"]},
            {"before": "The board reached a", "after": "(decide) by Friday afternoon.", "answers": ["decision"]},
            {"before": "The", "after": "(significant) of the results was discussed at length.", "answers": ["significance"]},
            {"before": "", "after": "(implement) of the new policy begins next month. (Capitalised noun)", "answers": ["Implementation"]},
            {"before": "There has been a noticeable improvement in", "after": "(efficient) since the changes.", "answers": ["efficiency"]},
            {"before": "The company's", "after": "(fail) to meet the deadline caused real concern.", "answers": ["failure"]},
        ],
        "second": {
            "type": "categorise", "title": "Verb-based or adjective-based nominalisation?",
            "instruction": "Decide whether each noun in bold comes from a verb or from an adjective.",
            "categories": ["From a verb", "From an adjective"],
            "items": [
                {"prompt": "\"The **implementation** of the plan began in April.\"", "correct": "From a verb"},
                {"prompt": "\"The **significance** of the finding surprised everyone.\"", "correct": "From an adjective"},
                {"prompt": "\"A thorough **assessment** was carried out by the board.\"", "correct": "From a verb"},
                {"prompt": "\"There is growing **awareness** of the issue among staff.\"", "correct": "From an adjective"},
            ],
        },
        "builders": [
            {"words": ["A", "decision", "was", "made", "to", "approve", "the", "merger."]},
            {"words": ["Implementation", "of", "the", "policy", "begins", "next", "month."]},
            {"words": ["The", "significance", "of", "the", "results", "was", "emphasised."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a recent decision or change at your workplace or school using at least three nominalised nouns (e.g. decision, implementation, assessment, significance, awareness).",
        "group_questions": [
            "Why might a company prefer to write \"a decision was made\" rather than \"we decided\" in an official report?",
            "Describe a restructuring, reorganisation or major change you've experienced or heard about.",
            "Do you think overly formal, nominalised writing makes a report sound more trustworthy, or just harder to read? Discuss.",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing a colleague's promotion over lunch.",
        "dialogue": [
            {"speaker": "Anna", "line": "Have you heard of the Peter Principle? I think it explains exactly what happened with our new team lead."},
            {"speaker": "Tomasz", "line": "The idea that people get promoted until they're no longer competent? Yeah, I've read about it."},
            {"speaker": "Anna", "line": "Exactly. His promotion was based entirely on how good he was as a technician, not as a manager."},
            {"speaker": "Tomasz", "line": "Right, and delegation and interpersonal skills weren't even part of the assessment."},
            {"speaker": "Anna", "line": "Now the whole team is struggling because he's clearly out of his depth."},
            {"speaker": "Tomasz", "line": "But a formal demotion would look terrible for the company, so nobody wants to reverse the decision."},
            {"speaker": "Anna", "line": "Meanwhile the workforce underneath him just sits there, waiting for a vacancy that never opens."},
            {"speaker": "Tomasz", "line": "It's a slow stagnation, exactly like the theory describes."},
        ],
        "comprehension": [
            {"prompt": "What was the new team lead's promotion based on, according to Anna?", "options": [{"label": "How good he was as a technician, not as a manager.", "value": "right", "correct": True}, {"label": "His interpersonal and delegation skills.", "value": "wrong", "correct": False}]},
            {"prompt": "Why does Tomasz say the company won't reverse the decision?", "options": [{"label": "A formal demotion would look bad for the company.", "value": "right", "correct": True}, {"label": "It would be illegal to demote him.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Anna say is happening to the workforce underneath him?", "options": [{"label": "They are waiting for a vacancy that never opens.", "value": "right", "correct": True}, {"label": "They are all being promoted ahead of schedule.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "The noun form of \"decide\" is…", "options": [{"label": "decision", "value": "right", "correct": True}, {"label": "decidement", "value": "wrong", "correct": False}]},
        {"prompt": "The noun form of \"aware\" is…", "options": [{"label": "awareness", "value": "right", "correct": True}, {"label": "awarement", "value": "wrong", "correct": False}]},
        {"prompt": "\"They implemented the plan quickly\" nominalised: \"___ of the plan was swift.\"", "options": [{"label": "Implementation", "value": "right", "correct": True}, {"label": "Implement", "value": "wrong", "correct": False}]},
        {"prompt": "The noun form of \"significant\" is…", "options": [{"label": "significance", "value": "right", "correct": True}, {"label": "significantness", "value": "wrong", "correct": False}]},
        {"prompt": "\"They failed to deliver on time\" nominalised: \"There was a ___ to deliver on time.\"", "options": [{"label": "failure", "value": "right", "correct": True}, {"label": "failing", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 14 — Advanced articles & quantifiers
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-14-advanced-articles-quantifiers",
    "num": 14, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Advanced Articles & Quantifiers",
    "subtitle": "Generic articles for generalisations, and formal quantifiers like \"a number of\" and \"the majority of\".",
    "warmup_intro": "Articles (a/the/zero) can describe whole categories, not just individual things — \"a manager should listen\" or \"the smartphone changed everything\" are generalisations. Formal quantifiers like \"a number of\", \"a great deal of\" and \"the majority of\" add precision to those generalisations.",
    "warmup": [
        {"prompt": "\"The computer has transformed the modern office\" uses \"the\" to talk about…",
         "options": [{"label": "computers in general, as an invention", "value": "right", "correct": True}, {"label": "one specific computer in that office", "value": "wrong", "correct": False}]},
        {"prompt": "\"Few employees complained\" (with plain \"few\") suggests…",
         "options": [{"label": "almost none did, a negative sense", "value": "right", "correct": True}, {"label": "quite a lot did, a positive sense", "value": "wrong", "correct": False}]},
        {"prompt": "\"A few employees complained\" suggests…",
         "options": [{"label": "some did, a small but notable number", "value": "right", "correct": True}, {"label": "almost none did at all", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "\"Few/little\" (no article) = almost none, a negative feel. \"A few/a little\" = some, a positive or neutral feel. The difference is entirely in that one small word \"a\".",
    "diagnostic": [
        {"prompt": "___ smartphone has changed how we communicate at work.", "options": [{"label": "The", "value": "right", "correct": True}, {"label": "A the", "value": "wrong", "correct": False}]},
        {"prompt": "___ of employees surveyed said they preferred remote work.", "options": [{"label": "The majority", "value": "right", "correct": True}, {"label": "The majorities", "value": "wrong", "correct": False}]},
        {"prompt": "There was ___ interest in the proposal, so it was quietly dropped.", "options": [{"label": "little", "value": "right", "correct": True}, {"label": "a little", "value": "wrong", "correct": False}]},
        {"prompt": "___ candidates had the exact skill set the role required.", "options": [{"label": "A number of", "value": "right", "correct": True}, {"label": "A number", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Talking about categories, and measuring amounts precisely",
        "intro": "Generic articles let us make broad statements about a whole class of things. Formal quantifiers add precision to how much or how many, and are especially common in reports, surveys and academic writing.",
        "tabs": [{"key": "generic", "label": "Generic Articles"}, {"key": "quant", "label": "Formal Quantifiers"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "generic": [
                {"label": "the + singular noun, for an invention/category as a whole", "example": "The internet has reshaped global business."},
                {"label": "a/an + singular noun, for any typical member of a category", "example": "A good manager listens before making decisions."},
                {"label": "zero article + plural/uncountable noun, for a category in general", "example": "Employees value flexibility more than ever."},
            ],
            "quant": [
                {"label": "a number of / a great deal of — a fairly large amount, formal", "example": "A number of clients raised the same concern."},
                {"label": "few / little vs. a few / a little — negative vs. positive amount", "example": "Few candidates met every requirement; a few came close."},
                {"label": "the majority of — most of a group, formal", "example": "The majority of staff supported the change."},
            ],
        },
        "quiz_labels": {"generic": "Generic articles", "quant": "Formal quantifiers"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Generic reference: <b>the + singular</b> (inventions/species), <b>a/an + singular</b> (any typical example), or <b>zero article + plural/uncountable</b> (general category).</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ Formal quantifiers: <b>a number of / a great deal of + noun</b> (a fair amount, formal), <b>the majority of + noun</b> (most of a group).</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> "few/little" and "a few/a little" look almost identical but carry opposite emotional colouring.<br><br>
            ✅ "Few managers understood the new system." — negative: almost none did, implying a problem.<br>
            ✅ "A few managers understood the new system." — neutral/positive: some did, framed as a reasonable number.<br>
            ❌ Mixing them up completely reverses your meaning, even though the words look almost the same — always check for that tiny "a".</span>
          </div>'''
    },
    "compare": {
        "title": "General categories vs. precise amounts",
        "instruction": "Hover over each to see exactly what's being claimed.",
        "items": [
            {"key": "c1", "label": "Generic \"the\"", "text": "The laptop replaced the desktop computer in most modern offices.", "explain": "\"The\" here refers to laptops and desktops as categories/inventions, not one specific machine."},
            {"key": "c2", "label": "Generic zero article", "text": "Managers today expect faster decision-making than ever before.", "explain": "No article at all, because \"managers\" as a plural category needs none for a generalisation."},
            {"key": "c3", "label": "Few vs. a few", "text": "Few candidates met every requirement, though a few came impressively close.", "explain": "The same base word, but \"few\" (negative) and \"a few\" (positive) tell almost opposite stories."},
        ]
    },
    "reading": {
        "heading": "Survivorship Bias in Success Stories",
        "passage_paragraphs": [
            f'''{gram("g1","The startup founder")} who drops out of university and builds a billion-dollar company has become one of the most repeated stories in modern business writing. {gram("g2","Successful entrepreneurs")} are held up constantly as proof that talent and persistence are all it takes. What almost never gets mentioned is {gram("g3","a number of")} equally talented, equally hardworking founders who tried the exact same approach and simply failed.''',
            f'''This distortion is known as survivorship bias: {gram("g4","a great deal of")} our understanding of success comes exclusively from people who made it, while {gram("g5","the majority of")} people who tried and failed simply disappear from the record. Failed ventures leave behind no bestselling memoir, no {vocab("keynote","keynote")} speech, no inspiring interview — {gram("g6","few")} of them are ever written about at all, because there is no obvious audience for a story that ends in {vocab("quiet","quiet")} failure rather than {vocab("triumphant","triumphant")} success.''',
            f'''{gram("g7","A few")} researchers have tried to correct for this by studying failed companies directly rather than relying on survivors' accounts, and their findings are sobering: {vocab("identical","identical")} habits, routines and even personality traits show up just as often among people who failed as among those who succeeded. In other words, {vocab("perseverance","perseverance")} and confidence may be far less {vocab("predictive","predictive")} of success than the survivors themselves like to believe — {vocab("luck","luck")} and timing, it turns out, play a much larger role than most success stories are willing to {vocab("acknowledge","acknowledge")}.''',
        ],
        "comprehension": [
            {"prompt": "According to the passage, what is survivorship bias?", "options": [
                {"label": "Understanding success mainly through people who succeeded, ignoring those who failed.", "value": "right", "correct": True},
                {"label": "The tendency of successful people to exaggerate their achievements.", "value": "wrong", "correct": False}]},
            {"prompt": "Why do failed ventures rarely get written about, according to the passage?", "options": [
                {"label": "There is no obvious audience for a story that ends in quiet failure.", "value": "right", "correct": True},
                {"label": "Companies are legally prevented from discussing failed ventures.", "value": "wrong", "correct": False}]},
            {"prompt": "What did researchers find when they studied failed companies directly?", "options": [
                {"label": "Identical habits and traits appeared just as often among those who failed.", "value": "right", "correct": True},
                {"label": "Failed founders were consistently less hardworking than successful ones.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "keynote": {"word": "keynote", "ipa": "/ˈkiː.nəʊt/", "meaning": "a main speech at a conference, usually delivered by someone prominent", "example": "She was invited to deliver the keynote speech."},
            "quiet": {"word": "quiet", "ipa": "/ˈkwaɪ.ət/", "meaning": "(here) not noticed or talked about publicly", "example": "Most failed ventures end in quiet failure."},
            "triumphant": {"word": "triumphant", "ipa": "/traɪˈʌm.fənt/", "meaning": "celebrating or expressing great success", "example": "The story ends in triumphant success, not quiet failure."},
            "identical": {"word": "identical", "ipa": "/aɪˈden.tɪ.kəl/", "meaning": "exactly the same", "example": "Researchers found identical habits among both groups."},
            "perseverance": {"word": "perseverance", "ipa": "/ˌpɜː.sɪˈvɪə.rəns/", "meaning": "continued effort despite difficulty", "example": "Perseverance may be less predictive of success than people think."},
            "predictive": {"word": "predictive", "ipa": "/prɪˈdɪk.tɪv/", "meaning": "able to indicate what is likely to happen", "example": "Confidence may be far less predictive of success than believed."},
            "luck": {"word": "luck", "ipa": "/lʌk/", "meaning": "success or failure caused by chance rather than effort", "example": "Luck and timing play a larger role than most stories admit."},
            "acknowledge": {"word": "acknowledge", "ipa": "/əkˈnɒl.ɪdʒ/", "meaning": "to accept or admit that something is true", "example": "Success stories are rarely willing to acknowledge the role of luck."},
        },
        "gram_explanations": {
            "g1": "Generic \"the\" + singular noun — refers to a whole recognisable type of person (the archetypal founder), not one specific individual.",
            "g2": "Generic zero article + plural noun — a generalisation about entrepreneurs as a group, no article needed.",
            "g3": "Formal quantifier \"a number of\" — a fairly large, unspecified amount, typical of formal writing about groups.",
            "g4": "Formal quantifier \"a great deal of\" — a large amount of an uncountable noun (\"understanding\"), common in academic register.",
            "g5": "Formal quantifier \"the majority of\" — most of a specific, implied group (people who tried).",
            "g6": "\"Few\" (no article) — a small, negatively-coloured amount: almost none get written about.",
            "g7": "\"A few\" (with article) — a small but notable, more positive amount: some researchers, framed as a meaningful group."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "\"Triumphant\" describes something that…", "options": [{"label": "celebrates or expresses great success", "value": "right", "correct": True}, {"label": "ends in quiet, unnoticed failure", "value": "wrong", "correct": False}, {"label": "is deliberately kept secret", "value": "wrong2", "correct": False}]},
            {"prompt": "If two things are \"identical\", they are…", "options": [{"label": "exactly the same", "value": "right", "correct": True}, {"label": "completely different from each other", "value": "wrong", "correct": False}, {"label": "loosely related but distinct", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Perseverance\" means…", "options": [{"label": "continued effort despite difficulty", "value": "right", "correct": True}, {"label": "giving up as soon as something gets hard", "value": "wrong", "correct": False}, {"label": "sudden, unplanned success", "value": "wrong2", "correct": False}]},
            {"prompt": "If something is \"predictive\" of an outcome, it…", "options": [{"label": "indicates what is likely to happen", "value": "right", "correct": True}, {"label": "has no connection to the outcome at all", "value": "wrong", "correct": False}, {"label": "happened only after the outcome occurred", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"acknowledge\" something is to…", "options": [{"label": "accept or admit that it is true", "value": "right", "correct": True}, {"label": "deny that it happened", "value": "wrong", "correct": False}, {"label": "forget about it completely", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "She was invited to deliver the", "after": "speech at the conference.", "answers": ["keynote"], "width": 100},
            {"before": "Most failed ventures end in", "after": "failure, with no public record at all.", "answers": ["quiet"], "width": 80},
            {"before": "Timing and", "after": "played a bigger role than most people admit.", "answers": ["luck"], "width": 70},
            {"before": "Researchers found", "after": "habits among both successful and failed founders.", "answers": ["identical"], "width": 100},
        ],
    },
    "practice": {
        "gapfill_focus": "generic articles or formal quantifiers — choose the correct form.",
        "gapfill": [
            {"before": "", "after": "(the/smartphone) has changed how teams communicate. (Generic \"the\")", "answers": ["The smartphone"]},
            {"before": "", "after": "(a number/of) staff members raised the same objection.", "answers": ["A number of"]},
            {"before": "There was", "after": "(little) enthusiasm for the idea, so it was dropped. (negative)", "answers": ["little"]},
            {"before": "", "after": "(the majority/of) respondents supported the new policy.", "answers": ["The majority of"]},
            {"before": "There was", "after": "(a little) interest in the proposal, enough to move forward. (positive)", "answers": ["a little"]},
            {"before": "", "after": "(a/manager) should always listen before deciding. (Generic \"a\")", "answers": ["A manager"]},
        ],
        "second": {
            "type": "errorspot", "title": "Spot the mistake",
            "instruction": "One word is wrong in each sentence. Tap it, then check the correction.",
            "items": [
                {"words": ["Few", "of", "the", "staff", "complained,", "so", "morale", "was", "clearly", "high."], "error_indices": [0], "correction": "\"Few\" → \"A few\" (a small but positive number fits a high-morale reading)"},
                {"words": ["A", "number", "of", "clients", "was", "unhappy", "with", "the", "delay."], "error_indices": [4], "correction": "\"was\" → \"were\" (\"a number of\" takes a plural verb)"},
                {"words": ["The", "majority", "of", "staff", "was", "in", "favour", "of", "the", "change."], "error_indices": [4], "correction": "\"was\" → \"were\" (\"the majority of\" + plural noun takes a plural verb)"},
            ],
        },
        "builders": [
            {"words": ["The", "internet", "has", "transformed", "global", "business."]},
            {"words": ["A", "number", "of", "clients", "raised", "the", "same", "concern."]},
            {"words": ["The", "majority", "of", "staff", "preferred", "hybrid", "work."]},
        ],
    },
    "speaking": {
        "solo_text": "Summarise the results of an imaginary workplace survey using at least two formal quantifiers (a number of, a great deal of, the majority of, few, a few) and one generic article generalisation.",
        "group_questions": [
            "Do you think \"the majority of\" employees at most companies genuinely prefer hybrid work? Why or why not?",
            "Can you think of an invention (like the smartphone or the internet) that changed your field of work or study, using generic \"the\"?",
            "Describe a situation where \"few\" people agreed with you, versus one where \"a few\" people did.",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are talking about a podcast episode on survivorship bias.",
        "dialogue": [
            {"speaker": "Anna", "line": "I listened to this podcast about survivorship bias last night — it's basically about why we only ever hear success stories."},
            {"speaker": "Tomasz", "line": "Like the startup founder who drops out of university and becomes a billionaire?"},
            {"speaker": "Anna", "line": "Exactly that story. A number of founders try the exact same thing and just fail quietly, but nobody talks about them."},
            {"speaker": "Tomasz", "line": "Makes sense. The majority of failed ventures probably never even get mentioned anywhere."},
            {"speaker": "Anna", "line": "Right, and apparently few of them are ever written about, because there's no audience for a quiet failure."},
            {"speaker": "Tomasz", "line": "Did the podcast mention any actual research on this?"},
            {"speaker": "Anna", "line": "Yeah, a few researchers studied failed companies directly and found identical habits in both successful and failed founders."},
            {"speaker": "Tomasz", "line": "So luck and timing matter a lot more than everyone likes to acknowledge."},
        ],
        "comprehension": [
            {"prompt": "What does Anna say survivorship bias explains?", "options": [{"label": "Why we only ever hear success stories.", "value": "right", "correct": True}, {"label": "Why most startups eventually succeed.", "value": "wrong", "correct": False}]},
            {"prompt": "According to Tomasz, what does the majority of failed ventures probably never do?", "options": [{"label": "Get mentioned anywhere.", "value": "right", "correct": True}, {"label": "Receive any funding at all.", "value": "wrong", "correct": False}]},
            {"prompt": "What did the researchers Anna mentions find?", "options": [{"label": "Identical habits among both successful and failed founders.", "value": "right", "correct": True}, {"label": "Successful founders worked far harder than failed ones.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "___ internet has completely changed how businesses operate.", "options": [{"label": "The", "value": "right", "correct": True}, {"label": "A the", "value": "wrong", "correct": False}]},
        {"prompt": "___ of the clients raised concerns about pricing.", "options": [{"label": "A number", "value": "right", "correct": True}, {"label": "A numbers", "value": "wrong", "correct": False}]},
        {"prompt": "There was ___ support for the proposal, so it was abandoned.", "options": [{"label": "little", "value": "right", "correct": True}, {"label": "a little", "value": "wrong", "correct": False}]},
        {"prompt": "___ of staff surveyed preferred the new schedule.", "options": [{"label": "The majority", "value": "right", "correct": True}, {"label": "The majorities", "value": "wrong", "correct": False}]},
        {"prompt": "___ candidates had every skill the role demanded, though a handful came close.", "options": [{"label": "Few", "value": "right", "correct": True}, {"label": "A few", "value": "wrong", "correct": False}]},
    ],
})
