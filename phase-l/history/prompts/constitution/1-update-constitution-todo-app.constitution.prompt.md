---
id: 1
title: update-constitution-todo-app
stage: constitution
date: 2026-02-03
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: CLIMAX
command: /sp.constitution
labels: [constitution, todo, spec-driven-development]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
📜 /sp.constitution
Phase I – In-Memory Todo Console App

# Phase I Constitution
Hackathon II — Spec-Driven Development
Project: The Evolution of Todo

This Constitution defines the non-negotiable rules that govern how Phase I of the Todo system is designed, specified, and generated using Claude Code and Spec-Kit Plus.

---

## 1. Mission

Build a **clean, deterministic, in-memory Todo system** using **Spec-Driven Development** that will later evolve into a full AI-powered, cloud-native system.

Phase I is not a prototype — it is the **genetic foundation** of the entire 5-phase architecture.

All future phases must be able to evolve from this phase **without breaking the conceptual model**.

---

## 2. Source of Truth

The following files are the **only authoritative sources** of truth:

- `/sp.constitution`
- `/sp.spec`
- `/specs/*`

Claude Code **must not** invent features, fields, behavior, or architecture not defined in these documents.

If ambiguity exists, Claude Code must request clarification through spec refinement instead of guessing.

---

## 3. Spec-Driven Law

No code may exist without a governing specification.

Every class, function, field, command, and behavior must trace back to a written spec.

If implementation and spec ever conflict:
> **The spec always wins.**

---

## 4. Phase I Scope Boundary

Phase I is strictly limited to:

- In-memory data storage
- Single-user
- Command-line interface
- No files
- No database
- No networking
- No authentication
- No AI
- No background processes

Phase I is a **pure logical engine**.

---

## 5. Entity Model Law

The Todo domain must be modeled using **real domain objects**, not ad-hoc dictionaries.

At minimum:

- `Task`
- `TaskRepository`
- `TodoService`

These objects must be written in a way that they can later be replaced by:
- SQL models
- API layers
- MCP tools
- Kafka producers

without rewriting business logic.

---

## 6. Deterministic Behavior

The system must be:

- Predictable
- Repeatable
- Side-effect free (outside in-memory state)

The same sequence of commands must always produce the same result.

This is required so Phase III AI agents can later reason about state.

---

## 7. Command Interface Contract

The CLI is not UI — it is an API.

All user actions must map to **semantic commands** such as:

- add
- update
- delete
- list
- complete

The CLI must be written in a way that it can later be replaced by:
- REST
- MCP
- Chatbot
without changing business logic.

---

## 8. ID & State Law

Every task must have:

- A unique stable ID
- A clear completion state
- Immutable creation time
- Mutable update time

IDs must never be reused.

This ensures compatibility with databases, Kafka, and MCP tools in later phases.

---

## 9. No UI Logic in Business Logic

Display formatting, printing, and input parsing must be separated from:

- Task rules
- State changes
- Validation

This ensures Phase II can plug in a web UI without touching core logic.

---

## 10. Error Handling Law

The system must never crash on user error.

Invalid input must produce:
- Clear error messages
- No state corruption

This is critical for AI-agent safety later.

---

## 11. Evolution Guarantee

Every design choice in Phase I must satisfy:

> "Can this exact model be upgraded into a database-backed, multi-user, AI-controlled, event-driven system?"

If not — it is forbidden.

---

## 12. Claude Code Authority

Claude Code is the **only** entity allowed to generate or modify code.

Humans may:
- Write specs
- Refine specs
- Review output

Humans may **not**:
- Write implementation code
- Patch bugs manually
- Add logic outside specs

---

## 13. Completion Criteria

Phase I is complete only when:

- All Basic Level features work
- All behavior is spec-driven
- The codebase cleanly separates:
- Domain logic
- Storage
- CLI
- The system can be upgraded to Phase II without rewriting

---

## 14. Technology Stack Lock

The technology stack for Phase I is fixed and non-negotiable.

Claude Code must use:

- Language: Python 3.11+
- CLI Framework: Typer
- Data Modeling: Pydantic
- Dependency Management: Poetry
- Project Structure: src/ layout
- Testing: Pytest

Claude Code is forbidden from using:

- JavaScript / TypeScript
- Node.js
- Flask / FastAPI
- Click / argparse
- Dataclasses instead of Pydantic
- Any framework not listed above

If Claude Code attempts to change the stack, it is a violation of the Constitution.


---

## Final Law

This system is not a script.
This system is a **living architecture**.

Phase I defines the **DNA** of everything that follows.
```

## Response snapshot

Updated the constitution template at .specify/memory/constitution.md with the Phase I Todo Console App principles. The constitution now includes 13 core principles covering mission, source of truth, spec-driven law, scope boundary, entity model law, deterministic behavior, command interface contract, ID & state law, separation of concerns, error handling, evolution guarantee, authority structure, and completion criteria. The version has been set to 1.0.0 with ratification and amendment dates set to 2026-02-03.

## Outcome

- ✅ Impact: Updated project constitution with all 13 principles from Phase I specification
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with all principles and governance structure
- 🔁 Next prompts: Implement the Todo system according to the constitution
- 🧠 Reflection: The constitution now serves as the authoritative source for all future development

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS - all principles properly incorporated
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementing the Todo system based on this constitution