import click

from utils import reddit_stuff


@click.command()
def main():
    # Get top 3 comments from reddit pinned post
    top_three_comments = reddit_stuff.get_top_pinned_post_comments('crowdcast')
    print(top_three_comments)

    # For each, generate a section script

    # Given section scripts, generate Summary and Outro

    # Use elevenlabs to generate the MP3

    # Upload the podcast to buzzsprout


if __name__ == '__main__':
    main()
