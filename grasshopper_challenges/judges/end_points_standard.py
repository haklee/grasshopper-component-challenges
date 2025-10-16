from .helper.comparer import compare_point3d

_msg = "Wrong Answer"


def judge_s(a, b):
    return "Correct" if compare_point3d(a, b) else (_msg)


def judge_e(a, b):
    return "Correct" if compare_point3d(a, b) else (_msg)
