import argparse
import typing
from typing import ClassVar, Optional, List, Type
from pydantic import BaseModel, ConfigDict

_ApiType = typing.Literal["openai", "gemini"]


class Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(
        extra="ignore",
    )

    version: Optional[str] = None

    api_type: Optional[_ApiType] = None
    api_version: Optional[str] = None

    # internal, set by subparsers to parse their specific args
    args_model: Optional[Type[BaseModel]] = None

    # internal, used so that subparsers can forward unknown arguments
    unknown_args: List[str] = []
    allow_unknown_args: bool = False


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=None, prog="llm")
    parser.add_argument("-k", "--api-key", help="What API key to use.")
    parser.add_argument(
        "-t",
        "--api-type",
        type=str,
        choices=("openai", "gemini"),
        help="The backend API to call, must be `openai` or `gemini`",
    )

    def help() -> None:
        parser.print_help()

    parser.set_defaults(func=help)
    return parser

