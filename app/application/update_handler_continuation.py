"""
Update handler continuation
"""
from application.user_interaction_service import UserInteractionService


class UpdateHandlerContinuation:
    """Continuation of update handler for remaining methods"""
    
    def __init__(self, update_service):
        self.update_service = update_service
        self.ui = UserInteractionService()
    
    def show_comparison_and_confirm(self, backup_info, xlsx_data):
        """Show comparison and ask for confirmation"""
        print("\n4. COMPARISON SUMMARY:")
        self.update_service.show_comparison(backup_info, xlsx_data)
        return self.ui.confirm_action("\nProceed with update?")
    
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
