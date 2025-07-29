"""
Command handler for processing user commands
"""
from infrastructure.database import DatabaseConnection
from domain.services.backup_service import BackupService
from domain.services.update_service import UpdateService
from domain.services.xlsx_reader_service import XlsxReaderService
from domain.services.local_rollback_service import LocalRollbackService
from application.update_handler import UpdateHandler
from application.rollback_handler import RollbackHandler
from application.local_rollback_handler import LocalRollbackHandler


class CommandHandler:
    """Handles application commands"""
    
    def __init__(self, use_local=True):
        self.db_connection = DatabaseConnection(use_local=use_local)
        self.backup_service = BackupService(self.db_connection)
        self.update_service = UpdateService(self.db_connection)
        self.xlsx_reader = XlsxReaderService()
        self.local_rollback_service = LocalRollbackService()
    
    def handle_update(self):
        """Handle update command"""
        try:
            handler = UpdateHandler(
                self.backup_service, 
                self.update_service, 
                self.xlsx_reader
            )
            handler.execute()
        finally:
            self.db_connection.close()
    
    def handle_rollback(self):
        """Handle rollback command"""
        try:
            handler = RollbackHandler(
                self.backup_service, 
                self.update_service
            )
            handler.execute()
        finally:
            self.db_connection.close()
    
    def handle_rollback_from_local(self):
        """Handle rollback from local XLSX command"""
        try:
            handler = LocalRollbackHandler(
                self.update_service,
                self.local_rollback_service
            )
            handler.execute()
        finally:
            self.db_connection.close()
