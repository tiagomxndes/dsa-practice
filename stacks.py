"""
In this chapter we'll build a stack from scratch! A stack will be useful at LockedIn when we need undo/redo functionality. For example, a user can add other users to their "connections" list, and then undo the last connection they added. Stacks are a great way to implement undo functionality.

For now, we'll just focus on two methods: push and size. Notice that the Stack class already has a constructor and the underlying List that we'll use to store items.

    Complete the push method. It should add an item to the top of the stack. The "top" of the stack is the end of the list in our implementation.
    Complete the size method. It should return the number of items in the stack.

"""

"""
Assignment

    Complete the peek method. It should return the top item from the stack without modifying the stack. If the stack is empty, return None.
    Complete the pop method. It should remove and return the top item from the stack. If the stack is empty, return None.

"""
from typing import Any


class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> Any:
        if not self.items:
            return None
        return self.items[-1]

    def pop(self) -> Any:
        if not self.items:
            return None

        last = self.items.pop(-1)
        return last


"""
Balanced Parentheses
Parentheses are balanced when each parenthesis has a corresponding parenthesis, and the pairs of parentheses are properly nested. For example:

    ()
    ()()
    ((()))
    (()(()))

Unbalanced Parentheses

    (
    ())
    (()()
    (()))
    )(

As you scan the string, consider what each item on the stack should represent.
Assignment
Complete the is_balanced function.
It takes a string as input and returns True if the parentheses in the string are balanced, and False otherwise. Use an instance of the provided Stack class in stack.py to keep track of the parentheses.
"""


def is_balanced(input_str: str) -> bool:
    stack = Stack()
    for paranthese in input_str:
        if paranthese == "(":
            stack.push(paranthese)
        elif paranthese == ")" and not stack.size():
            return False
        elif paranthese == ")" and stack.size():
            stack.pop()
    return stack.size() == 0
