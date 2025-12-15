"""
Hemoglobin Prediction and Anemia Diagnosis

This script:
1. Takes blood parameters from user input
2. Predicts Hemoglobin using the trained regression model
3. Determines anemia status using clinical rules (not ML)

Usage:
    python predict.py
"""

import os
import joblib
from utils import anemia_decision, get_threshold


# Constants (must match train.py)
MODEL_DIR = 'model'
MODEL_FILENAME = 'hemoglobin_model.pkl'

# Valid ranges for blood parameters (for input validation)
VALID_RANGES = {
    'MCH': (15.0, 40.0),   # pg (picograms)
    'MCHC': (25.0, 40.0),  # g/dL
    'MCV': (60.0, 120.0)   # fL (femtoliters)
}


def load_model():
    """
    Load the saved model using joblib.
    
    Returns:
        dict: Contains 'model' and 'feature_columns'
    
    Raises:
        FileNotFoundError: If model file doesn't exist
    """
    filepath = os.path.join(MODEL_DIR, MODEL_FILENAME)
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Model file not found: {filepath}\n"
            "Please run 'python train.py' first to train the model."
        )
    
    model_data = joblib.load(filepath)
    return model_data


def validate_input(name, value, valid_range):
    """
    Validate that an input value is within a reasonable range.
    
    Args:
        name (str): Parameter name
        value (float): Input value
        valid_range (tuple): (min, max) acceptable range
    
    Returns:
        bool: True if valid, prints warning if outside range
    """
    min_val, max_val = valid_range
    
    if value < 0:
        raise ValueError(f"{name} cannot be negative: {value}")
    
    if value < min_val or value > max_val:
        print(f"  WARNING: {name}={value} is outside typical range ({min_val}-{max_val})")
        return False
    
    return True


def get_user_input():
    """
    Get blood parameters and gender from user via console.
    
    Features collected: MCH, MCHC, MCV
    Gender: "male" or "female" (string)
    
    Returns:
        tuple: (features_dict, gender_str)
    """
    print()
    print("=" * 50)
    print("  HEMOGLOBIN PREDICTION & ANEMIA DIAGNOSIS")
    print("=" * 50)
    print()
    print("Enter blood parameters:")
    print()
    
    # Collect blood parameters one by one
    try:
        mch = float(input("  MCH (pg): "))
        validate_input('MCH', mch, VALID_RANGES['MCH'])
        
        mchc = float(input("  MCHC (g/dL): "))
        validate_input('MCHC', mchc, VALID_RANGES['MCHC'])
        
        mcv = float(input("  MCV (fL): "))
        validate_input('MCV', mcv, VALID_RANGES['MCV'])
        
    except ValueError as e:
        raise ValueError(f"Invalid numeric input: {e}")
    
    # Collect gender (for clinical decision only, NOT for model)
    print()
    gender = input("  Gender (male/female): ").strip().lower()
    
    if gender not in ["male", "female"]:
        raise ValueError(
            f"Invalid gender: '{gender}'. "
            "Please enter 'male' or 'female'."
        )
    
    features = {
        'MCH': mch,
        'MCHC': mchc,
        'MCV': mcv
    }
    
    return features, gender


def predict_hemoglobin(model_data, features):
    """
    Predict Hemoglobin from blood parameters using Linear Regression.
    
    Args:
        model_data (dict): Loaded model data
        features (dict): Blood parameters {MCH, MCHC, MCV}
    
    Returns:
        float: Predicted Hemoglobin value (g/dL)
    """
    model = model_data['model']
    feature_columns = model_data['feature_columns']
    
    # Build feature array in correct order
    X = [[features[col] for col in feature_columns]]
    
    # Predict (no scaling needed - model was trained without scaling)
    hemoglobin = model.predict(X)[0]
    
    return hemoglobin


def display_results(predicted_hb, gender, status):
    """Display prediction results in a formatted way."""
    threshold = get_threshold(gender)
    
    print()
    print("-" * 50)
    print("  RESULTS")
    print("-" * 50)
    print(f"  Predicted Hemoglobin: {predicted_hb:.2f} g/dL")
    print(f"  Gender: {gender}")
    print(f"  Threshold: {threshold:.1f} g/dL")
    print()
    
    if status == "Anemia":
        print(f"  Anemia Status: ** {status} **")
        print(f"  (Hemoglobin is below {threshold:.1f} g/dL for {gender})")
    else:
        print(f"  Anemia Status: {status}")
    
    print("-" * 50)
    print()


def main():
    """Main prediction pipeline."""
    try:
        # 1. Load trained model
        model_data = load_model()
        print("Model loaded successfully.")
        
        # 2. Get user input (blood parameters + gender)
        features, gender = get_user_input()
        
        # 3. Predict Hemoglobin using Linear Regression
        predicted_hb = predict_hemoglobin(model_data, features)
        
        # 4. Determine anemia status using clinical rules (NOT ML)
        status = anemia_decision(predicted_hb, gender)
        
        # 5. Display results
        display_results(predicted_hb, gender, status)
        
    except FileNotFoundError as e:
        print()
        print(f"ERROR: {e}")
        print()
    except ValueError as e:
        print()
        print(f"ERROR: {e}")
        print()
    except KeyboardInterrupt:
        print()
        print("Operation cancelled by user.")
        print()


if __name__ == "__main__":
    main()
