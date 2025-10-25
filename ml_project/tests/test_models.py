"""
Tests for model training and evaluation
"""
import pytest
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from src.models.evaluate import evaluate_classification


def test_evaluate_classification():
    """Test classification evaluation metrics"""
    # Generate sample data
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    
    metrics = evaluate_classification(y_true, y_pred)
    
    assert 'accuracy' in metrics
    assert 'precision' in metrics
    assert 'recall' in metrics
    assert 'f1' in metrics
    assert 0 <= metrics['accuracy'] <= 1


def test_model_training():
    """Test basic model training"""
    X, y = make_classification(n_samples=100, n_features=10, random_state=42)
    
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)
    
    predictions = model.predict(X)
    assert len(predictions) == len(y)
    assert set(predictions).issubset(set(y))
