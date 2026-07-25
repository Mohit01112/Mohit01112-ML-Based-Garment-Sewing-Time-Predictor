import streamlit as st
from src.predict import PredictionPipeline

# Page configuration
st.set_page_config(
    page_title="Garment Sewing Time Predictor",
    page_icon="🧵",
    layout="centered"
)

# Load model
@st.cache_resource
def load_pipeline():
    return PredictionPipeline()

pipeline = load_pipeline()

st.title("🧵 ML-Based Garment Sewing Time Predictor")
st.write("Predict the sewing time for a garment based on production details.")

# Input widgets
garment_type = st.selectbox(
    "Select Garment Type",
    [
        "Blazer",
        "Dress",
        "Hoodie",
        "Jacket",
        "Jeans",
        "Kurti",
        "Shirt",
        "T-Shirt",
        "Trouser",
        "Uniform"
    ]
)

order_quantity = st.number_input(
    "Order Quantity",
    min_value=1,
    value=100
)

num_stitch_operations = st.number_input(
    "Number of Stitch Operations",
    min_value=1,
    value=20
)

# Prediction
if st.button("Predict Sewing Time"):

    prediction = pipeline.predict(
        garment_type=garment_type,
        order_quantity=int(order_quantity),
        num_stitch_operations=int(num_stitch_operations)
    )

    st.success(f"Predicted Sewing Time: **{prediction:.2f} minutes**")