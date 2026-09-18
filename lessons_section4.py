# -*- coding: utf-8 -*-
"""Section 4 — Discourse & Complex Sentences (Lessons 15-20)."""
from gen_lesson_template import vocab, gram

SECTION_NAME = "Discourse & Complex Sentences"
THEME = "theme-discourse"

LESSONS = []

# ============================================================
# LESSON 15 — Participle Clauses
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-15-participle-clauses",
    "num": 15, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Participle Clauses",
    "subtitle": "Using -ing, -ed and having + past participle clauses to write tighter, more fluent sentences.",
    "warmup_intro": "Participle clauses let you fold a relative or adverbial clause into a shorter, more economical structure — very common in reports, emails and formal writing, where wordiness reads as sloppy.",
    "warmup": [
        {"prompt": "\"Having reviewed the proposal, she approved it\" replaces which longer structure?", "options": [{"label": "\"After she had reviewed the proposal, she approved it.\"", "value": "right", "correct": True}, {"label": "\"She reviews the proposal and approves it.\"", "value": "wrong", "correct": False}]},
        {"prompt": "\"Concerned about the delay, the client called twice\" explains the client's reason by using…", "options": [{"label": "a past participle clause (concerned = being concerned)", "value": "right", "correct": True}, {"label": "a present participle clause showing an ongoing action", "value": "wrong", "correct": False}]},
        {"prompt": "\"The report, written by three departments, took months\" uses a participle clause instead of…", "options": [{"label": "\"which was written by three departments\"", "value": "right", "correct": True}, {"label": "\"because it was written by three departments\"", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "Present participle (-ing) = active/ongoing; past participle (-ed/3rd form) = passive/completed; \"having + past participle\" = completed before the main action.",
    "diagnostic": [
        {"prompt": "___ the budget twice, the finance team still found an error.", "options": [{"label": "Having checked", "value": "right", "correct": True}, {"label": "Having check", "value": "wrong", "correct": False}]},
        {"prompt": "___ by the sudden resignation, the board called an emergency meeting.", "options": [{"label": "Alarmed", "value": "right", "correct": True}, {"label": "Alarming", "value": "wrong", "correct": False}]},
        {"prompt": "The candidate ___ the strongest interview got the offer.", "options": [{"label": "giving", "value": "right", "correct": True}, {"label": "given", "value": "wrong", "correct": False}]},
        {"prompt": "___ overnight, the server updates caused no disruption at all.", "options": [{"label": "Installed", "value": "right", "correct": True}, {"label": "Installing", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Three participle forms, three jobs",
        "intro": "Present participle clauses (-ing) usually show an active or simultaneous action. Past participle clauses (-ed/irregular) show a passive meaning or a state. \"Having + past participle\" shows something completed before the main clause's action.",
        "tabs": [{"key": "present", "label": "-ing clauses"}, {"key": "past", "label": "-ed clauses"}, {"key": "having", "label": "Having + p.p."}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "present": [
                {"label": "an active action happening at the same time", "example": "Checking her inbox, she noticed the client's reply."},
                {"label": "replacing a defining relative clause", "example": "Employees working remotely must log in by nine."},
            ],
            "past": [
                {"label": "a passive meaning (something done to the subject)", "example": "Delayed by the traffic, the courier missed the deadline."},
                {"label": "replacing a passive relative clause", "example": "The documents left on the desk were confidential."},
            ],
            "having": [
                {"label": "an action completed before the main clause", "example": "Having finished the audit, she submitted her report."},
                {"label": "a reason rooted in something already done", "example": "Having worked there for a decade, he knew every shortcut."},
            ],
        },
        "quiz_labels": {"present": "-ing (active/simultaneous)", "past": "-ed (passive/state)", "having": "Having + past participle (completed before)"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Present participle: <b>verb-ing</b> — active, ongoing, or simultaneous with the main verb. "Feeling exhausted, she left early."</div>
          <div class="formula" style="border-left-color:var(--c-continuous)">✅ Past participle: <b>verb-ed / 3rd form</b> — passive meaning or a resulting state. "Written in haste, the memo contained several errors."</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ Having + past participle: <b>having + verb-ed/3rd form</b> — completed clearly before the main action. "Having signed the contract, they shook hands."</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> the subject of the participle clause must be the same as the subject of the main clause — otherwise you get a "dangling participle", a classic C1 error.<br><br>
            ❌ "Walking into the office, the lights were off." (the lights weren't walking)<br>
            ✅ "Walking into the office, she noticed the lights were off."<br><br>
            Also remember: participle clauses only work when the two actions/subjects genuinely belong together — don't force one in just to sound formal.</span>
          </div>'''
    },
    "compare": {
        "title": "Same idea, three participle forms",
        "instruction": "Hover over each to see why that particular form was chosen.",
        "items": [
            {"key": "c1", "label": "Present participle", "text": "Reviewing the contract carefully, she spotted a missing clause.",
             "explain": "An active action happening at the same time as the main verb — she is the one reviewing."},
            {"key": "c2", "label": "Past participle", "text": "Confused by the wording, several clients called the helpline.",
             "explain": "A passive meaning: the clients were confused (something was done to them) by the wording."},
            {"key": "c3", "label": "Having + past participle", "text": "Having reviewed the contract twice, she finally signed it.",
             "explain": "The reviewing was completed clearly before the signing — sequence matters here."},
        ]
    },
    "reading": {
        "heading": "The Number That Anchors Everything",
        "passage_paragraphs": [
            f'''Salary negotiations rarely unfold as rationally as we like to imagine. {gram("g1","Having anchored on the first figure mentioned")}, both sides tend to judge every subsequent number in relation to it, rather than on its own merits. Psychologists call this the anchoring effect: once a number enters the room, it quietly reshapes what counts as reasonable, {vocab("disproportionately","disproportionately")} favouring whoever names it first. A {vocab("candidate","candidate")}, {gram("g2","concerned about seeming unreasonable")}, will often accept a {vocab("lowball","lowball")} offer far sooner than the market would justify, while a {vocab("recruiter","recruiter")} gains real {vocab("leverage","leverage")} simply by speaking first.''',
            f'''{gram("g3","Framed as a routine opening figure")}, the initial number rarely feels like a tactic at all — yet {vocab("benchmark","benchmark")} studies show that candidates who receive a high opening figure end up with significantly higher final salaries than those who don't, regardless of qualifications. {gram("g4","Once presented with a number")}, most people struggle to move far from it, even when they know, intellectually, that the figure was essentially arbitrary.''',
            f'''{gram("g5","Realising how powerful anchors can be")}, some negotiation coaches now teach candidates to prepare a {vocab("counteroffer","counteroffer")} in advance, rather than reacting to the anchor in the moment. {gram("g6","Trained to recognise the bias")}, an experienced negotiator can consciously discount the anchor and argue instead from independent salary data. {gram("g7","Having rehearsed their position beforehand")}, a candidate is far less likely to {vocab("undervalue","undervalue")} their own worth simply because the other side spoke first.''',
        ],
        "comprehension": [
            {"prompt": "According to the passage, why does the first number mentioned matter so much?", "options": [
                {"label": "It reshapes what both sides judge to be a reasonable range afterwards.", "value": "right", "correct": True},
                {"label": "It is always legally binding once it has been spoken aloud.", "value": "wrong", "correct": False}]},
            {"prompt": "What do the benchmark studies mentioned in the passage show?", "options": [
                {"label": "Candidates who open with a high figure end up earning more overall.", "value": "right", "correct": True},
                {"label": "Opening figures make no real difference to final salaries.", "value": "wrong", "correct": False}]},
            {"prompt": "What do some negotiation coaches now recommend?", "options": [
                {"label": "Preparing a counteroffer in advance rather than reacting in the moment.", "value": "right", "correct": True},
                {"label": "Always waiting for the employer to name a number first.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "disproportionately": {"word": "disproportionately", "ipa": "/ˌdɪs.prəˈpɔː.ʃən.ət.li/", "meaning": "to an extent that is too large or too small in relation to something else", "example": "The first number named disproportionately shapes the final outcome."},
            "candidate": {"word": "candidate", "ipa": "/ˈkæn.dɪ.dət/", "meaning": "a person applying for a job or position", "example": "The candidate accepted the offer without much hesitation."},
            "lowball": {"word": "lowball", "ipa": "/ˈləʊ.bɔːl/", "meaning": "an offer deliberately set well below what something is actually worth", "example": "She almost accepted the lowball offer out of nerves."},
            "recruiter": {"word": "recruiter", "ipa": "/rɪˈkruː.tər/", "meaning": "a person whose job is to find and hire suitable candidates", "example": "The recruiter asked about salary expectations early on."},
            "leverage": {"word": "leverage", "ipa": "/ˈliː.vər.ɪdʒ/", "meaning": "power or influence used to gain an advantage in a negotiation", "example": "Speaking first gave the recruiter unexpected leverage."},
            "benchmark": {"word": "benchmark", "ipa": "/ˈbentʃ.mɑːk/", "meaning": "a standard or point of reference used for comparison", "example": "Benchmark studies compared candidates with similar qualifications."},
            "counteroffer": {"word": "counteroffer", "ipa": "/ˈkaʊn.tərˌɒf.ər/", "meaning": "an alternative offer made in response to one already proposed", "example": "She had a counteroffer ready before the call even began."},
            "undervalue": {"word": "undervalue", "ipa": "/ˌʌn.dəˈvæl.juː/", "meaning": "to underestimate the true worth of something or someone", "example": "It's easy to undervalue your own experience under pressure."},
        },
        "gram_explanations": {
            "g1": "\"Having + past participle\" — the anchoring is completed before both sides start evaluating every later number in relation to it.",
            "g2": "Past participle clause (from \"being concerned\") — a state, not an action, describing the candidate.",
            "g3": "Past participle clause — passive meaning: the number is framed by the situation, replacing \"which is framed...\".",
            "g4": "Reduced past participle clause with \"once\" — replacing \"once they are presented with a number\".",
            "g5": "Present participle clause showing the reason, simultaneous with coaches changing their advice.",
            "g6": "Past participle clause — passive meaning: the negotiator has been trained, replacing \"who has been trained...\".",
            "g7": "\"Having + past participle\" — the rehearsing is completed before the negotiation itself takes place."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "If an outcome is shaped \"disproportionately\" by one factor, that factor…", "options": [{"label": "has an unfairly large effect relative to its actual importance", "value": "right", "correct": True}, {"label": "has almost no measurable effect at all", "value": "wrong", "correct": False}, {"label": "is applied equally and fairly to everyone", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"lowball\" offer is one that is…", "options": [{"label": "deliberately set well below what something is worth", "value": "right", "correct": True}, {"label": "generous and above the market rate", "value": "wrong", "correct": False}, {"label": "identical to the market benchmark", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Leverage\" in a negotiation refers to…", "options": [{"label": "power or influence that gives you an advantage", "value": "right", "correct": True}, {"label": "a legal document signed by both parties", "value": "wrong", "correct": False}, {"label": "the final agreed salary figure", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"benchmark\" is…", "options": [{"label": "a standard used as a point of comparison", "value": "right", "correct": True}, {"label": "a one-off, unrepeatable exception", "value": "wrong", "correct": False}, {"label": "a formal written apology", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"undervalue\" something means to…", "options": [{"label": "underestimate its true worth", "value": "right", "correct": True}, {"label": "pay far more for it than necessary", "value": "wrong", "correct": False}, {"label": "advertise it aggressively", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "She almost accepted the", "after": "offer out of nerves.", "answers": ["lowball"], "width": 100},
            {"before": "The", "after": "asked about salary expectations early on.", "answers": ["recruiter"], "width": 110},
            {"before": "The", "after": "accepted the offer without much hesitation.", "answers": ["candidate"], "width": 110},
            {"before": "She had a", "after": "ready before the call even began.", "answers": ["counteroffer"], "width": 130},
        ],
    },
    "practice": {
        "gapfill_focus": "present, past, or 'having + past participle' clause?",
        "gapfill": [
            {"before": "", "after": "(check) the figures twice, the accountant found the discrepancy.", "answers": ["Having checked"]},
            {"before": "", "after": "(exhaust) after the long flight, she went straight to bed.", "answers": ["Exhausted"]},
            {"before": "The employees", "after": "(work) overtime received a bonus.", "answers": ["working"]},
            {"before": "", "after": "(finish) the report, he emailed it to the whole team.", "answers": ["Having finished"]},
            {"before": "The email,", "after": "(send) late on Friday, went unnoticed until Monday.", "answers": ["sent"]},
            {"before": "", "after": "(worry) about the deadline, she stayed late every night that week.", "answers": ["Worried"]},
        ],
        "second": {
            "type": "errorspot", "title": "Spot the mistake",
            "instruction": "One word is wrong in each sentence. Tap it, then check the correction.",
            "items": [
                {"words": ["Having", "checked", "the", "figures", "twice,", "the", "error", "still", "slip", "through."], "error_indices": [8], "correction": "\"slip\" → \"slipped\" (a completed past action, not base form)"},
                {"words": ["Concerning", "about", "the", "delay,", "the", "client", "called", "the", "office", "twice."], "error_indices": [0], "correction": "\"Concerning\" → \"Concerned\" (a past participle showing a state, not present participle)"},
                {"words": ["The", "report", "writing", "by", "three", "departments", "took", "months", "to", "finish."], "error_indices": [2], "correction": "\"writing\" → \"written\" (passive meaning needs the past participle)"},
            ],
        },
        "builders": [
            {"words": ["Having", "reviewed", "the", "proposal,", "she", "approved", "it", "at", "once."]},
            {"words": ["Concerned", "about", "the", "delay,", "the", "client", "called", "twice."]},
            {"words": ["The", "documents", "left", "on", "the", "desk", "were", "confidential."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a decision you made at work or in life, using at least one -ing participle clause, one -ed participle clause, and one 'having + past participle' clause.",
        "group_questions": [
            "Tell your group about a document, contract or agreement you once had to review very carefully. What happened once you'd finished checking it?",
            "Describe a situation where you felt concerned, worried or alarmed about something at work — what did you do next?",
            "Can you think of a rule or clause at your workplace that was rewritten after causing a problem?",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are chatting after Anna's salary review, having both just read about anchoring bias.",
        "dialogue": [
            {"speaker": "Anna", "line": "Having just read about anchoring bias, I finally understand why recruiters always ask your expected salary first."},
            {"speaker": "Tomasz", "line": "Right, whoever names a number first sets the anchor for the whole conversation."},
            {"speaker": "Anna", "line": "Exactly. Concerned about seeming unreasonable, most candidates just accept whatever range comes up first."},
            {"speaker": "Tomasz", "line": "Trained to recognise the bias, though, you can consciously push back against it."},
            {"speaker": "Anna", "line": "Having rehearsed a counteroffer beforehand definitely helps — you don't end up anchoring on their number instead."},
            {"speaker": "Tomasz", "line": "I read that candidates who mention a high figure first end up earning disproportionately more, even with identical qualifications."},
            {"speaker": "Anna", "line": "That benchmark data is honestly a bit alarming."},
            {"speaker": "Tomasz", "line": "It is. Next negotiation, I'm speaking first."},
        ],
        "comprehension": [
            {"prompt": "According to Anna, why do recruiters often ask for expected salary first?", "options": [{"label": "Whoever names a number first sets the anchor for the conversation.", "value": "right", "correct": True}, {"label": "It is required by employment law in most companies.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Tomasz say helps you resist an anchor?", "options": [{"label": "Being trained to recognise the bias.", "value": "right", "correct": True}, {"label": "Refusing to discuss salary at all.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Tomasz decide to do in his next negotiation?", "options": [{"label": "Speak first and name a figure himself.", "value": "right", "correct": True}, {"label": "Let the other side make every offer.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "___ the report twice, she finally sent it to the client.", "options": [{"label": "Having checked", "value": "right", "correct": True}, {"label": "Having check", "value": "wrong", "correct": False}]},
        {"prompt": "___ about the budget, the manager called an urgent meeting.", "options": [{"label": "Worried", "value": "right", "correct": True}, {"label": "Worrying", "value": "wrong", "correct": False}]},
        {"prompt": "The staff ___ overtime were given extra leave.", "options": [{"label": "working", "value": "right", "correct": True}, {"label": "worked", "value": "wrong", "correct": False}]},
        {"prompt": "The memo, ___ in a hurry, contained two errors.", "options": [{"label": "written", "value": "right", "correct": True}, {"label": "writing", "value": "wrong", "correct": False}]},
        {"prompt": "___ every detail, they finally signed the agreement.", "options": [{"label": "Having agreed on", "value": "right", "correct": True}, {"label": "Having agree on", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 16 — Advanced Relative Clauses
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-16-advanced-relative-clauses",
    "num": 16, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Advanced Relative Clauses",
    "subtitle": "Whereby, whereupon, whole-clause 'which', and prepositions placed before whom/which in formal style.",
    "warmup_intro": "Beyond who/which/that, formal and written English uses a small set of advanced relative structures that let a clause refer to a whole idea, a process, or attach a preposition more elegantly.",
    "warmup": [
        {"prompt": "\"A system whereby employees can report issues anonymously\" means a system…", "options": [{"label": "by means of which / through which employees can report issues", "value": "right", "correct": True}, {"label": "that employees are forbidden from using", "value": "wrong", "correct": False}]},
        {"prompt": "\"She was promoted, which surprised nobody\" — what does \"which\" refer to?", "options": [{"label": "the whole idea that she was promoted, not one noun", "value": "right", "correct": True}, {"label": "only the word \"promoted\" as a single noun", "value": "wrong", "correct": False}]},
        {"prompt": "In formal writing, \"the colleague to whom I reported\" is preferred over…", "options": [{"label": "\"the colleague who I reported to\"", "value": "right", "correct": True}, {"label": "\"the colleague that I reported\"", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "\"Whereby\" = by which/through which (a process). A comma + \"which\" referring back to a whole clause is extremely common in professional writing. Preposition-before-relative-pronoun (to whom, on which) is the formal register's version of ending a sentence with a preposition.",
    "diagnostic": [
        {"prompt": "The company introduced a scheme ___ staff could work four days a week.", "options": [{"label": "whereby", "value": "right", "correct": True}, {"label": "whereupon", "value": "wrong", "correct": False}]},
        {"prompt": "He missed the deadline, ___ annoyed the entire team.", "options": [{"label": "which", "value": "right", "correct": True}, {"label": "that", "value": "wrong", "correct": False}]},
        {"prompt": "The client ___ we submitted the proposal has not replied yet.", "options": [{"label": "to whom", "value": "right", "correct": True}, {"label": "who", "value": "wrong", "correct": False}]},
        {"prompt": "She announced her resignation, ___ the room fell silent.", "options": [{"label": "whereupon", "value": "right", "correct": True}, {"label": "wherein", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Beyond who, which and that",
        "intro": "\"Whereby\" introduces a process or mechanism. \"Whereupon\" introduces an immediate consequence, very formal and often literary. A comma + \"which\" can refer to an entire preceding clause, not just a noun. Prepositions placed before whom/which sound more formal than stranding them at the end.",
        "tabs": [{"key": "whereby", "label": "Whereby"}, {"key": "whichclause", "label": "Whole-clause which"}, {"key": "prepwhom", "label": "Preposition + whom/which"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "whereby": [
                {"label": "a process or mechanism (= by/through which)", "example": "They set up a system whereby refunds are processed automatically."},
                {"label": "a formal arrangement", "example": "An agreement whereby both parties share the costs equally."},
            ],
            "whichclause": [
                {"label": "referring to an entire preceding statement", "example": "The flight was delayed, which meant we missed the connection."},
                {"label": "adding an evaluative comment on the whole clause", "example": "He apologised publicly, which impressed the board."},
            ],
            "prepwhom": [
                {"label": "formal register, preposition before the pronoun", "example": "The manager to whom she reports is based abroad."},
                {"label": "formal register with 'which'", "example": "The issue on which they disagreed was never resolved."},
            ],
        },
        "quiz_labels": {"whereby": "Whereby (a process)", "whichclause": "Comma + which (whole clause)", "prepwhom": "Preposition + whom/which"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Whereby: <b>noun + whereby + clause</b> = by/through which. "A policy whereby latecomers are fined."</div>
          <div class="formula" style="border-left-color:var(--c-continuous)">✅ Comma + which: refers back to the <b>whole previous clause</b>, not a single noun. "He resigned suddenly, which shocked everyone."</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ Preposition + whom/which: <b>to/with/on/for + whom/which</b> — formal, never with "that" or "who" in this position.</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> "whereupon" (= and then, immediately) is much rarer and more literary than "whereby" — don't confuse the two, and don't overuse "whereupon" in ordinary business writing.<br><br>
            ✅ "A policy whereby employees can request remote work." — describes a mechanism.<br>
            ✅ "She raised the objection, whereupon the meeting was adjourned." — an immediate, almost dramatic consequence.<br><br>
            Also: never write "to who" or "for which that" — prepositions combine only with whom (people) or which (things), never with "that".</span>
          </div>'''
    },
    "compare": {
        "title": "Which relative structure fits?",
        "instruction": "Hover over each to see why that specific form was chosen.",
        "items": [
            {"key": "c1", "label": "Whereby", "text": "The firm created a scheme whereby staff could buy shares at a discount.",
             "explain": "Describes the mechanism of the scheme itself — \"whereby\" = through which."},
            {"key": "c2", "label": "Whole-clause which", "text": "The merger fell through, which relieved almost everyone on the team.",
             "explain": "\"Which\" here refers to the entire event of the merger falling through, not just one noun."},
            {"key": "c3", "label": "Preposition + whom", "text": "The consultant with whom we worked closely has since retired.",
             "explain": "Formal register: the preposition \"with\" is placed directly before \"whom\" rather than stranded at the end."},
        ]
    },
    "reading": {
        "heading": "Reading Between the Lines: High-Context vs. Low-Context Teams",
        "passage_paragraphs": [
            f'''Global teams often stumble not over what is said, but over how it is said. Researchers describe a spectrum of communication styles {gram("g1","whereby")} meaning is conveyed either directly, through explicit words, or indirectly, through context, tone and shared assumptions. In a low-context culture, a manager typically states an instruction outright; in a high-context culture, the same message is often left as {vocab("subtext","subtext")}, wrapped in enough {vocab("ambiguity","ambiguity")} that no one need lose face if it is declined. The colleague {gram("g2","to whom")} an indirect request is addressed may need considerable {vocab("tact","tact")} simply to work out what is actually being asked.''',
            f'''Managers frequently misjudge these signals, {gram("g3","which")} explains why so many cross-border projects stall within the first few months. A manager's {vocab("bluntness","bluntness")}, entirely normal in a low-context office, can easily be {vocab("misconstrued","misconstrued")} as outright hostility elsewhere. In one well-known account, a Japanese colleague raised a gentle, indirect objection, {gram("g4","whereupon")} the meeting was quietly rescheduled without anyone stating the real reason aloud.''',
            f'''The issue {gram("g5","on which")} most cross-cultural trainers agree is that neither style is objectively better — each simply optimises for something different: {vocab("candour","candour")} and speed in low-context settings, {vocab("deference","deference")} and long-term harmony in high-context ones. Experienced managers develop a kind of bilingual sensitivity, {gram("g6","which")} allows them to read {vocab("nuance","nuance")} in one setting and be reassuringly direct in another. The manager {gram("g7","with whom")} a new hire feels comfortable enough to ask what they actually mean has usually already solved most of the problem.''',
        ],
        "comprehension": [
            {"prompt": "According to the passage, what mainly distinguishes a high-context culture from a low-context one?", "options": [
                {"label": "Whether meaning is conveyed explicitly in words or left to context and tone.", "value": "right", "correct": True},
                {"label": "Whether employees are allowed to work remotely or not.", "value": "wrong", "correct": False}]},
            {"prompt": "What happened after the Japanese colleague raised a gentle, indirect objection?", "options": [
                {"label": "The meeting was quietly rescheduled without the reason being stated.", "value": "right", "correct": True},
                {"label": "The objection was formally recorded and debated at length.", "value": "wrong", "correct": False}]},
            {"prompt": "What do most cross-cultural trainers agree on, according to the passage?", "options": [
                {"label": "That neither communication style is objectively better than the other.", "value": "right", "correct": True},
                {"label": "That low-context communication should always be preferred at work.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "subtext": {"word": "subtext", "ipa": "/ˈsʌb.tekst/", "meaning": "an implied meaning that is not stated directly", "example": "The real request was left as subtext rather than spelled out."},
            "ambiguity": {"word": "ambiguity", "ipa": "/ˌæm.bɪˈɡjuː.ə.ti/", "meaning": "the quality of having more than one possible meaning, causing uncertainty", "example": "The message was wrapped in enough ambiguity to allow a graceful refusal."},
            "tact": {"word": "tact", "ipa": "/tækt/", "meaning": "sensitivity and skill in dealing with others without causing offence", "example": "Reading an indirect request takes real tact."},
            "bluntness": {"word": "bluntness", "ipa": "/ˈblʌnt.nəs/", "meaning": "the quality of speaking very directly, without softening the message", "example": "His bluntness was normal at home but shocked colleagues abroad."},
            "misconstrued": {"word": "misconstrued", "ipa": "/ˌmɪs.kənˈstruːd/", "meaning": "interpreted incorrectly, understood in a way that was not intended", "example": "Her direct email was misconstrued as an insult."},
            "candour": {"word": "candour", "ipa": "/ˈkæn.dər/", "meaning": "openness and honesty in expressing oneself", "example": "Low-context settings tend to reward candour and speed."},
            "deference": {"word": "deference", "ipa": "/ˈdef.ər.əns/", "meaning": "respectful yielding to someone else's wishes, status or authority", "example": "Deference to seniority shaped how the objection was raised."},
            "nuance": {"word": "nuance", "ipa": "/ˈnjuː.ɑːns/", "meaning": "a subtle difference in meaning, tone or expression", "example": "She had learned to read the nuance in her colleagues' silence."},
        },
        "gram_explanations": {
            "g1": "\"Whereby\" — introduces the mechanism of the communication spectrum (= through which meaning is conveyed).",
            "g2": "\"To whom\" — a preposition placed before the relative pronoun, formal register (replacing \"who...to\").",
            "g3": "Comma + \"which\" — refers to the whole idea that managers misjudge these signals, not to one noun.",
            "g4": "\"Whereupon\" — an immediate consequence: the objection was raised, and then the meeting was rescheduled.",
            "g5": "\"On which\" — the preposition placed before \"which\", formal register (replacing \"which...on\").",
            "g6": "Comma + \"which\" — refers to the whole idea that managers develop a kind of bilingual sensitivity.",
            "g7": "\"With whom\" — a preposition placed before the relative pronoun, formal register (replacing \"who...with\")."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "\"Subtext\" is…", "options": [{"label": "an implied meaning that is not stated directly", "value": "right", "correct": True}, {"label": "a formal written summary", "value": "wrong", "correct": False}, {"label": "the exact opposite of what is said", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Ambiguity\" means…", "options": [{"label": "having more than one possible meaning", "value": "right", "correct": True}, {"label": "being completely clear and precise", "value": "wrong", "correct": False}, {"label": "being deliberately rude", "value": "wrong2", "correct": False}]},
            {"prompt": "If someone's remark is \"misconstrued\", it is…", "options": [{"label": "understood in a way that was not intended", "value": "right", "correct": True}, {"label": "understood exactly as intended", "value": "wrong", "correct": False}, {"label": "ignored completely", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Deference\" means…", "options": [{"label": "respectful yielding to someone's wishes or authority", "value": "right", "correct": True}, {"label": "open, forceful disagreement", "value": "wrong", "correct": False}, {"label": "complete indifference", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Bluntness\" describes speech that is…", "options": [{"label": "very direct, without softening the message", "value": "right", "correct": True}, {"label": "vague and full of hints", "value": "wrong", "correct": False}, {"label": "extremely polite and formal", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "Reading an indirect request takes real", "after": ".", "answers": ["tact"], "width": 90},
            {"before": "Low-context settings tend to reward", "after": "and speed.", "answers": ["candour"], "width": 100},
            {"before": "She had learned to read the", "after": "in her colleagues' silence.", "answers": ["nuance"], "width": 100},
            {"before": "The real request was left as", "after": "rather than spelled out.", "answers": ["subtext"], "width": 100},
        ],
    },
    "practice": {
        "gapfill_focus": "whereby, whereupon, or comma + which?",
        "gapfill": [
            {"before": "They introduced a rule", "after": "(process) latecomers lose their parking space for a week.", "answers": ["whereby"]},
            {"before": "She interrupted the presentation,", "after": "(consequence) her colleague simply left the room.", "answers": ["whereupon"]},
            {"before": "He was late again,", "after": "(whole clause) annoyed his manager considerably.", "answers": ["which"]},
            {"before": "The client", "after": "(preposition + whom) we owe the most has gone quiet lately.", "answers": ["to whom"]},
            {"before": "They designed a scheme", "after": "(process) profits are shared equally among staff.", "answers": ["whereby"]},
            {"before": "The topic", "after": "(preposition + which) they most disagreed was never resolved.", "answers": ["on which"]},
        ],
        "second": {
            "type": "categorise", "title": "Which advanced relative structure is this?",
            "instruction": "Tap the category that matches each sentence.",
            "categories": ["Whereby (a process)", "Whereupon (immediate result)", "Whole-clause which"],
            "items": [
                {"prompt": "\"They set up a fund whereby small businesses could apply for grants.\"", "correct": "Whereby (a process)"},
                {"prompt": "\"He announced his resignation, whereupon the office went completely silent.\"", "correct": "Whereupon (immediate result)"},
                {"prompt": "\"She got the promotion, which nobody in the office found surprising.\"", "correct": "Whole-clause which"},
                {"prompt": "\"The council approved a plan whereby residents can report faults online.\"", "correct": "Whereby (a process)"},
            ],
        },
        "builders": [
            {"words": ["They", "introduced", "a", "scheme", "whereby", "staff", "share", "profits."]},
            {"words": ["He", "resigned", "suddenly,", "which", "shocked", "everyone", "in", "the", "office."]},
            {"words": ["The", "manager", "to", "whom", "she", "reports", "is", "based", "abroad."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a policy, rule or system at your workplace or school using \"whereby\", then add a comment about it using comma + \"which\".",
        "group_questions": [
            "Is there a workplace policy whereby employees can request something unusual (flexible hours, remote work, extra leave)? Describe it.",
            "Tell your group about a time something surprising happened at work, which changed how people behaved afterwards.",
            "Describe a colleague or manager to whom you report, or with whom you work closely.",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are debriefing after an awkward video call with the Tokyo office.",
        "dialogue": [
            {"speaker": "Anna", "line": "I finally get why our Tokyo call felt so strange — it's this whole high-context thing, whereby half the meaning is never actually said out loud."},
            {"speaker": "Tomasz", "line": "Right, whereas we just say exactly what we mean, which apparently comes across as blunt."},
            {"speaker": "Anna", "line": "Exactly. The client to whom I sent that very direct email never replied, and now I understand why."},
            {"speaker": "Tomasz", "line": "I raised an objection once, whereupon everyone went completely silent — I had no idea what I'd done wrong."},
            {"speaker": "Anna", "line": "It probably wasn't the objection itself, which they don't mind, but how bluntly you phrased it."},
            {"speaker": "Tomasz", "line": "The real issue on which we still disagree internally is how direct our emails should be by default."},
            {"speaker": "Anna", "line": "The manager with whom I discussed this suggested softening requests with a bit more context first."},
            {"speaker": "Tomasz", "line": "Makes sense. I'll try that next time, which honestly should have been obvious from the start."},
        ],
        "comprehension": [
            {"prompt": "Why did Anna's direct email to the client go unanswered, in her view?", "options": [{"label": "The client comes from a high-context culture where directness can seem blunt.", "value": "right", "correct": True}, {"label": "The email was never actually delivered.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Anna suggest actually caused the silence after Tomasz's objection?", "options": [{"label": "How bluntly he phrased it, not the objection itself.", "value": "right", "correct": True}, {"label": "The objection being raised at the wrong time of day.", "value": "wrong", "correct": False}]},
            {"prompt": "What did the manager suggest to Anna?", "options": [{"label": "Softening requests with a bit more context first.", "value": "right", "correct": True}, {"label": "Avoiding email communication altogether.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "They introduced a system ___ complaints are logged automatically.", "options": [{"label": "whereby", "value": "right", "correct": True}, {"label": "whereupon", "value": "wrong", "correct": False}]},
        {"prompt": "She was promoted early, ___ surprised nobody in the office.", "options": [{"label": "which", "value": "right", "correct": True}, {"label": "that", "value": "wrong", "correct": False}]},
        {"prompt": "The colleague ___ I report is based in another city.", "options": [{"label": "to whom", "value": "right", "correct": True}, {"label": "who", "value": "wrong", "correct": False}]},
        {"prompt": "He raised the issue, ___ the meeting was extended by an hour.", "options": [{"label": "whereupon", "value": "right", "correct": True}, {"label": "whereby", "value": "wrong", "correct": False}]},
        {"prompt": "The topic ___ they disagreed most was never resolved.", "options": [{"label": "on which", "value": "right", "correct": True}, {"label": "which on", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 17 — Ellipsis & Substitution
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-17-ellipsis-substitution",
    "num": 17, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Ellipsis & Substitution",
    "subtitle": "Leaving words out and replacing whole clauses to sound natural, concise and fluent.",
    "warmup_intro": "Fluent English constantly avoids repeating itself. Ellipsis omits words that are obvious from context; substitution replaces a whole idea with a short word like \"so\", \"neither\" or \"one\". Both make speech and writing tighter and more natural.",
    "warmup": [
        {"prompt": "\"I think so\" is a shorter way of saying…", "options": [{"label": "\"I think that the thing we discussed is true.\"", "value": "right", "correct": True}, {"label": "\"I don't think about it at all.\"", "value": "wrong", "correct": False}]},
        {"prompt": "\"She finished early, and so did I\" means…", "options": [{"label": "I also finished early", "value": "right", "correct": True}, {"label": "I finished much later than her", "value": "wrong", "correct": False}]},
        {"prompt": "\"Call me if necessary\" is a shortened form of…", "options": [{"label": "\"Call me if it is necessary to call me.\"", "value": "right", "correct": True}, {"label": "\"Call me, because it's not necessary.\"", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "Substitution swaps a whole clause for a small word (so, neither, one). Ellipsis simply deletes words the listener can easily reconstruct from context.",
    "diagnostic": [
        {"prompt": "\"He didn't finish the report, and ___ did his colleague.\"", "options": [{"label": "neither", "value": "right", "correct": True}, {"label": "so", "value": "wrong", "correct": False}]},
        {"prompt": "\"Will the client approve it?\" \"I hope ___.\"", "options": [{"label": "so", "value": "right", "correct": True}, {"label": "it", "value": "wrong", "correct": False}]},
        {"prompt": "\"Please revise the draft ___ needed.\"", "options": [{"label": "if", "value": "right", "correct": True}, {"label": "if it if", "value": "wrong", "correct": False}]},
        {"prompt": "\"I'd like the blue folder, not the red ___.\"", "options": [{"label": "one", "value": "right", "correct": True}, {"label": "it", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Ellipsis vs. substitution",
        "intro": "Ellipsis deletes repeated words entirely (\"if necessary\" = \"if it is necessary\"). Substitution replaces a whole clause or noun with a small placeholder word (so, neither, one, do). Both avoid clumsy repetition.",
        "tabs": [{"key": "ellipsis", "label": "Ellipsis"}, {"key": "substitution", "label": "Substitution"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "ellipsis": [
                {"label": "omitting a repeated subject/verb after 'if', 'when', 'though'", "example": "Update the file if needed."},
                {"label": "omitting a repeated verb phrase after 'and', 'but'", "example": "She can attend the meeting, but I can't [attend]."},
            ],
            "substitution": [
                {"label": "'so'/'not' replacing a whole clause after report verbs", "example": "\"Is the deal final?\" \"I believe so.\""},
                {"label": "'so did / neither did / nor did' agreeing with a previous statement", "example": "He apologised, and so did she."},
                {"label": "'one/ones' replacing a countable noun", "example": "I'll take the smaller one."},
            ],
        },
        "quiz_labels": {"ellipsis": "Ellipsis (deleted words)", "substitution": "Substitution (replaced with so/one/neither)"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Ellipsis: <b>if/when/though + (subject + be) + adjective/participle</b> — "Contact HR if unsure." (= if you are unsure)</div>
          <div class="formula" style="border-left-color:var(--c-continuous)">✅ Substitution with so/not: <b>think/hope/believe/expect/say + so/not</b> — "Will it work?" "I expect so."</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ So/neither + auxiliary + subject: <b>so did I / neither does she / nor can they</b> — agreeing with a previous statement, positive or negative.</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> "so did I" (positive agreement) vs. "neither/nor did I" (negative agreement) invert subject and auxiliary — a very common C1 slip is forgetting the inversion.<br><br>
            ❌ "She didn't attend, and I neither." <br>
            ✅ "She didn't attend, and neither did I."<br><br>
            Also: "one/ones" replaces a countable noun already mentioned, but never an uncountable one — "I'd like some more information" not "some more one".</span>
          </div>'''
    },
    "compare": {
        "title": "Full form vs. the natural, shortened version",
        "instruction": "Hover to see exactly what's been left out or replaced.",
        "items": [
            {"key": "c1", "label": "Ellipsis", "text": "Please revise the draft if necessary.", "explain": "= \"if it is necessary\" — the subject and verb are deleted because they're obvious from context."},
            {"key": "c2", "label": "Substitution: so", "text": "\"Will the board approve the budget?\" \"I think so.\"", "explain": "\"So\" replaces the whole clause \"that the board will approve the budget\"."},
            {"key": "c3", "label": "Substitution: neither", "text": "He hasn't replied yet, and neither has she.", "explain": "\"Neither has she\" replaces \"she hasn't replied yet either\", with subject-auxiliary inversion."},
            {"key": "c4", "label": "Substitution: one", "text": "I don't want this laptop, I want the newer one.", "explain": "\"One\" replaces the repeated countable noun \"laptop\"."},
        ]
    },
    "reading": {
        "heading": "The Secret Doubts of High Achievers",
        "passage_paragraphs": [
            f'''Even the most outwardly accomplished professionals often carry a private conviction that they do not really deserve their success — a pattern researchers term impostor syndrome. A surgeon who has performed hundreds of {vocab("meticulous","meticulous")} operations may still privately suspect that her results come down to luck rather than skill; a professor may {vocab("attribute","attribute")} a landmark paper to a generous co-author rather than to his own {vocab("competence","competence")}. \"Do you ever feel like a total fraud?\" one colleague asked a newly promoted director. \"Honestly? I think {gram("g1","so")}, most days,\" she admitted.''',
            f'''Psychologists have found that the feeling rarely fades with more evidence of success; if anything, it can become {vocab("chronic","chronic")}. One study interviewed dozens of high achievers and found that most had never told a colleague about it — and {gram("g2","neither had")} their closest friends outside work, in many cases. When a mentor once {vocab("confided","confided")} her own doubts at a team dinner, a junior colleague admitted she felt exactly the same way. \"I thought it was just me,\" she said, \"and apparently {gram("g3","so did")} half the department.\"''',
            f'''Sufferers often {vocab("dismiss","dismiss")} compliments outright, treating genuine praise as unearned and quietly waiting to be exposed as a {vocab("fraud","fraud")}. Therapists recommend keeping a written record of achievements, to be reread {gram("g4","if necessary")} whenever self-doubt resurfaces, and seeking outside {vocab("validation","validation")} only sparingly. \"Should I mention this to my manager?\" one client asked. \"Only if it genuinely comes up — but {gram("g5","if so")}, be honest about it,\" the therapist replied. \"I hope it helps.\" \"I hope {gram("g6","so")} too,\" the client said quietly.''',
        ],
        "comprehension": [
            {"prompt": "According to the passage, what do high achievers with impostor syndrome often believe about their own success?", "options": [
                {"label": "That it is down to luck rather than their own competence.", "value": "right", "correct": True},
                {"label": "That it was achieved without any real effort at all.", "value": "wrong", "correct": False}]},
            {"prompt": "What did the junior colleague realise after the mentor confided her own doubts?", "options": [
                {"label": "That she herself, and much of the department, felt exactly the same way.", "value": "right", "correct": True},
                {"label": "That the mentor was planning to leave the company.", "value": "wrong", "correct": False}]},
            {"prompt": "What do sufferers of impostor syndrome typically do with genuine praise?", "options": [
                {"label": "They dismiss it outright, treating it as unearned.", "value": "right", "correct": True},
                {"label": "They accept it immediately and confidently.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "meticulous": {"word": "meticulous", "ipa": "/məˈtɪk.jʊ.ləs/", "meaning": "very careful and precise about details", "example": "She had performed hundreds of meticulous operations."},
            "attribute": {"word": "attribute", "ipa": "/əˈtrɪb.juːt/", "meaning": "to say that something is caused by or due to something else", "example": "He attributed the paper's success to his co-author, not himself."},
            "competence": {"word": "competence", "ipa": "/ˈkɒm.pɪ.təns/", "meaning": "the ability to do something well or effectively", "example": "She rarely gave herself credit for her own competence."},
            "chronic": {"word": "chronic", "ipa": "/ˈkrɒn.ɪk/", "meaning": "persisting for a long time; long-lasting rather than temporary", "example": "For some, the self-doubt becomes chronic rather than fading."},
            "confided": {"word": "confided", "ipa": "/kənˈfaɪ.dɪd/", "meaning": "told someone a secret or private feeling, trusting them", "example": "The mentor confided her own doubts at a team dinner."},
            "dismiss": {"word": "dismiss", "ipa": "/dɪˈsmɪs/", "meaning": "to refuse to take something seriously, to reject it as unimportant", "example": "She would dismiss every compliment she received."},
            "fraud": {"word": "fraud", "ipa": "/frɔːd/", "meaning": "a person who pretends to be something they are not, a deceiver", "example": "He lived in fear of being exposed as a fraud."},
            "validation": {"word": "validation", "ipa": "/ˌvæl.ɪˈdeɪ.ʃən/", "meaning": "confirmation or recognition that someone or something is valid or worthy", "example": "Therapists suggest seeking outside validation only sparingly."},
        },
        "gram_explanations": {
            "g1": "Substitution with \"so\" — replaces the whole clause \"that I feel like a fraud\" after the verb \"think\".",
            "g2": "Substitution with \"neither had\" — negative agreement with \"had never told a colleague\", with subject-auxiliary inversion.",
            "g3": "Substitution with \"so did\" — positive agreement with \"felt exactly the same way\", with subject-auxiliary inversion.",
            "g4": "Ellipsis after \"if\" — the full form would be \"if it is necessary\"; subject and verb are omitted.",
            "g5": "Substitution with \"if so\" — replaces the whole clause \"if it genuinely comes up\".",
            "g6": "Substitution with \"so\" — replaces the whole clause \"that it helps\" after the verb \"hope\"."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "Someone described as \"meticulous\" is…", "options": [{"label": "very careful and precise about details", "value": "right", "correct": True}, {"label": "careless and quick to make mistakes", "value": "wrong", "correct": False}, {"label": "indifferent to the outcome", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Competence\" refers to…", "options": [{"label": "the ability to do something well", "value": "right", "correct": True}, {"label": "a formal qualification or certificate", "value": "wrong", "correct": False}, {"label": "a feeling of extreme confidence", "value": "wrong2", "correct": False}]},
            {"prompt": "If a feeling is \"chronic\", it is…", "options": [{"label": "long-lasting rather than temporary", "value": "right", "correct": True}, {"label": "gone within a few minutes", "value": "wrong", "correct": False}, {"label": "impossible to describe", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"dismiss\" a compliment means to…", "options": [{"label": "refuse to take it seriously", "value": "right", "correct": True}, {"label": "accept it warmly", "value": "wrong", "correct": False}, {"label": "repeat it to someone else", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Validation\" is…", "options": [{"label": "confirmation that something or someone is worthy", "value": "right", "correct": True}, {"label": "a formal written complaint", "value": "wrong", "correct": False}, {"label": "a type of financial penalty", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "He", "after": "the paper's success to his co-author.", "answers": ["attributed"], "width": 100},
            {"before": "The mentor", "after": "her own doubts at dinner.", "answers": ["confided"], "width": 110},
            {"before": "He lived in fear of being exposed as a", "after": ".", "answers": ["fraud"], "width": 90},
            {"before": "For some, the self-doubt becomes", "after": "rather than fading.", "answers": ["chronic"], "width": 100},
        ],
    },
    "practice": {
        "gapfill_focus": "so / neither-nor / one / ellipsis — pick the right substitution or omission.",
        "gapfill": [
            {"before": "\"Is the deal confirmed?\" \"I believe", "after": ".\"", "answers": ["so"]},
            {"before": "She hasn't signed the contract yet, and", "after": "has her partner.", "answers": ["neither"]},
            {"before": "Please submit the form early", "after": "(=if it is possible).", "answers": ["if possible"]},
            {"before": "He didn't agree with the plan, and", "after": "did I.", "answers": ["neither", "nor"]},
            {"before": "I'll take the red folder, not the blue", "after": ".", "answers": ["one"]},
            {"before": "\"Will they approve the merger?\" \"I hope", "after": ".\"", "answers": ["so"]},
        ],
        "second": {
            "type": "categorise", "title": "Ellipsis or substitution?",
            "instruction": "Tap whether the underlined idea in each sentence was deleted (ellipsis) or replaced with a word (substitution).",
            "categories": ["Ellipsis (words deleted)", "Substitution (words replaced)"],
            "items": [
                {"prompt": "\"Contact IT if needed.\"", "correct": "Ellipsis (words deleted)"},
                {"prompt": "\"He passed the exam, and so did she.\"", "correct": "Substitution (words replaced)"},
                {"prompt": "\"She can present today, but I can't.\"", "correct": "Ellipsis (words deleted)"},
                {"prompt": "\"I don't want this version, I want the older one.\"", "correct": "Substitution (words replaced)"},
            ],
        },
        "builders": [
            {"words": ["He", "didn't", "reply,", "and", "neither", "did", "she."]},
            {"words": ["Update", "the", "spreadsheet", "if", "necessary."]},
            {"words": ["I'd", "rather", "take", "the", "smaller", "one."]},
        ],
    },
    "speaking": {
        "solo_text": "Talk about a recent decision at work (yours or a team's), using at least one substitution (so, neither, one) and one ellipsis (if necessary, when possible).",
        "group_questions": [
            "Tell your group about a time you agreed with someone using 'so did I' or disagreed using 'neither did I' or 'nor did I'.",
            "Describe two options you once had to choose between (\"I preferred the... one\").",
            "What's an instruction you've heard at work that used ellipsis, like 'if necessary' or 'when possible'?",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are having a surprisingly honest conversation over coffee.",
        "dialogue": [
            {"speaker": "Anna", "line": "Honestly, sometimes I still feel like a total fraud, even after ten years in this job."},
            {"speaker": "Tomasz", "line": "Same here. I think most people in this office feel like that, if I'm honest."},
            {"speaker": "Anna", "line": "Really? I always assumed it was just me."},
            {"speaker": "Tomasz", "line": "Definitely not — and apparently so did half the senior team, according to an article I read."},
            {"speaker": "Anna", "line": "I dismiss compliments constantly. I just assume people are being polite."},
            {"speaker": "Tomasz", "line": "Neither do I take them seriously, most of the time, if I'm honest."},
            {"speaker": "Anna", "line": "The article suggested keeping a list of achievements, to reread if necessary. Do you think that would actually help?"},
            {"speaker": "Tomasz", "line": "I hope so, honestly."},
        ],
        "comprehension": [
            {"prompt": "What does Tomasz say about feeling like a fraud?", "options": [{"label": "He thinks most people in the office feel that way too.", "value": "right", "correct": True}, {"label": "He has never felt that way at all.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Anna do when she receives a compliment?", "options": [{"label": "She dismisses it, assuming people are just being polite.", "value": "right", "correct": True}, {"label": "She accepts it confidently every time.", "value": "wrong", "correct": False}]},
            {"prompt": "What does the article Tomasz read suggest doing?", "options": [{"label": "Keeping a list of achievements to reread if necessary.", "value": "right", "correct": True}, {"label": "Avoiding all compliments from colleagues.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "\"Is the report ready?\" \"I think ___.\"", "options": [{"label": "so", "value": "right", "correct": True}, {"label": "it", "value": "wrong", "correct": False}]},
        {"prompt": "He didn't finish on time, and ___ did she.", "options": [{"label": "neither", "value": "right", "correct": True}, {"label": "so", "value": "wrong", "correct": False}]},
        {"prompt": "Please revise the plan ___ (=if it is needed).", "options": [{"label": "if needed", "value": "right", "correct": True}, {"label": "if it needed", "value": "wrong", "correct": False}]},
        {"prompt": "I don't like this design, I prefer the older ___.", "options": [{"label": "one", "value": "right", "correct": True}, {"label": "it", "value": "wrong", "correct": False}]},
        {"prompt": "\"Will they extend the deadline?\" \"I hope ___.\"", "options": [{"label": "so", "value": "right", "correct": True}, {"label": "that", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 18 — Negative Inversion for Emphasis
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-18-negative-inversion",
    "num": 18, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Negative Inversion for Emphasis",
    "subtitle": "Never have I..., Rarely does..., Not only... but also..., Under no circumstances... — fronting negatives for dramatic effect.",
    "warmup_intro": "When a negative or restrictive adverbial (never, rarely, not only, under no circumstances) is moved to the front of a sentence for emphasis, the subject and auxiliary verb invert — exactly like in a question.",
    "warmup": [
        {"prompt": "\"Never have I seen such chaos\" is a more emphatic version of…", "options": [{"label": "\"I have never seen such chaos.\"", "value": "right", "correct": True}, {"label": "\"I have seen chaos sometimes.\"", "value": "wrong", "correct": False}]},
        {"prompt": "\"Rarely does he arrive on time\" uses inversion because…", "options": [{"label": "\"rarely\" is fronted for emphasis, triggering subject-auxiliary inversion", "value": "right", "correct": True}, {"label": "\"rarely\" always requires the past tense", "value": "wrong", "correct": False}]},
        {"prompt": "\"Under no circumstances should you share this password\" is stronger than…", "options": [{"label": "\"You should not share this password under any circumstances.\"", "value": "right", "correct": True}, {"label": "\"You can share this password sometimes.\"", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "If the sentence starts with a negative/limiting expression (never, rarely, seldom, not only, under no circumstances, little), invert the subject and the first auxiliary — just like forming a question.",
    "diagnostic": [
        {"prompt": "Never ___ such a disorganised handover before.", "options": [{"label": "have I seen", "value": "right", "correct": True}, {"label": "I have seen", "value": "wrong", "correct": False}]},
        {"prompt": "Rarely ___ the board this divided on a single issue.", "options": [{"label": "is", "value": "right", "correct": True}, {"label": "was", "value": "wrong", "correct": False}]},
        {"prompt": "Not only ___ the deadline, but she also exceeded every target.", "options": [{"label": "did she meet", "value": "right", "correct": True}, {"label": "she met", "value": "wrong", "correct": False}]},
        {"prompt": "Under no circumstances ___ this data with a third party.", "options": [{"label": "should you share", "value": "right", "correct": True}, {"label": "you should share", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Fronted negatives trigger inversion",
        "intro": "Moving a negative or restrictive expression to the front of a sentence for emphasis forces subject-auxiliary inversion, exactly as in a question — a hallmark of formal, emphatic written English.",
        "tabs": [{"key": "never", "label": "Never / Rarely / Seldom"}, {"key": "notonly", "label": "Not only... but also"}, {"key": "circumstances", "label": "Under no circumstances / Little"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "never": [
                {"label": "emphasising something has never happened", "example": "Never have we faced a crisis of this scale."},
                {"label": "emphasising something happens very infrequently", "example": "Rarely does the CEO address staff directly."},
            ],
            "notonly": [
                {"label": "adding a second, stronger point", "example": "Not only did sales rise, but profits doubled too."},
                {"label": "emphasising a surprising combination", "example": "Not only is she a lawyer, but she also runs a startup."},
            ],
            "circumstances": [
                {"label": "an absolute prohibition", "example": "Under no circumstances should this door be left unlocked."},
                {"label": "a surprising realisation, formal/literary tone", "example": "Little did they know the merger would collapse within weeks."},
            ],
        },
        "quiz_labels": {"never": "Never / Rarely / Seldom + inversion", "notonly": "Not only + inversion... but also", "circumstances": "Under no circumstances / Little + inversion"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Never/Rarely/Seldom + auxiliary + subject + verb: "Rarely does she complain."</div>
          <div class="formula" style="border-left-color:var(--c-continuous)">✅ Not only + auxiliary + subject + verb, but (also) + clause: "Not only did he apologise, but he also offered a refund."</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ Under no circumstances / On no account / Little + auxiliary + subject + verb: "Under no circumstances should you forward this email."</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> if there's no existing auxiliary, you must add \"do/does/did\" — just like forming a question — you can't simply swap word order with the main verb.<br><br>
            ❌ "Rarely he arrives on time."<br>
            ✅ "Rarely does he arrive on time."<br><br>
            Also, this inversion only happens with a genuinely fronted negative/limiting expression — an ordinary sentence with "never" in its usual mid-position ("I have never seen that") does NOT invert.</span>
          </div>'''
    },
    "compare": {
        "title": "Neutral statement vs. emphatic inversion",
        "instruction": "Hover to see how fronting the negative changes the tone.",
        "items": [
            {"key": "c1", "label": "Neutral", "text": "I have never seen such a disorganised handover.", "explain": "Standard word order — a plain statement of fact."},
            {"key": "c2", "label": "Emphatic (inverted)", "text": "Never have I seen such a disorganised handover.", "explain": "Fronting \"never\" and inverting creates a much stronger, almost dramatic emphasis — common in speeches and formal writing."},
            {"key": "c3", "label": "Neutral", "text": "She met the deadline and also exceeded every target.", "explain": "A plain coordinated sentence — informative but unremarkable."},
            {"key": "c4", "label": "Emphatic (inverted)", "text": "Not only did she meet the deadline, but she also exceeded every target.", "explain": "\"Not only\" fronted with inversion sets up a stronger, more rhetorical second point introduced by \"but also\"."},
        ]
    },
    "reading": {
        "heading": "Why Everyone Suddenly Wants the Same Thing",
        "passage_paragraphs": [
            f'''{gram("g1","Never before has")} a management trend spread as fast as agile transformation did in the early 2010s, moving from a handful of software teams to entire corporations within a few short years. Researchers studying the phenomenon describe something close to a bandwagon effect: firms {vocab("adopt","adopt")} a new practice not because internal evidence supports it, but because enough visible rivals already have. A single influential case study, repeated at enough conferences, can turn a niche idea into an unavoidable {vocab("buzzword","buzzword")}.''',
            f'''{gram("g2","Rarely do executives")} pause long enough to ask whether a trend actually suits their own company, choosing instead to {vocab("imitate","imitate")} the confident language of consultants and competitors. Genuine {vocab("due diligence","due diligence")} — quietly testing an idea before committing budget to it — gets skipped almost entirely; {gram("g3","not once did")} anyone on the board of one major retailer ask whether the idea would actually work in their specific context.''',
            f'''{gram("g4","Not only do companies imitate")} their most visible rivals, but they also mistake popularity itself for proof of value — the more {vocab("faddish","faddish")} an idea appears, the more urgently it seems to demand adoption. {gram("g5","Under no circumstances would")} a rational planner recommend adopting an untested framework purely because it is fashionable, and yet {vocab("entrenched","entrenched")} habits of imitation quietly override that caution in one company after another. {gram("g6","Seldom does")} anyone {vocab("herald","herald")} the eventual, quiet abandonment of a failed trend with anything like the fanfare that greeted its arrival — it simply fades, adopted {vocab("unquestioningly","unquestioningly")} in one wave and abandoned just as quietly in the next.''',
        ],
        "comprehension": [
            {"prompt": "According to the passage, why do firms often adopt a new management trend?", "options": [
                {"label": "Because enough visible rivals have already adopted it, not because of internal evidence.", "value": "right", "correct": True},
                {"label": "Because independent research has proven it improves results.", "value": "wrong", "correct": False}]},
            {"prompt": "What does the passage say typically gets skipped when a trend spreads quickly?", "options": [
                {"label": "Genuine due diligence, such as quietly testing the idea first.", "value": "right", "correct": True},
                {"label": "The announcement of the new practice to staff.", "value": "wrong", "correct": False}]},
            {"prompt": "What happens when a trend eventually fails, according to the final paragraph?", "options": [
                {"label": "It quietly fades away, without the fanfare that greeted its arrival.", "value": "right", "correct": True},
                {"label": "Companies formally announce and analyse its failure in detail.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "adopt": {"word": "adopt", "ipa": "/əˈdɒpt/", "meaning": "to begin to use a new practice, method or idea", "example": "Firms adopt a trend because rivals already have."},
            "buzzword": {"word": "buzzword", "ipa": "/ˈbʌz.wɜːd/", "meaning": "a fashionable word or phrase, often with little real substance behind it", "example": "The idea turned into an unavoidable buzzword at conferences."},
            "imitate": {"word": "imitate", "ipa": "/ˈɪm.ɪ.teɪt/", "meaning": "to copy the behaviour, style or actions of someone else", "example": "Executives often imitate the language of confident competitors."},
            "due diligence": {"word": "due diligence", "ipa": "/ˌdjuː ˈdɪl.ɪ.dʒəns/", "meaning": "careful investigation or checking carried out before making a decision", "example": "Genuine due diligence gets skipped when a trend spreads fast."},
            "faddish": {"word": "faddish", "ipa": "/ˈfæd.ɪʃ/", "meaning": "temporarily fashionable, likely to go out of style quickly", "example": "The more faddish an idea seemed, the faster it spread."},
            "entrenched": {"word": "entrenched", "ipa": "/ɪnˈtren(t)ʃt/", "meaning": "firmly established and difficult to change", "example": "Entrenched habits of imitation override careful planning."},
            "herald": {"word": "herald", "ipa": "/ˈher.əld/", "meaning": "to announce or publicly signal the approach of something", "example": "Nobody tends to herald the quiet failure of a trend."},
            "unquestioningly": {"word": "unquestioningly", "ipa": "/ʌnˈkwes.tʃən.ɪŋ.li/", "meaning": "without asking questions or expressing any doubt", "example": "The framework was adopted unquestioningly across the company."},
        },
        "gram_explanations": {
            "g1": "\"Never before has\" — fronted negative time expression + present perfect inversion, emphasising this was unprecedented.",
            "g2": "\"Rarely do executives\" — fronted frequency adverb triggers inversion with \"do\".",
            "g3": "\"Not once did\" — fronted negative frequency expression triggers inversion with \"did\".",
            "g4": "\"Not only do companies imitate\" — fronted \"not only\" triggers inversion with \"do\", paired later with \"but also\".",
            "g5": "\"Under no circumstances would\" — fronted absolute-limiting phrase triggers inversion with \"would\".",
            "g6": "\"Seldom does\" — fronted frequency adverb triggers inversion with \"does\"."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "A \"buzzword\" is…", "options": [{"label": "a fashionable term often with little real substance", "value": "right", "correct": True}, {"label": "a precise technical measurement", "value": "wrong", "correct": False}, {"label": "a formal legal term", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"imitate\" someone means to…", "options": [{"label": "copy their behaviour or actions", "value": "right", "correct": True}, {"label": "strongly criticise them", "value": "wrong", "correct": False}, {"label": "completely ignore them", "value": "wrong2", "correct": False}]},
            {"prompt": "Something \"faddish\" is…", "options": [{"label": "temporarily fashionable, likely to fade quickly", "value": "right", "correct": True}, {"label": "permanently and reliably useful", "value": "wrong", "correct": False}, {"label": "extremely rare and unknown", "value": "wrong2", "correct": False}]},
            {"prompt": "If a habit is \"entrenched\", it is…", "options": [{"label": "firmly established and hard to change", "value": "right", "correct": True}, {"label": "brand new and untested", "value": "wrong", "correct": False}, {"label": "already completely abandoned", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"herald\" something means to…", "options": [{"label": "announce or signal its approach publicly", "value": "right", "correct": True}, {"label": "quietly hide it from view", "value": "wrong", "correct": False}, {"label": "formally cancel it", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "Firms often", "after": "a trend simply because rivals already have.", "answers": ["adopt"], "width": 100},
            {"before": "Genuine", "after": "gets skipped when a trend spreads fast.", "answers": ["due diligence"], "width": 130},
            {"before": "The framework was adopted", "after": "across the company.", "answers": ["unquestioningly"], "width": 140},
            {"before": "The idea turned into an unavoidable", "after": "at conferences.", "answers": ["buzzword"], "width": 110},
        ],
    },
    "practice": {
        "gapfill_focus": "negative inversion — never, rarely, not only, under no circumstances.",
        "gapfill": [
            {"before": "Never", "after": "(see) such a chaotic handover before.", "answers": ["have I seen"]},
            {"before": "Rarely", "after": "(arrive) before nine.", "answers": ["does he arrive"]},
            {"before": "Not only", "after": "(rise) revenue, but profits also doubled.", "answers": ["did"]},
            {"before": "Under no circumstances", "after": "(share) this password with anyone.", "answers": ["should you share"]},
            {"before": "Little", "after": "(know) how close the deal came to collapsing.", "answers": ["did we know", "did they know"]},
            {"before": "Seldom", "after": "(agree) so quickly on a major decision.", "answers": ["does the board agree", "has the board agreed"]},
        ],
        "second": {
            "type": "errorspot", "title": "Spot the mistake",
            "instruction": "One word is wrong in each sentence. Tap it, then check the correction.",
            "items": [
                {"words": ["Never", "I", "have", "seen", "such", "a", "disorganised", "handover", "before."], "error_indices": [1, 2], "correction": "\"I have\" → \"have I\" (fronted \"never\" requires subject-auxiliary inversion)"},
                {"words": ["Rarely", "he", "arrives", "before", "nine", "in", "the", "morning."], "error_indices": [1, 2], "correction": "\"he arrives\" → \"does he arrive\" (needs \"does\" inversion, no existing auxiliary)"},
                {"words": ["Under", "no", "circumstances", "you", "should", "share", "this", "data."], "error_indices": [3, 4], "correction": "\"you should\" → \"should you\" (fronted negative phrase requires inversion)"},
            ],
        },
        "builders": [
            {"words": ["Never", "have", "I", "seen", "such", "a", "volatile", "market."]},
            {"words": ["Not", "only", "did", "revenue", "rise,", "but", "profits", "doubled."]},
            {"words": ["Under", "no", "circumstances", "should", "you", "forward", "this", "email."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe an unusual or impressive result at work (or in your life), using at least two inverted structures: never/rarely + inversion, and not only... but also.",
        "group_questions": [
            "Tell your group about something you have never experienced before at work, using 'Never have I...'",
            "Describe a rule at your workplace that should never be broken, using 'Under no circumstances...'",
            "Can you think of a situation where two impressive things happened at once? Describe it using 'Not only... but also...'",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are questioning why their company just adopted yet another management trend.",
        "dialogue": [
            {"speaker": "Anna", "line": "Never before have I seen a company adopt something this fast without any real evaluation."},
            {"speaker": "Tomasz", "line": "I know. Rarely does anyone here ask if a trend actually fits what we do."},
            {"speaker": "Anna", "line": "Exactly. Not only did we adopt the new framework, but we also dropped the old one overnight."},
            {"speaker": "Tomasz", "line": "Under no circumstances should we have skipped due diligence like that."},
            {"speaker": "Anna", "line": "Seldom does management admit a trend failed once it's fashionable elsewhere."},
            {"speaker": "Tomasz", "line": "True. Not once did anyone ask what happens once everyone else moves on to the next buzzword."},
            {"speaker": "Anna", "line": "It's a classic bandwagon effect, if you ask me."},
            {"speaker": "Tomasz", "line": "Completely. Let's hope we ask better questions next time."},
        ],
        "comprehension": [
            {"prompt": "What does Anna find unusual about how the company adopted the new trend?", "options": [{"label": "It happened extremely fast without any real evaluation.", "value": "right", "correct": True}, {"label": "It took several years of careful discussion.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Tomasz say should not have happened?", "options": [{"label": "Skipping due diligence before adopting the framework.", "value": "right", "correct": True}, {"label": "Consulting external experts before deciding.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Anna call the pattern they are describing?", "options": [{"label": "A classic bandwagon effect.", "value": "right", "correct": True}, {"label": "A carefully planned strategic shift.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "Never ___ such a disorganised handover before.", "options": [{"label": "have I seen", "value": "right", "correct": True}, {"label": "I have seen", "value": "wrong", "correct": False}]},
        {"prompt": "Rarely ___ the team this united on a decision.", "options": [{"label": "is", "value": "right", "correct": True}, {"label": "was", "value": "wrong", "correct": False}]},
        {"prompt": "Not only ___ the target, but she also exceeded it.", "options": [{"label": "did she meet", "value": "right", "correct": True}, {"label": "she met", "value": "wrong", "correct": False}]},
        {"prompt": "Under no circumstances ___ this file with outside parties.", "options": [{"label": "should you share", "value": "right", "correct": True}, {"label": "you should share", "value": "wrong", "correct": False}]},
        {"prompt": "Little ___ how close the deal came to collapsing.", "options": [{"label": "did they know", "value": "right", "correct": True}, {"label": "they did know", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 19 — Fronting & Information Structure
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-19-fronting-information-structure",
    "num": 19, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Fronting & Information Structure",
    "subtitle": "Moving an object, complement or adverbial to the front of a sentence to control emphasis and cohesion.",
    "warmup_intro": "English word order is normally fixed (subject-verb-object), but writers often move an element to the front to emphasise it or link it smoothly to the previous sentence — a technique called fronting.",
    "warmup": [
        {"prompt": "\"Such was the demand that tickets sold out in minutes\" emphasises…", "options": [{"label": "the extreme scale of the demand", "value": "right", "correct": True}, {"label": "the exact time the tickets went on sale", "value": "wrong", "correct": False}]},
        {"prompt": "\"A particularly thorny issue is client confidentiality\" fronts the complement to…", "options": [{"label": "highlight the topic before naming it precisely", "value": "right", "correct": True}, {"label": "avoid mentioning who raised the issue", "value": "wrong", "correct": False}]},
        {"prompt": "\"This report, we cannot publish without legal review\" fronts the object mainly to…", "options": [{"label": "connect back to something already mentioned, for cohesion", "value": "right", "correct": True}, {"label": "make the sentence grammatically necessary", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "Fronting is optional, not required by grammar rules — writers choose it purely for emphasis or to link ideas smoothly across sentences.",
    "diagnostic": [
        {"prompt": "___ was the level of interest that the event had to be moved to a bigger venue.", "options": [{"label": "Such", "value": "right", "correct": True}, {"label": "So", "value": "wrong", "correct": False}]},
        {"prompt": "___ still unresolved is the question of funding.", "options": [{"label": "Also", "value": "right", "correct": True}, {"label": "There", "value": "wrong", "correct": False}]},
        {"prompt": "This particular clause, the lawyers ___ flagged as high-risk.", "options": [{"label": "have already", "value": "right", "correct": True}, {"label": "already have", "value": "wrong", "correct": False}]},
        {"prompt": "A key challenge ___ maintaining morale during the restructuring.", "options": [{"label": "is", "value": "right", "correct": True}, {"label": "are", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Fronting an object, complement, or adverbial",
        "intro": "Fronting moves something other than the subject to the front of the sentence, for emphasis or to connect smoothly with what came before. \"Such/so\" fronting with an inverted clause is a particularly formal variant.",
        "tabs": [{"key": "object", "label": "Fronted object"}, {"key": "complement", "label": "Fronted complement"}, {"key": "suchso", "label": "Such/So + inversion"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "object": [
                {"label": "connecting back to something already mentioned", "example": "This proposal, the board rejected outright."},
                {"label": "contrasting one thing with another already discussed", "example": "The first draft, everyone liked; the second, nobody did."},
            ],
            "complement": [
                {"label": "introducing a topic before naming the subject", "example": "A recurring problem is staff turnover."},
                {"label": "emphasising an evaluation before the subject", "example": "Far more concerning is the drop in customer satisfaction."},
            ],
            "suchso": [
                {"label": "'such' + be + subject + that-clause, showing extreme degree", "example": "Such was the chaos that the launch was postponed."},
                {"label": "'so' + adjective + be + subject, similar emphatic effect", "example": "So great was the pressure that two managers resigned."},
            ],
        },
        "quiz_labels": {"object": "Fronted object", "complement": "Fronted complement", "suchso": "Such/So + inversion"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Fronted object: <b>object + subject + verb</b> — "This report, we cannot publish yet."</div>
          <div class="formula" style="border-left-color:var(--c-continuous)">✅ Fronted complement: <b>complement + be + subject</b> — "A major concern is data security."</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ Such/So + inversion: <b>Such + be + subject + that...</b> or <b>So + adjective + be + subject + that...</b> — "Such was the demand that we sold out in an hour."</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> fronting a complement with "be" often requires subject-verb inversion too, because the complement is now doing the job a subject normally does at the front of the sentence.<br><br>
            ✅ "A recurring problem is staff turnover." (complement fronted, "is" stays before the real subject "staff turnover")<br>
            ✅ "Such was the demand that tickets sold out." — inversion after \"such\" is fixed and non-negotiable in this pattern.<br><br>
            Fronting an object rarely needs inversion — the subject and verb usually keep their normal order after the fronted object.</span>
          </div>'''
    },
    "compare": {
        "title": "Normal order vs. fronted for emphasis",
        "instruction": "Hover over each to see what fronting achieves here.",
        "items": [
            {"key": "c1", "label": "Normal order", "text": "We cannot publish this report without legal review.", "explain": "Standard SVO order — neutral, no special emphasis."},
            {"key": "c2", "label": "Fronted object", "text": "This report, we cannot publish without legal review.", "explain": "Fronting \"this report\" links back to something already under discussion and highlights it as the topic."},
            {"key": "c3", "label": "Normal order", "text": "Staff turnover is a recurring problem.", "explain": "Standard order, subject first."},
            {"key": "c4", "label": "Fronted complement", "text": "A recurring problem is staff turnover.", "explain": "Fronting the complement introduces the topic (\"a recurring problem\") before revealing exactly what it is."},
        ]
    },
    "reading": {
        "heading": "Why We Love What We Build Ourselves",
        "passage_paragraphs": [
            f'''{gram("g1","Such was the appeal")} of self-assembled furniture that one Swedish retailer built an entire empire on it. Researchers studying the phenomenon found something curious: people who {vocab("assemble","assemble")} a piece of furniture themselves consistently rate it as more valuable than an identical, pre-built version — even when the finished product looks objectively worse. {gram("g2","A particularly striking finding")} was that this effect held even for {vocab("laborious","laborious")} tasks that most participants openly disliked while doing them.''',
            f'''{gram("g3","This attachment")}, psychologists suspect, has little to do with the object itself and everything to do with effort. {gram("g4","So strong is the pull of one's own labour")} that people will {vocab("overvalue","overvalue")} a wobbly, imperfect shelf simply because they built it themselves. {gram("g5","Also documented")} is a matching effect in cooking, gardening and even spreadsheets: people rate a recipe, a garden, or a file as better once they have invested real effort building it.''',
            f'''{gram("g6","This flawed final product")}, participants rarely blame; instead, they grow quietly {vocab("sentimental","sentimental")} about the very screws and brackets that gave them so much trouble. {gram("g7","A key implication")} for {vocab("flat-pack","flat-pack")} retailers, and for anyone designing a product, is that a little {vocab("friction","friction")}, a chance to {vocab("tinker","tinker")} — deliberately included — can build stronger loyalty than a flawless, ready-made version ever could. Marketers now sometimes call this {vocab("effort-justification","effort justification")}: we justify our effort, after the fact, by inflating the value of what that effort produced.''',
        ],
        "comprehension": [
            {"prompt": "What did researchers find about people who assemble furniture themselves?", "options": [
                {"label": "They rate it as more valuable than an identical pre-built version.", "value": "right", "correct": True},
                {"label": "They consistently rate it as worse than a pre-built version.", "value": "wrong", "correct": False}]},
            {"prompt": "According to psychologists, what does the extra attachment mainly depend on?", "options": [
                {"label": "The effort invested, rather than the object itself.", "value": "right", "correct": True},
                {"label": "The original price of the materials used.", "value": "wrong", "correct": False}]},
            {"prompt": "What implication does the passage draw for product design?", "options": [
                {"label": "A little deliberate friction or assembly can build stronger loyalty.", "value": "right", "correct": True},
                {"label": "Products should always arrive fully assembled to maximise loyalty.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "assemble": {"word": "assemble", "ipa": "/əˈsem.bəl/", "meaning": "to fit parts together in order to build a complete object", "example": "Most customers assemble the furniture themselves at home."},
            "laborious": {"word": "laborious", "ipa": "/ləˈbɔː.ri.əs/", "meaning": "requiring a lot of time and effort; tedious", "example": "The task was laborious, yet people still valued the result."},
            "overvalue": {"word": "overvalue", "ipa": "/ˌəʊ.vəˈvæl.juː/", "meaning": "to judge something as worth more than it actually is", "example": "People tend to overvalue things they built themselves."},
            "sentimental": {"word": "sentimental", "ipa": "/ˌsen.tɪˈmen.təl/", "meaning": "feeling emotional attachment to something beyond its practical worth", "example": "She grew sentimental about the wonky shelf she'd built."},
            "flat-pack": {"word": "flat-pack", "ipa": "/ˈflæt.pæk/", "meaning": "(furniture) sold unassembled in a flat box, to be built by the buyer", "example": "Flat-pack retailers rely heavily on this psychological effect."},
            "friction": {"word": "friction", "ipa": "/ˈfrɪk.ʃən/", "meaning": "a small amount of difficulty or resistance built into a process", "example": "A little friction in the process can actually build loyalty."},
            "tinker": {"word": "tinker", "ipa": "/ˈtɪŋ.kər/", "meaning": "to make small adjustments or attempts to fix or improve something", "example": "Letting customers tinker with the design increased satisfaction."},
            "effort-justification": {"word": "effort justification", "ipa": "/ˈef.ət ˌdʒʌs.tɪ.fɪˈkeɪ.ʃən/", "meaning": "the tendency to inflate the value of an outcome to justify the effort spent achieving it", "example": "Marketers call this pattern effort justification."},
        },
        "gram_explanations": {
            "g1": "\"Such was the appeal\" — fronted \"such\" with inversion, showing an extreme degree, followed by a \"that\"-clause.",
            "g2": "Fronted complement — \"a particularly striking finding\" introduced before naming exactly what it was.",
            "g3": "Fronted object — \"this attachment\" links back to the idea just introduced, for cohesion.",
            "g4": "\"So strong is the pull\" — fronted \"so + adjective\" with inversion, showing extreme degree, followed by \"that\".",
            "g5": "Fronted complement with inversion — \"also documented\" introduces the topic before the real subject \"a matching effect\".",
            "g6": "Fronted object — \"this flawed final product\" links back to the previous idea and sets up the contrast that follows.",
            "g7": "Fronted complement — \"a key implication\" introduces the topic before revealing what it actually is."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "If a task is \"laborious\", it is…", "options": [{"label": "requiring a lot of time and effort", "value": "right", "correct": True}, {"label": "quick and effortless", "value": "wrong", "correct": False}, {"label": "impossible to complete", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"overvalue\" something means to…", "options": [{"label": "judge it as worth more than it actually is", "value": "right", "correct": True}, {"label": "judge it as worth less than it actually is", "value": "wrong", "correct": False}, {"label": "ignore its value entirely", "value": "wrong2", "correct": False}]},
            {"prompt": "If someone feels \"sentimental\" about an object, they…", "options": [{"label": "have an emotional attachment to it beyond its practical worth", "value": "right", "correct": True}, {"label": "have no feelings about it whatsoever", "value": "wrong", "correct": False}, {"label": "want to sell it immediately", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Flat-pack\" furniture is sold…", "options": [{"label": "unassembled, to be built by the buyer", "value": "right", "correct": True}, {"label": "fully built and ready to use", "value": "wrong", "correct": False}, {"label": "only as digital design plans", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Effort justification\" describes the tendency to…", "options": [{"label": "inflate the value of an outcome to justify the effort spent", "value": "right", "correct": True}, {"label": "avoid effort of any kind whenever possible", "value": "wrong", "correct": False}, {"label": "always underestimate one's own effort", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "Most customers", "after": "the furniture themselves at home.", "answers": ["assemble"], "width": 100},
            {"before": "Letting customers", "after": "with the design increased satisfaction.", "answers": ["tinker"], "width": 90},
            {"before": "A little", "after": "in the process can actually build loyalty.", "answers": ["friction"], "width": 100},
            {"before": "", "after": "retailers rely heavily on this effect.", "answers": ["Flat-pack"], "width": 100},
        ],
    },
    "practice": {
        "gapfill_focus": "fronted object, fronted complement, or such/so + inversion?",
        "gapfill": [
            {"before": "", "after": "(such/demand) that the servers crashed within minutes.", "answers": ["Such was the demand"]},
            {"before": "This particular clause,", "after": "(the lawyers/already/flag) as high-risk.", "answers": ["the lawyers had already flagged", "the lawyers have already flagged"]},
            {"before": "A recurring problem", "after": "(be) staff turnover in the sales team.", "answers": ["is"]},
            {"before": "", "after": "(so/severe/backlog) that new orders were suspended.", "answers": ["So severe was the backlog"]},
            {"before": "The original plan,", "after": "(in hindsight/we/should/test) more thoroughly.", "answers": ["we should have tested"]},
            {"before": "Far more concerning", "after": "(be) the drop in customer satisfaction.", "answers": ["is"]},
        ],
        "second": {
            "type": "categorise", "title": "Fronted object, complement, or such/so + inversion?",
            "instruction": "Tap the category that matches each sentence's fronted element.",
            "categories": ["Fronted object", "Fronted complement", "Such/So + inversion"],
            "items": [
                {"prompt": "\"This proposal, the board rejected outright.\"", "correct": "Fronted object"},
                {"prompt": "\"A key challenge is maintaining morale.\"", "correct": "Fronted complement"},
                {"prompt": "\"Such was the pressure that two managers resigned.\"", "correct": "Such/So + inversion"},
                {"prompt": "\"The first draft, everyone liked immediately.\"", "correct": "Fronted object"},
            ],
        },
        "builders": [
            {"words": ["Such", "was", "the", "demand", "that", "tickets", "sold", "out", "instantly."]},
            {"words": ["A", "recurring", "problem", "is", "staff", "turnover."]},
            {"words": ["This", "report,", "we", "cannot", "publish", "without", "review."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a challenge or crisis at work using at least one fronted complement ('A key issue is...') and one 'such/so + inversion' structure ('Such was the pressure that...').",
        "group_questions": [
            "Describe something so popular or in such demand that it caused problems. Use 'Such was the demand that...'",
            "What's a recurring problem at your workplace? Try describing it with a fronted complement ('A recurring problem is...').",
            "Tell your group about a decision or document that was strongly rejected or debated, fronting it as the object ('This proposal, they rejected...').",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are comparing notes on furniture they built themselves.",
        "dialogue": [
            {"speaker": "Anna", "line": "Such was my attachment to that wobbly bookshelf I built that I refused to throw it out for years."},
            {"speaker": "Tomasz", "line": "Ha, classic IKEA effect. A particularly striking finding is that people rate self-built furniture higher, even when it looks worse."},
            {"speaker": "Anna", "line": "This attachment, apparently, has nothing to do with the object itself — it's all about the effort."},
            {"speaker": "Tomasz", "line": "So strong is the pull of your own labour that you'll defend a crooked shelf to the death."},
            {"speaker": "Anna", "line": "Also documented is the exact same effect in cooking and gardening, funnily enough."},
            {"speaker": "Tomasz", "line": "This flawed final product thing explains so much about my garden, honestly."},
            {"speaker": "Anna", "line": "A key implication is that companies could build in a little friction on purpose."},
            {"speaker": "Tomasz", "line": "Smart. Let people tinker a bit, and they'll love the result even more."},
        ],
        "comprehension": [
            {"prompt": "Why did Anna refuse to throw out her wobbly bookshelf?", "options": [{"label": "She had built it herself and grew attached to it.", "value": "right", "correct": True}, {"label": "It was the most expensive item she owned.", "value": "wrong", "correct": False}]},
            {"prompt": "According to Tomasz, what is the striking finding about self-built furniture?", "options": [{"label": "People rate it higher even when it looks worse.", "value": "right", "correct": True}, {"label": "People always rate it lower than pre-built furniture.", "value": "wrong", "correct": False}]},
            {"prompt": "What implication does Anna draw for companies?", "options": [{"label": "They could deliberately build in a little friction.", "value": "right", "correct": True}, {"label": "They should remove all effort from the customer experience.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "___ that tickets sold out within minutes.", "options": [{"label": "Such was the demand", "value": "right", "correct": True}, {"label": "Demand was such", "value": "wrong", "correct": False}]},
        {"prompt": "A recurring problem ___ staff turnover.", "options": [{"label": "is", "value": "right", "correct": True}, {"label": "are", "value": "wrong", "correct": False}]},
        {"prompt": "This proposal, the board ___ outright.", "options": [{"label": "rejected", "value": "right", "correct": True}, {"label": "did rejected", "value": "wrong", "correct": False}]},
        {"prompt": "___ that two managers resigned that same week.", "options": [{"label": "So severe was the pressure", "value": "right", "correct": True}, {"label": "The pressure was so severe", "value": "wrong", "correct": False}]},
        {"prompt": "Far more concerning ___ the drop in morale.", "options": [{"label": "is", "value": "right", "correct": True}, {"label": "does", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 20 — Discourse Capstone
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-20-discourse-capstone",
    "num": 20, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Discourse Capstone",
    "subtitle": "Formal connectors (nonetheless, notwithstanding, whereas, in light of, insofar as) plus a cumulative review of the course's key structures.",
    "warmup_intro": "This final lesson introduces the last set of formal discourse connectors used in academic and professional writing, and also asks you to recall several structures from across the whole course — narrative tenses, conditionals, the passive, and participle clauses — all working together, the way real writing actually combines them.",
    "warmup": [
        {"prompt": "\"Nonetheless\" is closest in meaning to…", "options": [{"label": "\"however / despite that\"", "value": "right", "correct": True}, {"label": "\"therefore / as a result\"", "value": "wrong", "correct": False}]},
        {"prompt": "\"Notwithstanding the delays, the project finished on budget\" means…", "options": [{"label": "despite the delays, it finished on budget", "value": "right", "correct": True}, {"label": "because of the delays, it finished on budget", "value": "wrong", "correct": False}]},
        {"prompt": "\"Whereas the first team focused on design, the second focused on testing\" shows…", "options": [{"label": "a contrast between two parallel situations", "value": "right", "correct": True}, {"label": "a cause-and-effect relationship", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "Nonetheless/notwithstanding = formal \"however/despite\". Whereas = formal \"while\", for direct contrast. In light of = \"given/considering\". Insofar as = \"to the extent that\".",
    "diagnostic": [
        {"prompt": "The results were disappointing; ___, the team pressed on.", "options": [{"label": "nonetheless", "value": "right", "correct": True}, {"label": "therefore", "value": "wrong", "correct": False}]},
        {"prompt": "___ the risks involved, the board approved the investment.", "options": [{"label": "Notwithstanding", "value": "right", "correct": True}, {"label": "Because of", "value": "wrong", "correct": False}]},
        {"prompt": "Marketing prioritised speed, ___ engineering prioritised stability.", "options": [{"label": "whereas", "value": "right", "correct": True}, {"label": "so that", "value": "wrong", "correct": False}]},
        {"prompt": "___ the new evidence, the policy will need to be reviewed.", "options": [{"label": "In light of", "value": "right", "correct": True}, {"label": "In case of", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Formal academic and professional connectors",
        "intro": "These connectors mark contrast, concession and reasoning in a more formal register than everyday \"but\", \"so\" or \"because\" — common in reports, academic writing and formal presentations.",
        "tabs": [{"key": "contrast", "label": "Nonetheless / Notwithstanding"}, {"key": "whereas", "label": "Whereas"}, {"key": "reasoning", "label": "In light of / Insofar as"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "contrast": [
                {"label": "'however' in a more formal register", "example": "The launch was delayed; nonetheless, demand remained strong."},
                {"label": "'despite' + noun phrase, very formal", "example": "Notwithstanding the criticism, the plan went ahead unchanged."},
            ],
            "whereas": [
                {"label": "a direct, parallel contrast between two clauses", "example": "The old system was manual, whereas the new one is fully automated."},
            ],
            "reasoning": [
                {"label": "'given/considering' — reasoning from new information", "example": "In light of the recent complaints, the policy was revised."},
                {"label": "'to the extent that' — a limited, conditional claim", "example": "The plan works, insofar as it reduces costs, but it creates new risks."},
            ],
        },
        "quiz_labels": {"contrast": "Nonetheless / Notwithstanding", "whereas": "Whereas (parallel contrast)", "reasoning": "In light of / Insofar as"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Nonetheless (formal "however"): usually starts or joins a new sentence. "Sales fell; nonetheless, profit rose."</div>
          <div class="formula" style="border-left-color:var(--c-continuous)">✅ Notwithstanding + noun phrase (formal "despite"): "Notwithstanding the setbacks, the launch proceeded."</div>
          <div class="formula" style="border-left-color:var(--c-modal);margin-bottom:20px">✅ Whereas + clause (formal "while", for contrast); In light of + noun phrase ("given"); Insofar as + clause ("to the extent that").</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> "notwithstanding" takes a noun phrase, not a full clause, and can even follow the noun phrase it modifies in very formal style: "the risks notwithstanding" or "notwithstanding the risks" — both are correct.<br><br>
            Cumulative reminder: this whole course has combined narrative tenses, conditionals, the passive voice, modality, participle clauses and now discourse connectors — real professional writing constantly mixes all of these together in the same paragraph, exactly as the reading below does.</span>
          </div>'''
    },
    "compare": {
        "title": "Choosing the right formal connector",
        "instruction": "Hover over each to see exactly what relationship it signals.",
        "items": [
            {"key": "c1", "label": "Nonetheless", "text": "The quarter was difficult; nonetheless, the team hit every target.", "explain": "Formal \"however\" — a contrast between two full statements."},
            {"key": "c2", "label": "Notwithstanding", "text": "Notwithstanding the tight deadline, the report was thorough and well-argued.", "explain": "Formal \"despite\" + noun phrase — no full clause needed after it."},
            {"key": "c3", "label": "Whereas", "text": "The London office handles sales, whereas the Berlin office handles support.", "explain": "A direct, parallel contrast between two comparable situations."},
            {"key": "c4", "label": "In light of / Insofar as", "text": "In light of the feedback, the design was revised, insofar as budget allowed.", "explain": "\"In light of\" gives the reason for revising; \"insofar as\" limits the claim to what the budget actually permitted."},
        ]
    },
    "reading": {
        "heading": "Why Effort Shrinks in Teams: The Ringelmann Effect",
        "passage_paragraphs": [
            f'''When Max Ringelmann {gram("g1","conducted")} his now-famous rope-pulling experiments in 1913, he {gram("g2","had")} no idea he was about to name an effect that would apply just as neatly to modern meetings as to farm labourers pulling on a rope. Individuals, tested alone, pulled with a certain measurable force, {gram("g3","whereas")} that same effort, once spread across a group, {gram("g4","was found")} to shrink steadily as more people joined in. {gram("g5","Had each participant been pulling entirely alone")}, the total recorded force would have been dramatically higher.''',
            f'''{gram("g6","Notwithstanding")} a century of further research, the exact psychological mechanism remains only partly understood, though most explanations point to reduced accountability: in a large group, {vocab("diffused","diffused")} responsibility makes any single person's contribution feel less {vocab("consequential","consequential")}. {gram("g7","Rarely does")} anyone in a large team consciously decide to slack off; {vocab("coasting","coasting")} tends to happen quietly, below the level of conscious awareness. {gram("g8","Having studied")} dozens of workplace teams since, researchers now describe this social loafing as one of the most {vocab("replicated","replicated")} findings in group psychology.''',
            f'''{vocab("In light of","In light of")} this evidence, some companies have begun deliberately shrinking team sizes for tasks that reward individual {vocab("accountability","accountability")}, while keeping larger teams, {gram("g9","insofar as")} the work genuinely benefits from parallel effort, for tasks that don't. The effect is not universal — {gram("g10","nonetheless")}, it appears with remarkable consistency across cultures, industries and even species, {vocab("underscoring","underscoring")} just how deeply {vocab("ingrained","ingrained")} the pattern seems to be. A manager, {gram("g11","trained to notice the pattern")}, can design around it; one, {gram("g12","left unaware")}, will simply keep adding people to a struggling project and wonder why productivity per head keeps falling.''',
        ],
        "comprehension": [
            {"prompt": "What did Ringelmann's original rope-pulling experiments show?", "options": [
                {"label": "Individual effort shrank steadily as group size grew.", "value": "right", "correct": True},
                {"label": "Individual effort increased the more people joined in.", "value": "wrong", "correct": False}]},
            {"prompt": "According to the passage, what do most explanations for the effect point to?", "options": [
                {"label": "Reduced accountability once responsibility is diffused across a group.", "value": "right", "correct": True},
                {"label": "A lack of physical strength in larger groups.", "value": "wrong", "correct": False}]},
            {"prompt": "What have some companies begun doing in light of this evidence?", "options": [
                {"label": "Deliberately shrinking team sizes for tasks needing individual accountability.", "value": "right", "correct": True},
                {"label": "Removing all individual accountability from every task.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "diffused": {"word": "diffused", "ipa": "/dɪˈfjuːzd/", "meaning": "spread out among a group, no longer concentrated in one place", "example": "Diffused responsibility makes each person's role feel smaller."},
            "consequential": {"word": "consequential", "ipa": "/ˌkɒn.sɪˈkwen.ʃəl/", "meaning": "important, having significant effects or consequences", "example": "Each contribution felt less consequential in a bigger group."},
            "coasting": {"word": "coasting", "ipa": "/ˈkəʊs.tɪŋ/", "meaning": "making less effort than one is capable of, relying on momentum", "example": "Coasting tends to happen without anyone deciding to do it."},
            "replicated": {"word": "replicated", "ipa": "/ˈrep.lɪ.keɪ.tɪd/", "meaning": "repeated with the same or similar results, especially in research", "example": "It is one of the most replicated findings in group psychology."},
            "accountability": {"word": "accountability", "ipa": "/əˌkaʊn.təˈbɪl.ə.ti/", "meaning": "being responsible and answerable for one's own actions or results", "example": "Smaller teams can increase individual accountability."},
            "underscoring": {"word": "underscoring", "ipa": "/ˌʌn.dəˈskɔːr.ɪŋ/", "meaning": "emphasising or drawing attention to something", "example": "The consistency across cultures is underscoring how real the effect is."},
            "ingrained": {"word": "ingrained", "ipa": "/ɪnˈɡreɪnd/", "meaning": "firmly fixed or established, deeply rooted", "example": "The pattern seems deeply ingrained across species."},
            "In light of": {"word": "in light of", "ipa": "/ɪn laɪt ɒv/", "meaning": "considering, given a particular piece of information", "example": "In light of this evidence, some companies changed their structure."},
        },
        "gram_explanations": {
            "g1": "Narrative past simple — \"conducted\" (REVIEW): a single completed action at a specific point in the past.",
            "g2": "Past perfect — \"had no idea\" (REVIEW): a state that existed before the rest of the story unfolds.",
            "g3": "\"Whereas\" (NEW connector) — a direct, parallel contrast between individual and group effort.",
            "g4": "Passive voice — \"was found\" (REVIEW): the researchers are unimportant here, focus is on the result.",
            "g5": "Inverted third conditional, no \"if\" (REVIEW) — \"Had each participant been pulling alone\" = \"If each participant had been pulling alone\".",
            "g6": "\"Notwithstanding\" + noun phrase (NEW connector) — formal \"despite\".",
            "g7": "\"Rarely does\" (REVIEW, Lesson 18) — negative inversion: fronted frequency adverb triggering \"does\"-inversion.",
            "g8": "\"Having + past participle\" (REVIEW, Lesson 15) — the studying was completed before the description that follows.",
            "g9": "\"Insofar as\" (NEW connector) — limits the claim about larger teams to the extent it is actually true.",
            "g10": "\"Nonetheless\" (NEW connector) — formal \"however\", introducing a contrast with the previous statement.",
            "g11": "Past participle clause (REVIEW, Lesson 15) — \"trained to notice the pattern\" modifying \"manager\", passive meaning.",
            "g12": "Past participle clause (REVIEW, Lesson 15) — \"left unaware\" modifying \"one\", passive meaning, contrasting with g11."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "If responsibility is \"diffused\" across a group, it is…", "options": [{"label": "spread out, no longer concentrated in one place", "value": "right", "correct": True}, {"label": "concentrated entirely in one person", "value": "wrong", "correct": False}, {"label": "completely removed from the task", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Coasting\" means…", "options": [{"label": "making less effort than one is capable of", "value": "right", "correct": True}, {"label": "working at maximum possible effort", "value": "wrong", "correct": False}, {"label": "quitting a job suddenly", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"replicated\" finding is one that has been…", "options": [{"label": "repeated with similar results in further research", "value": "right", "correct": True}, {"label": "proven false by later studies", "value": "wrong", "correct": False}, {"label": "recorded only once, never repeated", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Accountability\" refers to…", "options": [{"label": "being responsible and answerable for one's actions", "value": "right", "correct": True}, {"label": "being completely free of any responsibility", "value": "wrong", "correct": False}, {"label": "a type of financial bonus", "value": "wrong2", "correct": False}]},
            {"prompt": "If a pattern is \"ingrained\", it is…", "options": [{"label": "deeply rooted and firmly established", "value": "right", "correct": True}, {"label": "brand new and not yet noticed", "value": "wrong", "correct": False}, {"label": "easily and instantly removed", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "Each contribution felt less", "after": "in a bigger group.", "answers": ["consequential"], "width": 110},
            {"before": "The consistency across cultures is", "after": "how real the effect is.", "answers": ["underscoring"], "width": 130},
            {"before": "Responsibility becomes", "after": "once a group grows large enough.", "answers": ["diffused"], "width": 100},
            {"before": "It is one of the most", "after": "findings in group psychology.", "answers": ["replicated"], "width": 110},
        ],
    },
    "practice": {
        "gapfill_focus": "formal connectors, plus a mix of structures from across the whole course.",
        "gapfill": [
            {"before": "The results were disappointing;", "after": "(nonetheless), the team pressed on.", "answers": ["nonetheless"]},
            {"before": "", "after": "(notwithstanding/the risks), the board approved the investment.", "answers": ["Notwithstanding the risks"]},
            {"before": "Marketing prioritised speed,", "after": "(whereas) engineering prioritised stability.", "answers": ["whereas"]},
            {"before": "By the time the audit began, the accountant", "after": "(already/review) every file. (review: past perfect)", "answers": ["had already reviewed"]},
            {"before": "", "after": "(if/the loan/not/secure), the venture would have collapsed. (review: third conditional)", "answers": ["Had the loan not been secured", "If the loan had not been secured"]},
            {"before": "", "after": "(having/finish) the restructuring, the company finally returned to profit. (review: participle clause)", "answers": ["Having finished"]},
        ],
        "second": {
            "type": "categorise", "title": "New connector, or a structure from earlier in the course?",
            "instruction": "Tap which category each sentence belongs to.",
            "categories": ["New: formal discourse connector", "Review: earlier course structure"],
            "items": [
                {"prompt": "\"Notwithstanding the delays, the project finished on time.\"", "correct": "New: formal discourse connector"},
                {"prompt": "\"Having reviewed the figures twice, she approved the budget.\"", "correct": "Review: earlier course structure"},
                {"prompt": "\"The London office handles sales, whereas Berlin handles support.\"", "correct": "New: formal discourse connector"},
                {"prompt": "\"Rarely does a single decision explain a decade of survival.\"", "correct": "Review: earlier course structure"},
            ],
        },
        "builders": [
            {"words": ["Notwithstanding", "the", "setbacks,", "the", "launch", "proceeded", "as", "planned."]},
            {"words": ["The", "old", "system", "was", "manual,", "whereas", "the", "new", "one", "is", "automated."]},
            {"words": ["In", "light", "of", "the", "feedback,", "the", "policy", "was", "revised."]},
        ],
    },
    "speaking": {
        "solo_text": "Give a short 'retrospective' about a project, job or course you've completed, using at least two formal connectors (nonetheless, notwithstanding, whereas, in light of, insofar as) and at least two earlier structures from this course (a conditional, a passive, a participle clause, or an inversion).",
        "group_questions": [
            "Describe something that went badly at first, but that you nonetheless kept working on. What changed?",
            "Compare two approaches, teams or periods of time using 'whereas' to highlight the contrast.",
            "In light of everything you've learned in this course, what's one grammar structure you now use more confidently than before?",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing why their largest team seems to be their least productive per person.",
        "dialogue": [
            {"speaker": "Anna", "line": "Having read about the Ringelmann effect, I finally understand why our biggest team is also our least productive per person."},
            {"speaker": "Tomasz", "line": "Right, whereas the four-person squad clearly pulls its weight, the twelve-person one seems to coast."},
            {"speaker": "Anna", "line": "Notwithstanding all the extra headcount, output barely changed this quarter."},
            {"speaker": "Tomasz", "line": "Rarely does anyone admit they're coasting, though — it happens without anyone deciding it."},
            {"speaker": "Anna", "line": "In light of this, maybe we should split the big team into smaller ones."},
            {"speaker": "Tomasz", "line": "Insofar as the work actually needs that many people, sure — but a lot of it probably doesn't."},
            {"speaker": "Anna", "line": "The effect is over a century old, and nonetheless it still applies to us today."},
            {"speaker": "Tomasz", "line": "Some things never change, apparently."},
        ],
        "comprehension": [
            {"prompt": "What does Tomasz notice about the twelve-person team compared to the four-person squad?", "options": [{"label": "The larger team seems to coast rather than pull its weight.", "value": "right", "correct": True}, {"label": "The larger team is far more productive overall.", "value": "wrong", "correct": False}]},
            {"prompt": "According to Tomasz, how does coasting typically happen?", "options": [{"label": "Without anyone consciously deciding to do it.", "value": "right", "correct": True}, {"label": "Only after a formal team announcement.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Anna suggest doing in light of the discussion?", "options": [{"label": "Splitting the big team into smaller ones.", "value": "right", "correct": True}, {"label": "Doubling the size of every team immediately.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "Sales were disappointing; ___, the team stayed motivated.", "options": [{"label": "nonetheless", "value": "right", "correct": True}, {"label": "therefore", "value": "wrong", "correct": False}]},
        {"prompt": "___ the setbacks, the project finished on schedule.", "options": [{"label": "Notwithstanding", "value": "right", "correct": True}, {"label": "Because of", "value": "wrong", "correct": False}]},
        {"prompt": "The old office was small, ___ the new one is huge.", "options": [{"label": "whereas", "value": "right", "correct": True}, {"label": "so that", "value": "wrong", "correct": False}]},
        {"prompt": "___ the new complaints, the policy will be revised. (review-adjacent, new connector)", "options": [{"label": "In light of", "value": "right", "correct": True}, {"label": "In case of", "value": "wrong", "correct": False}]},
        {"prompt": "___ the figures twice, she still made an error. (review: participle clause)", "options": [{"label": "Having reviewed", "value": "right", "correct": True}, {"label": "Have reviewed", "value": "wrong", "correct": False}]},
    ],
})
