"""
Data loading utilities
"""
import pandas as pd
from pathlib import Path


def load_raw_data(filepath):
    """
    Load raw data from file
    
    Args:
        filepath: Path to data file
        
    Returns:
        DataFrame with raw data
    """
    path = Path(filepath)
    
    if path.suffix == '.csv':
        return pd.read_csv(filepath)
    elif path.suffix == '.parquet':
        return pd.read_parquet(filepath)
    elif path.suffix in ['.xlsx', '.xls']:
        return pd.read_excel(filepath)
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")


def save_processed_data(df, filepath):
    """
    Save processed data
    
    Args:
        df: DataFrame to save
        filepath: Output path
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    if path.suffix == '.csv':
        df.to_csv(filepath, index=False)
    elif path.suffix == '.parquet':
        df.to_parquet(filepath, index=False)
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")
