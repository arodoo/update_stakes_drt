"""
Rollback process handler
"""
from application.user_interaction_service import UserInteractionService


class RollbackHandler:
    """Handles the rollback process workflow"""
    
    def __init__(self, backup_service, update_service):
        self.backup_service = backup_service
        self.update_service = update_service
        self.ui = UserInteractionService()
    
    def execute(self):
        """Execute the rollback process"""
        print("=== ROLLBACK PROCESS ===")
        
        backup_info = self._check_backups()
        if not backup_info:
            return
        
        current_info = self._show_comparison(backup_info)
        
        if not self.ui.confirm_action("\nProceed with rollback?"):
            print("✗ Rollback cancelled")
            return
        
        self._execute_rollback()
    
    def _check_backups(self):
        """Check if backups exist"""
        print("\n1. Checking for backups...")
        if not self.backup_service.backups_exist():
            print("   ✗ No backups found! Cannot rollback.")
            return None
        
        backup_info = self.backup_service.get_backup_info()
        print("   ✓ Backups found:")
        for table, count in backup_info.items():
            print(f"     - {table}: {count} records")
        return backup_info
    
    def _show_comparison(self, backup_info):
        """Show current vs backup comparison"""
        print("\n2. CURRENT vs BACKUP COMPARISON:")
        current_info = self.update_service.get_current_table_info()
        self.update_service.show_rollback_comparison(current_info, backup_info)
        return current_info
    
    def _execute_rollback(self):
        """Execute the rollback"""
        print("\n3. Executing rollback...")
        rollback_result = self.backup_service.execute_rollback()
        
        for table, count in rollback_result.items():
            print(f"   ✓ {table}: {count} records restored")
        
        print("✓ Rollback completed successfully!")
