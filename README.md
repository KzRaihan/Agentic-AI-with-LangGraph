# 🤖 Agentic AI with LangGraph

### The Complete Hands-On Course: From Foundations to Production-Ready AI Agents

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![LangSmith](https://img.shields.io/badge/LangSmith-Observability-FF6F00?style=for-the-badge&logo=langchain&logoColor=white)](https://smith.langchain.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/yourusername/agentic-ai-langgraph-mastery?style=for-the-badge&color=yellow)](https://github.com/yourusername/agentic-ai-langgraph-mastery)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

<!-- <br/>

<img src="assets/banner.png" alt="Agentic AI Banner" width="800"/>

<br/> -->

**Build autonomous AI agents that plan, reason, research, and execute — not just generate text.**



# 🎯 Learning Objectives

By completing this repository, the main objectives are to understand:

* What Agentic AI is and how it differs from Generative AI
* The relationship between LangChain and LangGraph
* LangGraph's graph-based execution model
* State, nodes, edges, and workflows
* Sequential, parallel, conditional, and iterative workflows
* Stateful chatbot development
* Persistence and database integration
* Streaming responses
* Short-term and long-term memory
* Tool-using AI agents
* MCP integration
* Human-in-the-loop workflows
* Subgraphs and modular agent architecture
* RAG with LangGraph
* Corrective RAG (CRAG)
* Self-RAG
* LangSmith tracing and observability
* Building autonomous research and writing agents
* Turning LangGraph prototypes into practical AI products

---

# 🧠 Curriculum

The curriculum is divided into six progressive modules.

```text
Foundation
    ↓
LangGraph Fundamentals
    ↓
Advanced LangGraph
    ↓
AI Agents
    ↓
Agentic RAG
    ↓
Productization Projects
```

---

# 📚 Module 01 — Foundation of Agentic AI

This module establishes the conceptual foundation required before building agents.

### Topics

* What is Agentic AI?
* What is an AI Agent?
* Generative AI vs Agentic AI
* Agentic AI architecture
* How AI agents reason and act
* Agent perception, reasoning, planning, and action
* LangChain vs LangGraph
* Why LangGraph is useful for agentic systems
* LangChain Core Components

### Core Concepts

```text
User
 │
 ▼
LLM
 │
 ├── Reason
 ├── Plan
 ├── Decide
 └── Act
       │
       ▼
    Tools / APIs
       │
       ▼
    Environment
```

---

# 📊 Module 02 — LangGraph Fundamentals

This module focuses on the fundamental building blocks of LangGraph.

### Topics

* LangGraph architecture
* State
* Nodes
* Edges
* Graph
* StateGraph
* START and END
* State transitions
* Sequential workflows
* Parallel workflows
* Conditional workflows
* Iterative workflows



### Project

**Build a Chatbot using LangGraph**

The chatbot will introduce:

* State management
* Message history
* Graph execution
* LLM integration
* Conversation flow

---

# ⚙️ Module 03 — Advanced LangGraph

This module moves from basic workflows to stateful and production-oriented applications.

### Topics

* Persistence in LangGraph
* Checkpoints
* Thread-based conversations
* Streaming
* Chatbot with UI
* Resume Chat feature
* SQLite integration
* LangGraph + SQLite
* Short-term memory
* Long-term memory
* Subgraphs
* LLM memory architecture

### Projects

#### 💬 Chatbot with Persistence

Build a chatbot capable of continuing conversations using persistent state.

#### 📄 Resume Chat

Build a ChatGPT-style resume interaction system where users can ask questions about a resume/document.

#### 🗄️ LangGraph + SQLite

Build a chatbot that stores conversation state using SQLite.

---

# 🤖 Module 04 — AI Agents

This module focuses on building actual tool-using agents.

### Topics

* What is an AI Agent?
* Agent architecture
* Tools in LangGraph
* Tool calling
* Tool selection
* Tool execution
* MCP
* Building an MCP client using LangGraph
* Human-in-the-loop (HITL)
* Subgraphs
* Autonomous agent workflows

### Agent Architecture

```text
                    ┌──────────────┐
                    │     User     │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │     Agent    │
                    │     / LLM    │
                    └──────┬───────┘
                           │
                    Decide what to do
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          Tool A         Tool B        Tool C
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                    ┌──────────────┐
                    │    Result    │
                    └──────┬───────┘
                           │
                           ▼
                         User
```

### Human-in-the-Loop

The agent should not always operate completely autonomously.

For sensitive or important operations:

```text
Agent
  │
  ▼
Decision
  │
  ▼
Human Approval
  │
  ├── Approved ──► Execute
  │
  └── Rejected ──► Revise / Stop
```

### Major Project

## 📝 Autonomous Research & Blog Writing Agent

Build an agent that can:

1. Receive a research topic
2. Plan the research
3. Search for information
4. Collect relevant findings
5. Analyze the information
6. Generate an outline
7. Write the article
8. Review the article
9. Improve the article
10. Produce the final blog

---

# 🔎 Module 05 — Agentic RAG

This module explores how traditional RAG can evolve into more intelligent retrieval systems.

### Topics

* RAG with LangGraph
* Retrieval workflow
* Query transformation
* Retrieval evaluation
* Corrective RAG (CRAG)
* Self-RAG
* Agentic retrieval
* Retrieval decision-making
* Fact-checking workflows

---

# 🚀 Module 06 — Productization Projects

The final module combines the concepts learned throughout the repository into practical AI applications.

### Potential Projects

### 1. 📄 Resume AI Assistant

A ChatGPT-style application that can answer questions about a user's resume.

Features:

* Document ingestion
* Chunking
* Embeddings
* Vector database
* Retrieval
* LangGraph workflow
* Conversation memory
* Streaming
* UI

---

### 2. 🤖 Stateful AI Assistant

An assistant with:

* LangGraph
* Tools
* Short-term memory
* Long-term memory
* Persistence
* SQLite
* Streaming
* Human approval
* LangSmith observability



---


# 🛠️ Technology Stack

The implementation will primarily use:

* **Python**
* **LangGraph**
* **LangChain**
* **LangChain Core**
* **LangSmith**
* **LLMs**
* **Embeddings**
* **Vector Databases**
* **SQLite**
* **MCP**
* **RAG**
* **CRAG**
* **Self-RAG**
* **Streamlit / Gradio**
* **Git & GitHub**

The exact model providers and supporting libraries may vary between individual projects.

---

# 📁 Repository Structure

```text
Agentic-AI-with-LangGraph/
│
├── 01_Foundation_of_Agentic_AI/
│   ├── 01_Generative_vs_Agentic_AI/
│   ├── 02_What_is_Agentic_AI/
│   ├── 03_LangChain_vs_LangGraph/
│   ├── 04_LangChain_Core_Components/
│   └── 05_LangGraph_Core_Components/
│
├── 02_LangGraph_Fundamentals/
│   ├── 01_Sequential_Workflow/
│   ├── 02_Parallel_Workflow/
│   ├── 03_Conditional_Workflow/
│   ├── 04_Iterative_Workflow/
│   └── 05_LangGraph_Chatbot/
│
├── 03_Advanced_LangGraph/
│   ├── 01_Persistence/
│   ├── 02_Streaming/
│   ├── 03_Chatbot_UI/
│   ├── 04_Resume_Chat/
│   ├── 05_LangGraph_SQLite/
│   ├── 06_Short_Term_Memory/
│   ├── 07_Long_Term_Memory/
│   └── 08_Subgraphs/
│
├── 04_AI_Agents/
│   ├── 01_Tools/
│   ├── 02_MCP_Client/
│   ├── 03_Human_in_the_Loop/
│   └── 04_Autonomous_Blog_Agent/
│
├── 05_Agentic_RAG/
│   ├── 01_RAG_with_LangGraph/
│   ├── 02_CRAG/
│   └── 03_Self_RAG/
│
├── 06_Productization_Projects/
│   ├── 01_Resume_AI_Assistant/
│   ├── 02_Stateful_AI_Assistant/
│   └── 03_Autonomous_Research_Agent/
│
├── assets/
├── notebooks/
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---


## 🚀 𝙃𝙤𝙬 𝙩𝙤 𝙍𝙪𝙣 𝙩𝙝𝙚 𝘼𝙥𝙥𝙡𝙞𝙘𝙖𝙩𝙞𝙤𝙣

### 1️⃣ Clone the Repository

```
    git clone https://github.com/KzRaihan/Agentic-AI-with-LangGraph.git

```

### 2️⃣ Create a Virtual Environment

```
    conda create -n GenAI python=3.11
```

### 3️⃣ Activate the Environment

```
    conda activate GenAI
```

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```


# 📚 References

* [LangGraph Documentation](https://docs.langchain.com/oss/python/langgraph/)
* [LangChain Documentation](https://docs.langchain.com/)
* [LangSmith Documentation](https://docs.langchain.com/langsmith/)
* [Model Context Protocol](https://modelcontextprotocol.io/)

---

# 👨‍💻 Author

**Md Kamruzzaman**

Computer Science & Engineering Graduate
Interested in **AI/ML, Deep Learning, Generative AI, Agentic AI, Computer Vision, and Intelligent AI Systems**.

* GitHub: [@KzRaihan](https://github.com/KzRaihan)
* LinkedIn: [@kzraihan](https://www.linkedin.com/in/kzraihan/)

