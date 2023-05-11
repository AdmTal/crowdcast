from utils.os import get_env_var_or_fail
import praw

client_id = get_env_var_or_fail('REDDIT_CLIENT_ID')
client_secret = get_env_var_or_fail('REDDIT_CLIENT_SECRET')
user_agent = get_env_var_or_fail('REDDIT_USER_AGENT')
username = get_env_var_or_fail('REDDIT_USERNAME')
password = get_env_var_or_fail('REDDIT_PASSWORD')


def get_top_pinned_post_comments(subreddit_name):
    subreddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=username,
        password=password,
    ).subreddit(subreddit_name)

    top_comments = []

    for submission in subreddit.hot(limit=10):
        if submission.stickied:
            # Get the top comments
            submission.comment_sort = "top"
            submission.comments.replace_more(limit=3)

            # Print the top comments
            for comment in submission.comments[:3]:
                top_comments.append(comment.body)

            break

    return top_comments
