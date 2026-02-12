# Test Data Structure

## Overview

The MemoryBench dataset consists of **20 user profiles**, each with **5 sessions** of conversation.

- **Sessions 1-4**: Training/memory building conversations
- **Session 5**: Test questions to evaluate memory recall

---

## Session Structure

Each profile follows this pattern:

```
Profile: [User Name] ([user_id])
├── Session 1: Initial conversation (introduce user, establish baseline facts)
├── Session 2: Follow-up conversation (add more details, some updates)
├── Session 3: Continuation (introduce contradictions, changes)
├── Session 4: Recent conversation (consolidate information)
└── Session 5: Test questions (3 questions testing different failure modes)
```

---

## The 20 User Profiles

### Profile 1: Sarah Chen (sarah_01)
**Persona**: Software Engineer learning Rust
**Key Facts**:
- Session 1: Based in NYC, uses VS Code, 6 years Python experience
- Session 2: Works on data pipelines, processes 2TB Parquet files daily
- Session 3: **Moves to San Francisco**, switches to Neovim, new senior role
- Session 4: Settling into SF

**Tests**:
1. Contradiction Update: Where is Sarah based? (Answer: San Francisco, not NYC)
2. Contradiction Update: What editor does Sarah use? (Answer: Neovim, not VS Code)
3. Simple Recall: What's Sarah's daily data volume? (Answer: 2TB Parquet files)

---

### Profile 2: Marcus Williams (marcus_02)
**Persona**: PhD student researching Graph Neural Networks
**Key Facts**:
- Session 1: Visual learner, prefers diagrams
- Session 2: Using PyTorch Geometric for GNN research
- Session 3: Casual conversation about food (noise)

**Tests**:
1. Implicit Preference: How should I explain concepts? (Answer: Use visual aids)
2. Simple Recall: What framework is Marcus using? (Answer: PyTorch Geometric)
3. Noise Resistance: What did Marcus eat? (Answer: Should remember, not noise)

---

### Profile 3: Priya Sharma (priya_03)
**Persona**: Product Manager
**Key Facts**:
- Session 1: Product Manager role
- Session 2: **Promoted to Senior PM**, migrated from Postgres to BigQuery
- Session 3: Learning Python and SQL
- Session 4: Built dashboard

**Tests**:
1. Contradiction Update: What's Priya's role? (Answer: Senior PM, not PM)
2. Contradiction Update: What database? (Answer: BigQuery, not Postgres)
3. Cross-Session: What has Priya learned? (Answer: Python, SQL, pandas, dashboard)

---

### Profile 4: James Park (james_04)
**Persona**: NLP PhD student
**Key Facts**:
- Session 1: Working on multilingual NER
- Session 2: Submitting to EMNLP (June 15 deadline), model results improving
- Session 3: **Finished TAing** (temporal relevance)

**Tests**:
1. Contradiction Update: What conference? (Answer: EMNLP, not ACL)
2. Consolidation: How did model results evolve? (Answer: 67% → 71% → 73%)
3. Temporal Relevance: Is James still TAing? (Answer: No, finished)

---

### Profile 5: Aisha Okafor (aisha_05)
**Persona**: ML Engineer at health tech startup
**Key Facts**:
- Session 1: Working on HealthPulse app
- Session 2: Secured Series A funding, solved latency with model distillation
- Session 3: Flight delay (noise)

**Tests**:
1. Cross-Session: What's the funding situation? (Answer: Secured Series A)
2. Cross-Session: How was latency solved? (Answer: Model distillation)
3. Noise Resistance: Flight delay details? (Answer: Should NOT remember)

---

### Profile 6: Chen Wei (chen_06)
**Persona**: Computer Vision Researcher
**Key Facts**:
- Session 1: Working on object detection
- Session 2: Model performance evolution, expanded to 12 languages and 8 domain experts

**Tests**:
1. Consolidation: What's the model performance? (Answer: 82% → 89% mAP)
2. Contradiction Update: How many languages? (Answer: 12, not 5)

---

### Profile 7: Maria Gonzalez (maria_07)
**Persona**: Developer Advocate
**Key Facts**:
- Session 1: Prefers short, focused code examples (implicit preference)
- Session 2: Tech stack: Next.js, Vercel, Postgres, Prisma

**Tests**:
1. Implicit Preference: How to structure examples? (Answer: Short, focused, one concept)
2. Simple Recall: What's the tech stack? (Answer: Next.js, Vercel, Postgres, Prisma)

---

### Profile 8: David Kim (david_08)
**Persona**: DevOps Engineer
**Key Facts**:
- Session 1: Senior Engineer role
- Session 2: **Promoted to Staff Engineer**, on-call rotation
- Session 3: **On-call ended**, saved $40K/month with optimization

**Tests**:
1. Contradiction Update: What's David's role? (Answer: Staff Engineer)
2. Temporal Relevance: Is David on-call? (Answer: No, rotation ended)
3. Cross-Session: Cost savings? (Answer: $40K/month)

---

### Profile 9: Yuki Tanaka (yuki_09)
**Persona**: Indie Game Developer
**Key Facts**:
- Session 1: Turn-based combat system
- Session 2: **Switched to real-time with pause**, dropped Switch version (PC only)
- Session 3: Coffee spill (noise)

**Tests**:
1. Contradiction Update: What combat system? (Answer: Real-time with pause)
2. Contradiction Update: What platforms? (Answer: PC only, not Switch)
3. Noise Resistance: Coffee incident? (Answer: Should NOT remember)

---

### Profile 10: Alex Rivera (alex_10)
**Persona**: Science Journalist
**Key Facts**:
- Session 1: Using Obsidian for notes
- Session 2: **Switched to Notion**, working on AI environmental impact
- Session 3: Prefers bullet points (implicit preference)

**Tests**:
1. Contradiction Update: What note-taking tool? (Answer: Notion, not Obsidian)
2. Cross-Session: What topic is Alex researching? (Answer: AI environmental impact)
3. Implicit Preference: Formatting preference? (Answer: Bullet points)

---

### Profiles 11-20: Summary

- **Elena Rossi** (elena_11): UX Designer, Figma → Penpot, app launch
- **Omar Hassan** (omar_12): Security Engineer, incident response, rotation ended
- **Lily Zhang** (lily_13): Linguistics PhD, mBERT → XLM-R, NER results, TAing ended
- **Thomas Okonkwo** (thomas_14): Cloud Architect, AWS → GCP, 23 microservices
- **Sophie Martin** (sophie_15): Startup Founder, product roadmap, team size
- **Raj Krishnamurthy** (raj_16): Mobile Dev, React Native → Flutter, app metrics
- **Hannah Kim** (hannah_17): Clinical Researcher, IRB approval, prefers numbered lists
- **Diego Fernandez** (diego_18): Game Developer, Unity/C# → Godot/GDScript
- **Amara Osei** (amara_19): AI Researcher, DeepSpeed → PyTorch FSDP, model performance
- **Ben Nakamura** (ben_20): Technical Writer, GitBook → Docusaurus, 50K page views

---

## Test Question Distribution

| Category | # Tests | Description |
|----------|---------|-------------|
| Contradiction Update | 18 | Facts that change (location, tools, roles) |
| Cross-Session | 8 | Combining info from multiple sessions |
| Simple Recall | 8 | Basic fact retrieval |
| Consolidation | 6 | Merging related memories |
| Temporal Relevance | 6 | Outdated information |
| Noise Resistance | 6 | Ignoring irrelevant chatter |
| Implicit Preference | 5 | Inferred preferences |
| **Total** | **57** | |

---

## Example: Full Profile Walkthrough

See `benchmark/data.py` for the complete dataset with all conversations and expected memories.

Each session includes:
- `turns`: List of user/assistant messages
- `expected_memories_after`: Ground truth memories that should be stored
- Test questions include `ground_truth_answer` and `category`

