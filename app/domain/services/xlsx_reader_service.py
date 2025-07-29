"""
XLSX reader service for reading Excel files
"""
import pandas as pd
import os


class XlsxReaderService:
    """Service for reading XLSX files"""
    
    def __init__(self):
        self.data_path = "../data/new_xlsx"  # Read from new_xlsx folder
        self.table_files = {
            'bamboopattern': 'bamboopattern.xlsx',
            'map': 'map.xlsx',
            'centerpos2x': 'centerpos2x.xlsx',
            'largescreenpixelpos': 'largescreenpixelpos.xlsx'
        }
    
    def read_all_files(self):
        """Read all XLSX files and return data count"""
        results = {}
        
        for table, filename in self.table_files.items():
            filepath = os.path.join(self.data_path, filename)
            
            if not os.path.exists(filepath):
                print(f"   ⚠️  File not found: {filepath}")
                results[table] = 0
                continue
            
            try:
                df = pd.read_excel(filepath)
                results[table] = len(df)
            except Exception as e:
                print(f"   ✗ Error reading {filename}: {e}")
                results[table] = 0
        
        return results
    
    def read_table_data(self, table_name):
        """Read specific table data"""
        if table_name not in self.table_files:
            raise ValueError(f"Unknown table: {table_name}")
        
        filename = self.table_files[table_name]
        filepath = os.path.join(self.data_path, filename)
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        return pd.read_excel(filepath)
