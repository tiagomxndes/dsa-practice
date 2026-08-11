"""
Nodes
Our nodes will be represented by a simple class with two fields:

    val - The raw string value that the node holds (e.g. 'Carla', 'James', etc)
    next - A reference to the next node in the list

Assignment
Let's lock-in and make LockedIn faster!

    Complete the Node's constructor.
        Set its val field to the provided value.
        Set its next field to None.
    Complete the Node's set_next method. It should set the next field to the provided node.

"""

from typing import Any


class Node:
    val: Any

    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None

    def set_next(self, node: "Node") -> None:
        self.next = node

    # don't touch below this line

    def __repr__(self) -> str:
        return self.val
