_tc = [
    ([1, 2, 3, 4, 5], [1], [10]),
    ([1, 2, 3, 4, 5], [6], [10]),
    ([1, 2, 3, 4, 5, 1, 1, 2, 2, 3], [1], [10]),
    ([1, 2, 3, 4, 5, 1, 1, 2, 2, 3], [1], [1]),
]

from .helper.mapper import map_to_int_list

tc_s = [map_to_int_list(_i) for _i in list(zip(*_tc))[0]]
tc_f = [map_to_int_list(_i) for _i in list(zip(*_tc))[1]]
tc_r = [map_to_int_list(_i) for _i in list(zip(*_tc))[2]]
