"""
Bamboo pattern repository interface
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.bamboo_pattern import BambooPattern


class BambooPatternRepository(ABC):
    """Abstract repository for bamboo pattern operations"""
    
    @abstractmethod
    def find_by_mag_id(self, mag_id: int) -> Optional[BambooPattern]:
        """Find bamboo pattern by mag ID"""
        pass
    
    @abstractmethod
    def find_by_stake(self, stake: str) -> Optional[BambooPattern]:
        """Find bamboo pattern by stake"""
        pass
    
    @abstractmethod
    def find_all(self) -> List[BambooPattern]:
        """Get all bamboo patterns"""
        pass
    
    @abstractmethod
    def count(self) -> int:
        """Get total count of bamboo patterns"""
        pass
