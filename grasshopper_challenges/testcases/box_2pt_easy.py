_tc = [
    (
        (0, 0, 0),
        (0, 0, 0),
    ),
    (
        (0, 0, 0),
        (1, 0, 0),
    ),
    (
        (0, 0, 0),
        (1, 1, 0),
    ),
    (
        (0, 0, 0),
        (1, 1, 1),
    ),
    (
        (1.3, 2.0, 33.2),
        (2.7, -3.3, 0.0),
    ),
]

from .helper.mapper import map_to_point3d_list

tc_a = map_to_point3d_list(list(zip(*_tc))[0])
tc_b = map_to_point3d_list(list(zip(*_tc))[1])
