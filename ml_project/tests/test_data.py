"""
Tests for data processing functions
"""
import pytest
import pandas as pd
import numpy as np
from src.data.preprocess import handle_missing_values, encode_categorical


def test_handle_missing_values_mean():
    """Test missing value imputation with mean strategy"""
    df = pd.DataFrame({
        'a': [1, 2, np.nan, 4],
        'b': [1, 2, 3, 4]
    })
    
    result = handle_missing_values(df, strategy='mean')
    assert not result.isnull().any().any()
    assert result['a'].iloc[2] == 2.333333333333333  # mean of 1, 2, 4


def test_encode_categorical():
    """Test categorical encoding"""
    df = pd.DataFrame({
        'category': ['A', 'B', 'C', 'A', 'B']
    })
    
    result = encode_categorical(df, ['category'])
    assert result['category'].dtype in [np.int32, np.int64]
    assert len(result['category'].unique()) == 3
