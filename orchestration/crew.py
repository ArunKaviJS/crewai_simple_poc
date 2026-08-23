from crewai import Crew, Process

from agents.research_agent import create_research_agent
from agents.content_agent import create_content_agent
from agents.social_agent import create_social_agent

from tasks.research_task import create_research_task
from tasks.article_task import create_article_task
from tasks.social_task import create_social_task


def build_crew(topic: str):

    # -------------------------
    # Agents
    # -------------------------

    researcher = create_research_agent()

    writer = create_content_agent()

    social_editor = create_social_agent()

    # -------------------------
    # Tasks
    # -------------------------

    research_task = create_research_task(
        researcher,
        topic
    )

    article_task = create_article_task(
        writer,
        topic,
        research_task
    )

    social_task = create_social_task(
        social_editor,
        article_task
    )

    # -------------------------
    # Crew
    # -------------------------

    crew = Crew(

        agents=[
            researcher,
            writer,
            social_editor,
        ],

        tasks=[
            research_task,
            article_task,
            social_task,
        ],

        process=Process.sequential,

        verbose=True,
    )

    return crew