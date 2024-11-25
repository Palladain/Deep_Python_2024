from argparse import ArgumentParser

import uvicorn

from src.presentation.api.factory import create_app


def get_parser() -> ArgumentParser:
    """Получить CLI-интерфейс."""
    parser = ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--start-api", action="store_true")

    return parser


def main() -> None:
    """Запустить компоненту."""
    parser = get_parser()
    args = parser.parse_args()

    if args.start_api:
        app = create_app()
        uvicorn.run(app)


if __name__ == "__main__":
    main()
