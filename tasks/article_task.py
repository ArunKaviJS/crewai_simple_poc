from pathlib import Path

from crewai import Task

from schemas.article import ArticleDraft


def create_article_task(
    agent,
    topic: str,
    research_task: Task
) -> Task:

    prompt = Path(
        "prompts/content_writer.md"
    ).read_text(encoding="utf-8")

    description = prompt.format(
        topic=topic,
        research_context=(
            "The research output from the previous task "
            "will be available through CrewAI task context."
        ),
    )

    return Task(
        description=description,

        expected_output=(
            "A structured ArticleDraft containing "
            "title, summary and article_markdown."
        ),

        agent=agent,

        context=[research_task],

        output_pydantic=ArticleDraft,

        markdown=True,
    )