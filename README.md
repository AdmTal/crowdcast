# Crowdcast

The code behind [https://www.reddit.com/r/crowdcast/](https://www.reddit.com/r/crowdcast/), the worlds first open-source, crowd-sourced, AI assisted weekly podcast.

[Listen to the Podcast here](https://www.buzzsprout.com/2188164/share).

## Stuff you need

This podcast is generated using a few 3rd party services.

You'll need the following API keys saved as environment variables:

* [Reddit](https://reddit.com/)
    * `REDDIT_CLIENT_ID`
    * `REDDIT_CLIENT_SECRET`
    * `REDDIT_USER_AGENT`
    * `REDDIT_USERNAME`
    * `REDDIT_PASSWORD`
* [Eleven Labs](https://elevenlabs.io/)
    * `ELEVEN_LABS_API_KEY`
* [Open AI](https://openai.com/)
    * `OPENAI_API_ORG`
    * `OPENAI_API_KEY`
* [Buzzsprout](https://buzzsprout.com/)
    * `BUZZSPROUT_API_KEY`

## Install

```commandline
pip install -r requirements.txt
```

## Generate Podcast

```commandline
python main.py
```