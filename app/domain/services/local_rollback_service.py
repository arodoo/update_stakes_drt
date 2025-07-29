"""
Local rollback service for reading old XLSX files
"""
import pandas as pd
import os


class LocalRollbackService:
    """Service for rollback from local old XLSX files"""
    
    def __init__(self):
        self.old_data_path = "../documentation/old_data"
        self.table_files = {
            'bamboopattern': 'bamboopattern.xlsx',
            'map': 'map.xlsx',
            'centerpos2x': 'centerpos2x.xlsx',
            'largescreenpixelpos': 'largescreenpixelpos.xlsx'
        }
    
    def read_old_files(self):
        """Read all old XLSX files and return data count"""
        results = {}
        
        for table, filename in self.table_files.items():
            filepath = os.path.join(self.old_data_path, filename)
            
            if not os.path.exists(filepath):
                print(f"   ⚠️  Old file not found: {filepath}")
                results[table] = 0
                continue
            
            try:
                df = pd.read_excel(filepath)
                results[table] = len(df)
            except Exception as e:
                print(f"   ✗ Error reading old {filename}: {e}")
                results[table] = 0
        
        return results
    
    def read_old_table_data(self, table_name):
        """Read specific old table data"""
        if table_name not in self.table_files:
            raise ValueError(f"Unknown table: {table_name}")
        
        filename = self.table_files[table_name]
        filepath = os.path.join(self.old_data_path, filename)
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Old file not found: {filepath}")
        
        return pd.read_excel(filepath)
