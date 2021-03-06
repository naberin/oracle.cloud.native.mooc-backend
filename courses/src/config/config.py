import os

from src.config.constants import EnvironmentConstants

DB_DSN = os.getenv(EnvironmentConstants.DB_DSN)
DB_USER = os.getenv(EnvironmentConstants.DB_USER)
DB_PWD = os.getenv(EnvironmentConstants.DB_PWD)

DARWIN_LOCATION = os.environ.get("HOME") + "/Downloads/instantclient_19_8"
WINDOWS_LOCATIONS = ""
