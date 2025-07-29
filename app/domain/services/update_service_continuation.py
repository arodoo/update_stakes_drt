"""
Update service continuation for additional methods
"""

class UpdateServiceContinuation:
    """Additional update service methods"""
    
    def __init__(self, db_connection):
        self.db = db_connection
        self.tables = ['bamboopattern', 'map', 'centerpos2x', 'largescreenpixelpos']
    
    def show_rollback_comparison(self, current_info, backup_info):
        """Show comparison for rollback"""
        print("   Table               | Current | Backup | Difference | Records Added/Removed")
        print("   -------------------|---------|--------|------------|----------------------")
        
        total_affected = 0
        
        for table in self.tables:
            current_count = current_info.get(table, 0)
            backup_count = backup_info.get(table, 0)
            difference = backup_count - current_count
            total_affected += abs(difference)
            
            if difference > 0:
                action = f"+{difference} will be RESTORED"
            elif difference < 0:
                action = f"{abs(difference)} will be REMOVED"
            else:
                action = "No change"
            
            print(f"   {table:<18} | {current_count:7} | {backup_count:6} | {difference:+10} | {action}")
        
        print(f"\n   📊 ROLLBACK SUMMARY:")
        print(f"   • Total records that will be affected: {total_affected:,}")
        print(f"   • Tables that will change: {sum(1 for table in self.tables if current_info.get(table, 0) != backup_info.get(table, 0))}/{len(self.tables)}")
        
        return total_affected
    
    def execute_update(self, xlsx_data):
        """Execute update from XLSX data (placeholder)"""
        # This would contain the actual update logic
        # For now, return current counts as if updated
        update_result = {}
        
        for table in self.tables:
            try:
                count_query = f"SELECT COUNT(*) FROM `{table}`"
                result = self.db.execute_one(count_query)
                update_result[table] = result[0] if result else 0
            except Exception as e:
                print(f"Error during update for {table}: {e}")
                update_result[table] = 0
        
        return update_result
    
    def validate_update(self, backup_info, update_result):
        """Validate update results"""
        errors = []
        
        for table in self.tables:
            backup_count = backup_info.get(table, 0)
            update_count = update_result.get(table, 0)
            
            if backup_count == 0 and update_count == 0:
                errors.append(f"{table}: Both backup and update are empty")
        
        return {
            'success': len(errors) == 0,
            'errors': errors
        }
