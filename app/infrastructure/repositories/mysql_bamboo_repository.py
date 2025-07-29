"""
MySQL implementation of bamboo pattern repository
"""
from typing import List, Optional
from domain.entities.bamboo_pattern import BambooPattern
from domain.repositories.bamboo_pattern_repository import BambooPatternRepository


class MySQLBambooRepository(BambooPatternRepository):
    """MySQL implementation of bamboo pattern repository"""
    
    def __init__(self, db_connection):
        self.db = db_connection
    
    def find_by_mag_id(self, mag_id: int) -> Optional[BambooPattern]:
        """Find bamboo pattern by mag ID"""
        query = """
        SELECT magId, stake, siteNumber, vehicleleft, top, 
               lineDirectionTypeId, lineId, platformName 
        FROM bamboopattern WHERE magId = %s
        """
        result = self.db.execute_one(query, (mag_id,))
        return self._map_to_entity(result) if result else None
    
    def find_by_stake(self, stake: str) -> Optional[BambooPattern]:
        """Find bamboo pattern by stake"""
        query = """
        SELECT magId, stake, siteNumber, vehicleleft, top, 
               lineDirectionTypeId, lineId, platformName 
        FROM bamboopattern WHERE stake = %s
        """
        result = self.db.execute_one(query, (stake,))
        return self._map_to_entity(result) if result else None
    
    def find_all(self) -> List[BambooPattern]:
        """Get all bamboo patterns"""
        query = """
        SELECT magId, stake, siteNumber, vehicleleft, top, 
               lineDirectionTypeId, lineId, platformName 
        FROM bamboopattern LIMIT 100
        """
        results = self.db.execute_query(query)
        return [self._map_to_entity(row) for row in results]
    
    def count(self) -> int:
        """Get total count of bamboo patterns"""
        query = "SELECT COUNT(*) FROM bamboopattern"
        result = self.db.execute_one(query)
        return result[0] if result else 0
    
    def _map_to_entity(self, row) -> BambooPattern:
        """Map database row to entity"""
        return BambooPattern(*row)
