from .helper.comparer import compare_list

_msg = "Wrong answer."


def judge(a, b):
    return "Correct" if compare_list(a, b) else _msg
