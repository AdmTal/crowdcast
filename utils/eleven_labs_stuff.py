from elevenlabs import generate, set_api_key, Voice, VoiceSettings
from pydub import AudioSegment
import io
import os
import hashlib
from utils.os_stuff import get_env_var_or_fail
import logging

set_api_key(get_env_var_or_fail('ELEVEN_LABS_API_KEY'))

HOST_VOICE = Voice(
    voice_id="21m00Tcm4TlvDq8ikWAM",
    name="Rachel",
    category="premade",
    settings=VoiceSettings(stability=0.2, similarity_boost=0.85),
)

ADS_VOICE = Voice(
    voice_id="TxGEqnHWrfWFTfGW9XjX",
    name="Josh",
    category="premade",
    settings=VoiceSettings(stability=0.2, similarity_boost=0.85),
)


def load_audio_bytes(audio_bytes):
    audio_file = io.BytesIO(audio_bytes)
    audio_segment = AudioSegment.from_file(audio_file, format='mp3')
    return audio_segment


def convert_text_to_mp3(text, voice):
    # Generate the cache key by MD5 hashing the text
    cache_key = hashlib.md5(text.encode()).hexdigest()

    # Check if the file already exists in cache
    cache_dir = ".eleven_labs_cache"
    cache_file = os.path.join(cache_dir, f"{cache_key}.mp3")

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    if os.path.exists(cache_file):
        # If it does exist, load and return as an AudioSegment
        audio_segment = AudioSegment.from_mp3(cache_file)
    else:
        # If it does not exist, call the API, create, save, and return as an AudioSegment
        char_count = len(text)
        logging.info(f'Calling eleven labs for {char_count} chars...')
        section_1_voice_over = load_audio_bytes(generate(
            text=text,
            voice=voice
        ))
        section_1_voice_over.export(cache_file, format='mp3')
        audio_segment = section_1_voice_over

    return audio_segment
