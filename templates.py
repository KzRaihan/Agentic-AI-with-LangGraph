"""
templates.py

Purpose:
    Automatically create the complete folder and file structure
    for the "Agentic-AI-with-LangGraph" learning repository.

Usage:
    python templates.py
"""

from pathlib import Path


# ============================================================
# 1. PROJECT ROOT
# ============================================================

# Name of the root project directory
PROJECT_NAME = "Agentic-AI-with-LangGraph"

# Create the root path in the current working directory
PROJECT_ROOT = Path.cwd() / PROJECT_NAME


# ============================================================
# 2. DIRECTORY STRUCTURE
# ============================================================

DIRECTORIES = [
    # --------------------------------------------------------
    # Module 01 - Foundation of Agentic AI
    # --------------------------------------------------------
    "01_Foundation_of_Agentic_AI/01_What_is_Agentic_AI",
    "01_Foundation_of_Agentic_AI/02_Generative_vs_Agentic_AI",
    "01_Foundation_of_Agentic_AI/03_LangChain_vs_LangGraph",
    "01_Foundation_of_Agentic_AI/04_LangChain_Core_Components",

    # --------------------------------------------------------
    # Module 02 - LangGraph Fundamentals
    # --------------------------------------------------------
    "02_LangGraph_Fundamentals/01_Sequential_Workflow",
    "02_LangGraph_Fundamentals/02_Parallel_Workflow",
    "02_LangGraph_Fundamentals/03_Conditional_Workflow",
    "02_LangGraph_Fundamentals/04_Iterative_Workflow",
    "02_LangGraph_Fundamentals/05_LangGraph_Chatbot",

    # --------------------------------------------------------
    # Module 03 - Advanced LangGraph
    # --------------------------------------------------------
    "03_Advanced_LangGraph/01_Persistence",
    "03_Advanced_LangGraph/02_Streaming",
    "03_Advanced_LangGraph/03_Chatbot_UI",
    "03_Advanced_LangGraph/04_Resume_Chat",
    "03_Advanced_LangGraph/05_LangGraph_SQLite",
    "03_Advanced_LangGraph/06_Short_Term_Memory",
    "03_Advanced_LangGraph/07_Long_Term_Memory",
    "03_Advanced_LangGraph/08_Subgraphs",

    # --------------------------------------------------------
    # Module 04 - AI Agents
    # --------------------------------------------------------
    "04_AI_Agents/01_Tools",
    "04_AI_Agents/02_MCP_Client",
    "04_AI_Agents/03_Human_in_the_Loop",
    "04_AI_Agents/04_Autonomous_Blog_Agent",

    # --------------------------------------------------------
    # Module 05 - Agentic RAG
    # --------------------------------------------------------
    "05_Agentic_RAG/01_RAG_with_LangGraph",
    "05_Agentic_RAG/02_CRAG",
    "05_Agentic_RAG/03_Self_RAG",

    # --------------------------------------------------------
    # Module 06 - Productization Projects
    # --------------------------------------------------------
    "06_Productization_Projects/01_Resume_AI_Assistant",
    "06_Productization_Projects/02_Stateful_AI_Assistant",
    "06_Productization_Projects/03_Autonomous_Research_Agent",

    # --------------------------------------------------------
    # Supporting directories
    # --------------------------------------------------------
    "assets",
    "assets/architecture",
    "assets/screenshots",
    "notebooks",
]


# ============================================================
# 3. FILE STRUCTURE
# ============================================================

FILES = [
    # Root files
    "README.md",
    "requirements.txt",
    ".gitignore",
    "LICENSE",

    # Module README files
    "01_Foundation_of_Agentic_AI/README.md",
    "02_LangGraph_Fundamentals/README.md",
    "03_Advanced_LangGraph/README.md",
    "04_AI_Agents/README.md",
    "05_Agentic_RAG/README.md",
    "06_Productization_Projects/README.md",
]


# ============================================================
# 4. FILE CONTENT
# ============================================================

ROOT_README = """# 🤖 Agentic AI with LangGraph

A practical learning and implementation repository for building
Agentic AI systems with LangGraph.

## Modules

- 01 - Foundation of Agentic AI
- 02 - LangGraph Fundamentals
- 03 - Advanced LangGraph
- 04 - AI Agents
- 05 - Agentic RAG
- 06 - Productization Projects

More documentation will be added as the learning journey progresses.
"""


REQUIREMENTS = """# Core
langchain
langchain-core
langgraph

# LangSmith
langsmith

# Environment
python-dotenv

# UI
streamlit
gradio

# Database
aiosqlite
"""

GITIGNORE = """# ============================================================
# Python
# ============================================================

__pycache__/
*.py[cod]
*.pyo
*.pyd

# Virtual environments
venv/
.venv/
env/
ENV/

# ============================================================
# Environment Variables
# ============================================================

.env
.env.*
!.env.example

# ============================================================
# Jupyter Notebook
# ============================================================

.ipynb_checkpoints/

# ============================================================
# VS Code
# ============================================================

.vscode/

# ============================================================
# OS Generated Files
# ============================================================

.DS_Store
Thumbs.db

# ============================================================
# Logs
# ============================================================

*.log

# ============================================================
# Python Packaging
# ============================================================

*.egg-info/
dist/
build/

# ============================================================
# SQLite
# ============================================================

*.db
*.sqlite
*.sqlite3

# ============================================================
# Secrets
# ============================================================

*.pem
*.key

# ============================================================
# Generated Files
# ============================================================

outputs/
tmp/
temp/
"""

LICENSE = """MIT License

Copyright (c) 2026 Md Kamruzzaman

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files, to deal
in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED.
"""


# ============================================================
# 5. MODULE README CONTENT
# ============================================================

MODULE_READMES = {
    "01_Foundation_of_Agentic_AI/README.md": """# Module 01 — Foundation of Agentic AI

This module introduces the fundamental concepts behind Agentic AI.

## Topics

- What is Agentic AI?
- Generative AI vs Agentic AI
- LangChain vs LangGraph
- LangChain Core Components
""",

    "02_LangGraph_Fundamentals/README.md": """# Module 02 — LangGraph Fundamentals

This module focuses on the fundamental workflow patterns
used in LangGraph.

## Topics

- Sequential Workflow
- Parallel Workflow
- Conditional Workflow
- Iterative Workflow
- LangGraph Chatbot
""",

    "03_Advanced_LangGraph/README.md": """# Module 03 — Advanced LangGraph

This module explores advanced LangGraph capabilities for
building stateful and practical AI applications.

## Topics

- Persistence
- Streaming
- Chatbot UI
- Resume Chat
- LangGraph + SQLite
- Short-Term Memory
- Long-Term Memory
- Subgraphs
""",

    "04_AI_Agents/README.md": """# Module 04 — AI Agents

This module focuses on building tool-using and autonomous
AI agents.

## Topics

- Tools
- MCP Client
- Human-in-the-Loop
- Autonomous Blog Agent
""",

    "05_Agentic_RAG/README.md": """# Module 05 — Agentic RAG

This module explores intelligent retrieval workflows
using LangGraph.

## Topics

- RAG with LangGraph
- Corrective RAG (CRAG)
- Self-RAG
""",

    "06_Productization_Projects/README.md": """# Module 06 — Productization Projects

This module combines the concepts learned throughout the
repository into practical AI applications.

## Projects

- Resume AI Assistant
- Stateful AI Assistant
- Autonomous Research Agent
""",
}


# ============================================================
# 6. HELPER FUNCTIONS
# ============================================================

def create_directories():
    """
    Create all directories defined in DIRECTORIES.
    """

    print("\nCreating directories...\n")

    for directory in DIRECTORIES:
        directory_path = PROJECT_ROOT / directory

        # parents=True creates any missing parent directories.
        # exist_ok=True prevents an error if the directory exists.
        directory_path.mkdir(parents=True, exist_ok=True)

        print(f"[DIR]  Created: {directory}")


def create_file(file_path: Path, content: str = ""):
    """
    Create a file with the provided content.

    If the file already exists, it will NOT be overwritten.
    """

    if file_path.exists():
        print(f"[SKIP] File already exists: {file_path.relative_to(PROJECT_ROOT)}")
        return

    file_path.parent.mkdir(parents=True, exist_ok=True)

    file_path.write_text(
        content,
        encoding="utf-8"
    )

    print(f"[FILE] Created: {file_path.relative_to(PROJECT_ROOT)}")


def create_root_files():
    """
    Create the main project files.
    """

    print("\nCreating root files...\n")

    root_files = {
        "README.md": ROOT_README,
        "requirements.txt": REQUIREMENTS,
        ".gitignore": GITIGNORE,
        "LICENSE": LICENSE,
    }

    for filename, content in root_files.items():
        create_file(
            PROJECT_ROOT / filename,
            content
        )


def create_module_readmes():
    """
    Create README.md files for each major module.
    """

    print("\nCreating module README files...\n")

    for filename, content in MODULE_READMES.items():
        create_file(
            PROJECT_ROOT / filename,
            content
        )


# ============================================================
# 7. MAIN FUNCTION
# ============================================================

def main():
    """
    Main execution function.

    Creates the complete Agentic AI with LangGraph
    repository structure.
    """

    print("=" * 70)
    print("🤖 Agentic AI with LangGraph - Repository Generator")
    print("=" * 70)

    print(f"\nProject Location:")
    print(PROJECT_ROOT)

    # --------------------------------------------------------
    # Create directories
    # --------------------------------------------------------

    create_directories()

    # --------------------------------------------------------
    # Create root files
    # --------------------------------------------------------

    create_root_files()

    # --------------------------------------------------------
    # Create module README files
    # --------------------------------------------------------

    create_module_readmes()

    # --------------------------------------------------------
    # Final message
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("Repository structure created successfully!")
    print("=" * 70)

    print(f"\n📁 Project: {PROJECT_NAME}")
    print(f"📍 Location: {PROJECT_ROOT}")

    print("\nNext steps:")
    print("1. cd Agentic-AI-with-LangGraph")
    print("2. Create your Python environment")
    print("3. Install dependencies")
    print("4. Start Module 01")
    print("5. Initialize Git")
    print("6. Push the repository to GitHub")


# ============================================================
# 8. SCRIPT ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()