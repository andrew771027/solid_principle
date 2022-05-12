import pytest


def test_violation_ocp():
    from src.solid.ocp.violation.main import main
    main()


def test_correspond_ocp():
    from src.solid.ocp.correspond.main import main
    main()
