import os
import logging


def os_getenv(key: str, default: str = None) -> str:
    env_value = os.getenv(key)
    if env_value is None:
        logging.warning(
            f"ENV variable {key} is set to empty string. Using default value {default}"
        )
        env_value = default
    return env_value
