"""
Assignment
Influencers need to be able to schedule posts to be published in the future. We've found that the order in which the posts are published drastically affects their performance.
Complete the num_possible_orders function. It takes the number of posts an influencer has in their backlog as input and returns the total number of possible orders in which we could publish the posts.
"""


def num_possible_orders(num_posts: int) -> int:

    product = 1
    for post in range(1, num_posts + 1):
        product *= post
    return product


print(num_possible_orders(3))
print(num_possible_orders(34))
