"""
MySQL implementation of map repository
"""
from typing import List, Optional
from domain.entities.map import Map
from domain.repositories.map_repository import MapRepository


class MySQLMapRepository(MapRepository):
    """MySQL implementation of map repository"""
    
    def __init__(self, db_connection):
        self.db = db_connection
    
    def find_by_mag_id(self, mag_id: int) -> Optional[Map]:
        """Find map entry by mag ID"""
        query = """
        SELECT magId, segment, lineDirectionTypeId, stake, type, epc, tid, 
               polar, hidenEnable, transverse, longitudinal, curvature, 
               coordinateX, coordinateY, coordinateE, coordinateN, 
               cruisingSpeed, limitSpeed, scene, stationType, stationNum, 
               signallamp, oneWayRoad, meetingVec, oppositeSegment 
        FROM map WHERE magId = %s
        """
        result = self.db.execute_one(query, (mag_id,))
        return self._map_to_entity(result) if result else None
    
    def find_by_stake(self, stake: str) -> Optional[Map]:
        """Find map entry by stake"""
        query = """
        SELECT magId, segment, lineDirectionTypeId, stake, type, epc, tid, 
               polar, hidenEnable, transverse, longitudinal, curvature, 
               coordinateX, coordinateY, coordinateE, coordinateN, 
               cruisingSpeed, limitSpeed, scene, stationType, stationNum, 
               signallamp, oneWayRoad, meetingVec, oppositeSegment 
        FROM map WHERE stake = %s
        """
        result = self.db.execute_one(query, (stake,))
        return self._map_to_entity(result) if result else None
    
    def find_all(self) -> List[Map]:
        """Get all map entries (limited for performance)"""
        query = """
        SELECT magId, segment, lineDirectionTypeId, stake, type, epc, tid, 
               polar, hidenEnable, transverse, longitudinal, curvature, 
               coordinateX, coordinateY, coordinateE, coordinateN, 
               cruisingSpeed, limitSpeed, scene, stationType, stationNum, 
               signallamp, oneWayRoad, meetingVec, oppositeSegment 
        FROM map LIMIT 100
        """
        results = self.db.execute_query(query)
        return [self._map_to_entity(row) for row in results]
    
    def count(self) -> int:
        """Get total count of map entries"""
        query = "SELECT COUNT(*) FROM map"
        result = self.db.execute_one(query)
        return result[0] if result else 0
    
    def _map_to_entity(self, row) -> Map:
        """Map database row to entity"""
        return Map(*row)
