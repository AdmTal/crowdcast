import os


def get_env_var_or_fail(name):
    if name not in os.environ:
        raise Exception(f'Env Var {name} is not set')

    return os.environ[name]
