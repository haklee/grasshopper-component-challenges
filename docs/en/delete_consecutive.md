# Delete Consecutive

## Grasshopper

- Component Name:
    - `Delete Consecutive`
- Input:
    - S (`List[Any]`): List to process.
    - W:(`bool`) Wrap list(if true, first and last items are considered to be next to each other.).
- Output:
    - S (`List[Any]`): New list with consecutive same items removed.
    - N (`int`): Number of removed Items.

## Difficulty

### Standard

- [.ghx file](../../problems/delete_consecutive_standard.ghx)
- conditions:
    - Input list is not empty.
    - All the items in the list are `int` type.
