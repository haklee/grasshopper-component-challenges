from .helper.comparer import compare_list
from .helper.messages import correct_answer, wrong_answer


def judge(a, b):
    return correct_answer() if compare_list(a, b) else wrong_answer()
