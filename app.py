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
import pandas as pd
import numpy as np
import os
from utils import anemia_decision, get_threshold, normalize_gender


# Constants
MODEL_PATH = os.path.join('model', 'hemoglobin_model.pkl')
DATA_PATH = os.path.join('data', 'anemia_new.csv')
K_NEIGHBORS = 30  # Number of similar samples to consider

# Valid ranges for input validation (soft warnings)
VALID_RANGES = {
    'RBC': (2.0, 7.0),
    'MCV': (60.0, 120.0),
    'MCH': (15.0, 40.0),
    'MCHC': (25.0, 40.0)
}

# Features used for similarity calculation
SIMILARITY_FEATURES = ['RBC', 'MCV', 'MCH', 'MCHC']


def apply_custom_style():
    """Apply custom CSS styling with animated gradient background."""
    
    # Dark mode colors
    bg_gradient = "linear-gradient(-45deg, #003FFF, #2E0EC7, #8B6AE6, #4CB4BB, #FF5772, #FFC600)"
    container_bg = "rgba(255, 255, 255, 0.15)"
    text_color = "white"
    text_secondary = "rgba(255, 255, 255, 0.8)"
    input_bg = "rgba(255, 255, 255, 0.2)"
    input_border = "rgba(255, 255, 255, 0.3)"
    divider_color = "rgba(255, 255, 255, 0.3)"
    
    st.markdown(f"""
    <style>
    /* Animated Gradient Background */
    .stApp {{
        background: {bg_gradient};
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }}
    
    @keyframes gradientBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    
    /* Glassmorphism effect for main container */
    .main .block-container {{
        background: {container_bg};
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid {input_border};
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    }}
    
    /* Header styling */
    h1 {{
        color: {text_color} !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }}
    
    h2, h3, h4 {{
        color: {text_color} !important;
    }}
    
    /* Text styling */
    p, label, .stMarkdown {{
        color: {text_color} !important;
    }}
    
    /* Input fields styling */
    .stNumberInput > div > div > input {{
        background: {input_bg} !important;
        border: 1px solid {input_border} !important;
        border-radius: 10px !important;
        color: {text_color} !important;
    }}
    
    .stSelectbox > div > div {{
        background: {input_bg} !important;
        border: 1px solid {input_border} !important;
        border-radius: 10px !important;
    }}
    
    /* Button styling */
    .stButton > button {{
        background: linear-gradient(135deg, #FF5772, #8B6AE6) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 0.75rem 2rem !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(255, 87, 114, 0.4) !important;
        transition: all 0.3s ease !important;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 87, 114, 0.6) !important;
    }}
    
    /* Metric cards styling */
    [data-testid="stMetricValue"] {{
        color: {text_color} !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
    }}
    
    [data-testid="stMetricLabel"] {{
        color: {text_secondary} !important;
    }}
    
    /* Success/Error message styling */
    .stSuccess {{
        background: rgba(76, 180, 187, 0.3) !important;
        border: 1px solid #4CB4BB !important;
        border-radius: 10px !important;
    }}
    
    .stError {{
        background: rgba(255, 87, 114, 0.3) !important;
        border: 1px solid #FF5772 !important;
        border-radius: 10px !important;
    }}
    
    .stWarning {{
        background: rgba(255, 198, 0, 0.3) !important;
        border: 1px solid #FFC600 !important;
        border-radius: 10px !important;
    }}
    
    .stInfo {{
        background: rgba(139, 106, 230, 0.3) !important;
        border: 1px solid #8B6AE6 !important;
        border-radius: 10px !important;
    }}
    
    /* Expander styling */
    .streamlit-expanderHeader {{
        background: {input_bg} !important;
        border-radius: 10px !important;
        color: {text_color} !important;
    }}
    
    /* Divider styling */
    hr {{
        border-color: {divider_color} !important;
    }}
    
    /* Theme toggle button styling */
    .theme-toggle {{
        position: fixed;
        top: 1rem;
        right: 1rem;
        z-index: 999;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        cursor: pointer;
        transition: all 0.3s ease;
        background: {container_bg};
        border: 1px solid {input_border};
        backdrop-filter: blur(10px);
    }}
    
    /* Caption styling */
    .stCaption {{
        color: {text_secondary} !important;
    }}
    </style>
    """, unsafe_allow_html=True)


@st.cache_resource
def load_model():
    """Load the trained model (cached for performance)."""
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)


@st.cache_data
def load_dataset():
    """Load the dataset for similarity analysis (cached)."""
    if not os.path.exists(DATA_PATH):
        return None
    return pd.read_csv(DATA_PATH)


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


def find_similar_samples(df, input_features, k=K_NEIGHBORS):
    """
    Find K most similar samples in the dataset based on Euclidean distance.
    
    Args:
        df: Dataset with features and true Hb values
        input_features: Dictionary of input feature values
        k: Number of nearest neighbors to return
    
    Returns:
        DataFrame of similar samples with distances
    """
    # Extract feature values from dataset
    X_data = df[SIMILARITY_FEATURES].values
    
    # Build input vector
    input_vector = np.array([input_features[col] for col in SIMILARITY_FEATURES])
    
    # Calculate Euclidean distances
    distances = np.sqrt(np.sum((X_data - input_vector) ** 2, axis=1))
    
    # Add distances to dataframe
    df_with_dist = df.copy()
    df_with_dist['_distance'] = distances
    
    # Sort by distance and get top K
    similar = df_with_dist.nsmallest(k, '_distance')
    
    return similar


def calculate_uncertainty(similar_samples, predicted_hb, total_samples):
    """
    Calculate prediction uncertainty based on similar samples.
    
    Args:
        similar_samples: DataFrame of similar samples
        predicted_hb: Model's predicted Hemoglobin value
        total_samples: Total number of samples in dataset
    
    Returns:
        Dictionary with uncertainty metrics including percentages
    """
    true_hb_values = similar_samples['Hb'].values
    
    # Calculate metrics
    mean_hb = np.mean(true_hb_values)
    std_hb = np.std(true_hb_values)
    min_hb = np.min(true_hb_values)
    max_hb = np.max(true_hb_values)
    
    # MAE between prediction and true values of similar samples
    mae = np.mean(np.abs(true_hb_values - predicted_hb))
    
    # Calculate percentage of similar samples within ±1 g/dL of prediction
    within_1 = np.sum(np.abs(true_hb_values - predicted_hb) <= 1.0)
    within_1_pct = (within_1 / len(true_hb_values)) * 100
    
    # Calculate percentage within ±2 g/dL
    within_2 = np.sum(np.abs(true_hb_values - predicted_hb) <= 2.0)
    within_2_pct = (within_2 / len(true_hb_values)) * 100
    
    # Confidence score based on how close prediction is to mean of similar samples
    # Lower difference = higher confidence
    diff_from_mean = abs(predicted_hb - mean_hb)
    # Scale: if diff is 0, confidence is 100%; if diff >= 3, confidence approaches 50%
    confidence_pct = max(50, 100 - (diff_from_mean * 16.67))
    confidence_pct = min(100, confidence_pct)
    
    return {
        'n_samples': len(similar_samples),
        'total_samples': total_samples,
        'mean_hb': mean_hb,
        'std_hb': std_hb,
        'min_hb': min_hb,
        'max_hb': max_hb,
        'mae': mae,
        'typical_deviation': std_hb,
        'within_1_pct': within_1_pct,
        'within_2_pct': within_2_pct,
        'confidence_pct': confidence_pct
    }


def main():
    # Page configuration
    st.set_page_config(
        page_title="Anemia Diagnosis System",
        page_icon="🩸",
        layout="centered"
    )
    
    # Apply custom styling
    apply_custom_style()
    
    # Header
    st.title("Hemoglobin Prediction & Anemia Diagnosis")
    st.markdown("---")
    
    # Load model and dataset
    model_data = load_model()
    dataset = load_dataset()
    
    if model_data is None:
        st.error("❌ Model file not found. Please run `python train.py` first.")
        st.stop()
    
    if dataset is None:
        st.warning("⚠️ Dataset not found. Uncertainty analysis will be unavailable.")
    
    # Model info
    with st.expander("About this system"):
        st.markdown("""
        This system uses **Linear Regression** to predict Hemoglobin (Hb) values
        from blood parameters, then applies **WHO clinical thresholds** to determine
        anemia status.
        
        **Anemia Thresholds (WHO):**
        - Male: Hb < 13 g/dL → Anemia
        - Female: Hb < 12 g/dL → Anemia
        
        **Prediction Uncertainty:**
        The system compares your input with similar individuals in the dataset
        to provide a typical deviation range.
        """)
    
    st.markdown("### Enter Blood Parameters")
    
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
    
    # Gender selection with stylish buttons
    st.markdown("### Patient Information")
    
    # Initialize session state for gender if not exists
    if 'selected_gender' not in st.session_state:
        st.session_state.selected_gender = "female"
    
    # Custom CSS for gender buttons
    st.markdown("""
    <style>
    .gender-btn {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 1.5rem;
        border-radius: 15px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: center;
    }
    .gender-btn-female {
        background: linear-gradient(135deg, #FF6B9D, #FF5772);
        border: 3px solid transparent;
    }
    .gender-btn-male {
        background: linear-gradient(135deg, #4CB4BB, #2E9DA6);
        border: 3px solid transparent;
    }
    .gender-btn-selected {
        border: 3px solid #FFC600 !important;
        box-shadow: 0 0 20px rgba(255, 198, 0, 0.5);
        transform: scale(1.05);
    }
    .gender-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .gender-label {
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Gender selection buttons
    gender_col1, gender_col2 = st.columns(2)
    
    with gender_col1:
        female_selected = st.session_state.selected_gender == "female"
        if st.button(
            "👩 Female",
            key="female_btn",
            use_container_width=True,
            type="primary" if female_selected else "secondary"
        ):
            st.session_state.selected_gender = "female"
            st.rerun()
    
    with gender_col2:
        male_selected = st.session_state.selected_gender == "male"
        if st.button(
            "👨 Male", 
            key="male_btn",
            use_container_width=True,
            type="primary" if male_selected else "secondary"
        ):
            st.session_state.selected_gender = "male"
            st.rerun()
    
    gender = st.session_state.selected_gender
    
    # Show selected gender
    st.markdown(f"<p style='text-align: center; color: rgba(255,255,255,0.7);'>Selected: <strong>{gender.capitalize()}</strong></p>", unsafe_allow_html=True)
    
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
        
        # Calculate uncertainty if dataset is available
        uncertainty = None
        if dataset is not None:
            similar_samples = find_similar_samples(dataset, features, k=K_NEIGHBORS)
            uncertainty = calculate_uncertainty(similar_samples, predicted_hb, len(dataset))
        
        # Display results
        st.markdown("---")
        st.markdown("### 📊 Results")
        
        # Main prediction result
        st.markdown(f"**Predicted Hemoglobin: {predicted_hb:.2f} g/dL**")
        
        # Uncertainty information with percentages
        if uncertainty:
            st.markdown(
                f"*Based on {uncertainty['n_samples']} similar individuals in the dataset*"
            )
            st.markdown(
                f"*Typical deviation: ±{uncertainty['typical_deviation']:.2f} g/dL*"
            )
        
        st.markdown("")
        
        # Metrics in columns (4 columns to include confidence)
        if uncertainty:
            result_col1, result_col2, result_col3, result_col4 = st.columns(4)
        else:
            result_col1, result_col2, result_col3 = st.columns(3)
            result_col4 = None
        
        with result_col1:
            st.metric(
                label="Predicted Hb",
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
        
        if result_col4 and uncertainty:
            with result_col4:
                st.metric(
                    label="Confidence",
                    value=f"{uncertainty['confidence_pct']:.0f}%",
                    help="Based on similarity to known cases"
                )
        
        # Percentage metrics display
        if uncertainty:
            st.markdown("")
            st.markdown("#### 📊 Similarity Analysis")
            
            pct_col1, pct_col2, pct_col3 = st.columns(3)
            
            with pct_col1:
                st.metric(
                    label="Within ±1 g/dL",
                    value=f"{uncertainty['within_1_pct']:.0f}%",
                    help="Percentage of similar cases within 1 g/dL of prediction"
                )
            
            with pct_col2:
                st.metric(
                    label="Within ±2 g/dL",
                    value=f"{uncertainty['within_2_pct']:.0f}%",
                    help="Percentage of similar cases within 2 g/dL of prediction"
                )
            
            with pct_col3:
                st.metric(
                    label="Match Rate",
                    value=f"{(uncertainty['n_samples'] / uncertainty['total_samples'] * 100):.1f}%",
                    help=f"{uncertainty['n_samples']} of {uncertainty['total_samples']} samples"
                )
        
        # Uncertainty details (expandable)
        if uncertainty:
            with st.expander("📈 Prediction Uncertainty Details"):
                st.markdown("""
                **How is uncertainty calculated?**
                
                We find similar individuals in our dataset based on their blood parameters
                (RBC, MCV, MCH, MCHC) and analyze the variation in their actual Hemoglobin values.
                """)
                
                unc_col1, unc_col2 = st.columns(2)
                
                with unc_col1:
                    st.markdown(f"**Similar samples:** {uncertainty['n_samples']}")
                    st.markdown(f"**Mean Hb in group:** {uncertainty['mean_hb']:.2f} g/dL")
                    st.markdown(f"**Standard deviation:** ±{uncertainty['std_hb']:.2f} g/dL")
                
                with unc_col2:
                    st.markdown(f"**Hb range in group:** {uncertainty['min_hb']:.1f} - {uncertainty['max_hb']:.1f} g/dL")
                    st.markdown(f"**Prediction vs. group MAE:** {uncertainty['mae']:.2f} g/dL")
                
                st.caption("*Deviation is calculated using similar cases in the dataset.*")
        
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
