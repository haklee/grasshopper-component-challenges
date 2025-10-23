from .helper.comparer import compare_point3d, compare_int, compare_float
from .helper.messages import correct_answer, wrong_answer


def judge_p(a, b):
    return correct_answer() if compare_point3d(a, b) else wrong_answer()


def judge_i(a, b):
    return correct_answer() if compare_int(a, b) else wrong_answer()


def judge_d(a, b):
    return correct_answer() if compare_float(a, b) else wrong_answer()
