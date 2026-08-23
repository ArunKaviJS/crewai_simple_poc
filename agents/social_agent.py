from crewai import Agent

from brain.llm import social_llm


def create_social_agent() -> Agent:

    return Agent(

        role="Social Media Editor",

        goal=(
            "Adapt the final article into platform-specific "
            "LinkedIn and X drafts while preserving factual accuracy."
        ),

        backstory=(
            "You specialize in distribution. "
            "You understand that LinkedIn and X require "
            "different levels of context and writing style."
        ),

        allow_delegation=False,

        llm=social_llm,

        verbose=True,

        max_iter=6,
    )