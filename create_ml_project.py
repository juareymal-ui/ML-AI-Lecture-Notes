#!/usr/bin/env python3
"""
ML Project Structure Generator
Creates a complete directory structure for Machine Learning projects
"""

import os
from pathlib import Path


def create_ml_project_structure(project_name="ml_project"):
    """
    Creates a complete ML project directory structure
    
    Args:
        project_name: Name of the project directory
    """
    
    # Define the structure
    structure = {
        project_name: {
            "data": {
                "raw": {},
                "processed": {},
                "interim": {},
                "external": {}
            },
            "notebooks": {},
            "src": {
                "data": {},
                "features": {},
                "models": {},
                "visualization": {},
                "utils": {}
            },
            "models": {},
            "reports": {
                "figures": {}
            },
            "tests": {},
            "config": {},
            "docs": {}
        }
    }
    
    # Files to create with their content
    files = {
        f"{project_name}/README.md": readme_content(),
        f"{project_name}/requirements.txt": requirements_content(),
        f"{project_name}/setup.py": setup_content(project_name),
        f"{project_name}/.gitignore": gitignore_content(),
        f"{project_name}/config/config.yaml": config_yaml_content(),
        f"{project_name}/config/__init__.py": "",
        f"{project_name}/src/__init__.py": "",
        f"{project_name}/src/data/__init__.py": "",
        f"{project_name}/src/data/load_data.py": load_data_content(),
        f"{project_name}/src/data/preprocess.py": preprocess_content(),
        f"{project_name}/src/features/__init__.py": "",
        f"{project_name}/src/features/build_features.py": build_features_content(),
        f"{project_name}/src/models/__init__.py": "",
        f"{project_name}/src/models/train.py": train_content(),
        f"{project_name}/src/models/predict.py": predict_content(),
        f"{project_name}/src/models/evaluate.py": evaluate_content(),
        f"{project_name}/src/visualization/__init__.py": "",
        f"{project_name}/src/visualization/visualize.py": visualize_content(),
        f"{project_name}/src/utils/__init__.py": "",
        f"{project_name}/src/utils/helpers.py": helpers_content(),
        f"{project_name}/tests/__init__.py": "",
        f"{project_name}/tests/test_data.py": test_data_content(),
        f"{project_name}/tests/test_models.py": test_models_content(),
        f"{project_name}/notebooks/01_exploration.ipynb": "",
        f"{project_name}/notebooks/02_preprocessing.ipynb": "",
        f"{project_name}/notebooks/03_modeling.ipynb": "",
        f"{project_name}/reports/results.md": "# Results\n\n## Model Performance\n\n## Insights\n",
        f"{project_name}/docs/project_overview.md": docs_content(),
    }
    
    # Create directories
    def create_dirs(d, parent=""):
        for key, value in d.items():
            path = os.path.join(parent, key)
            Path(path).mkdir(parents=True, exist_ok=True)
            if value:
                create_dirs(value, path)
    
    create_dirs(structure)
    
    # Create files
    for filepath, content in files.items():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"✓ ML Project structure '{project_name}' created successfully!")
    print(f"\nNext steps:")
    print(f"  cd {project_name}")
    print(f"  python -m venv venv")
    print(f"  source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
    print(f"  pip install -r requirements.txt")


def readme_content():
    return """# ML Project

## Project Overview
Brief description of the project, objectives, and business problem.

## Project Structure
```
├── data/               # Data directory
│   ├── raw/           # Original, immutable data
│   ├── processed/     # Cleaned, transformed data
│   ├── interim/       # Intermediate transformations
│   └── external/      # Third-party data
├── notebooks/         # Jupyter notebooks for exploration
├── src/               # Source code
│   ├── data/         # Data loading and preprocessing
│   ├── features/     # Feature engineering
│   ├── models/       # Model training and evaluation
│   ├── visualization/ # Visualization utilities
│   └── utils/        # Helper functions
├── models/           # Trained models
├── reports/          # Generated reports and figures
├── tests/            # Unit tests
└── config/           # Configuration files
```

## Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```

## Usage
```bash
# Train model
python src/models/train.py

# Make predictions
python src/models/predict.py

# Run tests
pytest tests/
```

## Data
- **Source**: [Data source description]
- **Size**: [Dataset size]
- **Features**: [Number and description of features]

## Model
- **Algorithm**: [Model type]
- **Performance**: [Key metrics]

## Results
See `reports/results.md` for detailed results.

## Contributors
- [Your Name]

## License
MIT License
"""


def requirements_content():
    return """# Core ML libraries
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.3.0
scipy>=1.11.0

# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0

# Data processing
joblib>=1.3.0

# Configuration
pyyaml>=6.0
python-dotenv>=1.0.0

# Jupyter
jupyter>=1.0.0
ipykernel>=6.23.0

# Testing
pytest>=7.3.0
pytest-cov>=4.1.0

# Code quality
black>=23.3.0
flake8>=6.0.0
mypy>=1.3.0

# Optional: Deep Learning (uncomment if needed)
# torch>=2.0.0
# tensorflow>=2.12.0

# Optional: Advanced ML (uncomment if needed)
# xgboost>=1.7.0
# lightgbm>=3.3.0
# catboost>=1.2.0
"""


def setup_content(project_name):
    return f"""from setuptools import find_packages, setup

setup(
    name='{project_name}',
    version='0.1.0',
    packages=find_packages(),
    description='Machine Learning Project',
    author='Your Name',
    author_email='your.email@example.com',
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'pyyaml',
    ],
    python_requires='>=3.8',
)
"""


def gitignore_content():
    return """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebook
.ipynb_checkpoints
*.ipynb_checkpoints

# Data
data/raw/*
data/processed/*
data/interim/*
data/external/*
!data/raw/.gitkeep
!data/processed/.gitkeep
!data/interim/.gitkeep
!data/external/.gitkeep

# Models
models/*.pkl
models/*.h5
models/*.pt
models/*.pth
*.joblib

# IDE
.vscode/
.idea/
*.swp
*.swo
.DS_Store

# Environment
.env
.envrc

# Logs
logs/
*.log

# Reports
reports/figures/*.png
reports/figures/*.pdf
"""


def config_yaml_content():
    return """# Configuration for ML project

data:
  raw_path: "data/raw"
  processed_path: "data/processed"
  train_test_split: 0.2
  random_state: 42

model:
  type: "random_forest"
  params:
    n_estimators: 100
    max_depth: 10
    random_state: 42

training:
  cv_folds: 5
  scoring: "accuracy"
  
features:
  numerical: []
  categorical: []
  target: ""

output:
  model_path: "models/model.pkl"
  figures_path: "reports/figures"
"""


def load_data_content():
    return """\"\"\"
Data loading utilities
\"\"\"
import pandas as pd
from pathlib import Path


def load_raw_data(filepath):
    \"\"\"
    Load raw data from file
    
    Args:
        filepath: Path to data file
        
    Returns:
        DataFrame with raw data
    \"\"\"
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
    \"\"\"
    Save processed data
    
    Args:
        df: DataFrame to save
        filepath: Output path
    \"\"\"
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    if path.suffix == '.csv':
        df.to_csv(filepath, index=False)
    elif path.suffix == '.parquet':
        df.to_parquet(filepath, index=False)
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")
"""


def preprocess_content():
    return """\"\"\"
Data preprocessing utilities
\"\"\"
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder


def handle_missing_values(df, strategy='mean'):
    \"\"\"
    Handle missing values in DataFrame
    
    Args:
        df: Input DataFrame
        strategy: Strategy for imputation ('mean', 'median', 'mode', 'drop')
        
    Returns:
        DataFrame with missing values handled
    \"\"\"
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
    \"\"\"
    Encode categorical variables
    
    Args:
        df: Input DataFrame
        columns: List of categorical columns
        
    Returns:
        DataFrame with encoded categories
    \"\"\"
    df = df.copy()
    
    for col in columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
    
    return df


def scale_features(X_train, X_test):
    \"\"\"
    Scale numerical features
    
    Args:
        X_train: Training features
        X_test: Test features
        
    Returns:
        Scaled train and test sets
    \"\"\"
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, scaler
"""


def build_features_content():
    return """\"\"\"
Feature engineering utilities
\"\"\"
import pandas as pd
import numpy as np


def create_polynomial_features(df, columns, degree=2):
    \"\"\"
    Create polynomial features
    
    Args:
        df: Input DataFrame
        columns: Columns to create polynomial features from
        degree: Degree of polynomial
        
    Returns:
        DataFrame with polynomial features
    \"\"\"
    from sklearn.preprocessing import PolynomialFeatures
    
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    poly_features = poly.fit_transform(df[columns])
    
    feature_names = poly.get_feature_names_out(columns)
    poly_df = pd.DataFrame(poly_features, columns=feature_names, index=df.index)
    
    return pd.concat([df, poly_df], axis=1)


def create_interaction_features(df, col1, col2):
    \"\"\"
    Create interaction features between two columns
    
    Args:
        df: Input DataFrame
        col1: First column
        col2: Second column
        
    Returns:
        DataFrame with interaction feature
    \"\"\"
    df = df.copy()
    df[f'{col1}_x_{col2}'] = df[col1] * df[col2]
    return df


def create_date_features(df, date_column):
    \"\"\"
    Extract features from date column
    
    Args:
        df: Input DataFrame
        date_column: Name of date column
        
    Returns:
        DataFrame with date features
    \"\"\"
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column])
    
    df[f'{date_column}_year'] = df[date_column].dt.year
    df[f'{date_column}_month'] = df[date_column].dt.month
    df[f'{date_column}_day'] = df[date_column].dt.day
    df[f'{date_column}_dayofweek'] = df[date_column].dt.dayofweek
    df[f'{date_column}_quarter'] = df[date_column].dt.quarter
    
    return df
"""


def train_content():
    return """\"\"\"
Model training script
\"\"\"
import yaml
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

import sys
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.data.load_data import load_raw_data
from src.data.preprocess import handle_missing_values, encode_categorical


def load_config():
    \"\"\"Load configuration from YAML file\"\"\"
    with open('config/config.yaml', 'r') as f:
        return yaml.safe_load(f)


def train_model(X_train, y_train, model_type='random_forest', **params):
    \"\"\"
    Train a machine learning model
    
    Args:
        X_train: Training features
        y_train: Training labels
        model_type: Type of model to train
        **params: Model parameters
        
    Returns:
        Trained model
    \"\"\"
    if model_type == 'random_forest':
        model = RandomForestClassifier(**params)
    elif model_type == 'logistic_regression':
        model = LogisticRegression(**params)
    else:
        raise ValueError(f"Unknown model type: {model_type}")
    
    model.fit(X_train, y_train)
    return model


def main():
    \"\"\"Main training pipeline\"\"\"
    # Load configuration
    config = load_config()
    
    # Load data
    print("Loading data...")
    # df = load_raw_data(config['data']['raw_path'])
    
    # Preprocess
    print("Preprocessing...")
    # df = handle_missing_values(df)
    
    # Split features and target
    # X = df.drop(columns=[config['features']['target']])
    # y = df[config['features']['target']]
    
    # Train-test split
    # X_train, X_test, y_train, y_test = train_test_split(
    #     X, y, 
    #     test_size=config['data']['train_test_split'],
    #     random_state=config['data']['random_state']
    # )
    
    # Train model
    print("Training model...")
    # model = train_model(
    #     X_train, y_train,
    #     model_type=config['model']['type'],
    #     **config['model']['params']
    # )
    
    # Cross-validation
    # scores = cross_val_score(model, X_train, y_train, 
    #                          cv=config['training']['cv_folds'],
    #                          scoring=config['training']['scoring'])
    # print(f"Cross-validation scores: {scores}")
    # print(f"Mean CV score: {scores.mean():.4f} (+/- {scores.std():.4f})")
    
    # Save model
    # model_path = Path(config['output']['model_path'])
    # model_path.parent.mkdir(parents=True, exist_ok=True)
    # joblib.dump(model, model_path)
    # print(f"Model saved to {model_path}")
    
    print("Training complete!")


if __name__ == '__main__':
    main()
"""


def predict_content():
    return """\"\"\"
Model prediction script
\"\"\"
import joblib
import pandas as pd
from pathlib import Path


def load_model(model_path):
    \"\"\"Load trained model\"\"\"
    return joblib.load(model_path)


def make_predictions(model, X):
    \"\"\"
    Make predictions on new data
    
    Args:
        model: Trained model
        X: Features for prediction
        
    Returns:
        Predictions
    \"\"\"
    predictions = model.predict(X)
    
    # Get prediction probabilities if available
    if hasattr(model, 'predict_proba'):
        probabilities = model.predict_proba(X)
        return predictions, probabilities
    
    return predictions, None


def main():
    \"\"\"Main prediction pipeline\"\"\"
    # Load model
    model_path = 'models/model.pkl'
    model = load_model(model_path)
    
    # Load new data
    # X_new = pd.read_csv('data/new_data.csv')
    
    # Make predictions
    # predictions, probabilities = make_predictions(model, X_new)
    
    # Save predictions
    # results = pd.DataFrame({
    #     'prediction': predictions,
    #     'probability': probabilities[:, 1] if probabilities is not None else None
    # })
    # results.to_csv('data/predictions.csv', index=False)
    
    print("Predictions complete!")


if __name__ == '__main__':
    main()
"""


def evaluate_content():
    return """\"\"\"
Model evaluation utilities
\"\"\"
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)
import numpy as np


def evaluate_classification(y_true, y_pred, y_proba=None):
    \"\"\"
    Evaluate classification model performance
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        y_proba: Prediction probabilities (optional)
        
    Returns:
        Dictionary of metrics
    \"\"\"
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='weighted'),
        'recall': recall_score(y_true, y_pred, average='weighted'),
        'f1': f1_score(y_true, y_pred, average='weighted'),
    }
    
    if y_proba is not None and len(np.unique(y_true)) == 2:
        metrics['roc_auc'] = roc_auc_score(y_true, y_proba[:, 1])
    
    print("\\nClassification Metrics:")
    print("-" * 40)
    for metric, value in metrics.items():
        print(f"{metric.capitalize()}: {value:.4f}")
    
    print("\\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    
    print("\\nClassification Report:")
    print(classification_report(y_true, y_pred))
    
    return metrics


def evaluate_regression(y_true, y_pred):
    \"\"\"
    Evaluate regression model performance
    
    Args:
        y_true: True values
        y_pred: Predicted values
        
    Returns:
        Dictionary of metrics
    \"\"\"
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    
    metrics = {
        'mse': mean_squared_error(y_true, y_pred),
        'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
        'mae': mean_absolute_error(y_true, y_pred),
        'r2': r2_score(y_true, y_pred)
    }
    
    print("\\nRegression Metrics:")
    print("-" * 40)
    for metric, value in metrics.items():
        print(f"{metric.upper()}: {value:.4f}")
    
    return metrics
"""


def visualize_content():
    return """\"\"\"
Visualization utilities
\"\"\"
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, auc


def plot_confusion_matrix(y_true, y_pred, labels=None, save_path=None):
    \"\"\"Plot confusion matrix\"\"\"
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=labels, yticklabels=labels)
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()


def plot_roc_curve(y_true, y_proba, save_path=None):
    \"\"\"Plot ROC curve\"\"\"
    fpr, tpr, _ = roc_curve(y_true, y_proba)
    roc_auc = auc(fpr, tpr)
    
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, 
             label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.grid(alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()


def plot_feature_importance(model, feature_names, top_n=20, save_path=None):
    \"\"\"Plot feature importance\"\"\"
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1][:top_n]
        
        plt.figure(figsize=(10, 6))
        plt.title(f'Top {top_n} Feature Importances')
        plt.barh(range(top_n), importances[indices])
        plt.yticks(range(top_n), [feature_names[i] for i in indices])
        plt.xlabel('Importance')
        plt.gca().invert_yaxis()
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        plt.show()
"""


def helpers_content():
    return """\"\"\"
Helper utility functions
\"\"\"
import random
import numpy as np
import yaml
from pathlib import Path


def set_seed(seed=42):
    \"\"\"
    Set random seed for reproducibility
    
    Args:
        seed: Random seed value
    \"\"\"
    random.seed(seed)
    np.random.seed(seed)


def load_config(config_path='config/config.yaml'):
    \"\"\"
    Load configuration from YAML file
    
    Args:
        config_path: Path to config file
        
    Returns:
        Configuration dictionary
    \"\"\"
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def ensure_dir(directory):
    \"\"\"
    Create directory if it doesn't exist
    
    Args:
        directory: Directory path
    \"\"\"
    Path(directory).mkdir(parents=True, exist_ok=True)


def get_project_root():
    \"\"\"Get project root directory\"\"\"
    return Path(__file__).parent.parent.parent
"""


def test_data_content():
    return """\"\"\"
Tests for data processing functions
\"\"\"
import pytest
import pandas as pd
import numpy as np
from src.data.preprocess import handle_missing_values, encode_categorical


def test_handle_missing_values_mean():
    \"\"\"Test missing value imputation with mean strategy\"\"\"
    df = pd.DataFrame({
        'a': [1, 2, np.nan, 4],
        'b': [1, 2, 3, 4]
    })
    
    result = handle_missing_values(df, strategy='mean')
    assert not result.isnull().any().any()
    assert result['a'].iloc[2] == 2.333333333333333  # mean of 1, 2, 4


def test_encode_categorical():
    \"\"\"Test categorical encoding\"\"\"
    df = pd.DataFrame({
        'category': ['A', 'B', 'C', 'A', 'B']
    })
    
    result = encode_categorical(df, ['category'])
    assert result['category'].dtype in [np.int32, np.int64]
    assert len(result['category'].unique()) == 3
"""


def test_models_content():
    return """\"\"\"
Tests for model training and evaluation
\"\"\"
import pytest
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from src.models.evaluate import evaluate_classification


def test_evaluate_classification():
    \"\"\"Test classification evaluation metrics\"\"\"
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
    \"\"\"Test basic model training\"\"\"
    X, y = make_classification(n_samples=100, n_features=10, random_state=42)
    
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)
    
    predictions = model.predict(X)
    assert len(predictions) == len(y)
    assert set(predictions).issubset(set(y))
"""


def docs_content():
    return """# Project Overview

## Objective
Describe the main goal of your ML project here.

## Dataset
- **Source**: 
- **Size**: 
- **Features**: 
- **Target Variable**: 

## Methodology
1. Data Collection
2. Exploratory Data Analysis
3. Feature Engineering
4. Model Selection
5. Training and Evaluation
6. Deployment

## Models Evaluated
- Model 1: Description and performance
- Model 2: Description and performance

## Best Model
- **Algorithm**: 
- **Hyperparameters**: 
- **Performance Metrics**: 

## Future Work
- Improvement 1
- Improvement 2

## References
- Reference 1
- Reference 2
"""


if __name__ == "__main__":
    import sys
    
    project_name = sys.argv[1] if len(sys.argv) > 1 else "ml_project"
    create_ml_project_structure(project_name)