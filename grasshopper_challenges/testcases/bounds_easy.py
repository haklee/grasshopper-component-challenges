_tc = [
    [1, 2, 3, 4, 5],
    [2, 2.7, -3.666, 0.001, -2],
]

from .helper.mapper import map_to_float_list

tc = [map_to_float_list(_i) for _i in _tc]
