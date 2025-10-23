from .helper.comparer import compare_bool
from .helper.messages import correct_answer, wrong_answer


def judge_gt(a, b):
    return correct_answer() if compare_bool(a, b) else wrong_answer()


def judge_ge(a, b):
    return correct_answer() if compare_bool(a, b) else wrong_answer()
