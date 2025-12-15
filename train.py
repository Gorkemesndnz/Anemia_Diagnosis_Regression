"""
Hemoglobin Regression Model Training

This script trains a Linear Regression model to predict Hemoglobin
from blood parameters and saves it using joblib.

Features used: MCH, MCHC, MCV
Target: Hemoglobin

Usage:
    python train.py
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib


# Constants
FEATURE_COLUMNS = ['MCH', 'MCHC', 'MCV']
TARGET_COLUMN = 'Hemoglobin'
MODEL_FILENAME = 'hemoglobin_model.pkl'
TEST_SIZE = 0.2
RANDOM_STATE = 42


def load_data(filepath):
    """Load the dataset from CSV file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found: {filepath}")
    
    df = pd.read_csv(filepath)
    print(f"Dataset loaded: {len(df)} rows")
    return df


def check_missing_values(df):
    """Check for missing values in the dataset."""
    missing = df.isnull().sum()
    total_missing = missing.sum()
    
    if total_missing > 0:
        print("WARNING: Missing values found:")
        for col in missing[missing > 0].index:
            print(f"  - {col}: {missing[col]} missing")
        return True
    else:
        print("No missing values found.")
        return False


def validate_data(df):
    """Validate that required columns exist and values are reasonable."""
    # Check required columns
    required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]
    missing_cols = [col for col in required_columns if col not in df.columns]
    
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    # Check for negative values in features
    for col in FEATURE_COLUMNS + [TARGET_COLUMN]:
        if (df[col] < 0).any():
            print(f"WARNING: Negative values found in {col}")
    
    print("Data validation passed.")


def prepare_features(df):
    """
    Prepare features and target variable.
    
    Features: MCH, MCHC, MCV (blood parameters)
    Target: Hemoglobin
    
    Note: Gender is NOT used as a feature.
          It is only used for clinical decision logic.
    """
    X = df[FEATURE_COLUMNS].values
    y = df[TARGET_COLUMN].values
    
    print(f"Features: {FEATURE_COLUMNS}")
    print(f"Target: {TARGET_COLUMN}")
    
    return X, y


def train_model(X_train, y_train):
    """Train a Linear Regression model (no scaling applied)."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate model performance using regression metrics only.
    
    Metrics:
        - MAE: Mean Absolute Error
        - RMSE: Root Mean Squared Error
        - R2: Coefficient of Determination
    """
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    return {
        'MAE': mae,
        'RMSE': rmse,
        'R2': r2,
        'n_samples': len(y_test)
    }


def save_model(model, model_dir='model'):
    """
    Save the trained model and metadata using joblib.
    
    Saved data includes:
        - model: Trained LinearRegression model
        - feature_columns: List of feature names used
    """
    os.makedirs(model_dir, exist_ok=True)
    
    model_data = {
        'model': model,
        'feature_columns': FEATURE_COLUMNS
    }
    
    filepath = os.path.join(model_dir, MODEL_FILENAME)
    joblib.dump(model_data, filepath)
    
    print(f"Model saved: {filepath}")


def main():
    """Main training pipeline."""
    print()
    print("=" * 50)
    print("  HEMOGLOBIN REGRESSION MODEL TRAINING")
    print("=" * 50)
    print()
    
    # 1. Load data
    data_path = os.path.join('data', 'anemia.csv')
    df = load_data(data_path)
    
    # 2. Validate data
    validate_data(df)
    
    # 3. Check for missing values
    has_missing = check_missing_values(df)
    if has_missing:
        print("Dropping rows with missing values...")
        df = df.dropna(subset=FEATURE_COLUMNS + [TARGET_COLUMN])
        print(f"Remaining rows: {len(df)}")
    
    # 4. Prepare features (Gender NOT included)
    X, y = prepare_features(df)
    
    # 5. Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )
    print()
    print(f"Training set: {len(X_train)} samples")
    print(f"Test set: {len(X_test)} samples")
    
    # 6. Train model
    print()
    print("Training Linear Regression model...")
    model = train_model(X_train, y_train)
    print("Training complete.")
    
    # 7. Evaluate model (regression metrics only)
    metrics = evaluate_model(model, X_test, y_test)
    
    print()
    print("-" * 50)
    print("  MODEL PERFORMANCE (Test Set)")
    print("-" * 50)
    print(f"  MAE:  {metrics['MAE']:.4f} g/dL")
    print(f"  RMSE: {metrics['RMSE']:.4f} g/dL")
    print(f"  R2:   {metrics['R2']:.4f}")
    print("-" * 50)
    
    # 8. Save model
    print()
    save_model(model)
    
    print()
    print("Training completed successfully!")
    print("To make predictions, run: python predict.py")
    print()


if __name__ == "__main__":
    main()
