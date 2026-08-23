from crewai import Agent

from brain.llm import research_llm
from tools.research_tools import build_research_tools


def create_research_agent() -> Agent:

    tools = build_research_tools()

    return Agent(
        role="Research Analyst",

        goal=(
            "Autonomously investigate the topic, "
            "evaluate evidence, and produce exactly "
            "five high-value research insights."
        ),

        backstory=(
            "You are a rigorous research analyst. "
            "You plan investigations before searching, "
            "evaluate evidence quality, and distinguish "
            "facts from assumptions."
        ),

        tools=tools,

        allow_delegation=False,

        llm=research_llm,

        verbose=True,

        max_iter=10,

        inject_date=True,
    )