from pydantic import BaseModel, Field


class TopicExplanation(BaseModel):
    topic: str = Field(description="Name of the topic")

    definition: str = Field(
        description="Short definition of the topic"
    )

    key_points: list[str] = Field(
        min_length=3,
        max_length=3,
        description="Exactly three important points"
    )