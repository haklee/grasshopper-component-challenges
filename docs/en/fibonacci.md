# Fibonacci

## Grasshopper

- Component Name:
    - `Fibonacci`
- Input:
    - A (`float`): First seed number for fibonacci sequence.
    - B (`float`): Second seed number for fibonacci sequence.
    - N (`int`): Number of values in the sequence.
- Output:
    - S (`List[float]`):
        - If N > 0, then first N + 2 values of fibonacci sequnce generated with seed A and B. The sequence starts with [A, B].
        - If N <= 0, then empty list.

## Difficulty

### Easy

- [.ghx file](../../problems/fibonacci_easy.ghx)
- conditions:
    - 1 <= N <= 20
