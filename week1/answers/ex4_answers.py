"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = """
It seems there are no Edinburgh venues currently available that can accommodate 300 people with vegan options. 
Would you like me to:\n
\n1. Search for venues with a lower capacity (e.g., 250-299)?
\n2. Look for venues with vegan options but no strict minimum capacity?
\n3. Check for non-vegan venues that could accommodate 300 people?\n\nLet me know how you'd like to proceed!
"""

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True  # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
I added a new tool check_venue_capacity to mcp_venue_server.py that returns just the capacity for a venue. 
When I reran exercise4_mcp_client.py without modifying it at all, the client automatically discovered 3 tools instead of 2. 
The client code (exercise4_mcp_client.py) required zero changes - it dynamically discovered the new tool through MCP's tool listing protocol. 
This demonstrates MCP's key value: server-side tool changes are instantly available to all clients without client code updates.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 4   # count in exercise2_langgraph.py 
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP provides dynamic tool discovery - the client automatically learns what tools exist and their schemas without hardcoded imports. 
This enables version independence (server updates don't require client changes), cross-language interoperability (Python server, TypeScript client), process isolation for security, and tool reusability across multiple agents. 
Multiple clients (LangGraph research agent, Rasa actions, future agents) can all connect to the same tool server without duplicating tool logic. 
It's a standardized protocol, not just file separation.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- Planner - A strong reasoning model (upstream of the loop) that breaks Rod's WhatsApp into subgoals. Lives in the autonomous loop half.

- Executor - Your current research_agent.py! It's the ReAct loop that calls tools and reasons through each step. Lives in the autonomous loop half.

- Shared MCP Tool Server - The mcp_venue_server.py already built, but expanded with web search, calendar, email. Sits between both halves, both agents connect to it.

- Structured Agent - Rasa CALM agent from Exercise 3. Handles the pub manager phone call with explicit flows and business rules. Lives in the structured agent half.

- Handoff Bridge - The component that lets the loop say "I need to make a phone call, pass this to Rasa" and lets Rasa say "I need research, pass this back to the loop". Lives between both halves
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
LangGraph for research, Rasa CALM for the confirmation call. 
In Exercise 2 Scenario 1, when The Bow Bar was too small (80 capacity), the LangGraph agent pivoted to The Albanach without being told how - this adaptability is essential for open-ended research. 
In Exercise 3, Rasa CALM consistently enforced the £300 deposit limit across all conversations, escalating when I said £800. 
Swapping them would fail: Rasa cannot improvise when the first venue is unavailable (flows.yml doesn't script every possibility), 
and LangGraph might inconsistently enforce business rules - accepting £800 in one conversation and rejecting it in another. 
"""
