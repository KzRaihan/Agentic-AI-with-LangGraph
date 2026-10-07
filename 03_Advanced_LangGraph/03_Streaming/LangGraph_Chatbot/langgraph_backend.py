#### Step 1: Import Necessary Libraries

from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver

from typing import TypedDict, Annotated
from dotenv import load_dotenv

load_dotenv()

#### Step 2: Define the State
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


#### Step 4: Define the Nodes
# Define the LLM for chat_node
llm =  ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# Node__1: Define chat_node
def chat_node(state: ChatState) -> dict:
    # Extract the user query from the state
    messages = state['messages']

    # Send the query to the LLM
    response = llm.invoke(messages)

    # response store the state and return 
    return {
        "messages": [response]
    }

#### Step 3: Build Graph
# initialize the Memory_Save into RAM
checkpointer = MemorySaver()

# initial an object of graph
graph = StateGraph(ChatState)

# add nodes
graph.add_node("chat_node", chat_node)


# add edges
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

# Compile
chatbot = graph.compile(checkpointer=checkpointer)

