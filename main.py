import sys
from pathlib import Path

from config.settings import (
    OUTPUT_DIR,
    validate_config,
    print_config_status,
)

from orchestration.crew import build_crew

from gates.publish_gate import publish_gate

from schemas.article import ArticleDraft
from schemas.social import SocialDrafts


def save_outputs(result):

    OUTPUT_DIR.mkdir(exist_ok=True)

    # -------------------------
    # Research
    # -------------------------

    research_output = result.tasks_output[0]

    research_path = OUTPUT_DIR / "research_notes.md"

    research_path.write_text(
        research_output.raw,
        encoding="utf-8"
    )

    # -------------------------
    # Article
    # -------------------------

    article = next(
        (
            output.pydantic
            for output in result.tasks_output
            if isinstance(
                output.pydantic,
                ArticleDraft
            )
        ),
        None,
    )

    if not article:
        raise RuntimeError(
            "ArticleDraft was not produced."
        )

    article_text = (
        f"# {article.title}\n\n"
        f"## Summary\n\n"
        f"{article.summary}\n\n"
        f"{article.article_markdown}\n"
    )

    article_path = OUTPUT_DIR / "article.md"

    article_path.write_text(
        article_text,
        encoding="utf-8"
    )

    # -------------------------
    # Social
    # -------------------------

    social = next(
        (
            output.pydantic
            for output in result.tasks_output
            if isinstance(
                output.pydantic,
                SocialDrafts
            )
        ),
        None,
    )

    if not social:
        raise RuntimeError(
            "SocialDrafts was not produced."
        )

    social_text = (
        "# Social Drafts\n\n"
        "## LinkedIn\n\n"
        f"{social.linkedin_post}\n\n"
        "## X\n\n"
        f"{social.x_post}\n\n"
        "## Publishing Status\n\n"
        f"{social.publishing_status}\n"
    )

    social_path = OUTPUT_DIR / "social.md"

    social_path.write_text(
        social_text,
        encoding="utf-8"
    )

    return article, social


def main():

    validate_config()

    print_config_status()

    # -------------------------
    # Topic
    # -------------------------

    if len(sys.argv) < 2:

        topic = input(
            "\nEnter topic: "
        ).strip()

    else:

        topic = " ".join(
            sys.argv[1:]
        )

    if not topic:
        raise ValueError(
            "Topic cannot be empty."
        )

    print("\n")
    print("=" * 70)
    print("CREWAI AGENTIC CONTENT PIPELINE")
    print("=" * 70)

    print(f"\nTopic: {topic}")

    # -------------------------
    # Build Crew
    # -------------------------

    crew = build_crew(topic)

    # -------------------------
    # Kickoff
    # -------------------------

    print("\n🚀 Starting CrewAI workflow...\n")

    result = crew.kickoff()

    if not result:
        raise RuntimeError(
            "Crew returned no result."
        )

    if not result.tasks_output:
        raise RuntimeError(
            "Crew returned no task outputs."
        )

    # -------------------------
    # Save
    # -------------------------

    article, social = save_outputs(
        result
    )

    print("\n✓ Research saved.")
    print("✓ Article saved.")
    print("✓ Social drafts saved.")

    # -------------------------
    # Human Gate
    # -------------------------

    approved = publish_gate(
        article,
        social
    )

    if approved:

        print(
            "\n✓ Approved."
        )

        print(
            "Publishing is intentionally "
            "separate from the autonomous agents."
        )

        # If you later want publishing:
        #
        # publish_to_webhook(...)
        #
        # should happen HERE.

    else:

        print(
            "\n✗ Publish rejected."
        )

        print(
            "Nothing was published."
        )


if __name__ == "__main__":
    main()