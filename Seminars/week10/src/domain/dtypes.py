from typing import Annotated

from pydantic import Field

from src.domain.constants import (
    NAME_MAX_LENGTH,
    NAME_MIN_LENGTH,
    NAME_REGEX,
    SURNAME_MAX_LENGTH,
    SURNAME_MIN_LENGTH,
    SURNAME_REGEX,
)

Name = Annotated[str, Field(
    pattern=NAME_REGEX,
    min_length=NAME_MIN_LENGTH,
    max_length=NAME_MAX_LENGTH,
    examples=["Тимур"],
)]

Surname = Annotated[str, Field(
    pattern=SURNAME_REGEX,
    min_length=SURNAME_MIN_LENGTH,
    max_length=SURNAME_MAX_LENGTH,
    examples=["Петров"],
)]
