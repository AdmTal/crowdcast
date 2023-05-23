from utils.os_stuff import get_env_var_or_fail
import openai
import os
import hashlib
import logging

openai.organization = get_env_var_or_fail("OPENAI_API_ORG")
openai.api_key = get_env_var_or_fail("OPENAI_API_KEY")


def generate_gpt4_response(system_prompt, user_prompt):
    logging.info(f'generate_gpt4_response SYSTEM: {system_prompt}')
    logging.info(f'generate_gpt4_response PROMPT: {user_prompt}')
    # Create MD5 hash of user_submitted_text
    md5 = hashlib.md5()
    hash_key = f'{system_prompt}{user_prompt}'
    md5.update(hash_key.encode('utf-8'))
    cache_id = md5.hexdigest()

    cache_dir = '.open_ai_cache'
    cache_file = f'{cache_dir}/{cache_id}.txt'

    # Create cache directory if it doesn't exist
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    # If cache file exists, read and return its contents
    if os.path.isfile(cache_file):
        with open(cache_file, 'r') as f:
            return f.read()

    char_count = len(user_prompt) + len(system_prompt)
    logging.info(f'Calling openai with {char_count}...')
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                'role': 'system',
                'content': system_prompt,
            },
            {
                'role': 'user',
                'content': user_prompt,
            }
        ]
    )
    result = response.choices[0].message.content

    # Write API response to cache file
    with open(cache_file, 'w') as f:
        f.write(result)

    logging.info(f'generate_gpt4_response RESULT: {result}')
    return result
