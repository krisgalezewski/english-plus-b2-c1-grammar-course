# -*- coding: utf-8 -*-
"""Section 2 — Sophisticated Conditionals (Lessons 7-10)."""
from gen_lesson_template import vocab, gram

SECTION_NAME = "Sophisticated Conditionals"
THEME = "theme-conditionals"

LESSONS = []

# ============================================================
# LESSON 7 — Inversion in Conditionals
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-07-inversion-conditionals",
    "num": 7, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Inversion in Conditionals",
    "subtitle": "Were I to..., Had I known..., Should you need... — dropping \"if\" for a more formal register.",
    "warmup_intro": "In formal writing and speech — reports, contracts, presentations — English often drops \"if\" entirely and inverts the subject and auxiliary instead. The meaning stays identical; only the register changes.",
    "warmup": [
        {"prompt": "\"Had I known about the delay, I would have rescheduled\" means the same as…",
         "options": [{"label": "\"If I had known about the delay, I would have rescheduled.\"", "value": "right", "correct": True},
                     {"label": "\"I know about the delay, so I will reschedule.\"", "value": "wrong", "correct": False}]},
        {"prompt": "\"Should you require further details, please contact HR\" is a formal way of saying…",
         "options": [{"label": "\"If you require further details, please contact HR.\"", "value": "right", "correct": True},
                     {"label": "\"You definitely require further details, so contact HR.\"", "value": "wrong", "correct": False}]},
        {"prompt": "\"Were she to accept the offer, the whole team would restructure\" describes…",
         "options": [{"label": "a hypothetical future possibility, not a certainty", "value": "right", "correct": True},
                     {"label": "something that has already happened", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "Inversion simply swaps \"if + subject\" for \"auxiliary + subject\" — Were I, Had I, Should you — and drops \"if\" completely. Nothing else in the sentence changes.",
    "diagnostic": [
        {"prompt": "___ the client sooner, we could have avoided the misunderstanding.", "options": [{"label": "Had we contacted", "value": "right", "correct": True}, {"label": "We had contacted", "value": "wrong", "correct": False}]},
        {"prompt": "___ you need anything during the audit, my door is always open.", "options": [{"label": "Should", "value": "right", "correct": True}, {"label": "Would", "value": "wrong", "correct": False}]},
        {"prompt": "___ I in your position, I'd renegotiate the whole contract.", "options": [{"label": "Were", "value": "right", "correct": True}, {"label": "Was", "value": "wrong", "correct": False}]},
        {"prompt": "___ the merger fall through, shareholders would need immediate reassurance.", "options": [{"label": "Should", "value": "right", "correct": True}, {"label": "If will", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Three inversion patterns, one purpose: sounding formal",
        "intro": "Formal or literary English can invert the subject and auxiliary of a conditional clause instead of using \"if\". Each pattern maps onto one of the three main conditional types.",
        "tabs": [{"key": "were", "label": "Were I to..."}, {"key": "had", "label": "Had I known..."}, {"key": "should", "label": "Should you..."}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "were": [
                {"label": "second conditional, replacing \"if I were\" or \"if I did\"", "example": "Were the board to reject the proposal, we'd need a backup plan."},
                {"label": "a hypothetical future scenario, formal tone", "example": "Were she to relocate, the entire office structure would shift."},
            ],
            "had": [
                {"label": "third conditional, replacing \"if I had\"", "example": "Had I reviewed the contract more carefully, I'd have spotted the clause."},
                {"label": "a past hypothetical, often regretful", "example": "Had the team tested earlier, the bug would never have reached production."},
            ],
            "should": [
                {"label": "first conditional, replacing \"if you should\" — a less-likely-but-possible future", "example": "Should the numbers change, please notify accounting immediately."},
                {"label": "polite, formal instructions in emails or contracts", "example": "Should you require an extension, submit the request in writing."},
            ],
        },
        "quiz_labels": {"were": "Were I to... (2nd cond.)", "had": "Had I known... (3rd cond.)", "should": "Should you... (1st cond.)"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Were + subject + (to) + base verb — inverted 2nd conditional: "Were I to resign, the project would stall."</div>
          <div class="formula" style="border-left-color:var(--c-modal)">✅ Had + subject + past participle — inverted 3rd conditional: "Had she called first, we would have prepared better."</div>
          <div class="formula" style="border-left-color:var(--c-future);margin-bottom:20px">✅ Should + subject + base verb — inverted 1st conditional: "Should the client object, escalate to the manager."</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> inversion only replaces the \"if\"-clause — never the main clause, and never with negatives contracted.<br><br>
            ❌ "Weren't I to attend..." — negative inversion needs the full form, never a contraction: <b>"Were I not to attend..."</b><br>
            ✅ "Had I not seen the email, I would have missed the deadline." — full "not", never "hadn't" in the inverted clause.<br><br>
            Also remember: this is a register choice, not a meaning change. "Had we known" and "If we had known" describe exactly the same hypothetical — inversion just sounds more formal, precise, and report-like.</span>
          </div>'''
    },
    "compare": {
        "title": "With \"if\" vs. inverted — same meaning, different register",
        "instruction": "Hover over each pair to see that the meaning never shifts, only the formality.",
        "items": [
            {"key": "c1", "label": "Standard, 2nd conditional", "text": "If the board rejected the proposal, we'd need a backup plan.",
             "explain": "Everyday spoken register — perfectly correct, just less formal."},
            {"key": "c2", "label": "Inverted, 2nd conditional", "text": "Were the board to reject the proposal, we'd need a backup plan.",
             "explain": "Identical meaning, but the inversion signals a more formal, written or boardroom register."},
            {"key": "c3", "label": "Standard, 3rd conditional", "text": "If we had tested earlier, the bug would never have reached production.",
             "explain": "A normal past hypothetical, conversational register."},
            {"key": "c4", "label": "Inverted, 3rd conditional", "text": "Had we tested earlier, the bug would never have reached production.",
             "explain": "Same regret, same logic — but the inverted opening reads as more polished, typical of incident reports."},
        ]
    },
    "reading": {
        "heading": "Why the Last Disaster Feels Like the Only Risk",
        "passage_paragraphs": [
            f'''{gram("g1","Had the team fully understood")} how easily a single {vocab("vivid","vivid")} example can distort judgement, they might have built structured probability checks into every planning meeting from the outset. When people estimate how risky an activity is, they rarely consult statistics; instead, they consult memory. This mental shortcut, known as the availability {vocab("heuristic","heuristic")}, ranks dangers not by their true frequency but by how easily {vocab("instances","instances")} of them come to mind.''',
            f'''A recent near-miss on the factory floor made safety risks feel far more {vocab("salient","salient")} than they statistically deserved to, and for weeks afterward spending on precautions rose {vocab("disproportionately","disproportionately")}, even though nothing about the underlying probability had changed. {gram("g2","Were managers to rely less")} on recent, dramatic cases and more on long-run data, budgets would almost certainly look different. Researchers studying judgement under uncertainty describe this as a form of {vocab("bias","bias")} that quietly substitutes ease of recall for actual likelihood.''',
            f'''The danger runs in both directions. {gram("g3","Should a rare but catastrophic risk materialise")} without ever having been discussed or imagined, teams routinely {vocab("underestimate","underestimate")} it, precisely because no memorable case exists to retrieve. {gram("g4","Had a single striking incident")} been reported in the trade press the previous year, that same risk would likely have been rated as far more urgent. "{gram("g5","Were we to audit")} our safety decisions honestly," one risk officer admitted, "we'd find that {vocab("anecdotal","anecdotal")} evidence has quietly outweighed the actual data more often than we'd like to admit." {gram("g6","Should any manager ever notice")} a decision leaning on a single dramatic story rather than a full data set, that is exactly the moment to pause and ask why.''',
        ],
        "comprehension": [
            {"prompt": "According to the passage, what actually determines how risky people judge an activity to be?", "options": [
                {"label": "How easily examples of that risk come to mind, not the true statistical frequency.", "value": "right", "correct": True},
                {"label": "A formal calculation the safety department runs every quarter.", "value": "wrong", "correct": False}]},
            {"prompt": "What happened to safety spending after the near-miss on the factory floor?", "options": [
                {"label": "It rose sharply, even though the underlying probability hadn't changed.", "value": "right", "correct": True},
                {"label": "It stayed exactly the same, since managers relied only on long-run data.", "value": "wrong", "correct": False}]},
            {"prompt": "Why do teams often fail to prepare for a rare but catastrophic risk?", "options": [
                {"label": "Because no memorable example of it exists for them to recall.", "value": "right", "correct": True},
                {"label": "Because insurance already covers every conceivable outcome.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "vivid": {"word": "vivid", "ipa": "/ˈvɪv.ɪd/", "meaning": "producing a strong, clear impression in the mind", "example": "A single vivid example can outweigh a mountain of statistics."},
            "heuristic": {"word": "heuristic", "ipa": "/hjʊˈrɪs.tɪk/", "meaning": "a mental shortcut used to make quick judgements", "example": "The availability heuristic ranks risks by how memorable they are."},
            "instances": {"word": "instances", "ipa": "/ˈɪn.stən.sɪz/", "meaning": "individual examples or occurrences of something", "example": "People recall instances of a risk more easily if they were dramatic."},
            "salient": {"word": "salient", "ipa": "/ˈseɪ.li.ənt/", "meaning": "very noticeable or prominent", "example": "The near-miss made the risk feel unusually salient."},
            "disproportionately": {"word": "disproportionately", "ipa": "/ˌdɪs.prəˈpɔː.ʃən.ət.li/", "meaning": "to an extent that is too large or small relative to something else", "example": "Spending rose disproportionately after the incident."},
            "bias": {"word": "bias", "ipa": "/ˈbaɪ.əs/", "meaning": "a systematic tendency to judge things inaccurately", "example": "The bias substitutes ease of recall for actual likelihood."},
            "underestimate": {"word": "underestimate", "ipa": "/ˌʌn.dər.ˈes.tɪ.meɪt/", "meaning": "to judge something as smaller, less likely or less serious than it really is", "example": "Teams often underestimate risks with no memorable example behind them."},
            "anecdotal": {"word": "anecdotal", "ipa": "/ˌæn.ɪkˈdəʊ.təl/", "meaning": "based on individual stories rather than systematic evidence", "example": "Anecdotal evidence quietly outweighed the actual data."},
        },
        "gram_explanations": {
            "g1": "Inverted past hypothetical (\"Had the team fully understood...\") replacing \"If the team had fully understood...\" — a formal, report-like register for describing what didn't happen.",
            "g2": "Inverted second conditional (\"Were managers to rely less...\") replacing \"If managers relied less...\" — a present/future hypothetical about changed behaviour.",
            "g3": "Inverted first conditional (\"Should a rare but catastrophic risk materialise...\") replacing \"If a rare risk materialises...\" — a formal, less-certain future condition.",
            "g4": "Inverted third conditional (\"Had a single striking incident been reported...\") — a past hypothetical explaining how a different memory would have changed the rating.",
            "g5": "Inverted second conditional (\"Were we to audit...\") — a hypothetical scenario raised by the risk officer, formal spoken register.",
            "g6": "Inverted first conditional (\"Should any manager ever notice...\") — a formal way of covering a possible future situation, suited to a closing warning."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "A cognitive \"heuristic\" is…", "options": [{"label": "a mental shortcut used to make quick judgements", "value": "right", "correct": True}, {"label": "a formal statistical model used by actuaries", "value": "wrong", "correct": False}, {"label": "a written safety regulation", "value": "wrong2", "correct": False}]},
            {"prompt": "If a risk feels unusually \"salient\", it feels…", "options": [{"label": "very noticeable or prominent", "value": "right", "correct": True}, {"label": "completely forgettable", "value": "wrong", "correct": False}, {"label": "statistically negligible", "value": "wrong2", "correct": False}]},
            {"prompt": "If spending rose \"disproportionately\", it rose…", "options": [{"label": "by an amount too large relative to the actual change in risk", "value": "right", "correct": True}, {"label": "by exactly the amount the risk had genuinely increased", "value": "wrong", "correct": False}, {"label": "not at all, despite expectations", "value": "wrong2", "correct": False}]},
            {"prompt": "\"Anecdotal\" evidence is based on…", "options": [{"label": "individual stories rather than systematic data", "value": "right", "correct": True}, {"label": "a large, carefully controlled study", "value": "wrong", "correct": False}, {"label": "government statistics collected over decades", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"underestimate\" a risk means to…", "options": [{"label": "judge it as less serious than it really is", "value": "right", "correct": True}, {"label": "calculate its exact probability correctly", "value": "wrong", "correct": False}, {"label": "exaggerate how dangerous it is", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "A single", "after": "example can outweigh a mountain of statistics.", "answers": ["vivid"], "width": 100},
            {"before": "People recall", "after": "of a risk more easily if they were dramatic.", "answers": ["instances"], "width": 100},
            {"before": "The near-miss made the risk feel unusually", "after": ".", "answers": ["salient"], "width": 100},
            {"before": "Without any dramatic story to recall, teams often", "after": "the danger.", "answers": ["underestimate"], "width": 130},
        ],
    },
    "practice": {
        "gapfill_focus": "rewrite the if-clause using inversion (Were / Had / Should).",
        "gapfill": [
            {"before": "", "after": "(If I were you) I'd escalate this to the director right away.", "answers": ["Were I you"]},
            {"before": "", "after": "(If we had known) about the outage sooner, we would have alerted customers.", "answers": ["Had we known"]},
            {"before": "", "after": "(If you should need) anything else, my office is just down the hall.", "answers": ["Should you need"]},
            {"before": "", "after": "(If she were to accept) the transfer, the whole team would need restructuring.", "answers": ["Were she to accept"]},
            {"before": "", "after": "(If he had reviewed) the figures earlier, he would have spotted the error.", "answers": ["Had he reviewed"]},
            {"before": "", "after": "(If the deadline should move) again, please inform every department.", "answers": ["Should the deadline move"]},
        ],
        "second": {
            "type": "errorspot", "title": "Spot the mistake",
            "instruction": "One word in each inverted conditional is wrong. Tap it, then check the correction.",
            "items": [
                {"words": ["Weren't", "I", "in", "your", "position,", "I'd", "accept", "the", "offer", "immediately."], "error_indices": [0], "correction": "\"Weren't\" → \"Were\" (inversion never contracts the negative; it would need \"Were I not in...\")"},
                {"words": ["Had", "she", "have", "known", "about", "the", "delay,", "she", "would", "have", "left", "earlier."], "error_indices": [2], "correction": "\"have\" → delete it (it is simply \"Had she known\", not \"Had she have known\")"},
                {"words": ["Should", "the", "client", "objects,", "escalate", "the", "issue", "to", "the", "manager."], "error_indices": [3], "correction": "\"objects\" → \"object\" (Should + subject + base verb, not the -s form)"},
            ],
        },
        "builders": [
            {"words": ["Had", "we", "contacted", "the", "client", "sooner,", "this", "wouldn't", "have", "happened."]},
            {"words": ["Should", "you", "require", "further", "details,", "please", "contact", "HR."]},
            {"words": ["Were", "I", "in", "your", "position,", "I'd", "renegotiate", "the", "contract."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a workplace decision you'd make differently in hindsight, using at least one inverted conditional (\"Had I known...\", \"Were I to do it again...\").",
        "group_questions": [
            "Should your company ever face a major crisis, what's the first thing you think should happen?",
            "Were you to redesign your team's onboarding process from scratch, what would you change?",
            "Tell your group about a decision where, had you had more information at the time, the outcome would have been different.",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing a report about how the company's safety spending reacts to risk.",
        "dialogue": [
            {"speaker": "Anna", "line": "Did you see the new safety spending numbers? They jumped right after that near-miss on the factory floor, even though the actual risk hadn't changed."},
            {"speaker": "Tomasz", "line": "That's the availability heuristic in action. Had the finance team looked at the long-run data first, they probably wouldn't have reacted so strongly."},
            {"speaker": "Anna", "line": "Exactly. Were we to rely more on statistics and less on the last dramatic story, our budgets would look completely different."},
            {"speaker": "Tomasz", "line": "Should a bigger, quieter risk ever materialise without a memorable case behind it, I bet we'd underestimate it badly."},
            {"speaker": "Anna", "line": "That's basically what the risk officer admitted in the report — anecdotal evidence keeps outweighing the actual data."},
            {"speaker": "Tomasz", "line": "Had a single striking incident been reported in the trade press last year, this exact risk would probably be rated as urgent already."},
            {"speaker": "Anna", "line": "Should any manager ever notice a decision leaning on one vivid story instead of the full data set, that's the moment to pause."},
            {"speaker": "Tomasz", "line": "Agreed. Let's build a proper review into the process before the next budget cycle."},
        ],
        "comprehension": [
            {"prompt": "Why did safety spending jump after the near-miss, according to Anna?", "options": [{"label": "Because of a vivid recent case, not because the actual risk had changed.", "value": "right", "correct": True}, {"label": "Because a new safety regulation came into force.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Tomasz predict could happen to a quieter, bigger risk?", "options": [{"label": "It could be badly underestimated for lack of a memorable example.", "value": "right", "correct": True}, {"label": "It would automatically be flagged by the finance team.", "value": "wrong", "correct": False}]},
            {"prompt": "What do Anna and Tomasz agree to do before the next budget cycle?", "options": [{"label": "Build a proper review into the process.", "value": "right", "correct": True}, {"label": "Cancel all future safety spending.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "___ I in charge, I'd delay the launch by a week.", "options": [{"label": "Were", "value": "right", "correct": True}, {"label": "Was", "value": "wrong", "correct": False}]},
        {"prompt": "___ we tested more thoroughly, the bug would never have shipped.", "options": [{"label": "Had", "value": "right", "correct": True}, {"label": "Have", "value": "wrong", "correct": False}]},
        {"prompt": "___ you need anything else, don't hesitate to call.", "options": [{"label": "Should", "value": "right", "correct": True}, {"label": "Would", "value": "wrong", "correct": False}]},
        {"prompt": "___ the board to reject it, we'd need a new proposal by Friday.", "options": [{"label": "Were", "value": "right", "correct": True}, {"label": "Should", "value": "wrong", "correct": False}]},
        {"prompt": "___ she known earlier, she would have changed her schedule.", "options": [{"label": "Had", "value": "right", "correct": True}, {"label": "Should", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 8 — Conditional Alternatives to If
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-08-conditional-alternatives",
    "num": 8, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Conditional Alternatives to If",
    "subtitle": "Provided that, as long as, unless, suppose, on condition that — precision beyond a plain \"if\".",
    "warmup_intro": "\"If\" is neutral and general. Other conditional linkers add nuance — a stricter requirement, an exception, a negotiated term. Recognising them is essential for contracts, negotiations and formal proposals.",
    "warmup": [
        {"prompt": "\"We'll sign the deal, provided that the price stays fixed\" adds a…",
         "options": [{"label": "strict requirement that must be met", "value": "right", "correct": True}, {"label": "vague possibility with no real condition", "value": "wrong", "correct": False}]},
        {"prompt": "\"Unless you object, we'll proceed as planned\" means we'll proceed…",
         "options": [{"label": "if you do NOT object", "value": "right", "correct": True}, {"label": "only if you DO object", "value": "wrong", "correct": False}]},
        {"prompt": "\"Suppose the client rejects the offer — what's our next move?\" is used to…",
         "options": [{"label": "introduce a hypothetical scenario for discussion", "value": "right", "correct": True}, {"label": "state a fact that has already happened", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "\"Unless\" secretly means \"if...not\" — it's the one that trips people up most, because the negative is built into the word itself.",
    "diagnostic": [
        {"prompt": "You can take the afternoon off, ___ you finish the report first.", "options": [{"label": "as long as", "value": "right", "correct": True}, {"label": "unless", "value": "wrong", "correct": False}]},
        {"prompt": "We won't renew the contract ___ the terms improve.", "options": [{"label": "unless", "value": "right", "correct": True}, {"label": "provided that", "value": "wrong", "correct": False}]},
        {"prompt": "The vendor agreed to the deadline, ___ we paid a deposit upfront.", "options": [{"label": "on condition that", "value": "right", "correct": True}, {"label": "unless", "value": "wrong", "correct": False}]},
        {"prompt": "___ the client calls before Friday, what should I tell them?", "options": [{"label": "Suppose", "value": "right", "correct": True}, {"label": "Unless", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Five ways to say \"if\", each with its own flavour",
        "intro": "These linkers all introduce a condition, but they aren't interchangeable — each carries a slightly different shade of meaning, from strict requirement to pure hypothesis.",
        "tabs": [{"key": "provided", "label": "Provided that / As long as"}, {"key": "unless", "label": "Unless"}, {"key": "suppose", "label": "Suppose / On condition"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "provided": [
                {"label": "a strict requirement, near-synonym of \"if and only if\"", "example": "You'll get the bonus, provided that targets are met."},
                {"label": "a firm condition, slightly less formal", "example": "As long as the numbers add up, the board will approve it."},
            ],
            "unless": [
                {"label": "\"if...not\" — the negative built in", "example": "We won't ship unless the tests pass."},
                {"label": "an exception to an otherwise fixed plan", "example": "The meeting goes ahead unless someone cancels."},
            ],
            "suppose": [
                {"label": "introducing a pure hypothetical for discussion", "example": "Suppose the merger falls through — then what?"},
                {"label": "on condition that: a formal, negotiated term", "example": "They'll extend the deadline, on condition that we report weekly."},
            ],
        },
        "quiz_labels": {"provided": "Provided that / As long as", "unless": "Unless", "suppose": "Suppose / On condition that"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Provided (that) / As long as + clause — a strict, near-mandatory requirement.</div>
          <div class="formula" style="border-left-color:var(--c-modal)">✅ Unless + clause — equivalent to "if...not"; an exception to the main statement.</div>
          <div class="formula" style="border-left-color:var(--c-future);margin-bottom:20px">✅ Suppose / Supposing + clause — a hypothetical raised for discussion; On condition that + clause — a formal negotiated term.</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> never double the negative with "unless".<br><br>
            ❌ "Unless you don't finish, you can leave." — this accidentally means the opposite of what's intended.<br>
            ✅ "Unless you finish, you can't leave." — "unless" already carries the "not", so the clause after it should be positive.<br><br>
            Also, "provided that" and "as long as" both take a present tense even for future meaning, exactly like "if": "provided that it arrives on time" (not "will arrive").</span>
          </div>'''
    },
    "compare": {
        "title": "Same idea, different shade of meaning",
        "instruction": "Hover over each version to see the subtle difference each linker adds.",
        "items": [
            {"key": "c1", "label": "Neutral", "text": "If the client approves the budget, we'll start next week.",
             "explain": "Plain, neutral condition — no extra nuance."},
            {"key": "c2", "label": "Strict requirement", "text": "Provided that the client approves the budget, we'll start next week.",
             "explain": "Sounds like a firm, near-contractual requirement, not a loose possibility."},
            {"key": "c3", "label": "Exception framing", "text": "We'll start next week unless the client rejects the budget.",
             "explain": "Frames the default as \"yes, we're starting\" — the condition is the exception, not the rule."},
            {"key": "c4", "label": "Negotiated term", "text": "The client will approve it, on condition that we cut costs by 10%.",
             "explain": "Formal, contract-style phrasing — implies a term that was actually negotiated."},
        ]
    },
    "reading": {
        "heading": "Why Losing Feels Worse Than Winning Feels Good",
        "passage_paragraphs": [
            f'''People tend to weigh losses roughly twice as heavily as equivalent gains — a well-documented {vocab("asymmetry","asymmetry")} that psychologists call loss {vocab("aversion","aversion")}. This bias shapes decisions well beyond the laboratory. An employee will keep funding a mediocre project {gram("g1","provided that")} killing it means formally admitting a loss, yet the same employee would walk away from an equally-sized potential gain without a second thought.''',
            f'''The effect depends heavily on the {vocab("reference point","reference point")} a person starts from. A manager who has already mentally spent a bonus treats losing part of it as a real loss, not merely a smaller gain — and {gram("g2","as long as")} that framing holds, she will take startling risks simply to avoid confirming the loss. Teams often become {vocab("entrenched","entrenched")} in failing strategies for exactly this reason: cutting losses feels worse than it logically should, purely because of how the brain accounts for money already committed.''',
            f'''Sensible risk-taking is still possible, but usually only under certain conditions. Employees say they would try a genuinely risky idea {gram("g3","provided that")} the {vocab("downside","downside")} is {vocab("capped","capped")} in advance — {gram("g4","unless")} the cap is missing entirely, in which case almost nobody volunteers. "{gram("g5","Suppose")} we removed the {vocab("safeguard","safeguard")} of a spending ceiling altogether," one operations director asked her team; "would anyone still take the same risk?" Nobody said yes. The company now approves experimental projects only {gram("g6","on condition that")} a maximum loss {vocab("threshold","threshold")} is agreed before work begins.''',
        ],
        "comprehension": [
            {"prompt": "According to the passage, how does loss aversion make employees treat a mediocre project?", "options": [
                {"label": "They keep funding it, because cancelling it means formally admitting a loss.", "value": "right", "correct": True},
                {"label": "They cancel it immediately, regardless of how much has already been spent.", "value": "wrong", "correct": False}]},
            {"prompt": "Why does the manager in the passage take startling risks to protect her bonus?", "options": [
                {"label": "Because she has already mentally spent it, so losing part of it feels like a real loss.", "value": "right", "correct": True},
                {"label": "Because company policy requires her to take risks every quarter.", "value": "wrong", "correct": False}]},
            {"prompt": "Under what condition are employees willing to try a genuinely risky idea?", "options": [
                {"label": "Only if the potential downside is capped in advance.", "value": "right", "correct": True},
                {"label": "Only if a senior director personally guarantees success.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "asymmetry": {"word": "asymmetry", "ipa": "/eɪˈsɪm.ə.tri/", "meaning": "a lack of balance or equality between two things", "example": "There's a well-documented asymmetry between how losses and gains are felt."},
            "aversion": {"word": "aversion", "ipa": "/əˈvɜː.ʃən/", "meaning": "a strong dislike or reluctance towards something", "example": "Loss aversion makes people avoid losses more than they pursue equal gains."},
            "reference point": {"word": "reference point", "ipa": "/ˈref.ər.əns pɔɪnt/", "meaning": "the starting position someone judges gains and losses against", "example": "A bonus already spent mentally becomes the new reference point."},
            "entrenched": {"word": "entrenched", "ipa": "/ɪnˈtrentʃt/", "meaning": "firmly established and difficult to change", "example": "Teams often become entrenched in failing strategies."},
            "downside": {"word": "downside", "ipa": "/ˈdaʊn.saɪd/", "meaning": "the negative or unfavourable aspect of a situation", "example": "Employees will take a risk only if the downside is capped."},
            "capped": {"word": "capped", "ipa": "/kæpt/", "meaning": "limited to a fixed maximum amount", "example": "The potential loss was capped before the project began."},
            "safeguard": {"word": "safeguard", "ipa": "/ˈseɪf.gɑːd/", "meaning": "a measure taken to protect against harm or loss", "example": "Removing the safeguard of a spending ceiling changed everyone's answer."},
            "threshold": {"word": "threshold", "ipa": "/ˈθreʃ.həʊld/", "meaning": "a fixed limit that triggers a rule once crossed", "example": "Projects are approved only once a maximum loss threshold is agreed."},
        },
        "gram_explanations": {
            "g1": "\"Provided that\" — a strict requirement: the employee keeps funding the project only under this exact condition.",
            "g2": "\"As long as\" — a firm condition on the framing (already-spent bonus) continuing to hold.",
            "g3": "\"Provided that\" — repeats the strict-requirement structure, now attached to trying a risky idea.",
            "g4": "\"Unless\" — equivalent to \"if...not\": if the cap is not in place, nobody volunteers.",
            "g5": "\"Suppose\" — introduces a hypothetical scenario the director raises for discussion, not a stated fact.",
            "g6": "\"On condition that\" — a formal, negotiated term the company now attaches to approving any project."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "Loss \"aversion\" describes…", "options": [{"label": "a strong reluctance to experience a loss", "value": "right", "correct": True}, {"label": "an eagerness to take on any available risk", "value": "wrong", "correct": False}, {"label": "indifference between gains and losses", "value": "wrong2", "correct": False}]},
            {"prompt": "The \"asymmetry\" between gains and losses means…", "options": [{"label": "the two are not weighed equally by the mind", "value": "right", "correct": True}, {"label": "the two are always felt with exactly equal intensity", "value": "wrong", "correct": False}, {"label": "gains are never noticed at all", "value": "wrong2", "correct": False}]},
            {"prompt": "A strategy that has become \"entrenched\" is…", "options": [{"label": "firmly established and hard to change", "value": "right", "correct": True}, {"label": "brand new and untested", "value": "wrong", "correct": False}, {"label": "abandoned after one failure", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"safeguard\" is put in place to…", "options": [{"label": "protect against harm or loss", "value": "right", "correct": True}, {"label": "increase the size of a potential loss", "value": "wrong", "correct": False}, {"label": "speed up an approval process", "value": "wrong2", "correct": False}]},
            {"prompt": "If a potential loss is \"capped\", it is…", "options": [{"label": "limited to a fixed maximum", "value": "right", "correct": True}, {"label": "allowed to grow without any limit", "value": "wrong", "correct": False}, {"label": "impossible to measure in advance", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "Employees will only take the risk if the", "after": "is capped in advance.", "answers": ["downside"], "width": 100},
            {"before": "A bonus already spent mentally becomes the new", "after": ".", "answers": ["reference point"], "width": 130},
            {"before": "Projects are approved only once a loss", "after": "is agreed.", "answers": ["threshold"], "width": 100},
            {"before": "Removing the spending ceiling changed the whole team's sense of", "after": ".", "answers": ["aversion"], "width": 100},
        ],
    },
    "practice": {
        "gapfill_focus": "provided that / as long as / unless / suppose / on condition that",
        "gapfill": [
            {"before": "You can leave early today,", "after": "(as long as) you finish the report first.", "answers": ["as long as"]},
            {"before": "We won't approve the budget", "after": "(unless) the numbers are revised.", "answers": ["unless"]},
            {"before": "", "after": "(Suppose) the client cancels at the last minute — what's our backup plan?", "answers": ["Suppose"]},
            {"before": "The vendor accepted the deadline,", "after": "(on condition that) we paid a deposit.", "answers": ["on condition that"]},
            {"before": "", "after": "(Provided that) the figures are accurate, the board should approve this easily.", "answers": ["Provided that"]},
            {"before": "The deal falls through", "after": "(unless) both sides sign by Friday.", "answers": ["unless"]},
        ],
        "second": {
            "type": "categorise", "title": "Which shade of meaning?",
            "instruction": "Decide what each sentence is really doing: stating a strict requirement, framing an exception, or raising a pure hypothetical.",
            "categories": ["Strict requirement", "Exception to the default", "Pure hypothetical"],
            "items": [
                {"prompt": "\"We'll sign, provided that the price stays fixed.\"", "correct": "Strict requirement"},
                {"prompt": "\"The launch proceeds unless the tests fail.\"", "correct": "Exception to the default"},
                {"prompt": "\"Suppose the funding doesn't come through — what's plan B?\"", "correct": "Pure hypothetical"},
                {"prompt": "\"They'll renew the lease, on condition that rent stays the same.\"", "correct": "Strict requirement"},
            ],
        },
        "builders": [
            {"words": ["You", "can", "take", "the", "afternoon", "off,", "as", "long", "as", "you", "finish."]},
            {"words": ["We", "won't", "renew", "the", "contract", "unless", "the", "terms", "improve."]},
            {"words": ["Suppose", "the", "client", "rejects", "the", "offer", "—", "what", "next?"]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a real or imagined negotiation (a job offer, a lease, a deal) using at least two different conditional linkers from today's lesson — not just \"if\".",
        "group_questions": [
            "What's a condition you'd insist on before accepting a new job (\"I'd accept, provided that...\")?",
            "Suppose your company had to cut costs by 20% overnight — what would you protect first?",
            "Tell your group about a rule at work that only applies unless a specific exception occurs.",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing why the team keeps funding a struggling project.",
        "dialogue": [
            {"speaker": "Anna", "line": "I still don't get why we're funding this project, provided that everyone agrees it's underperforming."},
            {"speaker": "Tomasz", "line": "It's classic loss aversion. Cancelling it now means admitting a loss, and nobody wants to be the one who does that."},
            {"speaker": "Anna", "line": "As long as we keep treating the sunk cost as a reference point, we'll never make an objective call."},
            {"speaker": "Tomasz", "line": "Right, unless someone forces the comparison to a fresh alternative, we'll stay entrenched."},
            {"speaker": "Anna", "line": "Suppose we asked the team to imagine starting from zero today — would they still choose this project?"},
            {"speaker": "Tomasz", "line": "Almost certainly not. But they'd only agree to a genuinely risky new idea provided that the downside is capped first."},
            {"speaker": "Anna", "line": "That's fair, honestly. On condition that we set a proper loss threshold, I'd actually back a new proposal."},
            {"speaker": "Tomasz", "line": "Agreed. Let's build that safeguard in before we bring anything to the board."},
        ],
        "comprehension": [
            {"prompt": "Why, according to Tomasz, does nobody want to cancel the underperforming project?", "options": [{"label": "Because cancelling it means formally admitting a loss.", "value": "right", "correct": True}, {"label": "Because the contract legally prevents cancellation.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Anna suggest asking the team to imagine?", "options": [{"label": "Whether they'd still choose the project if starting from zero today.", "value": "right", "correct": True}, {"label": "Whether they'd prefer a longer deadline.", "value": "wrong", "correct": False}]},
            {"prompt": "Under what condition would the team agree to a genuinely risky new idea?", "options": [{"label": "Provided that the downside is capped in advance.", "value": "right", "correct": True}, {"label": "Provided that the board approves it unanimously first.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "We'll approve the plan ___ the budget stays under control.", "options": [{"label": "provided that", "value": "right", "correct": True}, {"label": "unless", "value": "wrong", "correct": False}]},
        {"prompt": "The meeting goes ahead ___ someone cancels beforehand.", "options": [{"label": "unless", "value": "right", "correct": True}, {"label": "as long as", "value": "wrong", "correct": False}]},
        {"prompt": "___ the merger collapses tomorrow — what would our next step be?", "options": [{"label": "Suppose", "value": "right", "correct": True}, {"label": "Unless", "value": "wrong", "correct": False}]},
        {"prompt": "They extended the deadline, ___ we report weekly.", "options": [{"label": "on condition that", "value": "right", "correct": True}, {"label": "unless", "value": "wrong", "correct": False}]},
        {"prompt": "You'll get full access ___ you complete the training first.", "options": [{"label": "as long as", "value": "right", "correct": True}, {"label": "unless", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 9 — Hypothetical Meaning Without If
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-09-hypothetical-without-if",
    "num": 9, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Hypothetical Meaning Without If",
    "subtitle": "Otherwise, but for, without + gerund — conditional logic hiding inside ordinary connectors.",
    "warmup_intro": "You don't always need \"if\" to express a condition. Words like \"otherwise\", \"but for\" and \"without + -ing\" quietly carry the same hypothetical logic, often more compactly.",
    "warmup": [
        {"prompt": "\"We left early; otherwise, we would have missed the flight\" means…",
         "options": [{"label": "if we hadn't left early, we would have missed it", "value": "right", "correct": True}, {"label": "we definitely missed the flight anyway", "value": "wrong", "correct": False}]},
        {"prompt": "\"But for her quick thinking, the deal would have collapsed\" means…",
         "options": [{"label": "if it hadn't been for her quick thinking, the deal would have collapsed", "value": "right", "correct": True}, {"label": "her quick thinking caused the deal to collapse", "value": "wrong", "correct": False}]},
        {"prompt": "\"Without checking the figures, he approved the budget\" implies…",
         "options": [{"label": "if he had checked the figures, he might not have approved it", "value": "right", "correct": True}, {"label": "he checked the figures very carefully first", "value": "wrong", "correct": False}]},
        ],
    "warmup_tip": "All three — otherwise, but for, without + -ing — smuggle a hidden \"if...not\" or \"if it hadn't been for\" into the sentence without ever using the word \"if\".",
    "diagnostic": [
        {"prompt": "Book your ticket now; ___ the price will go up tomorrow.", "options": [{"label": "otherwise", "value": "right", "correct": True}, {"label": "but for", "value": "wrong", "correct": False}]},
        {"prompt": "___ the investor's last-minute support, the startup would have folded.", "options": [{"label": "But for", "value": "right", "correct": True}, {"label": "Otherwise", "value": "wrong", "correct": False}]},
        {"prompt": "She signed the contract ___ reading the fine print.", "options": [{"label": "without", "value": "right", "correct": True}, {"label": "unless", "value": "wrong", "correct": False}]},
        {"prompt": "We backed up the files first; ___ we would have lost everything.", "options": [{"label": "otherwise", "value": "right", "correct": True}, {"label": "without", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "Hidden conditionals: otherwise, but for, without + gerund",
        "intro": "Each of these expresses a hypothetical outcome without ever saying \"if\". Learn to recognise the hidden condition inside each pattern.",
        "tabs": [{"key": "otherwise", "label": "Otherwise"}, {"key": "butfor", "label": "But for"}, {"key": "without", "label": "Without + -ing"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "otherwise": [
                {"label": "states a real action first, then the unreal alternative", "example": "We left on time; otherwise, we'd have missed the connection."},
                {"label": "a warning about a consequence if something doesn't change", "example": "Fix the leak today, otherwise it'll get much worse."},
            ],
            "butfor": [
                {"label": "\"if it hadn't been for\" — credits one factor for preventing disaster", "example": "But for the backup generator, the whole server room would have gone dark."},
                {"label": "a slightly formal, literary way to highlight a single decisive factor", "example": "But for her intervention, the negotiation would have collapsed."},
            ],
            "without": [
                {"label": "\"if...didn't/hadn't\" compressed into without + gerund", "example": "Without double-checking the numbers, he sent the invoice."},
                {"label": "implies a missing step that changed (or risked changing) the outcome", "example": "Without asking permission, she rescheduled the whole meeting."},
            ],
        },
        "quiz_labels": {"otherwise": "Otherwise", "butfor": "But for", "without": "Without + -ing"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ [Real action], otherwise + would/will + base verb — states what really happened, then what would/will happen if it hadn't/doesn't.</div>
          <div class="formula" style="border-left-color:var(--c-modal)">✅ But for + noun phrase, + would have + past participle — "if it hadn't been for X..."</div>
          <div class="formula" style="border-left-color:var(--c-future);margin-bottom:20px">✅ Without + verb-ing, + subject + verb — compresses "if...hadn't" into a single phrase.</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> "but for" is always followed by a noun phrase, never a full clause.<br><br>
            ❌ "But for she helped us, we'd have failed." — ungrammatical.<br>
            ✅ "But for her help, we'd have failed." — noun phrase only.<br><br>
            Also, "otherwise" needs a real, stated action before it — it can't stand alone as the condition itself; it always contrasts with something that actually happened (or should happen).</span>
          </div>'''
    },
    "compare": {
        "title": "Three hidden conditionals, one underlying \"if\"",
        "instruction": "Hover to see the full \"if\" sentence each one is quietly standing in for.",
        "items": [
            {"key": "c1", "label": "With otherwise", "text": "We backed up the files first; otherwise, we'd have lost everything.",
             "explain": "Hidden meaning: \"If we hadn't backed up the files first, we'd have lost everything.\""},
            {"key": "c2", "label": "With but for", "text": "But for the backup, we'd have lost everything.",
             "explain": "Hidden meaning: \"If it hadn't been for the backup, we'd have lost everything.\""},
            {"key": "c3", "label": "With without + gerund", "text": "Without backing up the files, we would have lost everything.",
             "explain": "Hidden meaning: \"If we hadn't backed up the files, we would have lost everything.\""},
        ]
    },
    "reading": {
        "heading": "The Mug You Already Own Is Worth More Than the One You Don't",
        "passage_paragraphs": [
            f'''Ask someone to name a price for a mug they were just given, and they will typically ask for far more than they would ever pay to buy the very same mug new. This gap is known as the endowment effect: mere {vocab("ownership","ownership")} inflates perceived value. The pattern shows up constantly at the negotiating table. {gram("g1","But for")} that psychological quirk, many deals that stall for weeks over a small gap in price would close in a single afternoon.''',
            f'''Negotiators who already possess something — a contract, a supplier relationship, a piece of equipment — consistently {vocab("overvalue","overvalue")} it compared with an outside {vocab("counterpart","counterpart")} assessing the very same item fresh. {gram("g2","Without recognising")} this bias in themselves, sellers routinely reject offers that are, by any objective {vocab("valuation","valuation")}, entirely fair. The buyer, meanwhile, feels no such {vocab("attachment","attachment")} and anchors to a lower figure without ever suspecting the size of the gap.''',
            f'''Skilled negotiators learn to work around the effect rather than fight it directly. Reframe the deal as an exchange of two things owned, they advise, rather than a simple loss on one side; {gram("g3","otherwise")}, the seller's sense of loss will dominate the entire conversation. It also helps to let a party "try before owning" — a short trial period during which nothing has technically been {vocab("relinquished","relinquished")} yet. {gram("g4","Without that intervening step")}, an early sense of ownership can quietly harden into an inflated {vocab("stake","stake")} that no argument will move. "{gram("g5","But for")} one clause allowing a thirty-day trial," one mediator recalled, "the whole partnership would have collapsed before it began." {gram("g6","Without deliberately correcting for the bias")}, she added, negotiators on both sides simply overpay for their own attachments and underpay for everyone else's.''',
        ],
        "comprehension": [
            {"prompt": "What does the mug example in the passage illustrate?", "options": [
                {"label": "That merely owning something inflates how much a person thinks it's worth.", "value": "right", "correct": True},
                {"label": "That buyers always pay more than sellers expect for identical items.", "value": "wrong", "correct": False}]},
            {"prompt": "Why do sellers often reject offers that are objectively fair, according to the passage?", "options": [
                {"label": "Because they overvalue what they already own compared with an outside assessor.", "value": "right", "correct": True},
                {"label": "Because company policy requires them to negotiate for at least a week.", "value": "wrong", "correct": False}]},
            {"prompt": "What is the purpose of a trial period, as described by the mediator?", "options": [
                {"label": "It delays the sense of ownership hardening into an inflated stake.", "value": "right", "correct": True},
                {"label": "It guarantees both sides an equal share of any future profit.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "ownership": {"word": "ownership", "ipa": "/ˈəʊ.nə.ʃɪp/", "meaning": "the state of possessing something", "example": "Mere ownership inflates how valuable something feels."},
            "overvalue": {"word": "overvalue", "ipa": "/ˌəʊ.vəˈvæl.juː/", "meaning": "to judge something as worth more than it actually is", "example": "Negotiators tend to overvalue what they already possess."},
            "counterpart": {"word": "counterpart", "ipa": "/ˈkaʊn.tə.pɑːt/", "meaning": "a person holding an equivalent position on the other side", "example": "The seller's counterpart assessed the same item fresh."},
            "valuation": {"word": "valuation", "ipa": "/ˌvæl.juˈeɪ.ʃən/", "meaning": "an estimate of how much something is worth", "example": "The offer was fair by any objective valuation."},
            "attachment": {"word": "attachment", "ipa": "/əˈtætʃ.mənt/", "meaning": "an emotional connection to something", "example": "The buyer felt no such attachment to the item."},
            "relinquished": {"word": "relinquished", "ipa": "/rɪˈlɪŋ.kwɪʃt/", "meaning": "given up or surrendered something", "example": "During the trial, nothing had technically been relinquished yet."},
            "stake": {"word": "stake", "ipa": "/steɪk/", "meaning": "a share or interest in something, especially one that matters emotionally or financially", "example": "An early sense of ownership hardened into an inflated stake."},
        },
        "gram_explanations": {
            "g1": "\"But for\" + noun phrase — highlights the single psychological factor (the endowment effect) that slows deals down.",
            "g2": "\"Without\" + gerund — compresses \"because they don't recognise\" into a single phrase.",
            "g3": "\"Otherwise\" — contrasts the recommended reframing with the unwanted alternative (the seller's sense of loss dominating).",
            "g4": "\"Without\" + noun phrase — a hidden \"if that intervening step didn't exist\", explaining what would happen instead.",
            "g5": "\"But for\" + noun phrase — credits one specific clause with preventing the partnership from collapsing.",
            "g6": "\"Without\" + gerund — compresses \"if they don't deliberately correct for it\" into a closing warning."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "To \"overvalue\" something means to…", "options": [{"label": "judge it as worth more than it actually is", "value": "right", "correct": True}, {"label": "judge it with complete objectivity", "value": "wrong", "correct": False}, {"label": "refuse to put any price on it", "value": "wrong2", "correct": False}]},
            {"prompt": "A negotiator's \"counterpart\" is…", "options": [{"label": "the person holding an equivalent position on the other side", "value": "right", "correct": True}, {"label": "a lawyer hired to draft the contract", "value": "wrong", "correct": False}, {"label": "a junior assistant taking notes", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"valuation\" is…", "options": [{"label": "an estimate of how much something is worth", "value": "right", "correct": True}, {"label": "a signed final agreement", "value": "wrong", "correct": False}, {"label": "a legal penalty for breaking a deal", "value": "wrong2", "correct": False}]},
            {"prompt": "If someone feels \"attachment\" to an item, they feel…", "options": [{"label": "an emotional connection to it", "value": "right", "correct": True}, {"label": "complete indifference towards it", "value": "wrong", "correct": False}, {"label": "an urge to sell it immediately", "value": "wrong2", "correct": False}]},
            {"prompt": "A \"stake\" in something is…", "options": [{"label": "a share or interest in it", "value": "right", "correct": True}, {"label": "a formal written complaint about it", "value": "wrong", "correct": False}, {"label": "a temporary loan of it", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "During the trial, nothing had technically been", "after": "yet.", "answers": ["relinquished"], "width": 130},
            {"before": "The offer was fair by any objective", "after": ".", "answers": ["valuation"], "width": 110},
            {"before": "Mere", "after": "inflates how valuable something feels.", "answers": ["ownership"], "width": 110},
            {"before": "An early sense of ownership can harden into an inflated", "after": ".", "answers": ["stake"], "width": 90},
        ],
    },
    "practice": {
        "gapfill_focus": "otherwise / but for / without + gerund — pick the pattern that fits.",
        "gapfill": [
            {"before": "Submit the form today;", "after": "(otherwise) you'll lose your place on the list.", "answers": ["otherwise"]},
            {"before": "", "after": "(But for) her quick thinking, the whole deal would have collapsed.", "answers": ["But for"]},
            {"before": "He signed the contract", "after": "(without / read) the fine print.", "answers": ["without reading"]},
            {"before": "Back up your work now;", "after": "(otherwise) you risk losing everything.", "answers": ["otherwise"]},
            {"before": "", "after": "(Without / check) the figures twice, she approved the invoice.", "answers": ["Without checking"]},
            {"before": "", "after": "(But for) the backup generator, the server room would have gone dark.", "answers": ["But for"]},
        ],
        "second": {
            "type": "errorspot", "title": "Spot the mistake",
            "instruction": "One word in each sentence breaks the pattern. Tap it, then check the correction.",
            "items": [
                {"words": ["But", "for", "she", "helped", "us,", "the", "project", "would", "have", "failed."], "error_indices": [2, 3], "correction": "\"she helped\" → \"her help\" (but for takes a noun phrase, never a full clause)"},
                {"words": ["Fix", "the", "leak", "today,", "unless", "it", "will", "get", "much", "worse."], "error_indices": [4], "correction": "\"unless\" → \"otherwise\" (this is a warning about a consequence, not an exception)"},
                {"words": ["Without", "to", "check", "the", "numbers,", "he", "sent", "the", "invoice."], "error_indices": [1], "correction": "\"to check\" → \"checking\" (without is followed by a gerund, not a to-infinitive)"},
            ],
        },
        "builders": [
            {"words": ["Book", "the", "ticket", "now,", "otherwise", "the", "price", "will", "rise."]},
            {"words": ["But", "for", "her", "help,", "we", "would", "have", "missed", "the", "deadline."]},
            {"words": ["He", "approved", "it", "without", "checking", "the", "figures", "first."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a moment at work when one small factor made a huge difference, using \"but for\", \"otherwise\" and \"without + -ing\" at least once each.",
        "group_questions": [
            "Tell your group about a time someone's help saved a project — try starting with \"But for...\".",
            "What's a rule at your workplace that exists because of something that once went wrong without it?",
            "Describe a mistake you've seen someone make by doing something \"without checking\" or \"without asking\" first.",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are discussing why a supplier negotiation stalled for weeks.",
        "dialogue": [
            {"speaker": "Anna", "line": "I still can't believe the supplier rejected our offer. It was fair by any objective valuation."},
            {"speaker": "Tomasz", "line": "Classic endowment effect. Without recognising it, they're overvaluing the contract just because they already hold it."},
            {"speaker": "Anna", "line": "That would explain it. Their counterpart on our side sees the exact same numbers completely differently."},
            {"speaker": "Tomasz", "line": "But for that one clause allowing a thirty-day trial, I think this deal would have collapsed already."},
            {"speaker": "Anna", "line": "Right, because nothing's technically been relinquished during the trial — it softens the sense of loss."},
            {"speaker": "Tomasz", "line": "Exactly. Without that intervening step, their sense of ownership would have hardened into an inflated stake immediately."},
            {"speaker": "Anna", "line": "We should reframe it as an exchange, not a loss on their side — otherwise their attachment will dominate the whole conversation."},
            {"speaker": "Tomasz", "line": "Agreed. Without deliberately correcting for the bias, we'll just keep going in circles."},
        ],
        "comprehension": [
            {"prompt": "Why does Tomasz think the supplier rejected a fair offer?", "options": [{"label": "They are overvaluing the contract simply because they already own it.", "value": "right", "correct": True}, {"label": "They found a cheaper alternative supplier.", "value": "wrong", "correct": False}]},
            {"prompt": "What does the thirty-day trial clause achieve, according to Anna?", "options": [{"label": "It softens the sense of loss because nothing has technically been given up yet.", "value": "right", "correct": True}, {"label": "It guarantees a lower final price for both sides.", "value": "wrong", "correct": False}]},
            {"prompt": "What does Anna suggest doing to stop the supplier's attachment dominating the talks?", "options": [{"label": "Reframing the deal as an exchange rather than a loss.", "value": "right", "correct": True}, {"label": "Ending the negotiation and finding a new supplier.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "Leave now; ___ you'll be late for the meeting.", "options": [{"label": "otherwise", "value": "right", "correct": True}, {"label": "without", "value": "wrong", "correct": False}]},
        {"prompt": "___ his colleague's warning, he would have signed the wrong document.", "options": [{"label": "But for", "value": "right", "correct": True}, {"label": "Otherwise", "value": "wrong", "correct": False}]},
        {"prompt": "She left the office ___ telling anyone where she was going.", "options": [{"label": "without", "value": "right", "correct": True}, {"label": "unless", "value": "wrong", "correct": False}]},
        {"prompt": "Back up the files first; ___ we risk losing everything.", "options": [{"label": "otherwise", "value": "right", "correct": True}, {"label": "but for", "value": "wrong", "correct": False}]},
        {"prompt": "___ the extra funding, the project would have been cancelled.", "options": [{"label": "But for", "value": "right", "correct": True}, {"label": "Without to have", "value": "wrong", "correct": False}]},
    ],
})

# ============================================================
# LESSON 10 — Advanced Wish / If Only
# ============================================================
LESSONS.append({
    "id": "b2c1-lesson-10-advanced-wish",
    "num": 10, "section_name": SECTION_NAME, "theme_class": THEME,
    "title": "Advanced Wish / If Only",
    "subtitle": "Wish + would have, and layered regret: \"I wish I'd known, because if I had, I wouldn't have...\"",
    "warmup_intro": "You already know \"I wish I had done\" for past regret. Today we add \"wish + would have\" for annoyance at someone else's past action, and practise chaining regret across two linked clauses.",
    "warmup": [
        {"prompt": "\"I wish he would have told me sooner\" expresses…",
         "options": [{"label": "annoyance or frustration about a past action (or lack of one)", "value": "right", "correct": True}, {"label": "a neutral, factual observation about the past", "value": "wrong", "correct": False}]},
        {"prompt": "\"If only I had checked the schedule, I wouldn't have missed the flight\" chains together…",
         "options": [{"label": "a regret and its direct consequence", "value": "right", "correct": True}, {"label": "two completely unrelated past events", "value": "wrong", "correct": False}]},
        {"prompt": "\"I wish I'd known, because if I had, I wouldn't have signed\" is an example of…",
         "options": [{"label": "layered regret — wish plus a third conditional explaining the consequence", "value": "right", "correct": True}, {"label": "a simple present-tense wish about now", "value": "wrong", "correct": False}]},
    ],
    "warmup_tip": "\"Wish + would have\" almost always signals irritation about someone else's (in)action — it's rarely neutral, and it's rarely used about yourself.",
    "diagnostic": [
        {"prompt": "I wish the manager ___ the deadline before we all stayed up all night.", "options": [{"label": "had mentioned", "value": "right", "correct": True}, {"label": "would mention", "value": "wrong", "correct": False}]},
        {"prompt": "I wish he ___ interrupting every single meeting.", "options": [{"label": "would stop", "value": "right", "correct": True}, {"label": "stopped", "value": "wrong", "correct": False}]},
        {"prompt": "If only she ___ me earlier, I could have rearranged my schedule.", "options": [{"label": "had told", "value": "right", "correct": True}, {"label": "told", "value": "wrong", "correct": False}]},
        {"prompt": "I wish I'd backed up the file, because if I ___, I wouldn't have lost everything.", "options": [{"label": "had", "value": "right", "correct": True}, {"label": "did", "value": "wrong", "correct": False}]},
    ],
    "widget": {
        "heading": "From simple regret to layered regret",
        "intro": "\"Wish + past perfect\" is regret about your own past. \"Wish + would\" is frustration about someone else's repeated behaviour. And you can chain a wish onto a third conditional to spell out exactly what the consequence would have been.",
        "tabs": [{"key": "pastregret", "label": "Wish + past perfect"}, {"key": "wouldhave", "label": "Wish + would(n't)"}, {"key": "layered", "label": "Layered regret"}, {"key": "quiz", "label": "Quick check"}],
        "categories": {
            "pastregret": [
                {"label": "regret about your own past action or inaction", "example": "I wish I had asked for clarification before the meeting."},
                {"label": "regret framed with \"if only\" for extra emphasis", "example": "If only I hadn't forwarded that email to the whole team."},
            ],
            "wouldhave": [
                {"label": "irritation at someone else's repeated behaviour, still ongoing", "example": "I wish he would stop rescheduling at the last minute."},
                {"label": "frustration about a specific past action someone else took (or didn't)", "example": "I wish she would have mentioned the budget cut sooner."},
            ],
            "layered": [
                {"label": "wish + a linked third conditional spelling out the consequence", "example": "I wish I'd read the contract, because if I had, I wouldn't have agreed to those terms."},
                {"label": "if only + consequence chained with \"then\"", "example": "If only we'd tested it properly, then the bug would never have reached customers."},
            ],
        },
        "quiz_labels": {"pastregret": "Wish + past perfect", "wouldhave": "Wish + would(n't)", "layered": "Layered regret"},
        "rules_html": '''
          <div class="formula" style="border-left-color:var(--c-past)">✅ Wish/If only + subject + had + past participle — regret about your own past.</div>
          <div class="formula" style="border-left-color:var(--c-modal)">✅ Wish + subject + would(n't) + base verb — frustration at someone else's action/behaviour (never used about yourself).</div>
          <div class="formula" style="border-left-color:var(--c-future);margin-bottom:20px">✅ Wish + past perfect, + because if + past perfect, + would(n't) have + past participle — layering a wish onto its exact consequence.</div>
          <div class="warn-box">
            <span>🎯</span>
            <span style="flex:1;min-width:0"><b>The tricky part:</b> "wish + would" is almost never used about yourself, and never for something you have no control over changing about the present moment.<br><br>
            ❌ "I wish I would stop being late." — sounds wrong; use "I wish I wouldn't be late" (rare) or, far more naturally, "I wish I weren't always late."<br>
            ✅ "I wish he would stop being late." — perfectly natural, aimed at someone else's behaviour.<br><br>
            For layered regret, keep the logic consistent: the "if" clause should restate the exact same past action as the wish, so the consequence clause follows logically.</span>
          </div>'''
    },
    "compare": {
        "title": "Regret about yourself vs. frustration at someone else",
        "instruction": "Hover to see why each pattern is chosen.",
        "items": [
            {"key": "c1", "label": "Regret, own past action", "text": "I wish I had double-checked the figures before submitting them.",
             "explain": "\"Wish + past perfect\" — regret about the speaker's own past action."},
            {"key": "c2", "label": "Frustration at someone else", "text": "I wish he would stop changing the deadline every other day.",
             "explain": "\"Wish + would\" — irritation at someone else's ongoing, repeated behaviour."},
            {"key": "c3", "label": "Layered regret", "text": "I wish I'd flagged the risk sooner, because if I had, we wouldn't have lost the client.",
             "explain": "The wish is chained to a full third conditional, spelling out the exact consequence."},
        ]
    },
    "reading": {
        "heading": "Defending the Decision You Already Made",
        "passage_paragraphs": [
            f'''When a decision turns out badly, the mind rarely settles for simple regret. Instead it experiences {vocab("dissonance","dissonance")} — the {vocab("discomfort","discomfort")} of holding two {vocab("contradictory","contradictory")} beliefs at once: "I am a careful decision-maker" and "I just approved a project that failed badly." "{gram("g1","I wish I had asked")} more questions before signing off," the operations director admitted afterward. "{gram("g2","Because if I had")}, we might never have {vocab("overcommitted","overcommitted")} to that vendor in the first place."''',
            f'''Rather than sit with that discomfort, people typically {vocab("rationalise","rationalise")} the original choice instead of abandoning it — reinterpreting the evidence, minimising the failure, or quietly rewriting their own memory of how confident they actually felt at the time. "{gram("g3","I wish the board would stop")} pretending the numbers looked fine from the start," one finance manager complained; "they didn't, and everyone in that room knew it."''',
            f'''The pattern intensifies with sunk cost: the more money and reputation already invested, the harder people work to {vocab("justify","justify")} continuing rather than admit the original call was wrong. "{gram("g4","If only")} we had cancelled the contract after the first missed deadline," the director said quietly, "we would have saved ourselves eighteen months of this." Colleagues nodded; nobody disagreed, but nobody had said so at the time either.''',
            f'''By the final review, the regret had layered into something more complicated than simple hindsight. "{gram("g5","I wish I hadn't reassured")} the board that everything was under control," the director reflected, "{gram("g6","because if I hadn't")}, someone might have challenged the decision months earlier, before it became impossible to unwind." Learning to {vocab("reframe","reframe")} a bad decision honestly — rather than defending it indefinitely — turned out to be the harder, and more valuable, lesson.''',
        ],
        "comprehension": [
            {"prompt": "According to the passage, what does cognitive dissonance make someone experience after a bad decision?", "options": [
                {"label": "The discomfort of holding two contradictory beliefs about themselves at once.", "value": "right", "correct": True},
                {"label": "An immediate and complete change of career.", "value": "wrong", "correct": False}]},
            {"prompt": "What do people typically do instead of abandoning a decision that turned out badly?", "options": [
                {"label": "Rationalise it by reinterpreting the evidence or minimising the failure.", "value": "right", "correct": True},
                {"label": "Report it immediately to an external regulator.", "value": "wrong", "correct": False}]},
            {"prompt": "Why does the pattern intensify with sunk cost, according to the passage?", "options": [
                {"label": "The more already invested, the harder people work to justify continuing.", "value": "right", "correct": True},
                {"label": "Because sunk costs are automatically refunded after a set period.", "value": "wrong", "correct": False}]},
        ],
        "vocab_data": {
            "dissonance": {"word": "dissonance", "ipa": "/ˈdɪs.ən.əns/", "meaning": "a lack of harmony, especially between conflicting beliefs", "example": "Cognitive dissonance appears when two beliefs contradict each other."},
            "discomfort": {"word": "discomfort", "ipa": "/dɪsˈkʌm.fət/", "meaning": "a feeling of unease or mild distress", "example": "People rationalise a decision rather than sit with the discomfort."},
            "contradictory": {"word": "contradictory", "ipa": "/ˌkɒn.trəˈdɪk.tər.i/", "meaning": "opposed to or inconsistent with something else", "example": "The two beliefs were completely contradictory."},
            "overcommitted": {"word": "overcommitted", "ipa": "/ˌəʊ.və.kəˈmɪ.tɪd/", "meaning": "taken on more obligation than is sensible", "example": "They had overcommitted to a vendor without asking enough questions."},
            "rationalise": {"word": "rationalise", "ipa": "/ˈræʃ.ən.ə.laɪz/", "meaning": "to invent a logical-sounding reason to justify a decision or feeling", "example": "People rationalise a failed decision rather than admit it was wrong."},
            "justify": {"word": "justify", "ipa": "/ˈdʒʌs.tɪ.faɪ/", "meaning": "to give a reason showing that something is right or reasonable", "example": "The team worked hard to justify continuing the project."},
            "reframe": {"word": "reframe", "ipa": "/riːˈfreɪm/", "meaning": "to present or consider something from a different perspective", "example": "Learning to reframe a bad decision honestly is genuinely difficult."},
        },
        "gram_explanations": {
            "g1": "\"Wish + past perfect\" — the director's regret about her own past inaction (not asking more questions).",
            "g2": "Layered regret continued: \"because if I had [asked]\" — a third conditional spelling out the consequence.",
            "g3": "\"Wish + would\" — frustration at the board's ongoing, repeated behaviour, not a one-off action.",
            "g4": "\"If only\" + past perfect — a stronger, more emotional version of \"I wish\", regretting a decision not made.",
            "g5": "\"Wish + past perfect\" (negative) — regret about something the director did do (reassuring the board) that she now regrets.",
            "g6": "Layered regret continued: \"because if I hadn't [reassured them]\" — completing the third-conditional consequence chain."
        },
    },
    "vocab_check": {
        "match": [
            {"prompt": "Cognitive \"dissonance\" describes…", "options": [{"label": "the discomfort of holding two conflicting beliefs at once", "value": "right", "correct": True}, {"label": "complete agreement between two beliefs", "value": "wrong", "correct": False}, {"label": "a formal disagreement settled in court", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"rationalise\" a bad decision means to…", "options": [{"label": "invent a logical-sounding reason to justify it", "value": "right", "correct": True}, {"label": "openly admit it was a mistake", "value": "wrong", "correct": False}, {"label": "reverse it immediately", "value": "wrong2", "correct": False}]},
            {"prompt": "Two beliefs that are \"contradictory\" are…", "options": [{"label": "inconsistent with each other", "value": "right", "correct": True}, {"label": "identical in every way", "value": "wrong", "correct": False}, {"label": "unrelated to each other", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"justify\" continuing a project means to…", "options": [{"label": "give a reason showing it is the right choice", "value": "right", "correct": True}, {"label": "cancel it without explanation", "value": "wrong", "correct": False}, {"label": "hand it to a different team", "value": "wrong2", "correct": False}]},
            {"prompt": "To \"reframe\" a bad decision means to…", "options": [{"label": "consider it from a different perspective", "value": "right", "correct": True}, {"label": "delete all record of it", "value": "wrong", "correct": False}, {"label": "repeat it exactly as before", "value": "wrong2", "correct": False}]},
        ],
        "gapfill": [
            {"before": "People rationalise a decision rather than sit with the", "after": ".", "answers": ["discomfort"], "width": 110},
            {"before": "They had", "after": "to a vendor without asking enough questions.", "answers": ["overcommitted"], "width": 130},
            {"before": "Learning to", "after": "a bad decision honestly is genuinely difficult.", "answers": ["reframe"], "width": 90},
            {"before": "The two beliefs were completely", "after": ".", "answers": ["contradictory"], "width": 130},
        ],
    },
    "practice": {
        "gapfill_focus": "wish + past perfect, wish + would(n't), or layered regret with because if.",
        "gapfill": [
            {"before": "I wish I", "after": "(check) the figures before submitting the report.", "answers": ["had checked"]},
            {"before": "I wish he", "after": "(stop) cancelling meetings at the last minute.", "answers": ["would stop"]},
            {"before": "If only she", "after": "(tell) us sooner, we could have prepared properly.", "answers": ["had told"]},
            {"before": "I wish I'd backed up the file, because if I", "after": "(back up) it, I wouldn't have lost the data.", "answers": ["had backed up"]},
            {"before": "I wish they", "after": "(stop) interrupting each other during meetings.", "answers": ["would stop"]},
            {"before": "If only we'd escalated it earlier, because if we", "after": "(escalate) it, the client would still be with us.", "answers": ["had escalated"]},
        ],
        "second": {
            "type": "categorise", "title": "Which kind of regret?",
            "instruction": "Decide whether each sentence expresses regret about your own past, frustration at someone else's behaviour, or layered regret with a spelled-out consequence.",
            "categories": ["Regret about own past", "Frustration at someone else", "Layered regret (wish + because if)"],
            "items": [
                {"prompt": "\"I wish I had asked for help sooner.\"", "correct": "Regret about own past"},
                {"prompt": "\"I wish she would stop micromanaging every task.\"", "correct": "Frustration at someone else"},
                {"prompt": "\"I wish I'd spoken up, because if I had, this wouldn't have happened.\"", "correct": "Layered regret (wish + because if)"},
                {"prompt": "\"If only he would return my calls occasionally.\"", "correct": "Frustration at someone else"},
            ],
        },
        "builders": [
            {"words": ["I", "wish", "I", "had", "flagged", "the", "risk", "sooner."]},
            {"words": ["I", "wish", "he", "would", "stop", "rescheduling", "at", "the", "last", "minute."]},
            {"words": ["If", "only", "we'd", "tested", "it,", "the", "bug", "wouldn't", "have", "shipped."]},
        ],
    },
    "speaking": {
        "solo_text": "Describe a work situation you regret, first using \"I wish I had...\", then add a layered sentence: \"...because if I had, I wouldn't have...\".",
        "group_questions": [
            "Is there something a colleague does that makes you think \"I wish they would stop...\"? Describe it.",
            "Tell your group about a decision you regret, and spell out exactly what would have happened differently.",
            "What's something at your workplace you wish had been handled differently, and why?",
        ],
    },
    "listening": {
        "intro": "Anna and Tomasz are reviewing why nobody challenged a vendor decision until it was too late.",
        "dialogue": [
            {"speaker": "Anna", "line": "I wish I had asked more questions before we signed off on that vendor. Because if I had, we might never have overcommitted like this."},
            {"speaker": "Tomasz", "line": "Don't be too hard on yourself. Everyone rationalised it at the time — myself included."},
            {"speaker": "Anna", "line": "Honestly, I wish the board would stop pretending the numbers looked fine from the start. They didn't, and people knew it."},
            {"speaker": "Tomasz", "line": "If only we had cancelled after the first missed deadline, we'd have saved ourselves eighteen months of this."},
            {"speaker": "Anna", "line": "The sunk cost made it so much harder to justify walking away, even when everyone privately agreed it was failing."},
            {"speaker": "Tomasz", "line": "I wish I hadn't reassured everyone that it was under control. Because if I hadn't, someone might have challenged it months earlier."},
            {"speaker": "Anna", "line": "We need to get better at reframing a bad decision honestly instead of defending it forever."},
            {"speaker": "Tomasz", "line": "Agreed. Let's actually admit it in the review this time, not just talk around it."},
        ],
        "comprehension": [
            {"prompt": "What does Anna say she regrets not doing before the vendor was signed off?", "options": [{"label": "Asking more questions.", "value": "right", "correct": True}, {"label": "Hiring an external consultant.", "value": "wrong", "correct": False}]},
            {"prompt": "According to Tomasz, what would have happened if they had cancelled after the first missed deadline?", "options": [{"label": "They would have saved themselves eighteen months of trouble.", "value": "right", "correct": True}, {"label": "The vendor would have sued the company.", "value": "wrong", "correct": False}]},
            {"prompt": "What do Anna and Tomasz agree they need to get better at?", "options": [{"label": "Reframing a bad decision honestly instead of defending it forever.", "value": "right", "correct": True}, {"label": "Signing contracts more quickly in future.", "value": "wrong", "correct": False}]},
        ],
    },
    "exit": [
        {"prompt": "I wish I ___ the contract more carefully before signing.", "options": [{"label": "had read", "value": "right", "correct": True}, {"label": "would read", "value": "wrong", "correct": False}]},
        {"prompt": "I wish she ___ interrupting me during presentations.", "options": [{"label": "would stop", "value": "right", "correct": True}, {"label": "stopped", "value": "wrong", "correct": False}]},
        {"prompt": "If only we ___ earlier, we could have avoided the delay entirely.", "options": [{"label": "had started", "value": "right", "correct": True}, {"label": "started", "value": "wrong", "correct": False}]},
        {"prompt": "I wish I'd asked for feedback, because if I ___, I'd have fixed it in time.", "options": [{"label": "had", "value": "right", "correct": True}, {"label": "did", "value": "wrong", "correct": False}]},
        {"prompt": "I wish he ___ complaining about every small change.", "options": [{"label": "would stop", "value": "right", "correct": True}, {"label": "stops", "value": "wrong", "correct": False}]},
    ],
})
