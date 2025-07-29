"""
Help service for showing application usage
"""

class HelpService:
    """Service for displaying help information"""
    
    @staticmethod
    def show_help():
        """Show application usage help"""
        print("=== CCM Database Management Tool ===")
        print()
        print("Usage:")
        print("  python main.py update             - Update tables from new XLSX files")
        print("  python main.py rollback           - Rollback from database backups")
        print("  python main.py rollback_from_local - Rollback from old local XLSX files")
        print("  python main.py help               - Show this help")
        print()
        print("Update process:")
        print("  1. Reads new XLSX files from data/new_xlsx/")
        print("  2. Creates database backups")
        print("  3. Shows comparison and updates if confirmed")
        print()
        print("Rollback process:")
        print("  1. Restores from database backup tables")
        print()
        print("Rollback from local process:")
        print("  1. Reads old XLSX files from documentation/old_data/")
        print("  2. Shows comparison and restores if confirmed")
