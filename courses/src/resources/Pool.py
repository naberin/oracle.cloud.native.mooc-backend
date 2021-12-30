import cx_Oracle

import src.config.config as cfg
from src.config.constants import DBConfigurationConstants


class Pool:

    def __init__(self):
        self.pool = cx_Oracle.SessionPool(
            user=cfg.DB_USER,
            password=cfg.DB_PWD,
            dsn=cfg.DB_DSN,
            min=DBConfigurationConstants.DB_POOL_MIN,
            max=DBConfigurationConstants.DB_POOL_MAX,
            increment=DBConfigurationConstants.DB_POOL_INC,
            threaded=DBConfigurationConstants.DB_POOL_THR,
            encoding=DBConfigurationConstants.DB_POOL_ENC,
            getmode=cx_Oracle.SPOOL_ATTRVAL_WAIT
        )

    def get(self):
        return self.pool
