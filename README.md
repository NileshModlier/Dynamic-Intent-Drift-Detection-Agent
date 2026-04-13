# Dynamic Intent Drift Detection Agent

## Overview
This project focuses on detecting **intent drift** in long‑running customer conversations. In real CRM interactions, user intent often changes mid‑conversation, and naive per‑turn classification frequently locks users into incorrect flows.

The agent treats intent as a **time‑evolving signal**, tracking intent labels along with confidence scores across turns. Intent drift is detected using temporal comparison, confidence deltas, and stabilization thresholds rather than reacting to noise.

---

## Key Features
- Intent tracking across conversation turns
- Confidence‑aware drift detection
- Stabilization windows to prevent oscillation
- Guardrails against infinite re‑planning loops
- Designed to plug into escalation and routing systems

---

## Architecture
---

## Technologies Used
- Python
- Rule‑based + statistical logic
- Confidence scoring
- Agent‑friendly modular design

---

## Why Intent Drift Matters
- Users frequently change goals mid‑conversation
- Static flows degrade user experience
- Drift detection enables adaptive, human‑like behavior

---

## Future Improvements
- ML‑based intent confidence calibration
- Multi‑intent handling
- Drift‑aware conversation re‑planning

---

## License
MIT License
