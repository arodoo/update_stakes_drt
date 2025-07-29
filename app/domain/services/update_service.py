"""
Update service for managing table updates
"""
from domain.services.update_service_continuation import UpdateServiceContinuation


class UpdateService:
    """Service for update operations"""
    def __init__(self, db_connection):
        self.db = db_connection
        self.tables = ['bamboopattern', 'map', 'centerpos2x', 'largescreenpixelpos']
        self.continuation = UpdateServiceContinuation(db_connection)
    
    def show_comparison(self, backup_info, xlsx_data):
        """Show comparison between backup and XLSX data"""
        print("   Table               | Current | New XLSX | Difference | Records Added/Removed")
        print("   -------------------|---------|----------|------------|----------------------")
        
        total_affected = 0
        
        for table in self.tables:
            backup_count = backup_info.get(table, 0)
            xlsx_count = xlsx_data.get(table, 0)
            difference = xlsx_count - backup_count
            total_affected += abs(difference)
            
            if difference > 0:
                action = f"+{difference} will be ADDED"
            elif difference < 0:
                action = f"{difference} will be REMOVED"
            else:
                action = "No change"
            
            print(f"   {table:<18} | {backup_count:7} | {xlsx_count:8} | {difference:+10} | {action}")
        
        print(f"\n   📊 SUMMARY:")
        print(f"   • Total records that will be affected: {total_affected:,}")
        print(f"   • Tables that will change: {sum(1 for table in self.tables if backup_info.get(table, 0) != xlsx_data.get(table, 0))}/{len(self.tables)}")
        
        if total_affected == 0:
            print("   ⚠️  WARNING: No records will be changed - all tables have same count!")
        elif total_affected > 10000:
            print("   ⚠️  WARNING: Large number of records will be affected!")
        
        return total_affected
    
    def get_current_table_info(self):
        """Get current table information"""
        current_info = {}
        
        for table in self.tables:
            try:
                count_query = f"SELECT COUNT(*) FROM `{table}`"
                result = self.db.execute_one(count_query)
                current_info[table] = result[0] if result else 0
            except Exception as e:
                print(f"Error getting info for {table}: {e}")
                current_info[table] = 0
        
        return current_info
    
    def show_rollback_comparison(self, current_info, backup_info):
        """Show comparison for rollback"""
        return self.continuation.show_rollback_comparison(current_info, backup_info)
    
    def execute_update(self, xlsx_data):
        """Execute update from XLSX data"""
        return self.continuation.execute_update(xlsx_data)
    
    def validate_update(self, backup_info, update_result):
        """Validate update results"""
        return self.continuation.validate_update(backup_info, update_result)
    
    def commit(self):
        """Commit transaction"""
        self.db.connection.commit()
    
    def rollback(self):
        """Rollback transaction"""
        self.db.connection.rollback()
