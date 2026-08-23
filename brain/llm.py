from crewai import LLM

from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
)


def create_llm(temperature: float = 0.2) -> LLM:
    """
    Create the Azure OpenAI LLM used by CrewAI.

    Temperature is intentionally configurable because different
    agents have different reasoning/creativity requirements.
    """

    return LLM(
       model="azure/gpt-4o",
           api_key=AZURE_OPENAI_API_KEY,
           endpoint=f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_DEPLOYMENT}",
           api_version=AZURE_OPENAI_API_VERSION,
        temperature=temperature,
    )


# Research should be deterministic.
research_llm = create_llm(temperature=0.1)

# Writing needs slightly more creativity.
writer_llm = create_llm(temperature=0.5)

# Social adaptation can be more creative.
social_llm = create_llm(temperature=0.6)