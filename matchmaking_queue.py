"""
Assignment
Complete the matchmake function that simulates users joining and leaving the matchmaking queue. The function should take a queue instance and a user tuple containing a name and action (either "join" or "leave"):

user = ("Bob", "join")
user = ("Alice", "leave")

For each call to matchmake:

    If the action is "leave", search the queue for the user and remove them if they are in the queue.
    If the action is "join", push the user's name onto the queue.
    Lastly, check if the queue has at least 4 users in it. If so, pop the first 2 users from the queue and return the following string:

"{user1} matched {user2}!"

Where user1 is the first user popped and user2 is the second user popped.
    If there were less than 4 users in the queue, return the following string: "No match found"

"""

from queue import Queue


def matchmake(queue: Queue, user: tuple[str, str]) -> str:
    action = user[1]
    user_name = user[0]

    if action == "leave":
        queue.search_and_remove(user_name)
    elif action == "join":
        queue.push(user_name)

    if queue.size() >= 4:
        first_user = queue.pop()
        second_user = queue.pop()
        return f"{first_user} matched {second_user}!"
    return "No match found"
