```
# System Architecture  
Project: The Evolution of Todo  
Hackathon II — Spec-Driven Development  

This document defines the **permanent architecture** of the Todo system across all phases.

---

## 1. Architectural Style

The system uses **Clean Layered Architecture** with strict dependency flow:

```

Interface Layer
↓
Service Layer
↓
Domain Layer
↓
Storage Layer

```

No layer may depend on a layer above it.

---

## 2. Layer Responsibilities

### 2.1 Interface Layer  
Examples:
- CLI (Phase I)
- Web API (Phase II)
- Chatbot / MCP (Phase III)
- Event Consumers (Phase V)

Responsibilities:
- Accept user or agent input
- Convert input into service calls
- Display results

Forbidden:
- Business rules  
- State mutation  
- Database access  

---

### 2.2 Service Layer  
This is the **brain** of the system.

Contains:
- TodoService  
- Application logic  
- Validation  
- State transitions  

May call:
- Domain  
- Storage  

May NOT call:
- CLI  
- Web  
- AI  
- Databases directly  

---

### 2.3 Domain Layer  
Contains:
- Task entity  
- Domain invariants  
- Business rules  

This layer must survive unchanged from Phase I to Phase V.

---

### 2.4 Storage Layer  
Examples:
- In-memory repository (Phase I)  
- SQL database (Phase II)  
- Event store (Phase V)  

Responsibilities:
- Save  
- Load  
- Query  

No business logic allowed here.

---

## 3. Evolution Law

New phases may:
- Replace the Interface Layer  
- Replace the Storage Layer  
- Add Infrastructure  

No phase may:
- Rewrite Domain logic  
- Rewrite Service logic  

---

## 4. AI Safety Rule

In Phase III and beyond, AI agents may only interact with the **Service Layer**.

AI agents are forbidden from:
- Touching repositories  
- Accessing databases  
- Modifying domain objects directly  

---

## Final Law

This architecture is permanent.  
All future code, stacks, and infrastructure must conform to this document.
```

---

# 🧠 What just happened

You just upgraded your project from:

> “Claude wrote some code”

to:

> **“Claude is building inside a governed architecture.”**

This is what **real AI-native engineering** looks like.

---
