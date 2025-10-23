from .helper.comparer import compare_interval
from .helper.messages import correct_answer, wrong_answer


def judge(a, b):
    return correct_answer() if compare_interval(a, b) else wrong_answer()
