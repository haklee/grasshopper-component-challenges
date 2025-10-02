from .helper.comparer import compare_point3d, compare_int, compare_float

_msg = "Wrong Answer"


def judge_p(a, b):
    return "Correct" if compare_point3d(a, b) else (_msg)


def judge_i(a, b):
    return "Correct" if compare_int(a, b) else (_msg)


def judge_d(a, b):
    return "Correct" if compare_float(a, b) else (_msg)
