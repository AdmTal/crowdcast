from utils.os_stuff import get_env_var_or_fail

BUZZSPROUT_API_KEY = get_env_var_or_fail('BUZZSPROUT_API_KEY')

POD_ID = 2188164
API_URL = f'https://www.buzzsprout.com/api/{POD_ID}'
