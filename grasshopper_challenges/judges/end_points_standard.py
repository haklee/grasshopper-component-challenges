from .helper.comparer import compare_point3d
from .helper.messages import correct_answer, wrong_answer


def judge_s(a, b):
    return correct_answer() if compare_point3d(a, b) else wrong_answer()


def judge_e(a, b):
    return correct_answer() if compare_point3d(a, b) else wrong_answer()
