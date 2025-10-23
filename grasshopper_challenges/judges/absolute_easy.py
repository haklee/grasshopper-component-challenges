from .helper.comparer import compare_float
from .helper.messages import correct_answer, wrong_answer


def judge(a, b):
    return correct_answer() if compare_float(a, b) else wrong_answer()
