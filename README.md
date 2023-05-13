<p align="center">
    <a href="https://www.reddit.com/r/crowdcast" style="margin: 0px 10px; text-decoration: none;">
        <img src="images/crowdcast_banner.png">
    </a>
</p>

<div align="center">
  <div style="display: flex; justify-content: center;">
    <a href="https://open.spotify.com/show/58g6mlJPaEObyZ3xMqgWdh" style="margin: 0px 10px; text-decoration: none;">
      <img src="images/badge_spotify.png" style="width: 200px; height: 49px;">
    </a>
    <a href="https://podcasts.apple.com/us/podcast/crowdcast/id1687775887" style="margin: 0px 10px; text-decoration: none;">
      <img src="images/badge_apple.svg" style="width: 200px; height: 49px;">
    </a>
    <a href="https://player.fm/series/crowdcast" style="margin: 0px 10px; text-decoration: none;">
      <img src="images/badge_playerfm.png" style="width: 200px; height: 49px;">
    </a>
  </div>
  </a>
</div>

<div align="center">
  <div style="display: flex; justify-content: center;">
    <a href="http://reddit.com/r/crowdcast" style="margin: 0px 10px; text-decoration: none;">
      <img src="images/reddit-1.svg" style="width: 200px; height: 49px;">
    </a>
  </div>
  </a>
</div>

The code behind [https://www.reddit.com/r/crowdcast/](https://www.reddit.com/r/crowdcast/), the worlds first open-source, crowd-sourced, AI assisted weekly podcast.

Podcast hosted on Buzzsprout - [Click here to listen on 16 platforms](https://www.buzzsprout.com/2188164/share)!

<hr />

## How to Install & Run

### Stuff you need

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

### Install

```commandline
pip install -r requirements.txt
```

### Generate a Podcast

```commandline
python main.py
```