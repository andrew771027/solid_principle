import pytest

# def test_app():
#     input_values = [2, 3]
#     output = []

#     def mock_input(s):
#         output.append(s)
#         return input_values.pop(0)
#     app.input = mock_input
#     app.print = lambda s : output.append(s)

#     app.main()

#     assert output == [
#         'First: ',
#         'Second: ',
#         'The result is 5',
#     ]


def test_violation_srp():
    # from src.solid.srp.violation.main import main
    # main()
    pass


def test_violation_ocp():
    from src.solid.srp.correspond.main import main
    pass
