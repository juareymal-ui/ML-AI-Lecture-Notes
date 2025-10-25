"""
Helper utility functions
"""
import random
import numpy as np
import yaml
from pathlib import Path


def set_seed(seed=42):
    """
    Set random seed for reproducibility
    
    Args:
        seed: Random seed value
    """
    random.seed(seed)
    np.random.seed(seed)


def load_config(config_path='config/config.yaml'):
    """
    Load configuration from YAML file
    
    Args:
        config_path: Path to config file
        
    Returns:
        Configuration dictionary
    """
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def ensure_dir(directory):
    """
    Create directory if it doesn't exist
    
    Args:
        directory: Directory path
    """
    Path(directory).mkdir(parents=True, exist_ok=True)


def get_project_root():
    """Get project root directory"""
    return Path(__file__).parent.parent.parent
