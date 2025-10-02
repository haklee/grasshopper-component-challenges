# Closest Point

## Grasshopper

- Component Name:
    - `Closest Point`
- Input:
    - P: Point to search from.
    - C: List of points to search.
- Output:
    - P: Closest point from P in C.
    - i: Index of closest point in C.
    - D: Distance from closest point in C to P.

## Difficulty

### Easy

- [.ghx file](../../problems/closest_point_easy.ghx)
- conditions:
    - Let C_i denotes ith element of C, if i != j then `distance from P to C_i` != `distance from P to C_j`.
    - 1 <= Number of points in C <= 10
    - -100.0 < Coordinate x, y and z value of all points in C < 100.0
    - -100.0 < Coordinate x, y and z value of point P < 100.0
