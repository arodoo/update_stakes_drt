"""
Bamboo pattern domain model
"""

class BambooPattern:
    """Domain entity for bamboo pattern data"""
    
    def __init__(self, mag_id, stake, site_number, vehicle_left, 
                 top, line_direction_type_id, line_id, platform_name):
        self.mag_id = mag_id
        self.stake = stake
        self.site_number = site_number
        self.vehicle_left = vehicle_left
        self.top = top
        self.line_direction_type_id = line_direction_type_id
        self.line_id = line_id
        self.platform_name = platform_name
    
    def __str__(self):
        return f"BambooPattern(magId={self.mag_id}, stake={self.stake})"
    
    def to_dict(self):
        """Convert to dictionary representation"""
        return {
            'magId': self.mag_id,
            'stake': self.stake,
            'siteNumber': self.site_number,
            'vehicleleft': self.vehicle_left,
            'top': self.top,
            'lineDirectionTypeId': self.line_direction_type_id,
            'lineId': self.line_id,
            'platformName': self.platform_name
        }
