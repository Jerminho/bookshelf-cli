import sqlite3
import configparser

class Database:
    def __init__(self, config_path="config/settings.ini"):
        # Read the settings file
        config = configparser.ConfigParser()
        config.read(config_path)
        self.db_path = config["database"]["path"]

    def connect(self):
        """Return a connection to the SQLite database"""
        return sqlite3.connect(self.db_path)

    def execute(self, query, params=None):
        """Execute a query with optional parameters"""
        with self.connect() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            return cursor
