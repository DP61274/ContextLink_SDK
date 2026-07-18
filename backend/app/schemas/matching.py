"""Stable contract consumed by future matching and AI implementations."""

from pydantic import BaseModel, Field


class MatchingResult(BaseModel):
    """An explainable compatibility decision for two opted-in participants."""

    compatible: bool
    score: int = Field(ge=0, le=100)
    reasons: list[str]
    icebreaker: str | None = None
