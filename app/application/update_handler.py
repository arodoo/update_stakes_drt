"""
Update process handler
"""
from application.user_interaction_service import UserInteractionService
from application.update_handler_continuation import UpdateHandlerContinuation


class UpdateHandler:
    """Handles the update process workflow"""

    def __init__(self, backup_service, update_service, xlsx_reader):
        self.backup_service = backup_service
        self.update_service = update_service
        self.xlsx_reader = xlsx_reader
        self.ui = UserInteractionService()
        self.continuation = UpdateHandlerContinuation(update_service, xlsx_reader)
    
    def execute(self):
        """Execute the update process"""
        print("=== UPDATE PROCESS ===")
        
        if not self._handle_existing_backups():
            return
        
        backup_info = self._create_backups()
        xlsx_data = self._read_xlsx_files()
        
        if not self.continuation.show_comparison_and_confirm(backup_info, xlsx_data):
            print("✗ Update cancelled")
            return
        
        self.continuation.execute_update_and_validate(backup_info, xlsx_data)
    
    def _handle_existing_backups(self):
        """Handle existing backups check and cleanup"""
        print("\n1. Checking existing backups...")
        if self.backup_service.backups_exist():
            print("   ⚠️  Existing backups found!")
            if self.ui.confirm_action("   Remove existing backups?"):
                self.backup_service.remove_backups()
                print("   ✓ Existing backups removed")
                return True
            else:
                print("   ✗ Update cancelled")
                return False
        else:
            print("   ✓ No existing backups found")
            return True
    
    def _create_backups(self):
        """Create backups of current tables"""
        print("\n2. Creating backups of current tables...")
        backup_info = self.backup_service.create_backups()
        for table, count in backup_info.items():
            print(f"   ✓ {table}: {count} records backed up")
        return backup_info
    
    def _read_xlsx_files(self):
        """Read XLSX files"""
        print("\n3. Reading XLSX files...")
        xlsx_data = self.xlsx_reader.read_all_files()
        for table, count in xlsx_data.items():
            print(f"   ✓ {table}.xlsx: {count} records read")
        return xlsx_data
