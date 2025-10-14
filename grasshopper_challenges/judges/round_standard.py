from .helper.comparer import compare_int

_msg = "Wrong Answer."


def judge_n(a, b):
    return "Correct" if compare_int(a, b) else _msg


def judge_f(a, b):
    return "Correct" if compare_int(a, b) else _msg


def judge_c(a, b):
    return "Correct" if compare_int(a, b) else _msg
