from .helper.comparer import compare_vector3d

_msg = "Wrong: vector {} is not equal to {}."


def judge(a, b):
    return "Correct" if compare_vector3d(a, b) else (_msg.format(a, b))
