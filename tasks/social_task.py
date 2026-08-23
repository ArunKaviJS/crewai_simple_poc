from pathlib import Path

from crewai import Task

from schemas.social import SocialDrafts


def create_social_task(
    agent,
    article_task: Task
) -> Task:

    prompt = Path(
        "prompts/social_editor.md"
    ).read_text(encoding="utf-8")

    description = prompt.format(
        article_context=(
            "The completed article from the previous "
            "task will be available through CrewAI context."
        )
    )

    return Task(
        description=description,

        expected_output=(
            "Structured LinkedIn and X drafts "
            "with draft-only publishing status."
        ),

        agent=agent,

        context=[article_task],

        output_pydantic=SocialDrafts,

        markdown=True,
    )