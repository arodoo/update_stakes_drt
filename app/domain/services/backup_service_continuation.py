"""
Backup service continuation for additional methods
"""

class BackupServiceContinuation:
    """Additional backup service methods"""
    
    def __init__(self, db_connection):
        self.db = db_connection
        self.tables = ['bamboopattern', 'map', 'centerpos2x', 'largescreenpixelpos']
    
    def get_backup_info(self):
        """Get information about existing backups"""
        backup_info = {}
        
        for table in self.tables:
            backup_table = f"{table}_backup"
            try:
                count_query = f"SELECT COUNT(*) FROM `{backup_table}`"
                result = self.db.execute_one(count_query)
                backup_info[table] = result[0] if result else 0
            except Exception as e:
                print(f"Error getting backup info for {table}: {e}")
                backup_info[table] = 0
        
        return backup_info
    
    def execute_rollback(self):
        """Execute rollback from backup tables"""
        rollback_result = {}
        
        for table in self.tables:
            backup_table = f"{table}_backup"
            try:
                # Clear current table
                self.db.execute_query(f"DELETE FROM `{table}`")
                
                # Restore from backup
                restore_query = f"""
                INSERT INTO `{table}` 
                SELECT * FROM `{backup_table}`
                """
                self.db.execute_query(restore_query)
                
                # Count restored records
                count_query = f"SELECT COUNT(*) FROM `{table}`"
                result = self.db.execute_one(count_query)
                rollback_result[table] = result[0] if result else 0
                
            except Exception as e:
                print(f"Error during rollback for {table}: {e}")
                rollback_result[table] = 0
        
        return rollback_result
