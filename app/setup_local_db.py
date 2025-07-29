"""
Local database setup utility
This script sets up a local MySQL database for testing purposes.
Can be safely deleted after initial setup.
"""
import pymysql
from config.local_database_config import LOCAL_DATABASE_CONFIG


def setup_local_database():
    """Setup local database and tables"""
    try:
        # Connect without database first
        config = LOCAL_DATABASE_CONFIG.copy()
        del config['database']
        
        connection = pymysql.connect(**config)
        
        with connection.cursor() as cursor:
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS stakes")
            cursor.execute("USE stakes")
            
            # Check if tables exist
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            
            print(f"Database 'stakes' ready. Tables found: {tables}")
            
            if not tables:
                print("No tables found. You may need to create them manually.")
            else:
                print("Tables available for testing.")
                
        connection.close()
        return True
        
    except Exception as e:
        print(f"Local database setup error: {e}")
        return False


if __name__ == "__main__":
    setup_local_database()
