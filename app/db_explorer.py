"""
Database explorer utility to check available databases and tables
"""
import pymysql
from config.database_config import DATABASE_CONFIG


def explore_databases():
    """Explore available databases on the server"""
    try:
        # Connect without specifying a database
        config = DATABASE_CONFIG.copy()
        config.pop('database', None)  # Remove database from config
        
        connection = pymysql.connect(**config)
        
        with connection.cursor() as cursor:
            # Show databases
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            
            print("Available databases:")
            for db in databases:
                print(f"  - {db[0]}")
        
        connection.close()
        
    except Exception as e:
        print(f"Error exploring databases: {e}")


def explore_tables(database_name):
    """Explore tables in a specific database"""
    try:
        config = DATABASE_CONFIG.copy()
        config['database'] = database_name
        
        connection = pymysql.connect(**config)
        
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            
            print(f"\nTables in database '{database_name}':")
            for table in tables:
                print(f"  - {table[0]}")
        
        connection.close()
        
    except Exception as e:
        print(f"Error exploring tables in {database_name}: {e}")


if __name__ == "__main__":
    explore_databases()
    explore_tables("drt_campeche")
