import pytest


def test_violation():
    from src.solid.lsp.violation.main import main
    main()


def test_correspond():
    from src.solid.lsp.correspond.main import main
    main()
