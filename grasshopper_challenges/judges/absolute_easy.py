from .helper.comparer import compare_float

_msg = "Wrong: Absolute value of {} is not equal to {}."


def judge(a, b):
    return "Correct" if compare_float(a, b) else (_msg.format(a, b))
