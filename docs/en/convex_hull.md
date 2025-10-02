# Convex Hull

## Grasshopper

- Component Name:
    - `Convex Hull`
- Input:
    - P (`List[Point3d]`): List of points to create convex hull.
    - Pl (`Optional[Plane]`): Optional base plane. If base plane is not provided, best-fit plane will be calculated and used.
- Output:
    - H (`Polyline`): Convex hull in base plane space.
    - Hz (`Polyline`): Convex hull in world space, which means, closed polyline created by connecting original points in `P` in order of `I`.
    - I (`List[int]`): List of indices of points in convex hull `H`.

## Difficulty

### Easy

- [.ghx file](../../problems/convex_hull_easy.ghx)
- conditions:
    - All points in `P` are on XY plane, which means, coordinate z value of all points in `P` is 0.
    - Base plane is not given, which means, base plane is XY plane.
    - 3 <= Number of points in `P` <= 10
    - -100.0 <= Coordinate x, y and z value of all points in `P` <= 100.0
