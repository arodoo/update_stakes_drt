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
        print("\n1. Reading old XLSX files...")
        old_data = self.local_rollback_service.read_old_files()
        for table, count in old_data.items():
            print(f"   ✓ {table}.xlsx (old): {count} records read")
        return old_data
    
    def _show_comparison(self, old_data):
        """Show current vs old XLSX comparison"""
        print("\n2. DETAILED CONTENT COMPARISON ANALYSIS:")
        current_info = self.update_service.get_current_table_info()
        
        print("   Table               | Current   | Old XLSX  | Count Diff | Changed Records")
        print("   -------------------|-----------|-----------|------------|----------------")
        
        total_changed_records = 0
        
        for table in ['bamboopattern', 'map', 'centerpos2x', 'largescreenpixelpos']:
            current_count = current_info.get(table, 0)
            old_count = old_data.get(table, 0)
            count_difference = old_count - current_count
            
            print(f"   {table:<18} | {current_count:>9,} | {old_count:>9,} | {count_difference:>+10,} | Analyzing...")
            
            # Perform actual content comparison
            comparison_result = self.content_comparison.compare_table_content(table)
            
            if 'error' in comparison_result:
                changed_records_info = f"Error: {comparison_result['error'][:30]}..."
            else:
                changed_records = comparison_result['content_differences']
                total_changed_records += changed_records
                changed_records_info = f"{changed_records:,} records differ"
            
            # Update the line with actual results
            print(f"\r   {table:<18} | {current_count:>9,} | {old_count:>9,} | {count_difference:>+10,} | {changed_records_info}")
        
        print(f"\n   📊 CONTENT ANALYSIS SUMMARY:")
        print(f"   • Total records with different CONTENT: {total_changed_records:,}")
        print(f"   • This means {total_changed_records:,} records will be CHANGED in rollback")
        print(f"   • Operation: FULL TABLE REPLACEMENT (DELETE current + INSERT old)")
        print(f"   ⚠️  ALL current data will be replaced with old XLSX data")
        
        return current_info
