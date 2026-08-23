import os

from crewai_tools import SerperDevTool


def build_research_tools():
    """
    Enable web research only when SERPER_API_KEY exists.
    """

    if not os.getenv("SERPER_API_KEY"):
        print("⚠ SERPER_API_KEY not configured.")
        print("  Research agent will work without live web search.")
        return []

    print("✓ SerperDevTool enabled.")

    return [
        SerperDevTool(
            search_type="search",
            n_results=5
        )
    ]