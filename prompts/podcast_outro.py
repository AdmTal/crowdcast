SYSTEM_PROMPT = """
You are an AI scriptwriter for a solo-hosted podcast. Your content creation should mirror the quality and engagement level of popular, top-tier podcasts.

Ensure the language and tonality employed aligns with what is deemed suitable for a middle-school audience.

Abstain from any form of profanity or language that could be considered sensitive, taboo, or potentially emotionally triggering. Stick to language that would be acceptable in a middle-school setting or opt for more neutral vocabulary if necessary.

Take liberties with the script, you can deviate from this script as long as you maintain the intended tone.

Write in straightforward text, not in script format.
"""

PROMPT = """
Write a podcast outro for a podcast called "Crowd Cast" -- which is the worlds first Open-source Crowd Sourced, AI assisted Podcast, Automatically generated weekly based on the top three comments on the crowdcast sub-reddit.  Two ads have also been submitted, so give attribution to the ad submitters as well.  Thank them because they are the sponsors, and they make this all possible.

The basic gist should be like "That's it for today, thanks for listening!"

And then go over some show notes.

Thank the user's who contributed this weeks topics:

For each topic, thank the user like "We want to thank NAME who suggested that we cover YYY this week"

And then list them all, and aim for a natural, informal tone.

You can mention that the code that runs this podcast is available open source on GitHub, and also contains the transcript from today's episode.

End the outro with some sort of - "Be sure to check out the Crowdcast subreddit for more info, and to submit your own ideas and vote on others, and see you next time on Crowdcast!"

On today's podcast the segments were:

SEGMENT_1:
SUBMITTED_BY: {user_1}
{segment_1}

SEGMENT_2:
SUBMITTED_BY: {user_2}
{segment_2}

SEGMENT_3:
SUBMITTED_BY: {user_3}
{segment_3}

AD_1:
SUBMITTED_BY: {user_4}
{ad_1}

AD_2:
SUBMITTED_BY: {user_5}
{ad_2}

"""
