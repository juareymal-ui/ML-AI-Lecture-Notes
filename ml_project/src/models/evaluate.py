"""
Model evaluation utilities
"""
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)
import numpy as np


def evaluate_classification(y_true, y_pred, y_proba=None):
    """
    Evaluate classification model performance
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        y_proba: Prediction probabilities (optional)
        
    Returns:
        Dictionary of metrics
    """
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='weighted'),
        'recall': recall_score(y_true, y_pred, average='weighted'),
        'f1': f1_score(y_true, y_pred, average='weighted'),
    }
    
    if y_proba is not None and len(np.unique(y_true)) == 2:
        metrics['roc_auc'] = roc_auc_score(y_true, y_proba[:, 1])
    
    print("\nClassification Metrics:")
    print("-" * 40)
    for metric, value in metrics.items():
        print(f"{metric.capitalize()}: {value:.4f}")
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))
    
    return metrics


def evaluate_regression(y_true, y_pred):
    """
    Evaluate regression model performance
    
    Args:
        y_true: True values
        y_pred: Predicted values
        
    Returns:
        Dictionary of metrics
    """
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    
    metrics = {
        'mse': mean_squared_error(y_true, y_pred),
        'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
        'mae': mean_absolute_error(y_true, y_pred),
        'r2': r2_score(y_true, y_pred)
    }
    
    print("\nRegression Metrics:")
    print("-" * 40)
    for metric, value in metrics.items():
        print(f"{metric.upper()}: {value:.4f}")
    
    return metrics
