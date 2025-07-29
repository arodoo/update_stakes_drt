"""
Bamboo pattern service
"""
from domain.repositories.bamboo_pattern_repository import BambooPatternRepository
from infrastructure.repositories.mysql_bamboo_repository import MySQLBambooRepository


class BambooService:
    """Service for bamboo pattern business logic"""
    
    def __init__(self, db_connection):
        self.repository: BambooPatternRepository = MySQLBambooRepository(db_connection)
    
    def get_by_mag_id(self, mag_id: int):
        """Get bamboo pattern by mag ID"""
        return self.repository.find_by_mag_id(mag_id)
    
    def get_by_stake(self, stake: str):
        """Get bamboo pattern by stake"""
        return self.repository.find_by_stake(stake)
    
    def get_all_patterns(self):
        """Get all bamboo patterns"""
        return self.repository.find_all()
    
    def get_total_count(self):
        """Get total count of patterns"""
        return self.repository.count()
    
    def find_patterns_by_line(self, line_id: int):
        """Business logic: find patterns by line ID"""
        all_patterns = self.repository.find_all()
        return [p for p in all_patterns if p.line_id == line_id]
