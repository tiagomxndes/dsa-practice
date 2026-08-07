"""
Assignment
LockedIn needs a new tool that allows big brands to see how many of an influencer's followers are loyal to their brand. Complete the get_avg_brand_followers function. It takes two inputs:
    all_handles: a 2-dimensional list, or "list of lists" of strings representing user handles on a per-influencer basis.
    brand_name: a string.
get_avg_brand_followers returns the average number of handles that contain the brand_name across all the lists. Each list represents the audience of a single influencer.
"""


def get_avg_brand_followers(all_handles: list[list[str]], brand_name: str) -> float:
    total_brand_followers = 0

    for handle in all_handles:
        influencer_brand_followers = 0

        for follower in handle:
            if brand_name in follower:
                influencer_brand_followers += 1

        total_brand_followers += influencer_brand_followers

    return total_brand_followers / len(all_handles)
