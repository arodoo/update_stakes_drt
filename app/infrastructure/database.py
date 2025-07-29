"""
Database connection infrastructure
"""
import pymysql
from config.database_config import DATABASE_CONFIG


class DatabaseConnection:
    """Handles database connection and operations"""
    
    def __init__(self):
        self.connection = None
        self.connect()
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = pymysql.connect(**DATABASE_CONFIG)
            print("Database connection established")
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
