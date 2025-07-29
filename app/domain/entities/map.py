"""
Map domain model
"""

class Map:
    """Domain entity for map data"""
    
    def __init__(self, mag_id, segment, line_direction_type_id, stake,
                 map_type, epc, tid, polar, hide_enable, transverse,
                 longitudinal, curvature, coordinate_x, coordinate_y,
                 coordinate_e, coordinate_n, cruising_speed, limit_speed,
                 scene, station_type, station_num, signal_lamp,
                 one_way_road, meeting_vec, opposite_segment):
        self.mag_id = mag_id
        self.segment = segment
        self.line_direction_type_id = line_direction_type_id
        self.stake = stake
        self.map_type = map_type
        self.epc = epc
        self.tid = tid
        self.polar = polar
        self.hide_enable = hide_enable
        self.transverse = transverse
        self.longitudinal = longitudinal
        self.curvature = curvature
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.coordinate_e = coordinate_e
        self.coordinate_n = coordinate_n
        self.cruising_speed = cruising_speed
        self.limit_speed = limit_speed
        self.scene = scene
        self.station_type = station_type
        self.station_num = station_num
        self.signal_lamp = signal_lamp
        self.one_way_road = one_way_road
        self.meeting_vec = meeting_vec
        self.opposite_segment = opposite_segment
    
    def __str__(self):
        return f"Map(magId={self.mag_id}, stake={self.stake})"
