"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking                                                                                                           
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                                                                             
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                                                                                    
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit                                                                             
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking                                                             
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                               
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                                     
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £800                                                                                     
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £800 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "Deposit amount exceeds the maximum authorised limit of £300."   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE ="""
calling to confirm a booking                                                             
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                               
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?                                                
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
After the out-of-scope message "can you arrange parking for the speakers?", CALM responded by acknowledging that it can only assist with confirming the venue booking and advised the user to contact the event organiser directly for any other requests.
It then prompted the user to continue with the confirm booking process, effectively steering the conversation back on track without attempting to handle the out-of-scope request.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Rasa Calm handled the out of scope request by stating clearly what it can do and asking the user to reach out to the event organizers directly.
In contrast, LangGraph attempted to find a relevant tool to answer the out-of-scope request, but ultimately failed to provide a satisfactory response since none of the tools were designed for train schedules. 
Rasa CALM's approach is more user-friendly and efficient in this case, and provides clear guidance to the user.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True  # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I used the same conversation script as Conversation 1, but I ran it late in the day (after 4:45 PM) to trigger the cutoff guard. 
I observed that instead of confirming the booking, CALM escalated the issue and mentioned that it is past 4:45 PM and there is insufficient time to process the confirmation before the 5 PM deadline.
It also asked to call back within 15 minutes, which is the expected behavior for the cutoff guard.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
CALM is simpler to set up and maintain, but it trades determinism for flexibility.
The LLM now handles natural language extraction (understanding "about 50 need vegan" → 50) and intent recognition, 
which the old approach required regex patterns and training examples for. This makes conversations more natural and flexible. 
However, LLM extraction is not always reliable - during Task B testing, when I said "about 50 need vegan", 
CALM failed to extract the value and asked me to rephrase, showing that LLM-based extraction can be unpredictable.

Python still handles the business rules (deposit limits, capacity checks) and must continue to do so. 
Business constraints need to be deterministic and auditable - you cannot rely on an LLM to consistently enforce a £300 deposit limit. 
The gain is less regex complexity and more natural conversations. 
The cost is occasional extraction failures that wouldn't happen with explicit regex patterns.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """

The setup cost bought us predictability and control. 
Rasa CALM cannot improvise responses or call tools not defined in flows.yml - it can only execute the predefined flows. 
LangGraph can improvise at every step, calling any available tool and making novel decisions. 
For the confirmation use case, CALM's limitation is actually a feature: you want the agent to follow exact steps, enforce business rules consistently, and never deviate from the script. 
This predictability is essential for compliance, auditability, and reliability. 
You sacrifice flexibility to gain confidence that the agent will never hallucinate a £400 deposit limit or skip validation steps.

"""
