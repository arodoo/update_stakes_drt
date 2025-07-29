"""
Update handler continuation
"""
from application.user_interaction_service import UserInteractionService
from domain.services.content_comparison_service import ContentComparisonService


class UpdateHandlerContinuation:
    """Continuation of update handler for remaining methods"""
    
    def __init__(self, update_service, xlsx_reader):
        self.update_service = update_service
        self.xlsx_reader = xlsx_reader
        self.ui = UserInteractionService()
        self.content_comparison = ContentComparisonService(update_service.db, xlsx_reader)
    
    def show_comparison_and_confirm(self, backup_info, xlsx_data):
        """Show detailed comparison including content analysis and ask for confirmation"""
        print("\n4. DETAILED UPDATE ANALYSIS:")
        
        # Show count comparison
        self.update_service.show_comparison(backup_info, xlsx_data)
        
        # Show content analysis
        print("\n   📋 CONTENT ANALYSIS (Current DB vs New XLSX):")
        print("   Table               | Records Changed | % Changed | Impact")
        print("   -------------------|-----------------|-----------|--------")
        
        total_changed_records = 0
        
        for table in ['bamboopattern', 'map', 'centerpos2x', 'largescreenpixelpos']:
            current_count = backup_info.get(table, 0)
            new_count = xlsx_data.get(table, 0)
            
            if current_count > 0 and new_count > 0:
                print(f"   {table:<18} | Analyzing...    |           |")
                
                # Perform actual content comparison
                comparison_result = self.content_comparison.compare_table_content_for_update(table)
                
                if 'error' in comparison_result:
                    changed_info = f"Error: {comparison_result['error'][:20]}..."
                    percent_changed = "N/A"
                    impact = "Unknown"
                else:
                    changed_records = comparison_result['content_differences']
                    total_changed_records += changed_records
                    percent_changed = f"{(changed_records/current_count)*100:.1f}%" if current_count > 0 else "N/A"
                    
                    if changed_records == 0:
                        impact = "No change"
                    elif changed_records < current_count * 0.1:
                        impact = "Low"
                    elif changed_records < current_count * 0.5:
                        impact = "Medium"
                    else:
                        impact = "High"
                    
                    changed_info = f"{changed_records:,}"
                
                # Update the line with results
                print(f"\r   {table:<18} | {changed_info:<15} | {percent_changed:<9} | {impact}")
            else:
                print(f"   {table:<18} | {'FULL REPLACE':<15} | {'100.0%':<9} | High")
                total_changed_records += max(current_count, new_count)
        
        print(f"\n   📊 UPDATE IMPACT SUMMARY:")
        print(f"   • Total records that will be MODIFIED: {total_changed_records:,}")
        print(f"   • This shows how many records have DIFFERENT CONTENT")
        print(f"   • Operation: UPDATE existing records with new XLSX data")
        print(f"   ⚠️  {total_changed_records:,} records will have their data changed")
        
        return self.ui.confirm_action(f"\nProceed with updating {total_changed_records:,} records?")
    
    def execute_update_and_validate(self, backup_info, xlsx_data):
        """Execute update and validate results"""
        print("\n5. Executing update...")
        update_result = self.update_service.execute_update(xlsx_data)
        
        print("\n6. VALIDATION:")
        validation_result = self.update_service.validate_update(
            backup_info, update_result
        )
        
        if validation_result['success']:
            print("✓ All validations passed!")
            if self.ui.confirm_action("Commit changes?"):
                self.update_service.commit()
                print("✓ Changes committed successfully!")
            else:
                self.update_service.rollback()
                print("✗ Changes rolled back")
        else:
            print("✗ Validation failed:")
            for error in validation_result['errors']:
                print(f"   - {error}")
            self.update_service.rollback()
            print("✗ Changes automatically rolled back")
