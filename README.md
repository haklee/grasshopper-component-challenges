# Grasshopper Component Challenges

A collection of coding challenges for Grasshopper components.

## Installation

WIP

## Usage

Access to test cases like,

```python
# Access test cases
from grasshopper_challenges.testcases import addition_easy

print(addition_easy.tc_a)  # Test case inputs A
print(addition_easy.tc_b)  # Test case inputs B
```

Or, access to judges like,

```python
# Use judges
from grasshopper_challenges.judges import addition_easy
result = addition_easy.judge(1, 2)  # Example usage
print(result)
```

## Package Structure

```md
# Package structure (installed):
grasshopper_challenges/
├── __init__.py
├── testcases/          # Test case data
└── judges/             # Judge functions

# Development repository structure:
├── grasshopper_challenges/  # Main package
├── docs/                   # Documentation (dev only)
├── setup.py               # Package configuration
├── pyproject.toml         # Modern packaging config
└── README.md              # This file
```
