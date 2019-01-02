import os

env = os.environ

config = {
    'SANIC_RUN': {
        'host': env.get('SANIC_HOST', '0.0.0.0'),
        'port': int(env.get('SANIC_PORT', 8000)),
    }
}

# @see Default Sanic Config
# at https://sanic.readthedocs.io/en/latest/sanic/config.html#builtin-configuration-values
