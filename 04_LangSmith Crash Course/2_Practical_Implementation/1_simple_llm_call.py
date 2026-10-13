
# ===============================================================
# Project: Building a Simple LLM Workflow with LangChain and LangSmith
#
# Objective:
# Develop a basic LLM workflow using LangChain and visualize its
# execution traces in the LangSmith interface.
#
# Workflow:
# User Query → Prompt Template → LLM → Output Parser → Final Output
#
# Key Learning Outcomes:
# 1. Understand the fundamentals of LLM workflow orchestration.
# 2. Connect a prompt template, language model, and output parser.
# 3. Enable LangSmith tracing to monitor and inspect workflow execution.
# 4. Analyze intermediate steps and final outputs in LangSmith.
# ===============================================================


from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Simple one-line Prompt
prompt = PromptTemplate.from_template("{question}")

# Define the model
model = ChatGroq(
    model="openai/gpt-oss-20b",
)

# initial Parser
parser = StrOutputParser()

# Define chain
chain = prompt | model | parser

# Run it
result = chain.invoke(
    {
        "question": "Tell about the Capital of Italy?"
    }
)
print(result)