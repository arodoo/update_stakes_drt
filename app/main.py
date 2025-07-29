"""
Main application entry point for CCM database connection
"""
from infrastructure.database import DatabaseConnection
from domain.services.bamboo_service import BambooService
from domain.services.map_service import MapService


def main():
    """Main application function"""
    try:
        # Initialize database connection
        db_connection = DatabaseConnection()
        
        # Initialize services
        bamboo_service = BambooService(db_connection)
        map_service = MapService(db_connection)
        
        # Test connections
        print("Testing database connection...")
        if db_connection.test_connection():
            print("✓ Database connection successful!")
            
            # Example operations
            print("\nTesting services...")
            bamboo_count = bamboo_service.get_total_count()
            map_count = map_service.get_total_count()
            
            print(f"Bamboo patterns: {bamboo_count}")
            print(f"Map entries: {map_count}")
            
        else:
            print("✗ Database connection failed!")
            
    except Exception as e:
        print(f"Application error: {e}")
    finally:
        if 'db_connection' in locals():
            db_connection.close()


if __name__ == "__main__":
    main()
