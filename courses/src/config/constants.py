
class ErrorConstants:
    """Common Errors"""
    DEFAULT_NOT_FOUND_ERROR = "Not Found"
    DEFAULT_NOT_FOUND_DETAIL = "Resource was not found"

    DEFAULT_INTERNAL_ERROR = "Internal Service Error"
    DEFAULT_INTERNAL_DETAIL = "Request cannot be currently completed. Please contact support or your administrator."


class EnvironmentConstants:
    """environment variables to read from"""
    DB_DSN = "DPT_DB_DSN"
    DB_USER = "DPT_DB_USER"
    DB_PWD = "DPT_DB_PWD"


class DBConfigurationConstants:
    DB_POOL_MIN = 1
    DB_POOL_MAX = 15
    DB_POOL_INC = 1
    DB_POOL_THR = True
    DB_POOL_ENC = "UTF-8"
    DB_SCHEMA = "OC_DEPTH"
