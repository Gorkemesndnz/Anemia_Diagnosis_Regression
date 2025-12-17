"""
Clinical Anemia Decision Logic

This module contains rule-based clinical logic for anemia diagnosis.
This is NOT a machine learning model.

WHO Threshold Values:
    - Male (m):   Hemoglobin < 13 g/dL → Anemia
    - Female (f): Hemoglobin < 12 g/dL → Anemia

Gender input format: "male" or "female" (string, case-insensitive)
"""


# Clinical threshold values (WHO standards)
THRESHOLD_MALE = 13.0    # g/dL
THRESHOLD_FEMALE = 12.0  # g/dL


def anemia_decision(predicted_hb, gender):
    """
    Determine anemia status based on Hemoglobin value and gender.
    
    This is a RULE-BASED clinical decision, NOT a machine learning model.
    
    Args:
        predicted_hb (float): Predicted or measured Hemoglobin value (g/dL)
        gender (str): Patient gender ("male", "female", "m", or "f")
    
    Returns:
        str: "Anemia" or "Normal"
    
    Raises:
        ValueError: If gender is invalid
        ValueError: If predicted_hb is negative
    
    Clinical Rules:
        Male   & Hb < 13 g/dL → "Anemia"
        Female & Hb < 12 g/dL → "Anemia"
        Otherwise            → "Normal"
    """
    # Validate hemoglobin value
    if predicted_hb < 0:
        raise ValueError(f"Invalid Hemoglobin value: {predicted_hb}. Must be positive.")
    
    # Normalize gender input
    gender_normalized = gender.lower().strip()
    
    # Determine threshold based on gender
    if gender_normalized in ["male", "m"]:
        threshold = THRESHOLD_MALE
    elif gender_normalized in ["female", "f"]:
        threshold = THRESHOLD_FEMALE
    else:
        raise ValueError(
            f"Invalid gender: '{gender}'. "
            "Please use 'male', 'female', 'm', or 'f'."
        )
    
    # Apply clinical decision rule
    if predicted_hb < threshold:
        return "Kansızlık"
    else:
        return "Normal"


def get_threshold(gender):
    """
    Get the anemia threshold for a given gender.
    
    Args:
        gender (str): "male", "female", "m", or "f"
    
    Returns:
        float: Threshold value in g/dL
    """
    gender_normalized = gender.lower().strip()
    
    if gender_normalized in ["male", "m"]:
        return THRESHOLD_MALE
    elif gender_normalized in ["female", "f"]:
        return THRESHOLD_FEMALE
    else:
        raise ValueError(f"Invalid gender: '{gender}'")


def normalize_gender(gender):
    """
    Normalize gender input to standard format.
    
    Args:
        gender (str): "male", "female", "m", or "f"
    
    Returns:
        str: "male" or "female"
    """
    gender_normalized = gender.lower().strip()
    
    if gender_normalized in ["male", "m"]:
        return "male"
    elif gender_normalized in ["female", "f"]:
        return "female"
    else:
        raise ValueError(f"Invalid gender: '{gender}'")
