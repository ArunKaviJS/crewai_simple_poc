from typing import List

from pydantic import BaseModel, Field


class ResearchInsight(BaseModel):
    insight: str = Field(
        ...,
        description="The core researched insight."
    )

    explanation: str = Field(
        ...,
        description="Concise explanation of why the insight matters."
    )

    evidence: str = Field(
        ...,
        description="Evidence supporting the insight."
    )

    source: str = Field(
        ...,
        description="Institution, publication, or source supporting the claim."
    )


class ResearchOutput(BaseModel):
    topic: str

    insights: List[ResearchInsight] = Field(
        ...,
        min_length=5,
        max_length=5,
        description="Exactly five research-backed insights."
    )