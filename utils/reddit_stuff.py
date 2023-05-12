from utils.os import get_env_var_or_fail
import praw

client_id = get_env_var_or_fail('REDDIT_CLIENT_ID')
client_secret = get_env_var_or_fail('REDDIT_CLIENT_SECRET')
user_agent = get_env_var_or_fail('REDDIT_USER_AGENT')
username = get_env_var_or_fail('REDDIT_USERNAME')
password = get_env_var_or_fail('REDDIT_PASSWORD')


def get_pinned_post_comments(subreddit_name, pinned_post_number, comment_limit):
    subreddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=username,
        password=password,
    ).subreddit(subreddit_name)

    top_comments = []
    stickied_counter = 0

    for submission in subreddit.hot(limit=10):
        if submission.stickied:
            stickied_counter += 1

            if stickied_counter == pinned_post_number:
                # Get the top comments
                submission.comment_sort = "top"
                submission.comments.replace_more(limit=comment_limit)

                # Append the top comments
                for comment in submission.comments[:comment_limit]:
                    top_comments.append((
                        comment.author.name,
                        comment.body
                    ))

                break

    return top_comments

