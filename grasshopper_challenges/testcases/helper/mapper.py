"""Map values to target type"""

from Rhino.Geometry import Point3d, Vector3d


def map_to_float_list(a):
    """Map list of values to float"""
    return list(map(float, a))


def map_to_int_list(a):
    """Map list of values to int"""
    return list(map(int, a))


def map_to_point3d(a):
    """Map list of values to Point3d"""
    return Point3d(*a)


def map_to_point3d_list(a):
    """Map list of values to list of Point3d"""
    return [Point3d(*_i) for _i in a]


def map_to_vector3d(a):
    """Map list of values to Vector3d"""
    return Vector3d(*a)


def map_to_vector3d_list(a):
    """Map list of values to list of Vector3d"""
    return [Vector3d(*_i) for _i in a]
