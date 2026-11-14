"""ASHENVEIL game entry point.

Run from the repository root with: python main.py
"""
from engine.core.app import AshenveilApp


def main() -> None:
    app = AshenveilApp()
    app.run()


if __name__ == "__main__":
    main()
