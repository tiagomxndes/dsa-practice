"""
Complete the get_follower_prediction function. It takes a follower_count integer, an influencer_type string and a num_months integer, and returns an integer.

Calculate the number of followers an influencer will have after a given number of months according to the influencer type:

    "fitness": follower count quadruples each month
    "cosmetic": follower count triples each month
    other: follower count doubles each month

For example, if a "fitness" influencer starts with 10 followers, then after 1 month they would have 40 followers. After 2 months, they would have 160 followers, and so on.
"""


def get_follower_prediction(
    follower_count: int, influencer_type: str, num_months: int
) -> int:

    if influencer_type == "fitness":
        return follower_count * 4**num_months
    elif influencer_type == "cosmetic":
        return follower_count * 3**num_months
    else:
        return follower_count * 2**num_months


print(
    get_follower_prediction(follower_count=2, influencer_type="fitness", num_months=4)
)
print(
    get_follower_prediction(follower_count=4, influencer_type="cosmetic", num_months=5)
)
print(get_follower_prediction(follower_count=5, influencer_type="tech", num_months=9))
