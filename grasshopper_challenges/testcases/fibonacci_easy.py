_tc = [
    (1, 1, 1),
    (1.3, 2.7, 2),
    (1.333, -3.666, 3),
    (2222, 2222, 10),
    (2, 3, 20),
]

from .helper.mapper import map_to_float_list, map_to_int_list

tc_a = map_to_float_list(list(zip(*_tc))[0])
tc_b = map_to_float_list(list(zip(*_tc))[1])
tc_n = map_to_int_list(list(zip(*_tc))[2])
