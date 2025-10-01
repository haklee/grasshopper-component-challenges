_tc = [
    (1, 0, 0),
    (1000000000000000000, 0, 0),
    (0.00000000000000001, 0, 0),
    (0, 0, 0),
    (1, 2, 3),
    (-1, 2, 3000000000000000000),
]

from Rhino.Geometry import Vector3d

tc = [Vector3d(*_v) for _v in [map(float, _i) for _i in _tc]]
