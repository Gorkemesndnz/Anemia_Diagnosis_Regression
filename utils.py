"""
Clinical Anemia Decision Logic

This module contains rule-based clinical logic for anemia diagnosis.
This is NOT a machine learning model.

WHO Threshold Values:
    - Male:   Hemoglobin < 13 g/dL → Anemia
    - Female: Hemoglobin < 12 g/dL → Anemia

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
        gender (str): Patient gender ("male" or "female")
    
    Returns:
        str: "Anemia" or "Normal"
    
    Raises:
        ValueError: If gender is not "male" or "female"
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
    if gender_normalized == "male":
        threshold = THRESHOLD_MALE
    elif gender_normalized == "female":
        threshold = THRESHOLD_FEMALE
    else:
        raise ValueError(
            f"Invalid gender: '{gender}'. "
            "Please use 'male' or 'female'."
        )
    
    # Apply clinical decision rule
    if predicted_hb < threshold:
        return "Anemia"
    else:
        return "Normal"


def get_threshold(gender):
    """
    Get the anemia threshold for a given gender.
    
    Args:
        gender (str): "male" or "female"
    
    Returns:
        float: Threshold value in g/dL
    """
    gender_normalized = gender.lower().strip()
    
    if gender_normalized == "male":
        return THRESHOLD_MALE
    elif gender_normalized == "female":
        return THRESHOLD_FEMALE
    else:
        raise ValueError(f"Invalid gender: '{gender}'")
