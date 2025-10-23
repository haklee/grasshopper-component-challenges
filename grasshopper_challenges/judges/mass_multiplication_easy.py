from .helper.comparer import compare_float, compare_list
from .helper.messages import correct_answer, wrong_answer


def judge_r(a, b):
    return correct_answer() if compare_float(a, b) else wrong_answer()


def judge_pr(a, b):
    return correct_answer() if compare_list(a, b) else wrong_answer()
