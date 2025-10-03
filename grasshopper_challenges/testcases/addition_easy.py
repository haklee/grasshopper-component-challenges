_tc = [
    (1, 2),
    (1.3, 2.7),
    (1.333, -3.666),
    (111111111111111, 2222222222222222),
    (123456789123456789, -123456789123456788),
]

from .helper.mapper import map_to_float_list

tc_a = map_to_float_list(zip(*_tc)[0])
tc_b = map_to_float_list(zip(*_tc)[1])
