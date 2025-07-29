"""
User interaction service for confirmations
"""

class UserInteractionService:
    """Service for user interactions"""
    
    @staticmethod
    def confirm_action(message):
        """Ask user for confirmation"""
        while True:
            response = input(f"{message} (y/n): ").lower().strip()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'")
