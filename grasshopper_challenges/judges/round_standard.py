from .helper.comparer import compare_int
from .helper.messages import correct_answer, wrong_answer


def judge_n(a, b):
    return correct_answer() if compare_int(a, b) else wrong_answer()


def judge_f(a, b):
    return correct_answer() if compare_int(a, b) else wrong_answer()


def judge_c(a, b):
    return correct_answer() if compare_int(a, b) else wrong_answer()
