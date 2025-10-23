from .helper.comparer import compare_list, compare_int
from .helper.messages import correct_answer, wrong_answer


def judge_s(a, b):
    return correct_answer() if compare_list(a, b) else wrong_answer()


def judge_n(a, b):
    return correct_answer() if compare_int(a, b) else wrong_answer()
