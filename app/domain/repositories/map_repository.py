"""
Map repository interface
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.map import Map


class MapRepository(ABC):
    """Abstract repository for map operations"""
    
    @abstractmethod
    def find_by_mag_id(self, mag_id: int) -> Optional[Map]:
        """Find map entry by mag ID"""
        pass
    
    @abstractmethod
    def find_by_stake(self, stake: str) -> Optional[Map]:
        """Find map entry by stake"""
        pass
    
    @abstractmethod
    def find_all(self) -> List[Map]:
        """Get all map entries"""
        pass
    
    @abstractmethod
    def count(self) -> int:
        """Get total count of map entries"""
        pass
