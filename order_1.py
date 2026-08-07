"""
We need to be able to search our LockedIn user base more quickly! Our users are complaining that the search bar is painfully slow. The starter code searches every entry, which takes a very long time for large inputs.
The find_last_name function takes
    names_dict: a dictionary of first_name -> last_name.
    first_name: a string.

If first_name is a key in the dictionary, find_last_name returns the associated last name. If the key is not found, it returns None.
Write the function so that it runs quickly! It should be O(1).
"""

# Def provided:
# def find_last_name(names_dict: dict[str, str], first_name: str) -> str | None:
#    for current_first_name, last_name in names_dict.items():
#       if current_first_name == first_name:
#           return last_name


# My solution
def find_last_name(names_dict: dict[str, str], first_name: str) -> str | None:
    if first_name in names_dict.keys():
        return names_dict.get(first_name)
