"""
Append: Appending an element to the end of a list, e.g. cars.append("ford") is (on average) O(1). We go directly to the end and add the element.
Index: Accessing an element by index, e.g. cars[2] is O(1). We go directly to the index and return the element.
Delete: Removing an element from the middle of a list, e.g. cars.pop(2) is O(n). We have to shift all the elements after the deleted element down one index.
Search: Searching for an element in a list, e.g. cars.index("ford") is O(n). We have to iterate over the list until we find the element.

Assignment

We need to display a user's last job title on their profile.

Implement the last_work_experience function. It takes a list of our user's work history (strings) and returns the last place they worked.

    Assume the list is ordered from oldest to most recent.
    If the list is empty, return None.

"""


def last_work_experience(work_experiences: list[str]) -> str | None:
    if not work_experiences:
        return None
    return work_experiences[-1]
