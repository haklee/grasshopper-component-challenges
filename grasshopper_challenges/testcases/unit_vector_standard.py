_tc = [
    (1, 0, 0),
    (1000000000000000000, 0, 0),
    (0.00000000000000001, 0, 0),
    (0, 0, 0),
    (1, 2, 3),
    (-1, 2, 3000000000000000000),
]

from .helper.mapper import map_to_vector3d_list

tc = map_to_vector3d_list(_tc)
