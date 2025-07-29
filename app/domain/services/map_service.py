"""
Map service
"""
from domain.repositories.map_repository import MapRepository
from infrastructure.repositories.mysql_map_repository import MySQLMapRepository


class MapService:
    """Service for map business logic"""
    
    def __init__(self, db_connection):
        self.repository: MapRepository = MySQLMapRepository(db_connection)
    
    def get_by_mag_id(self, mag_id: int):
        """Get map entry by mag ID"""
        return self.repository.find_by_mag_id(mag_id)
    
    def get_by_stake(self, stake: str):
        """Get map entry by stake"""
        return self.repository.find_by_stake(stake)
    
    def get_all_entries(self):
        """Get all map entries"""
        return self.repository.find_all()
    
    def get_total_count(self):
        """Get total count of entries"""
        return self.repository.count()
    
    def find_entries_by_segment(self, segment: int):
        """Business logic: find entries by segment"""
        all_entries = self.repository.find_all()
        return [e for e in all_entries if e.segment == segment]
