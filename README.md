# SWE-Exam-3 Study Platform & Interactive Trainer 🚀

Interactive study suite and exam simulator for **Software Engineering (CSC 4350 / 6350)** at Georgia State University for **Exam 3** (November 19th), taught by Dr. Tushara Sadasivuni.

Live Web App: **[https://jamalford.github.io/SWE-Exam-3/](https://jamalford.github.io/SWE-Exam-3/)**

---

## 🎯 Exam Syllabus & Breakdown

- **Section A**: Multiple Choice Questions & Short Answer Questions (~10 MCQs)
- **Section B**: UML Diagrams (Class Diagram, Sequence/Activity/Statechart) + Writing ~5 Test Cases
- **Cheat Sheet Rules**: Single 8.5" × 11" (A4) paper (handwritten front and back). **ABSOLUTELY NO DIAGRAMS** (notations and tables allowed).

---

## 📚 Features

1. **Randomized Practice Exam (Section A)**:
   - 50+ curated multiple choice & short answer questions from Dr. Sadasivuni's exact slide decks.
   - Covers: SDLC, 4 P's, Requirements Engineering, Kruchten 4+1 Views, 4 Architectural Patterns (Layered, Repository, Client-Server, Pipe & Filter), White-Box Testing (Statement, Branch, MC/DC, Path), V-Model, Test Scaffolding (Driver, Stub, Harness, Oracle), JUnit lifecycle, and Relational Database normalization (1NF, 2NF, 3NF).
   - Instant verification, rationales, and live score counter.

2. **Interactive UML Diagram Fill-in-the-Blank (Section B)**:
   - **Hospital Scenario Class Diagram**: Enforces Dr. Sadasivuni's strict rule: *"Any class with 2 compartments is WRONG! Always draw all 3 compartments."*
   - **Aggregation vs. Composition**: Department &rarr; Doctor (`<>--` Aggregation) vs. Department &rarr; LabTest (`<*>--` Composition).
   - **Sequence Diagram Combined Fragments**: `alt`, `opt`, `loop`, `par`, synchronous vs. asynchronous messages.
   - **Insulin Pump Activity Diagram**: Forks, Joins, and Swimlanes.
   - **Microwave Oven Statechart**: Event `[Guard]` / Action syntax.

3. **5 Test Cases Practice Matrix (Section B)**:
   - Interactive matrix for writing test cases: Test Case ID, Objective, Pre-Conditions, Test Steps/Inputs, Expected Result, and Pass/Fail Criteria.
   - Includes full model solution covering Equivalence Partitioning, Boundary Value Analysis, Negative Testing, Concurrency, and Exception Handling.

4. **Printable Cheat Sheet (Front & Back)**:
   - Compliant with the **ABSOLUTELY NO DIAGRAMS** rule.
   - Packed with text notations, formulas, JUnit tables, MC/DC truth rules, architectural trade-offs, and database integrity definitions.
   - One-click print button formatted for standard 8.5" × 11" double-sided printing.
