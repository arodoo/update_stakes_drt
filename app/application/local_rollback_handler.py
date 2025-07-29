"""
Local rollback process handler
"""
from application.user_interaction_service import UserInteractionService
from application.local_rollback_handler_continuation import LocalRollbackHandlerContinuation
from domain.services.content_comparison_service import ContentComparisonService


class LocalRollbackHandler:
    """Handles the rollback from local XLSX files workflow"""

    def __init__(self, update_service, local_rollback_service):
        self.update_service = update_service
        self.local_rollback_service = local_rollback_service
        self.ui = UserInteractionService()
        self.continuation = LocalRollbackHandlerContinuation(update_service, local_rollback_service)
        self.content_comparison = ContentComparisonService(update_service.db, local_rollback_service)
    
    def execute(self):
        """Execute the local rollback process"""
        print("=== ROLLBACK FROM LOCAL XLSX ===")
        
        old_data = self._read_old_xlsx_files()
        current_info = self._show_comparison(old_data)        
        if not self.ui.confirm_action("\nProceed with rollback from local XLSX?"):
            print("✗ Local rollback cancelled")
            return
        
        self.continuation.execute_local_rollback(old_data)

    def _read_old_xlsx_files(self):
        """Read old XLSX files"""
        print("1. Reading old XLSX files...")
        old_data = self.local_rollback_service.read_old_files()
        total_records = sum(old_data.values())
        table_count = len(old_data)
        print(f"   ✓ {table_count} files read with {total_records:,} total records")
        return old_data

    def _show_comparison(self, old_data):
        """Show current vs old XLSX comparison"""
        print("\n2. Comparing current database vs old XLSX files:")
        current_info = self.update_service.get_current_table_info()
        total_current = sum(current_info.values())
        total_old = sum(old_data.values())
        print(f"   Source: documentation/old_data/")
        print(f"   Tables to update: {', '.join(old_data.keys())}")
        print(f"   Current DB total: {total_current:,}")
        print(f"   Old XLSX total:   {total_old:,}")
        print(f"   Net change:       {total_old - total_current:+,} records")
        return current_info
