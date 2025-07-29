"""
Backup service for managing table backups
"""
from domain.services.backup_service_continuation import BackupServiceContinuation


class BackupService:
    """Service for backup operations"""
    
    def __init__(self, db_connection):
        self.db = db_connection
        self.tables = ['bamboopattern', 'map', 'centerpos2x', 'largescreenpixelpos']
        self.continuation = BackupServiceContinuation(db_connection)
    
    def backups_exist(self):
        """Check if backup tables exist"""
        try:
            for table in self.tables:
                backup_table = f"{table}_backup"
                query = f"SHOW TABLES LIKE '{backup_table}'"
                result = self.db.execute_one(query)
                if result:
                    return True
            return False
        except Exception as e:
            print(f"Error checking backups: {e}")
            return False
    
    def remove_backups(self):
        """Remove existing backup tables"""
        for table in self.tables:
            backup_table = f"{table}_backup"
            try:
                query = f"DROP TABLE IF EXISTS `{backup_table}`"
                self.db.execute_query(query)
            except Exception as e:
                print(f"Error removing backup {backup_table}: {e}")
    
    def create_backups(self):
        """Create backup tables from current tables"""
        backup_info = {}
        
        for table in self.tables:
            backup_table = f"{table}_backup"
            try:
                # Create backup table
                query = f"CREATE TABLE `{backup_table}` AS SELECT * FROM `{table}`"
                self.db.execute_query(query)
                
                # Count records
                count_query = f"SELECT COUNT(*) FROM `{backup_table}`"
                result = self.db.execute_one(count_query)
                backup_info[table] = result[0] if result else 0
                
            except Exception as e:
                print(f"Error creating backup for {table}: {e}")
                backup_info[table] = 0
        
        return backup_info
    
    def get_backup_info(self):
        """Get information about existing backups"""
        return self.continuation.get_backup_info()
    
    def execute_rollback(self):
        """Execute rollback from backup tables"""
        return self.continuation.execute_rollback()
