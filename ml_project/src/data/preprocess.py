"""
Data preprocessing utilities
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder


def handle_missing_values(df, strategy='mean'):
    """
    Handle missing values in DataFrame
    
    Args:
        df: Input DataFrame
        strategy: Strategy for imputation ('mean', 'median', 'mode', 'drop')
        
    Returns:
        DataFrame with missing values handled
    """
    df = df.copy()
    
    if strategy == 'drop':
        return df.dropna()
    
    for col in df.columns:
        if df[col].isnull().any():
            if df[col].dtype in ['int64', 'float64']:
                if strategy == 'mean':
                    df[col].fillna(df[col].mean(), inplace=True)
                elif strategy == 'median':
                    df[col].fillna(df[col].median(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)
    
    return df


def encode_categorical(df, columns):
    """
    Encode categorical variables
    
    Args:
        df: Input DataFrame
        columns: List of categorical columns
        
    Returns:
        DataFrame with encoded categories
    """
    df = df.copy()
    
    for col in columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
    
    return df


def scale_features(X_train, X_test):
    """
    Scale numerical features
    
    Args:
        X_train: Training features
        X_test: Test features
        
    Returns:
        Scaled train and test sets
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, scaler
