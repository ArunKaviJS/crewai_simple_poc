from pydantic import BaseModel, Field


class ArticleDraft(BaseModel):
    title: str = Field(
        ...,
        description="Concise and compelling article title."
    )

    summary: str = Field(
        ...,
        description="Two or three sentence summary."
    )

    article_markdown: str = Field(
        ...,
        description=(
            "Complete article body in Markdown. "
            "Must contain introduction, sections and conclusion. "
            "Do not use code fences."
        )
    )