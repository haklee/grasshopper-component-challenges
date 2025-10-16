from .helper.comparer import compare_list

_msg = "Wrong Answer."


def judge(a, b):
    return "Correct" if compare_list(a, b) else _msg
