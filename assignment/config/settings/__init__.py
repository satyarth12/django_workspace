# Selecting appropriate settings
import os
import configparser

config = configparser.ConfigParser()
config.optionxform = str
config.read(os.path.abspath("config/settings/__env__.ini"))

ENV_INFO_ = config["env"]

if ENV_INFO_.get("SERVER_ENV") == "dev":
    SESNSITIVE_ = config["dev_sensitive"]
    from config.settings.dev import *

elif ENV_INFO_.get("SERVER_ENV") == "prod":
    # SESNSITIVE_ = config["prod_sensitive"]
    # from config.settings.prod import *
    pass

else:
    raise ValueError('No environment given')
