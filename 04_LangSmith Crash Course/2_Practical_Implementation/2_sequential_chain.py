
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
import os

# Define the Project name
os.environ['LANGSMITH_PROJECT'] = "Sequential LLM Application"

load_dotenv()

# Prompt 1
prompt1 = PromptTemplate(
    template="Generate a details report on {topic}",
    input_variables=['topic']
)
# Prompt 2
prompt2 = PromptTemplate(
    template="Generate a 5 pointer summary from the following text \n {text}",
    input_variables=['text']
)


# Define the first model
model1 = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)

# Define the first model
# Initialize the Groq language model
model2 = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5
)

# initial Parser
parser = StrOutputParser()

# Define chain
chain = prompt1 | model1 | parser | prompt2 | model2 | parser

# Configuration and add the tags and set the metadata
CONFIG = {
    "run_name": "sequential_chain",
    "tags": ["LLM APP", "report generation", "summarization"],
    "metadata":{
        "model1": "openai/gpt-oss-20b", "model1_temp": 0.5,
        "model2": "openai/gpt-oss-120b", "model1_temp": 0.5,
        "parser": "StrOutputParser"
        }
}

# Run it
result = chain.invoke(
    {
        "topic": "AI impact in Computer Vision"
    },
    config = CONFIG
)
print(result)