# -*- coding: utf-8 -*-
"""Test content for the four end-of-section tests (b2c1-test-01..04).

Each test dict follows the schema in gen_test_template.py:
  {id, num, title, subtitle, part1: {heading, intro, items}, part2: {heading, intro, items} | None}
"""

TESTS = []

# ============================================================
# TEST 1 — Section 1 only (Lessons 1-6), no Part 2
# ============================================================
TESTS.append({
    "id": "b2c1-test-01",
    "num": 1,
    "title": "Test 1: Aspect & Modality, Refined",
    "subtitle": "Covers Lessons 1-6: narrative tenses through deduction with continuous aspect.",
    "part1": {
        "heading": "Part 1 — Aspect & Modality, Refined",
        "intro": "Review narrative tenses, used to vs would, future in the past, academic hedging, needn't have vs didn't need to, and deduction with continuous aspect.",
        "items": [
            # Lesson 1 - narrative tenses (4)
            {"type": "mcq", "prompt": "While the auditor ___ the accounts, the fire alarm went off.",
             "options": [{"label": "was checking", "value": "right", "correct": True}, {"label": "checked", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "By the time the client called back, the team ___ the whole proposal.",
             "options": [{"label": "had rewritten", "value": "right", "correct": True}, {"label": "wrote", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "He opened his laptop, checked his inbox, then", "after": "(call) his manager.", "answers": ["called"], "width": 100},
            {"type": "gapfill", "before": "She realised she", "after": "(forget) to attach the file to the email.", "answers": ["had forgotten"], "width": 130},
            # Lesson 2 - used to vs would (4)
            {"type": "mcq", "prompt": "My first boss ___ a huge office overlooking the river. (a past state)",
             "options": [{"label": "used to have", "value": "right", "correct": True}, {"label": "would have", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "Every Friday, the whole team ___ lunch together downstairs.",
             "options": [{"label": "would order", "value": "right", "correct": True}, {"label": "are ordering", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "I", "after": "(believe) the rumours completely when I first started. (a past state)", "answers": ["used to believe"], "width": 130},
            {"type": "gapfill", "before": "She", "after": "(own) a small consultancy before she joined us. (a past state)", "answers": ["used to own"], "width": 120},
            # Lesson 3 - future in the past + future perfect continuous (4)
            {"type": "mcq", "prompt": "We ___ announce the merger in June, but the deal collapsed at the last minute.",
             "options": [{"label": "were going to", "value": "right", "correct": True}, {"label": "will", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "By next April, she ___ this branch for exactly a decade.",
             "options": [{"label": "will have been managing", "value": "right", "correct": True}, {"label": "will manage", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "He told the client the shipment", "after": "(arrive) by Friday, but it never did.", "answers": ["would arrive"], "width": 120},
            {"type": "gapfill", "before": "By the time the guests arrive, we", "after": "(cook) for nearly six hours.", "answers": ["will have been cooking"], "width": 160},
            # Lesson 4 - academic hedging (4)
            {"type": "mcq", "prompt": "The latest figures ___ support the team's original forecast.",
             "options": [{"label": "appear to", "value": "right", "correct": True}, {"label": "are appearing to", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "Junior staff ___ raise concerns informally rather than through official channels, though not always.",
             "options": [{"label": "tend to", "value": "right", "correct": True}, {"label": "are tending to", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "Given current demand, prices", "after": "(likely/rise) again before the quarter ends.", "answers": ["are likely to rise"], "width": 150},
            {"type": "gapfill", "before": "The candidate", "after": "(seem/misunderstand) the scope of the role during the interview.", "answers": ["seems to have misunderstood"], "width": 190},
            # Lesson 5 - needn't have vs didn't need to (4)
            {"type": "mcq", "prompt": "She ___ printed the whole contract — the client only wanted the summary page.",
             "options": [{"label": "needn't have", "value": "right", "correct": True}, {"label": "didn't need to", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "We ___ book a translator — every delegate spoke fluent English.",
             "options": [{"label": "didn't need to", "value": "right", "correct": True}, {"label": "needn't have", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "He", "after": "(needn't/rewrite) the whole report — one paragraph needed changing.", "answers": ["needn't have rewritten"], "width": 190},
            {"type": "gapfill", "before": "They", "after": "(not need/renew) the licence yet — it still had six months left.", "answers": ["didn't need to renew"], "width": 190},
            # Lesson 6 - deduction with continuous aspect (4)
            {"type": "mcq", "prompt": "The desk is covered in paperwork — she ___ on the quarterly report all night.",
             "options": [{"label": "must have been working", "value": "right", "correct": True}, {"label": "must have worked", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "He can't ___ — the office phone never once rang while I was there.",
             "options": [{"label": "have been calling", "value": "right", "correct": True}, {"label": "been calling", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "They", "after": "(must/argue) — I could hear raised voices for a good ten minutes.", "answers": ["must have been arguing"], "width": 190},
            {"type": "gapfill", "before": "The invoice", "after": "(must/send) already — the deadline passed hours ago. (completed action)", "answers": ["must have been sent"], "width": 190},
        ],
    },
    "part2": None,
})

# ============================================================
# TEST 2 — Part 1: Section 2 only (Lessons 7-10); Part 2: cumulative 1+2
# ============================================================
TESTS.append({
    "id": "b2c1-test-02",
    "num": 2,
    "title": "Test 2: Sophisticated Conditionals",
    "subtitle": "Part 1 covers Lessons 7-10; Part 2 reviews Lessons 1-10 cumulatively.",
    "part1": {
        "heading": "Part 1 — Sophisticated Conditionals",
        "intro": "Review inversion in conditionals, conditional alternatives to if, hypothetical meaning without if, and advanced wish / if only.",
        "items": [
            # Lesson 7 - inversion (4)
            {"type": "mcq", "prompt": "___ we consulted legal sooner, the whole dispute could have been avoided.",
             "options": [{"label": "Had", "value": "right", "correct": True}, {"label": "Have", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "___ the board reject the proposal, we would need to present an alternative by Friday.",
             "options": [{"label": "Should", "value": "right", "correct": True}, {"label": "Would", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "", "after": "(If I were you), I'd escalate this straight to the director.", "answers": ["Were I you"], "width": 150},
            {"type": "gapfill", "before": "", "after": "(If you should need) any further documents, contact HR directly.", "answers": ["Should you need"], "width": 170},
            # Lesson 8 - conditional alternatives to if (4)
            {"type": "mcq", "prompt": "We won't extend the contract ___ the delivery times improve significantly.",
             "options": [{"label": "unless", "value": "right", "correct": True}, {"label": "provided that", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "The vendor accepted our terms, ___ we paid a deposit upfront.",
             "options": [{"label": "on condition that", "value": "right", "correct": True}, {"label": "unless", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "You can leave early today,", "after": "(as long as) you finish the handover notes first.", "answers": ["as long as"], "width": 140},
            {"type": "gapfill", "before": "", "after": "(Suppose) the funding falls through at the last minute — what's our backup plan?", "answers": ["Suppose"], "width": 100},
            # Lesson 9 - hypothetical without if (4)
            {"type": "mcq", "prompt": "Submit the form today; ___ you'll lose your place on the shortlist.",
             "options": [{"label": "otherwise", "value": "right", "correct": True}, {"label": "but for", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "___ her colleague's timely warning, she would have sent the invoice to the wrong client.",
             "options": [{"label": "But for", "value": "right", "correct": True}, {"label": "Otherwise", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "He approved the budget", "after": "(without/double-check) the figures first.", "answers": ["without double-checking"], "width": 190},
            {"type": "gapfill", "before": "Back up the files now;", "after": "(otherwise) we risk losing everything overnight.", "answers": ["otherwise"], "width": 100},
            # Lesson 10 - advanced wish / if only (4)
            {"type": "mcq", "prompt": "I wish I ___ the contract more carefully before signing it.",
             "options": [{"label": "had read", "value": "right", "correct": True}, {"label": "would read", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "I wish he ___ interrupting every single client call.",
             "options": [{"label": "would stop", "value": "right", "correct": True}, {"label": "stopped", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "If only we", "after": "(escalate) it sooner, we could have kept the client.", "answers": ["had escalated"], "width": 140},
            {"type": "gapfill", "before": "I wish I'd flagged the risk, because if I had, we", "after": "(not/lose) the account.", "answers": ["wouldn't have lost", "would not have lost"], "width": 190},
        ],
    },
    "part2": {
        "heading": "Part 2 — Cumulative Review: Sections 1 & 2",
        "intro": "A balanced mix across all ten lessons covered so far — aspect, modality and conditionals together.",
        "items": [
            {"type": "mcq", "prompt": "By the time she arrived at the office, the whole team ___ for over an hour.",
             "options": [{"label": "had already been meeting", "value": "right", "correct": True}, {"label": "already met", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "Every summer, the interns ___ a farewell party on their last day.",
             "options": [{"label": "would organise", "value": "right", "correct": True}, {"label": "are organising", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "We", "after": "(go) ahead with the launch in March, but the funding fell through.", "answers": ["were going to go"], "width": 190},
            {"type": "mcq", "prompt": "The new packaging ___ reduce shipping costs by roughly ten percent.",
             "options": [{"label": "appears to", "value": "right", "correct": True}, {"label": "is appearing to", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "She ___ cancelled the meeting — everyone had already read the memo.",
             "options": [{"label": "needn't have", "value": "right", "correct": True}, {"label": "didn't need to", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "He's out of breath — he", "after": "(must/run) to catch the train.", "answers": ["must have been running"], "width": 190},
            {"type": "mcq", "prompt": "___ the board approved the merger sooner, the deal wouldn't have collapsed.",
             "options": [{"label": "Had", "value": "right", "correct": True}, {"label": "Have", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "We'll approve the plan ___ the budget stays under control.",
             "options": [{"label": "provided that", "value": "right", "correct": True}, {"label": "unless", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "", "after": "(But for) the backup generator, the entire server room would have gone dark.", "answers": ["But for"], "width": 100},
            {"type": "mcq", "prompt": "I wish she ___ complaining about every small change to the schedule.",
             "options": [{"label": "would stop", "value": "right", "correct": True}, {"label": "stops", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "By the time we land, I", "after": "(wait) at the gate for over an hour.", "answers": ["will have been waiting"], "width": 190},
            {"type": "mcq", "prompt": "He ___ terrified of public speaking as a teenager. (a past state)",
             "options": [{"label": "used to be", "value": "right", "correct": True}, {"label": "would be", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "___ the deadline move again, please notify every department immediately.",
             "options": [{"label": "Should", "value": "right", "correct": True}, {"label": "Would", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "She signed the lease", "after": "(without/read) the small print at all.", "answers": ["without reading"], "width": 170},
            {"type": "mcq", "prompt": "If only he ___ us about the delay earlier, we could have rearranged the schedule.",
             "options": [{"label": "had told", "value": "right", "correct": True}, {"label": "told", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "They", "after": "(not need/book) early — plenty of seats were still free.", "answers": ["didn't need to book"], "width": 190},
        ],
    },
})

# ============================================================
# TEST 3 — Part 1: Section 3 only (Lessons 11-14); Part 2: cumulative 1+2+3
# ============================================================
TESTS.append({
    "id": "b2c1-test-03",
    "num": 3,
    "title": "Test 3: Advanced Passive & Noun Phrases",
    "subtitle": "Part 1 covers Lessons 11-14; Part 2 reviews Lessons 1-14 cumulatively.",
    "part1": {
        "heading": "Part 1 — Advanced Passive & Noun Phrases",
        "intro": "Review passive with combined aspects, impersonal & get-passive, nominalisation, and advanced articles & quantifiers.",
        "items": [
            # Lesson 11 - passive combined aspects (4)
            {"type": "mcq", "prompt": "The new servers ___ installed while the office is closed for the weekend.",
             "options": [{"label": "are being", "value": "right", "correct": True}, {"label": "have been", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "___ approved by finance, the proposal moved straight to the CEO's desk.",
             "options": [{"label": "Having been", "value": "right", "correct": True}, {"label": "Being", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "The invoices", "after": "(process) as we speak, so please be patient.", "answers": ["are being processed"], "width": 190},
            {"type": "gapfill", "before": "", "after": "(reject) once already, the proposal was rewritten from scratch. (Having...)", "answers": ["Having been rejected"], "width": 190},
            # Lesson 12 - impersonal & get-passive (4)
            {"type": "mcq", "prompt": "___ that the two firms will merge before the end of the year.",
             "options": [{"label": "It is rumoured", "value": "right", "correct": True}, {"label": "It rumours", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "She ___ promoted twice within the same calendar year.",
             "options": [{"label": "got", "value": "right", "correct": True}, {"label": "got to", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "The director", "after": "(believe/have) known about the plan for months. (impersonal passive)", "answers": ["is believed to have"], "width": 190},
            {"type": "gapfill", "before": "The whole department", "after": "(get/reorganise) after the merger.", "answers": ["got reorganised"], "width": 170},
            # Lesson 13 - nominalisation (4)
            {"type": "mcq", "prompt": "The noun form of \"decide\" used in formal reports is…",
             "options": [{"label": "decision", "value": "right", "correct": True}, {"label": "decidement", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "\"They implemented the plan quickly\" nominalised becomes: \"___ of the plan was swift.\"",
             "options": [{"label": "Implementation", "value": "right", "correct": True}, {"label": "Implement", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "The board reached a", "after": "(decide) by Friday afternoon.", "answers": ["decision"], "width": 110},
            {"type": "gapfill", "before": "There has been a real improvement in", "after": "(efficient) since the restructuring.", "answers": ["efficiency"], "width": 130},
            # Lesson 14 - advanced articles & quantifiers (4)
            {"type": "mcq", "prompt": "___ smartphone has completely changed how teams communicate at work.",
             "options": [{"label": "The", "value": "right", "correct": True}, {"label": "A the", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "There was ___ interest in the proposal, so it was quietly shelved. (a negative sense)",
             "options": [{"label": "little", "value": "right", "correct": True}, {"label": "a little", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "", "after": "(the majority/of) staff surveyed preferred hybrid work.", "answers": ["The majority of"], "width": 150},
            {"type": "gapfill", "before": "", "after": "(a number/of) clients raised the exact same concern during consultation.", "answers": ["A number of"], "width": 150},
        ],
    },
    "part2": {
        "heading": "Part 2 — Cumulative Review: Sections 1, 2 & 3",
        "intro": "A balanced mix across all fourteen lessons covered so far, spanning aspect, modality, conditionals, the passive and noun phrases.",
        "items": [
            {"type": "mcq", "prompt": "While the technician ___ the cable, the lights flickered twice.",
             "options": [{"label": "was replacing", "value": "right", "correct": True}, {"label": "replaced", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "Every winter, the office ___ a small charity fundraiser.",
             "options": [{"label": "would run", "value": "right", "correct": True}, {"label": "is running", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "By next spring, she", "after": "(run) her own business for five years.", "answers": ["will have been running"], "width": 190},
            {"type": "mcq", "prompt": "Remote workers ___ report higher job satisfaction, though not universally.",
             "options": [{"label": "tend to", "value": "right", "correct": True}, {"label": "are tending to", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "He ___ explained it twice — I understood the first time, but he did it anyway.",
             "options": [{"label": "needn't have", "value": "right", "correct": True}, {"label": "didn't need to", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "She's covered in paint — she", "after": "(must/paint) the fence all afternoon.", "answers": ["must have been painting"], "width": 190},
            {"type": "mcq", "prompt": "___ we tested it more thoroughly, the bug would never have shipped.",
             "options": [{"label": "Had", "value": "right", "correct": True}, {"label": "Have", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "The meeting goes ahead ___ someone cancels beforehand.",
             "options": [{"label": "unless", "value": "right", "correct": True}, {"label": "as long as", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "", "after": "(Without/check) the figures twice, she approved the invoice.", "answers": ["Without checking"], "width": 170},
            {"type": "mcq", "prompt": "I wish they ___ interrupting each other during every single meeting.",
             "options": [{"label": "would stop", "value": "right", "correct": True}, {"label": "stopped", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "The kitchen", "after": "(renovate) while the restaurant is closed this month.", "answers": ["is being renovated"], "width": 190},
            {"type": "mcq", "prompt": "___ tested twice already, the app was finally released.",
             "options": [{"label": "Having been", "value": "right", "correct": True}, {"label": "Being", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "___ that the merger will be announced sometime next week.",
             "options": [{"label": "It is understood", "value": "right", "correct": True}, {"label": "It understands", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "He", "after": "(get/fire) without any warning at all.", "answers": ["got fired"], "width": 150},
            {"type": "mcq", "prompt": "The noun form of \"significant\" used in formal writing is…",
             "options": [{"label": "significance", "value": "right", "correct": True}, {"label": "significantness", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "", "after": "(a/manager) should always listen before deciding. (generic \"a\")", "answers": ["A manager"], "width": 150},
            {"type": "mcq", "prompt": "___ candidates had every skill the role demanded, though a handful came close.",
             "options": [{"label": "Few", "value": "right", "correct": True}, {"label": "A few", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "I wish I'd backed up the file, because if I", "after": "(back up) it, I wouldn't have lost the data.", "answers": ["had backed up"], "width": 190},
            {"type": "mcq", "prompt": "We ___ apply for a visa — our stay was under ninety days.",
             "options": [{"label": "didn't need to", "value": "right", "correct": True}, {"label": "needn't have", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "The candidates", "after": "(interview) one after another all morning.", "answers": ["are being interviewed"], "width": 190},
        ],
    },
})

# ============================================================
# TEST 4 — Part 1: Section 4 only (Lessons 15-20); Part 2: ALL 20 lessons (final exam)
# ============================================================
TESTS.append({
    "id": "b2c1-test-04",
    "num": 4,
    "title": "Test 4: Discourse & Complex Sentences",
    "subtitle": "Part 1 covers Lessons 15-20; Part 2 is the course's final cumulative exam across all 20 lessons.",
    "part1": {
        "heading": "Part 1 — Discourse & Complex Sentences",
        "intro": "Review participle clauses, advanced relative clauses, ellipsis & substitution, negative inversion, fronting, and the formal connectors from the discourse capstone.",
        "items": [
            # Lesson 15 - participle clauses (4)
            {"type": "mcq", "prompt": "___ the report twice, she finally sent it to the client.",
             "options": [{"label": "Having checked", "value": "right", "correct": True}, {"label": "Having check", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "___ about the budget, the manager called an urgent meeting.",
             "options": [{"label": "Worried", "value": "right", "correct": True}, {"label": "Worrying", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "The memo,", "after": "(write) in a hurry, contained two glaring errors.", "answers": ["written"], "width": 130},
            {"type": "gapfill", "before": "The staff", "after": "(work) overtime were given an extra day of leave.", "answers": ["working"], "width": 120},
            # Lesson 16 - advanced relative clauses (4)
            {"type": "mcq", "prompt": "They introduced a system ___ complaints are logged automatically.",
             "options": [{"label": "whereby", "value": "right", "correct": True}, {"label": "whereupon", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "She was promoted early, ___ surprised nobody in the office.",
             "options": [{"label": "which", "value": "right", "correct": True}, {"label": "that", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "The colleague", "after": "(preposition + whom) I report is based in another city.", "answers": ["to whom"], "width": 110},
            {"type": "gapfill", "before": "He raised the issue,", "after": "(consequence) the meeting was extended by an hour.", "answers": ["whereupon"], "width": 130},
            # Lesson 17 - ellipsis & substitution (4)
            {"type": "mcq", "prompt": "\"Is the report ready?\" \"I think ___.\"",
             "options": [{"label": "so", "value": "right", "correct": True}, {"label": "it", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "He didn't finish on time, and ___ did she.",
             "options": [{"label": "neither", "value": "right", "correct": True}, {"label": "so", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "Please revise the plan", "after": "(=if it is needed).", "answers": ["if needed"], "width": 100},
            {"type": "gapfill", "before": "I don't like this design, I prefer the older", "after": ".", "answers": ["one"], "width": 70},
            # Lesson 18 - negative inversion (4)
            {"type": "mcq", "prompt": "Never ___ such a disorganised handover before.",
             "options": [{"label": "have I seen", "value": "right", "correct": True}, {"label": "I have seen", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "Not only ___ the target, but she also exceeded it comfortably.",
             "options": [{"label": "did she meet", "value": "right", "correct": True}, {"label": "she met", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "Under no circumstances", "after": "(share) this file with outside parties.", "answers": ["should you share"], "width": 190},
            {"type": "gapfill", "before": "Little", "after": "(know) how close the deal came to collapsing.", "answers": ["did they know", "did we know"], "width": 190},
            # Lesson 19 - fronting (4)
            {"type": "mcq", "prompt": "___ that tickets sold out within minutes of going on sale.",
             "options": [{"label": "Such was the demand", "value": "right", "correct": True}, {"label": "Demand was such", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "A recurring problem ___ staff turnover in the sales team.",
             "options": [{"label": "is", "value": "right", "correct": True}, {"label": "are", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "This proposal, the board", "after": "(reject) outright at the last meeting.", "answers": ["rejected"], "width": 130},
            {"type": "gapfill", "before": "", "after": "(so/severe/backlog) that new orders were suspended entirely.", "answers": ["So severe was the backlog"], "width": 200},
            # Lesson 20 - discourse capstone connectors (4)
            {"type": "mcq", "prompt": "Sales were disappointing; ___, the team stayed motivated.",
             "options": [{"label": "nonetheless", "value": "right", "correct": True}, {"label": "therefore", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "The old office was small, ___ the new one is huge.",
             "options": [{"label": "whereas", "value": "right", "correct": True}, {"label": "so that", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "", "after": "(notwithstanding/the setbacks), the launch proceeded exactly as planned.", "answers": ["Notwithstanding the setbacks"], "width": 220},
            {"type": "gapfill", "before": "", "after": "(in light/of) the new evidence, the policy will need to be reviewed.", "answers": ["In light of"], "width": 130},
        ],
    },
    "part2": {
        "heading": "Part 2 — Final Cumulative Review: All 20 Lessons",
        "intro": "The course's final exam: a balanced sweep across all four sections, from narrative tenses to formal discourse connectors.",
        "items": [
            # Section 1 (7 items)
            {"type": "mcq", "prompt": "By the time the investors arrived, the team ___ the entire presentation.",
             "options": [{"label": "had rehearsed", "value": "right", "correct": True}, {"label": "rehearsed", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "Every Friday, my old manager ___ the whole team for coffee.",
             "options": [{"label": "would treat", "value": "right", "correct": True}, {"label": "is treating", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "We", "after": "(launch) in March, but we pushed the date back twice.", "answers": ["were going to launch"], "width": 190},
            {"type": "mcq", "prompt": "The latest results ___ support the original hypothesis.",
             "options": [{"label": "appear to", "value": "right", "correct": True}, {"label": "are appearing to", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "She ___ rushed to the airport — her flight was delayed by three hours anyway.",
             "options": [{"label": "needn't have", "value": "right", "correct": True}, {"label": "didn't need to", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "The lights were on all night — someone", "after": "(must/work) late.", "answers": ["must have been working"], "width": 190},
            {"type": "mcq", "prompt": "By next June, he ___ this department for a full decade.",
             "options": [{"label": "will have been running", "value": "right", "correct": True}, {"label": "will run", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "I", "after": "(own) a small consultancy before I joined this company. (a past state)", "answers": ["used to own"], "width": 190},
            # Section 2 (5 items)
            {"type": "mcq", "prompt": "___ she known about the delay sooner, she would have changed her schedule.",
             "options": [{"label": "Had", "value": "right", "correct": True}, {"label": "Should", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "They extended the deadline, ___ we agreed to report weekly.",
             "options": [{"label": "on condition that", "value": "right", "correct": True}, {"label": "unless", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "Book the ticket now,", "after": "(otherwise) the price will rise sharply.", "answers": ["otherwise"], "width": 130},
            {"type": "mcq", "prompt": "I wish I'd asked for feedback, because if I ___, I'd have fixed it in time.",
             "options": [{"label": "had", "value": "right", "correct": True}, {"label": "did", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "", "after": "(But for) her quick thinking, the whole deal would have collapsed.", "answers": ["But for"], "width": 100},
            {"type": "mcq", "prompt": "The meeting goes ahead ___ someone cancels beforehand.",
             "options": [{"label": "unless", "value": "right", "correct": True}, {"label": "as long as", "value": "wrong", "correct": False}]},
            # Section 3 (5 items)
            {"type": "mcq", "prompt": "The applications ___ reviewed one by one this week.",
             "options": [{"label": "are being", "value": "right", "correct": True}, {"label": "have been", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "The manager ___ have known about the leak beforehand.",
             "options": [{"label": "is thought to", "value": "right", "correct": True}, {"label": "is thinking to", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "", "after": "(implement) of the new policy begins next month. (Capitalised noun)", "answers": ["Implementation"], "width": 190},
            {"type": "mcq", "prompt": "___ of employees surveyed said they preferred remote work.",
             "options": [{"label": "The majority", "value": "right", "correct": True}, {"label": "The majorities", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "There was", "after": "(little) support for the proposal, so it was abandoned. (negative)", "answers": ["little"], "width": 100},
            {"type": "mcq", "prompt": "The kitchen ___ renovated while the restaurant is closed this month.",
             "options": [{"label": "is being", "value": "right", "correct": True}, {"label": "is", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "The board reached a", "after": "(decide) on the restructuring by Friday afternoon.", "answers": ["decision"], "width": 190},
            # Section 4 (8 items)
            {"type": "mcq", "prompt": "___ the report twice, she still made an error.",
             "options": [{"label": "Having reviewed", "value": "right", "correct": True}, {"label": "Have reviewed", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "The topic ___ they disagreed most was never actually resolved.",
             "options": [{"label": "on which", "value": "right", "correct": True}, {"label": "which on", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "\"Will they extend the deadline?\" \"I hope", "after": ".\"", "answers": ["so"], "width": 70},
            {"type": "mcq", "prompt": "Rarely ___ the team this united on a single decision.",
             "options": [{"label": "is", "value": "right", "correct": True}, {"label": "was", "value": "wrong", "correct": False}]},
            {"type": "mcq", "prompt": "Far more concerning ___ the recent drop in morale.",
             "options": [{"label": "is", "value": "right", "correct": True}, {"label": "does", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "", "after": "(such/pressure) that two managers resigned that same week.", "answers": ["Such was the pressure"], "width": 190},
            {"type": "mcq", "prompt": "___ the new complaints, the policy will need to be revised.",
             "options": [{"label": "In light of", "value": "right", "correct": True}, {"label": "In case of", "value": "wrong", "correct": False}]},
            {"type": "gapfill", "before": "The old system was manual,", "after": "(whereas) the new one is fully automated.", "answers": ["whereas"], "width": 110},
        ],
    },
})
