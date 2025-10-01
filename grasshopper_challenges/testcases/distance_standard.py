_tc = [
    (
        (0, 0, 0),
        (1, 0, 0),
    ),
    (
        (1.3, 2.0, 33.2),
        (2.7, -3.3, 0.0),
    ),
    (
        (0, 0, 0),
        (0, 0, 0),
    ),
    (
        (111111111111111, 111111111111111, 111111111111111),
        (2222222222222222, 2222222222222222, 2222222222222222),
    ),
]

from Rhino.Geometry import Point3d

tc_a = [Point3d(*_pt) for _pt in [map(float, [_j for _j in _i[0]]) for _i in _tc]]

tc_b = [Point3d(*_pt) for _pt in [map(float, [_j for _j in _i[1]]) for _i in _tc]]
