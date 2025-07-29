"""
Local rollback process handler
"""
from application.user_interaction_service import UserInteractionService
from application.local_rollback_handler_continuation import LocalRollbackHandlerContinuation


class LocalRollbackHandler:
    """Handles the rollback from local XLSX files workflow"""
    
    def __init__(self, update_service, local_rollback_service):
        self.update_service = update_service
        self.local_rollback_service = local_rollback_service
        self.ui = UserInteractionService()
        self.continuation = LocalRollbackHandlerContinuation(update_service, local_rollback_service)
    
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
        print("\n1. Reading old XLSX files...")
        old_data = self.local_rollback_service.read_old_files()
        for table, count in old_data.items():
            print(f"   ✓ {table}.xlsx (old): {count} records read")
        return old_data

    def _show_comparison(self, old_data):
        """Show current vs old XLSX comparison"""
        print("\n2. DETAILED COMPARISON ANALYSIS:")
        current_info = self.update_service.get_current_table_info()
        print("   Table               | Current   | Old XLSX  | Difference | Records Added/Removed")
        print("   -------------------|-----------|-----------|------------|----------------------")
        total_affected = 0
        for table in ['bamboopattern', 'map', 'centerpos2x', 'largescreenpixelpos']:
            current_count = current_info.get(table, 0)
            old_count = old_data.get(table, 0)
            difference = old_count - current_count
            total_affected += abs(difference)
            if difference > 0:
                action = f"+{difference:,} will be ADDED"
            elif difference < 0:
                action = f"{abs(difference):,} will be REMOVED"
            else:
                action = "No change"
            # Show full numbers without width limits
            print(f"   {table:<18} | {current_count:>9,} | {old_count:>9,} | {difference:>+10,} | {action}")
        print(f"\n   📊 SUMMARY:")
        print(f"   • Total records that will be affected: {total_affected:,}")
        print(f"   • Tables that will change: {sum(1 for table in ['bamboopattern', 'map', 'centerpos2x', 'largescreenpixelpos'] if current_info.get(table, 0) != old_data.get(table, 0))}/4")
        return current_info
