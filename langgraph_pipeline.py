from langgraph.graph import StateGraph
from typing import TypedDict
from agents.drafting_agent import drafting_agent
from agents.compliance_agent import compliance_agent
from agents.localization_agent import localization_agent
from publishing.linkedin_simulator import publish_to_linkedin

class State(TypedDict):
    idea: str
    draft: str
    compliance: str
    localized: str
    language: str
    content_type: str
    publish_result: dict

def draft_node(state):
    return {"draft": drafting_agent(state["idea"], state["content_type"])}

def compliance_node(state):
    return {"compliance": compliance_agent(state["draft"])}

def localization_node(state):
    return {"localized": localization_agent(state["draft"], state["language"])}

def publish_node(state):
    return {"publish_result": publish_to_linkedin(state["localized"])}

def route(state):
    if "FAIL" in state["compliance"]:
        return "__end__"
    return "localize"

builder = StateGraph(State)
builder.add_node("draft", draft_node)
builder.add_node("compliance", compliance_node)
builder.add_node("localize", localization_node)
builder.add_node("publish", publish_node)

builder.set_entry_point("draft")
builder.add_edge("draft", "compliance")
builder.add_conditional_edges("compliance", route, {"localize": "localize", "__end__": "__end__"})
builder.add_edge("localize", "publish")
builder.add_edge("publish", "__end__")

graph = builder.compile()

def run_langgraph(idea, language, content_type):
    return graph.invoke({
        "idea": idea,
        "language": language,
        "content_type": content_type
    })
