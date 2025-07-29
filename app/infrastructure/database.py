"""
Database connection infrastructure
"""
import pymysql
import os
from config.database_config import DATABASE_CONFIG
from config.local_database_config import LOCAL_DATABASE_CONFIG


class DatabaseConnection:
    """Handles database connection and operations"""
    
    def __init__(self, use_local=True):
        self.connection = None
        # Use local config by default, remote if use_local=False
        self.config = LOCAL_DATABASE_CONFIG if use_local else DATABASE_CONFIG
        self.connect()
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = pymysql.connect(**self.config)
            db_name = self.config['database']
            print(f"Database connection established to: {db_name}")
        except Exception as e:
            print(f"Database connection error: {e}")
            raise
    
    def test_connection(self):
        """Test if connection is alive"""
        try:
            if self.connection:
                with self.connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    return True
            return False
        except Exception as e:
            print(f"Connection test failed: {e}")
            return False
    
    def execute_query(self, query, params=None):
        """Execute a query and return results"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            print(f"Query execution error: {e}")
            raise
    
    def execute_one(self, query, params=None):
        """Execute query and return single result"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()
        except Exception as e:
            print(f"Query execution error: {e}")
            raise
    
    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("Database connection closed")
