# Replace Members

## Grasshopper

- Component Name:
    - `Replace Members`
- Input:
    - S (`List[T]`): List to process.
    - F (`List[T]`): Item(s) to replace.
    - R (`List[T]`): Item(s) to replace with.
- Output:
    - R (`List[T]`): List with replaced members.

## Difficulty

### Easy

- [.ghx file](../../problems/replace_members_easy.ghx)
- conditions:
    - Length of input list `S` is less than 20.
    - Only one item is given to replace. Length of input list `F` is 1.
    - Only one item is given to replace with. Length of input list `R` is 1.
    - Type of the items in list `S`, `F`, `R` is integer.
