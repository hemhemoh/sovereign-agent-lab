"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True  # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
I noticed that the plain context condition returned "The haymarket vaults" as its answer which is correct but is not the first venue on the list of options to meet the condition. 
This suggests that the model was probably not paying attention to the order of the venues in the context and the first venue that met the context was ignored.
However, for the XML and sandwich conditions, the model returned "The Albanach" which is the first venue on the list of options to meet the condition. 
To me, this suggests that formatting makes a difference in how the model processes the context and that the model is more likely to pay attention to the order of the venues in the context when it is formatted in a certain way.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Hollyrood Arms was the distractor that was more likely to cause a wrong answer because it is the only other venue on the list of options that meets all the other conditions except that the venue was full).
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C showed that even with the smaller model, the agent understood the context and was able to give correct answers.
The major difference between the smaller model and the larger was the smaller had consistent answers across all formatting options.
Unlike the larger model where the answer was different for the plain formatting option and the other two formatting options.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the model is large and the data is noisy.
Based on the results from this exercise, I believe it is important to not just pass your answers in as ...
plain text and also to use smaller models as they are just as good in retrieving information. I noticed that the part c generally consumed lesser tokens than part and and b which is more cost effective in the long run.
"""
