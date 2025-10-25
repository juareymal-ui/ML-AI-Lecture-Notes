"""
Model training script
"""
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
    """Load configuration from YAML file"""
    with open('config/config.yaml', 'r') as f:
        return yaml.safe_load(f)


def train_model(X_train, y_train, model_type='random_forest', **params):
    """
    Train a machine learning model
    
    Args:
        X_train: Training features
        y_train: Training labels
        model_type: Type of model to train
        **params: Model parameters
        
    Returns:
        Trained model
    """
    if model_type == 'random_forest':
        model = RandomForestClassifier(**params)
    elif model_type == 'logistic_regression':
        model = LogisticRegression(**params)
    else:
        raise ValueError(f"Unknown model type: {model_type}")
    
    model.fit(X_train, y_train)
    return model


def main():
    """Main training pipeline"""
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
