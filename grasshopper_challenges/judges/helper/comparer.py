"""Compare two values"""

# Compare python native type values
# region Native


def compare_bool(a, b):
    """Compare two bool values"""
    return a == b


def compare_float(a, b):
    """Compare two float values"""
    return a == b


def compare_float(a, b):
    """Compare two float values"""
    return a == b


def compare_int(a, b):
    """Compare two int values"""
    return a == b


def compare_string(a, b):
    """Compare two string values"""
    return a == b


# endregion Native


# Compare Rhino.Geometry type values
# region Rhino.Geometry
def compare_point3d(a, b):
    """Compare two Point3d values"""
    return a.CompareTo(b) == 0


def compare_vector3d(a, b):
    """Compare two Vector3d values"""
    return a.CompareTo(b) == 0


def compare_box(a, b):
    """Compare two Box values"""
    # Operator == is not documented in RhinoCommon API page, but it seems to work.
    # ref: https://developer.rhino3d.com/api/rhinocommon/rhino.geometry.box
    return a == b


def compare_interval(a, b):
    """Compare two Interval values"""
    return a.CompareTo(b) == 0


# endregion Rhino.Geometry


# Compare iterables
# region Iterable
def compare_list(a, b):
    """Compare two lists"""
    return len(a) == len(b) and all(i == j for i, j in zip(a, b))


def compare_tuple(a, b):
    """Compare two tuples"""
    return a == b


def compare_dictionary(a, b):
    """Compare two dictionaries"""
    return a == b


def compare_set(a, b):
    """Compare two sets"""
    return a == b


# endregion Iterable
