"""
Hemoglobin Prediction & Anemia Diagnosis - Streamlit UI

This is a simple web interface for the anemia diagnosis system.
It uses the trained Linear Regression model to predict Hemoglobin
and applies WHO clinical thresholds to determine anemia status.

Usage:
    streamlit run app.py
"""

import streamlit as st
import joblib
import os
from utils import anemia_decision, get_threshold, normalize_gender


# Constants
MODEL_PATH = os.path.join('model', 'hemoglobin_model.pkl')

# Valid ranges for input validation (soft warnings)
VALID_RANGES = {
    'RBC': (2.0, 7.0),
    'MCV': (60.0, 120.0),
    'MCH': (15.0, 40.0),
    'MCHC': (25.0, 40.0)
}


@st.cache_resource
def load_model():
    """Load the trained model (cached for performance)."""
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)


def check_range(name, value, valid_range):
    """Check if value is within typical range, return warning message if not."""
    min_val, max_val = valid_range
    if value < min_val or value > max_val:
        return f"⚠️ {name} = {value} is outside typical range ({min_val} - {max_val})"
    return None


def predict_hemoglobin(model_data, features):
    """Predict Hemoglobin from blood parameters."""
    model = model_data['model']
    feature_columns = model_data['feature_columns']
    
    # Build feature array in correct order
    X = [[features[col] for col in feature_columns]]
    
    # Predict
    hemoglobin = model.predict(X)[0]
    return hemoglobin


def main():
    # Page configuration
    st.set_page_config(
        page_title="Anemia Diagnosis System",
        page_icon="🩸",
        layout="centered"
    )
    
    # Header
    st.title("🩸 Hemoglobin Prediction & Anemia Diagnosis")
    st.markdown("---")
    
    # Load model
    model_data = load_model()
    
    if model_data is None:
        st.error("❌ Model file not found. Please run `python train.py` first.")
        st.stop()
    
    # Model info
    with st.expander("ℹ️ About this system"):
        st.markdown("""
        This system uses **Linear Regression** to predict Hemoglobin (Hb) values
        from blood parameters, then applies **WHO clinical thresholds** to determine
        anemia status.
        
        **Anemia Thresholds (WHO):**
        - Male: Hb < 13 g/dL → Anemia
        - Female: Hb < 12 g/dL → Anemia
        """)
    
    st.markdown("### 📋 Enter Blood Parameters")
    
    # Input fields in two columns
    col1, col2 = st.columns(2)
    
    with col1:
        rbc = st.number_input(
            "RBC (million cells/mcL)",
            min_value=0.0,
            max_value=10.0,
            value=4.5,
            step=0.1,
            help="Red Blood Cell count. Typical range: 2.0 - 7.0"
        )
        
        mcv = st.number_input(
            "MCV (fL)",
            min_value=0.0,
            max_value=150.0,
            value=80.0,
            step=1.0,
            help="Mean Corpuscular Volume. Typical range: 60 - 120"
        )
    
    with col2:
        mch = st.number_input(
            "MCH (pg)",
            min_value=0.0,
            max_value=50.0,
            value=27.0,
            step=0.5,
            help="Mean Corpuscular Hemoglobin. Typical range: 15 - 40"
        )
        
        mchc = st.number_input(
            "MCHC (g/dL)",
            min_value=0.0,
            max_value=50.0,
            value=33.0,
            step=0.5,
            help="Mean Corpuscular Hb Concentration. Typical range: 25 - 40"
        )
    
    # Gender selection
    st.markdown("### 👤 Patient Information")
    gender = st.selectbox(
        "Gender",
        options=["female", "male"],
        index=0,
        help="Required for applying WHO anemia thresholds"
    )
    
    st.markdown("---")
    
    # Predict button
    if st.button("🔬 Predict Hemoglobin", type="primary", use_container_width=True):
        
        # Show range warnings
        warnings = []
        warnings.append(check_range('RBC', rbc, VALID_RANGES['RBC']))
        warnings.append(check_range('MCV', mcv, VALID_RANGES['MCV']))
        warnings.append(check_range('MCH', mch, VALID_RANGES['MCH']))
        warnings.append(check_range('MCHC', mchc, VALID_RANGES['MCHC']))
        
        # Display warnings if any
        warnings = [w for w in warnings if w is not None]
        if warnings:
            for w in warnings:
                st.warning(w)
        
        # Build features
        features = {
            'RBC': rbc,
            'MCV': mcv,
            'MCH': mch,
            'MCHC': mchc
        }
        
        # Predict Hemoglobin
        predicted_hb = predict_hemoglobin(model_data, features)
        
        # Get clinical decision
        status = anemia_decision(predicted_hb, gender)
        threshold = get_threshold(gender)
        
        # Display results
        st.markdown("---")
        st.markdown("### 📊 Results")
        
        # Metrics in columns
        result_col1, result_col2, result_col3 = st.columns(3)
        
        with result_col1:
            st.metric(
                label="Predicted Hemoglobin",
                value=f"{predicted_hb:.2f} g/dL"
            )
        
        with result_col2:
            st.metric(
                label="Threshold",
                value=f"{threshold:.1f} g/dL",
                help=f"WHO threshold for {gender}"
            )
        
        with result_col3:
            st.metric(
                label="Gender",
                value=gender.capitalize()
            )
        
        # Anemia status with appropriate styling
        st.markdown("---")
        
        if status == "Anemia":
            st.error(f"### ⚠️ Result: **{status}**")
            st.markdown(f"Predicted Hemoglobin ({predicted_hb:.2f} g/dL) is below the threshold ({threshold:.1f} g/dL) for {gender}.")
        else:
            st.success(f"### ✅ Result: **{status}**")
            st.markdown(f"Predicted Hemoglobin ({predicted_hb:.2f} g/dL) is at or above the threshold ({threshold:.1f} g/dL) for {gender}.")
        
        # Clinical note
        st.info("💡 **Note:** This is a decision support tool for educational purposes. Clinical diagnosis requires comprehensive evaluation by healthcare professionals.")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray; font-size: 12px;'>"
        "Hemoglobin Regression Model | Linear Regression | WHO Thresholds"
        "</div>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
