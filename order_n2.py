"""
Assignment
LockedIn needs search capabilities! For now, we'll build something slow (and frankly awful) so we can see an n^2 algorithm in practice.
Complete the does_name_exist function.

    For each first name in first_names:
        For each last name in last_names:
            If a first/last name combination (joined with a space) matches the full_name, it should return True.
    If the loop finishes, it should return False.

"""


def does_name_exist(
    first_names: list[str], last_names: list[str], full_name: str
) -> bool:
    for first_name in first_names:
        for last_name in last_names:
            complete_name = f"{first_name} {last_name}"

            if complete_name == full_name:
                return True
    return False
