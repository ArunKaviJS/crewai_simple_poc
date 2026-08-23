from crewai import Agent

from brain.llm import writer_llm


def create_content_agent() -> Agent:

    return Agent(

        role="Content Writer",

        goal=(
            "Transform validated research into "
            "a clear, accurate and useful article."
        ),

        backstory=(
            "You are an experienced technical content writer "
            "who turns complex research into clear narratives "
            "without inventing facts."
        ),

        allow_delegation=False,

        llm=writer_llm,

        verbose=True,

        max_iter=6,
    )