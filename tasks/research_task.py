from pathlib import Path

from crewai import Task

from schemas.research import ResearchOutput


def create_research_task(
    agent,
    topic: str
) -> Task:

    prompt = Path(
        "prompts/research.md"
    ).read_text(encoding="utf-8")

    description = prompt.format(
        topic=topic
    )

    return Task(
        description=description,

        expected_output=(
            "Exactly five structured research insights."
        ),

        agent=agent,

        output_pydantic=ResearchOutput,

        markdown=True,
    )