_tc = [
    ([1, 2, 3, 4, 5], True),
    ([1, 1, 1, 1, 1], False),
    ([1, 2, 2, 2, 3, 3, 2, 1], False),
    ([1, 2, 2, 2, 3, 3, 2, 1, 1, 1], True),
]

from .helper.mapper import map_to_int_list, map_to_bool_list

tc_s = [map_to_int_list(_i) for _i in list(zip(*_tc))[0]]
tc_w = map_to_bool_list(list(zip(*_tc))[1])
