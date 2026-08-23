from pydantic import BaseModel, Field


class SocialDrafts(BaseModel):
    linkedin_post: str = Field(
        ...,
        description=(
            "LinkedIn post with useful paragraphs and "
            "3-5 relevant hashtags."
        )
    )

    x_post: str = Field(
        ...,
        max_length=280,
        description="X/Twitter post of no more than 280 characters."
    )

    publishing_status: str = Field(
        ...,
        description=(
            'Must exactly equal '
            '"Draft only — not published."'
        )
    )