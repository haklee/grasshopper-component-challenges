from .helper.comparer import compare_float, compare_list

_msg = "Wrong Answer."


def judge_r(a, b):
    return "Correct" if compare_float(a, b) else (_msg)


def judge_pr(a, b):
    return "Correct" if compare_list(a, b) else (_msg)
