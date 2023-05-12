import logging
import datetime
import uuid

from pydub import AudioSegment
from prompts import (
    podcast_segment,
    podcast_ads,
    podcast_intro,
    podcast_outro,
    podcast_segue,
)
from utils import (
    reddit_stuff,
    open_ai_stuff,
    date_stuff,
    eleven_labs_stuff,
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

_SUBREDDIT = 'crowdcast'
_SECOND = 1000


def main():
    # (CONTENT) Generate scripts for top 3 comments from FIRST pinned post
    top_three_segments_comments = reddit_stuff.get_pinned_post_comments(_SUBREDDIT, 1, 3)
    script_segments = []
    authors = []
    for author, comment in top_three_segments_comments:
        authors.append(author)
        segment = open_ai_stuff.generate_gpt4_response(podcast_segment.SYSTEM_PROMPT, comment)
        script_segments.append(segment)

    # (ADS) Generate scripts for top 2 comments from SECOND pinned post
    top_two_ads_comments = reddit_stuff.get_pinned_post_comments(_SUBREDDIT, 2, 2)
    script_ads = []
    for author, comment in top_two_ads_comments:
        authors.append(author)
        script_ad = open_ai_stuff.generate_gpt4_response(
            podcast_ads.SYSTEM_PROMPT,
            podcast_ads.PROMPT.format(product=comment)
        )
        script_ads.append(script_ad)

    # Generate an intro for the generated material
    intro = open_ai_stuff.generate_gpt4_response(
        podcast_intro.SYSTEM_PROMPT,
        podcast_intro.PROMPT.format(
            date=date_stuff.get_todays_date(),
            segment_1=script_segments[0],
            segment_2=script_segments[1],
            segment_3=script_segments[2],
        )
    )

    segue_1 = open_ai_stuff.generate_gpt4_response(
        podcast_segue.SYSTEM_PROMPT,
        podcast_segue.PROMPT.format(
            count_descriptor='first',
            segment=script_segments[0],
        )
    )

    segue_2 = open_ai_stuff.generate_gpt4_response(
        podcast_segue.SYSTEM_PROMPT,
        podcast_segue.PROMPT.format(
            count_descriptor='second',
            segment=script_segments[1],
        )
    )

    segue_3 = open_ai_stuff.generate_gpt4_response(
        podcast_segue.SYSTEM_PROMPT,
        podcast_segue.PROMPT.format(
            count_descriptor='third',
            segment=script_segments[2],
        )
    )

    outro = open_ai_stuff.generate_gpt4_response(
        podcast_outro.SYSTEM_PROMPT,
        podcast_outro.PROMPT.format(
            user_1=authors[0],
            segment_1=script_segments[0],
            user_2=authors[1],
            segment_2=script_segments[1],
            user_3=authors[2],
            segment_3=script_segments[2],
            user_4=authors[3],
            ad_1=script_ads[0],
            user_5=authors[4],
            ad_2=script_ads[1],
        )
    )

    # Use elevenlabs to generate the MP3s
    intro_audio = eleven_labs_stuff.convert_text_to_mp3(
        text=intro,
        voice=eleven_labs_stuff.HOST_VOICE)
    segue_1_audio = eleven_labs_stuff.convert_text_to_mp3(
        text=segue_1,
        voice=eleven_labs_stuff.HOST_VOICE)
    segue_2_audio = eleven_labs_stuff.convert_text_to_mp3(
        text=segue_2,
        voice=eleven_labs_stuff.HOST_VOICE)
    segue_3_audio = eleven_labs_stuff.convert_text_to_mp3(
        text=segue_3,
        voice=eleven_labs_stuff.HOST_VOICE)
    segment_1_audio = eleven_labs_stuff.convert_text_to_mp3(
        text=script_segments[0],
        voice=eleven_labs_stuff.HOST_VOICE)
    segment_2_audio = eleven_labs_stuff.convert_text_to_mp3(
        text=script_segments[1],
        voice=eleven_labs_stuff.HOST_VOICE)
    segment_3_audio = eleven_labs_stuff.convert_text_to_mp3(
        text=script_segments[2],
        voice=eleven_labs_stuff.HOST_VOICE)
    ad_1_audio = eleven_labs_stuff.convert_text_to_mp3(
        text=script_ads[0],
        voice=eleven_labs_stuff.ADS_VOICE)
    ad_2_audio = eleven_labs_stuff.convert_text_to_mp3(
        text=script_ads[1],
        voice=eleven_labs_stuff.ADS_VOICE)
    outro_audio = eleven_labs_stuff.convert_text_to_mp3(
        text=outro,
        voice=eleven_labs_stuff.HOST_VOICE)

    # Load music segments
    music_forest = AudioSegment.from_mp3("music/ES_Forest_Trekking__Adriel Fair.mp3")
    music_beachside = AudioSegment.from_mp3("music/ES_Beachside_Dancing_Dylan_Joseph.mp3")
    music_feriado = AudioSegment.from_mp3("music/ES_Feriado_Cornelio.mp3")
    music_typewriter = AudioSegment.from_mp3("music/ES_Typewriter_Song_Mac_Taboel.mp3")

    # Trim and apply fade outs to music segments
    music_forest = music_forest[:6 * _SECOND].fade_out(2 * _SECOND)
    music_beachside = music_beachside[:6 * _SECOND].fade_out(2 * _SECOND)
    music_feriado = music_feriado[:6 * _SECOND].fade_out(2 * _SECOND)
    music_typewriter = music_typewriter[:6 * _SECOND].fade_out(2 * _SECOND)

    # Stitch together podcast
    podcast = music_forest.overlay(intro_audio[:_SECOND], position=5 * _SECOND)
    podcast += intro_audio[_SECOND:]  # Add remaining part of intro_audio
    podcast += AudioSegment.silent(duration=1 * _SECOND)
    podcast += segue_1_audio
    podcast += AudioSegment.silent(duration=1 * _SECOND)
    podcast += music_beachside.overlay(segment_1_audio[:_SECOND], position=5 * _SECOND)
    podcast += segment_1_audio[_SECOND:]  # Add remaining part of segment_1_audio
    podcast += AudioSegment.silent(duration=2 * _SECOND)
    podcast += ad_1_audio
    podcast += AudioSegment.silent(duration=2 * _SECOND)
    podcast += segue_2_audio
    podcast += AudioSegment.silent(duration=1 * _SECOND)
    podcast += music_feriado.overlay(segment_2_audio[:_SECOND], position=5 * _SECOND)
    podcast += segment_2_audio[_SECOND:]  # Add remaining part of segment_2_audio
    podcast += AudioSegment.silent(duration=2 * _SECOND)
    podcast += ad_2_audio
    podcast += AudioSegment.silent(duration=2 * _SECOND)
    podcast += segue_3_audio
    podcast += AudioSegment.silent(duration=1 * _SECOND)
    podcast += music_typewriter.overlay(segment_3_audio[:_SECOND], position=5 * _SECOND)
    podcast += segment_3_audio[_SECOND:]  # Add remaining part of segment_3_audio
    podcast += AudioSegment.silent(duration=2 * _SECOND)
    podcast += music_forest
    podcast += outro_audio

    # Export the final audio file
    output_dir = "generated_podcast_mp3s/"
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    unique_id = uuid.uuid4()
    output_file = f"{output_dir}{unique_id}_{current_date}.mp3"
    podcast.export(output_file, format="mp3")

    # Write the script to a file
    output_dir = "generated-podcast-scripts/"
    output_file = f"{output_dir}{unique_id}_{current_date}.txt"
    with open(output_file, 'w+') as script_file:
        script_file.write('\n\n\n'.join([
            intro,
            segue_1,
            script_segments[0],
            script_ads[0],
            segue_2,
            script_segments[1],
            script_ads[1],
            segue_3,
            script_segments[2],
            outro,
        ]))

    # Upload the podcast to buzzsprout


if __name__ == '__main__':
    main()
