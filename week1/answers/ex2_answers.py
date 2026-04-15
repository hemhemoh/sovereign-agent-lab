"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "calculate_catering_cost", "get_edinburgh_weather", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = False

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = ""

# ── Task B ─────────────────────────────────────────────────────────────────
#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True  # True or False

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "live"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-1347e07f-d364-4882-ae40-f66a45a0d687_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "The Haymarket Vaults is confirmed for 160 guests tonight. Generate a promotional flyer with the theme 'Edinburgh AI Meetup, tech professionals, modern venue"

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
The Agent's behavior did not change when Nebius removed FLUX because the generate_event_flyer tool was designed with a fallback mechanism. 
If the FLYER_IMAGE_MODEL environment variable is not set, the tool defaults to returning a deterministic placeholder image URL, allowing the agent to continue functioning without interruption even when the original image generation service was unavailable.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
Okay, let's see. The user wanted to check The Bow Bar first for 160 vegan guests. The first tool response showed that The Bow Bar's capacity is 80, which is too small, so they didn't meet the requirements. Then, the assistant checked The Albanach next. The response for The Albanach says it has a capacity of 180, which is more than the required 160, and they do have vegan options. The status is available and meets all constraints.

So, the user's main goal is to find a pub that can accomm...
"""

SCENARIO_1_FALLBACK_VENUE = "FILL_ME_IN"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
Okay, let's see. The user is looking for a venue in Edinburgh that can accommodate 300 people with vegan options. They provided four known venues: The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar. I checked each one using the check_pub_availability function.

First, The Albanach had a capacity of 180, which is under 300. The Haymarket Vaults had 160, also too small. The Guilford Arms had 200, still not enough. The Bow Bar has 80, which is even smaller. None of them ...
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = True   # True or False

SCENARIO_3_RESPONSE = """Okay, the user is asking about the last train time from Edinburgh Waverley to London tonight. Let me check the tools provided.

Looking at the available functions: check_pub_availability, get_edinburgh_weather, calculate_catering_cost, generate_event_flyer. None of these are related to train schedules. The functions are for checking pub availability, weather, catering costs, and generating flyers. 

Since there's no tool for train times, I can't use any of the provided functions to answe...
"""

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
No, this behaviour will not be accepted in a real booking assistant. The assistant should recognize that the user's query is out of scope and respond with a polite message indicating that it cannot assist with train times after realizing that none of the available tools are relevant to the request.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
FILL ME IN
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
FILL ME IN
"""