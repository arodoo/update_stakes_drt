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
        print("  python main.py [COMMAND] [DATABASE_TARGET]")
        print()
        print("COMMANDS:")
        print("  update             - Update tables from new XLSX files")
        print("  rollback           - Rollback from database backups")
        print("  rollback_from_local - Rollback from old local XLSX files")
        print("  help               - Show this help")
        print()
        print("DATABASE_TARGET (optional, defaults to 'local'):")
        print("  local              - Use local database (stakes)")
        print("                       Host: localhost, User: root, Pass: root")
        print("  remote             - Use remote database (drt_fleet)")
        print("                       Host: 172.17.200.183, User: campeche")
        print()
        print("EXAMPLES:")
        print("  python main.py update              → Update LOCAL database")
        print("  python main.py update local        → Update LOCAL database")
        print("  python main.py update remote       → Update REMOTE database")
        print("  python main.py rollback remote     → Rollback REMOTE database")
        print()
        print("DATA SOURCES:")
        print("  • New XLSX files: data/new_xlsx/")
        print("  • Old XLSX files: documentation/old_data/")
        print()
        print("PROCESS DETAILS:")
        print("Update process:")
        print("  1. Reads new XLSX files from data/new_xlsx/")
        print("  2. Creates database backups")
        print("  3. Shows detailed comparison and updates if confirmed")
        print()
        print("Rollback process:")
        print("  1. Restores from database backup tables")
        print()
        print("Rollback from local process:")
        print("  1. Reads old XLSX files from documentation/old_data/")
        print("  2. Shows detailed comparison and restores if confirmed")
