"""
Database utility for exploring available databases and tables
"""
import pymysql
from config.database_config import DATABASE_CONFIG


def explore_databases():
    """Explore available databases and tables"""
    try:
        # Connect without specifying database first
        config = DATABASE_CONFIG.copy()
        del config['database']
        
        connection = pymysql.connect(**config)
        
        with connection.cursor() as cursor:
            # List databases
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            print("Available databases:")
            for db in databases:
                print(f"  - {db[0]}")
              # Try to connect to 'drt_campeche' database
            cursor.execute("USE drt_campeche")
            print("\nSuccessfully connected to 'drt_campeche' database")
            
            # List tables
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print("\nAvailable tables:")
            for table in tables:
                print(f"  - {table[0]}")
                
        connection.close()
        return True
        
    except Exception as e:
        print(f"Database exploration error: {e}")
        return False


if __name__ == "__main__":
    explore_databases()
