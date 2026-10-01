"""Editor configuration practice.

Lesson: phases/00-setup-and-tooling/08-editor-setup/docs/en.md
Verifies formatting and a correctly typed function call.
Uses only the Python standard library.
"""

numbers = [1, 2, 3]
total = sum(numbers)
print(total)


def double(value: int) -> int:
    return value * 2


result = double(3)

print(result)
print(type(result))
