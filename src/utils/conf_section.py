import configparser
import os


def get_conf_section(section, key):
    config = configparser.ConfigParser()
    config.read(os.path.join("conf", "conf.ini"))
    if section not in config.sections():
        return None
    try:
        return config.get(section, key)
    except Exception as err:
        print(str(err))
    return None
