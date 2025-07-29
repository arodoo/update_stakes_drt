"""
Main application entry point - Database Management Tool
"""
import sys
from application.command_handler import CommandHandler
from application.help_service import HelpService


def main():
    """Main application function"""
    valid_commands = ['update', 'rollback', 'rollback_from_local', 'help']
    valid_targets = ['local', 'remote']
    
    # Parse arguments: python main.py [command] [database_target]
    if len(sys.argv) < 2:
        HelpService.show_help()
        return
    
    command = sys.argv[1]
    
    if command not in valid_commands:
        HelpService.show_help()
        return
    
    if command == 'help':
        HelpService.show_help()
        return
    
    # Check for database target (default to local)
    database_target = 'local'  # default
    if len(sys.argv) >= 3:
        if sys.argv[2] in valid_targets:
            database_target = sys.argv[2]
        else:
            print(f"❌ Invalid database target: {sys.argv[2]}")
            print(f"Valid targets: {', '.join(valid_targets)}")
            return
    
    use_local = (database_target == 'local')
    
    print(f"🔗 Connecting to: {database_target.upper()} database")
    
    try:
        handler = CommandHandler(use_local=use_local)
        
        if command == 'update':
            handler.handle_update()
        elif command == 'rollback':
            handler.handle_rollback()
        elif command == 'rollback_from_local':
            handler.handle_rollback_from_local()
            
    except Exception as e:
        print(f"Application error: {e}")


if __name__ == "__main__":
    main()
