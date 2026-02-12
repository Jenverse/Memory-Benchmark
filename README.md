# Memory Systems Evaluation - Documentation


## 🎯 Purpose

We built a diagnostic benchmark to evaluate how well different memory systems help AI agents remember user information across conversations. This will help us evaluate Redis Agent Memory performance compared to other players int the market. 

We evaluated an agent-driven memory architecture, in which the agent determines what information to store, retrieve, and update, and compared it against LangMem, Mem0, Redis, and Zep.
---

## 📊 Key Results

| System | Accuracy | Type | Key Finding |
|--------|----------|------|-------------|
| **Agent-Driven** | **82.1%** | Active reasoning | ✅ **Best overall** - AI decides what to remember |
| **LangMem** | 57.9% | Automatic extraction | Good general performance |
| **Mem0** | 57.1% | Automatic extraction | Similar to LangMem |
| **Redis** | 43.9% | Automatic extraction | Moderate performance |
| **Zep** | 10.5% | Automatic extraction | ❌ **Failed** - Cannot update facts |

---

## 🔬 What We Tested

### Test Dataset
- **20 diverse user profiles** (engineers, researchers, designers, etc.)
- **100 conversations** (5 sessions per user: 4 training + 1 testing)
- **57 test questions** across 7 failure categories

### 7 Failure Categories
1. **Contradiction Update** (31.6% of tests) - Facts that change over time
   - Example: User moves from NYC → SF (must update, not duplicate)

2. **Simple Recall** - Basic fact retrieval
3. **Implicit Preference** - Inferred from behavior, never stated
4. **Temporal Relevance** - Information that becomes outdated
5. **Consolidation** - Merging related memories
6. **Noise Resistance** - Ignoring irrelevant chatter
7. **Cross-Session** - Combining facts from multiple sessions



## 📈 Detailed Performance by Category

### Complete Category-by-Category Breakdown

| Category | N | Base | Zep | Redis | Mem0 | LangMem | Agent | ∆ |
|----------|---|------|-----|-------|------|---------|-------|---|
| **Contradiction Update** | 18 | 0% | 0% | 33% | 67% | 83% | **89%** | +6 |
| **Simple Recall** | 8 | 0% | 0% | 38% | 50% | 50% | **75%** | +25 |
| **Implicit Preference** | 5 | 0% | 0% | **100%** | 80% | **100%** | **100%** | 0 |
| **Temporal Relevance** | 6 | 17% | 17% | 50% | 50% | 67% | **83%** | +16 |
| **Consolidation** | 6 | 0% | 0% | 50% | **67%** | 33% | 50% | −17 |
| **Noise Resistance** | 6 | **89%** | 83% | 83% | 67% | 83% | 83% | 0 |
| **Cross-Session** | 8 | 0% | 0% | 0% | **25%** | 13% | **25%** | 0 |

**Legend:**
- **N** = Number of tests in this category
- **Base** = Current-session-only baseline (0/No persistent memory) i.e. agent knows nothing about previous 4 session 
- **Zep, Redis, Mem0, LangMem** = External memory systems 
- **Agent** = Agent-Driven memory (active reasoning)
- **∆** = Difference between Agent and best external system (LangMem)

**Key Findings:**
- **Agent-Driven wins 4 out of 7 categories outright**
- **Contradiction Update**: Agent's biggest advantage (+6 over LangMem, +89 over Zep)
- **Simple Recall**: Agent +25 points over best external system
- **Consolidation**: Only category where external system (Mem0) beats Agent
- **Noise Resistance**: Baseline performs best (89%) - simpler is better for filtering noise


---

## 📚 Documentation

### 1. [EVALUATION_OVERVIEW.md](EVALUATION_OVERVIEW.md)
**Start here!** High-level summary of the entire evaluation.

**Contents**:
- Executive summary with key results
- What we evaluated (5 memory systems)
- Dataset structure (20 profiles, 5 sessions each)
- Key findings and insights
- Quick stats table

**Read this if**: You want a quick understanding of the evaluation and results.

---

### 2. [TEST_DATA_STRUCTURE.md](TEST_DATA_STRUCTURE.md)
Detailed breakdown of the 20 user profiles and session structure.

**Contents**:
- Session structure (4 training + 1 test)
- All 20 user profiles with examples
- Test question distribution
- Example walkthrough

**Read this if**: You want to understand the test data in detail.

---

### 3. [RESULTS_SUMMARY.md](RESULTS_SUMMARY.md)
Complete results from all 5 memory systems.

**Contents**:
- Overall performance comparison
- Performance by category (7 categories)
- Failure mode analysis
- System-by-system breakdown
- Key findings

**Read this if**: You want detailed performance metrics and comparisons.

---

### 4. [METHODOLOGY.md](METHODOLOGY.md)
Detailed evaluation strategy and metrics.

**Contents**:
- Evaluation strategy
- Test categories (7 failure modes)
- Evaluation process
- Scoring criteria
- Metrics definitions
- Experimental controls
- Limitations

**Read this if**: You want to understand how the evaluation was conducted.

---

### 5. [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
Visual summary with charts and quick stats.

**Contents**:
- Performance bar charts
- Category winners
- Performance matrix
- System strengths & weaknesses
- Key learnings

**Read this if**: You want a visual overview of the results.

---

### 6. [TEST_DATA.md](TEST_DATA_README.md) and [TEST_DATA.py](TEST_DATA.py)
Complete test dataset information and access guide.

**Contents**:
- Dataset structure explanation
- How to access the full test data
- All 20 user profiles listed
- Test category breakdown
- Example profile structure

**Read this if**: You want to access or understand the complete test dataset.


