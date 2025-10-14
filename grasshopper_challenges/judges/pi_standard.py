from .helper.comparer import compare_float

_msg = "Wrong Answer."


def judge(a, b):
    return "Correct" if compare_float(a, b) else _msg
