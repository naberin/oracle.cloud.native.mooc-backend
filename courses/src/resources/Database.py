import app
import cx_Oracle

from src.config.constants import DBConfigurationConstants


class Database:

    def __init__(self):
        self.connection = app.pool.acquire()
        self.connection.current_schema = DBConfigurationConstants.DB_SCHEMA
        self.cursor = self.connection.cursor()

    def set_row_factory(self):
        columns = [str.lower(col[0]) for col in self.cursor.description]
        self.cursor.rowfactory = lambda *args: dict(zip(columns, args))

    def fetch_all(self, query: str, data: dict = None) -> list:
        try:
            if data:
                self.cursor.execute(query, dict)
            else:
                self.cursor.execute(query)

            self.set_row_factory()
            items = self.cursor.fetchall()
            return items

        except cx_Oracle.DatabaseError as err:
            return []

        except cx_Oracle.InterfaceError as err:
            return []

        except cx_Oracle.Error:
            return []

        finally:
            self.connection.close()
