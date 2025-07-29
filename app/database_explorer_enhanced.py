"""
Enhanced database utility for exploring available databases and tables
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
            
            # Check each database for bamboopattern and map tables
            print("\nChecking for bamboopattern and map tables...")
            
            for db in databases:
                db_name = db[0]
                if db_name in ['information_schema', 'mysql', 'performance_schema', 'sys']:
                    continue
                    
                try:
                    cursor.execute(f"USE `{db_name}`")
                    cursor.execute("SHOW TABLES")
                    tables = cursor.fetchall()
                    table_names = [table[0] for table in tables]
                    
                    if 'bamboopattern' in table_names or 'map' in table_names:
                        print(f"\n*** Found target tables in database: {db_name} ***")
                        print("Tables in this database:")
                        for table in table_names:
                            print(f"  - {table}")
                            if table in ['bamboopattern', 'map']:
                                print(f"    ★ TARGET TABLE FOUND: {table}")
                                
                except Exception as e:
                    print(f"Error checking database {db_name}: {e}")
                    continue
                
        connection.close()
        return True
        
    except Exception as e:
        print(f"Database exploration error: {e}")
        return False


def test_ccm_connection():
    """Test connection specifically to CCM database"""
    try:
        config = DATABASE_CONFIG.copy()
        print(f"Testing connection to database: {config['database']}")
        
        connection = pymysql.connect(**config)
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE()")
            current_db = cursor.fetchone()
            print(f"Connected to database: {current_db[0]}")
            
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print(f"Tables found: {len(tables)}")
            for table in tables:
                print(f"  - {table[0]}")
                
        connection.close()
        return True
        
    except Exception as e:
        print(f"CCM connection test failed: {e}")
        return False


if __name__ == "__main__":
    print("=== Database Exploration ===")
    explore_databases()
    
    print("\n=== CCM Database Test ===")
    test_ccm_connection()
