from .helper.comparer import compare_interval

_msg = "Wrong Answer."


def judge(a, b):
    return "Correct" if compare_interval(a, b) else (_msg)
