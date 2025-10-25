"""
Feature engineering utilities
"""
import pandas as pd
import numpy as np


def create_polynomial_features(df, columns, degree=2):
    """
    Create polynomial features
    
    Args:
        df: Input DataFrame
        columns: Columns to create polynomial features from
        degree: Degree of polynomial
        
    Returns:
        DataFrame with polynomial features
    """
    from sklearn.preprocessing import PolynomialFeatures
    
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    poly_features = poly.fit_transform(df[columns])
    
    feature_names = poly.get_feature_names_out(columns)
    poly_df = pd.DataFrame(poly_features, columns=feature_names, index=df.index)
    
    return pd.concat([df, poly_df], axis=1)


def create_interaction_features(df, col1, col2):
    """
    Create interaction features between two columns
    
    Args:
        df: Input DataFrame
        col1: First column
        col2: Second column
        
    Returns:
        DataFrame with interaction feature
    """
    df = df.copy()
    df[f'{col1}_x_{col2}'] = df[col1] * df[col2]
    return df


def create_date_features(df, date_column):
    """
    Extract features from date column
    
    Args:
        df: Input DataFrame
        date_column: Name of date column
        
    Returns:
        DataFrame with date features
    """
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column])
    
    df[f'{date_column}_year'] = df[date_column].dt.year
    df[f'{date_column}_month'] = df[date_column].dt.month
    df[f'{date_column}_day'] = df[date_column].dt.day
    df[f'{date_column}_dayofweek'] = df[date_column].dt.dayofweek
    df[f'{date_column}_quarter'] = df[date_column].dt.quarter
    
    return df
