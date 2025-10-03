_tc = [
    [1, 2, 3],
    [2, 2.7, -3.666],
]

from .helper.mapper import map_to_float

tc = [map_to_float(_i) for _i in _tc]
