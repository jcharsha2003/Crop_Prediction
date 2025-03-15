import streamlit as st
import pandas as pd
import numpy as np
import pickle
import xgboost as xgb
import json
from streamlit_lottie import st_lottie
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

# ✅ Load the trained files
@st.cache_resource
def load_model():
    model = xgb.Booster()
    model.load_model("./data/xgboost_model.json")
    return model

@st.cache_resource
def load_scaler():
    return joblib.load("./data/scaler.pkl")

@st.cache_resource
def load_label_encoder():
    return joblib.load("./data/label_encoder.pkl")

@st.cache_resource
def load_crop_mapping():
    with open("./data/crop_mapping.pkl", "rb") as f:
        return pickle.load(f)

# ✅ Load required assets
xgb_model = load_model()
scaler = load_scaler()
le = load_label_encoder()
crop_mapping = load_crop_mapping()

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_predict_dark = load_lottiefile("./assets/area.json")

# # 🎯 Title Section with Emoji and Styling
# st.markdown("""
#     <h1 style='text-align: center; color: #4CAF50;'>🌾 TCrop - Telangana Crop Prediction 🌱</h1>
#     <h3 style='text-align: center;'>Predict the best crops for your region and maximize yield! 🚜</h3>
#     <hr style='border: 1px solid #4CAF50;'>
# """, unsafe_allow_html=True)

label_dicts = {
    "District_Name": {
    0: "ADILABAD", 1: "HYDERABAD", 2: "KARIMNAGAR", 3: "KHAMMAM",
    4: "MAHBUBNAGAR", 5: "MEDAK", 6: "NALGONDA", 7: "NIZAMABAD",
    8: "RANGAREDDI", 9: "WARANGAL"
},
    "Season": {0: "Kharif", 1: "Rabi", 2: "Whole Year"},
    "A_C Zones": {0: "Northern Zone", 2: "Southern Zone", 1: "Central Zone"}
}

def crop_prediction():
    st.subheader("🔍 Review your information and make a prediction!")
    
    user_data = st.session_state.get("user_data", {})
    required_fields = ["District_Name", "Season", "Area", "Production", "Soil_Type"]
    
    user_input = {
        "District_Name": user_data.get("District_Name", "Not Filled"),
        "Season": user_data.get("Season", "Not Filled"),
        "Area": user_data.get("Area", "Not Filled"),
        "Production": user_data.get("Production", "Not Filled"),
        "A_C Zones": user_data.get("A_C Zones", "Not Filled"),
        "Red Soil": user_data.get("Red Soil", "Not Filled"),
        "Black Soil (black cotton soils)": user_data.get("Black Soil (Black Cotton Soil)", "Not Filled"),
        "Alluvial Soil": user_data.get("Alluvial Soil", "Not Filled"),
        "Sandy Soil": user_data.get("Sandy Soil", "Not Filled"),
        "Laterite Soil": user_data.get("Laterite Soil", "Not Filled"),
        "Sandy clay loam": user_data.get("Sandy Clay Loam", "Not Filled"),
        "Sandy loam soil": user_data.get("Sandy Loam Soil", "Not Filled"),
        "Red loam soil": user_data.get("Red Loam Soil", "Not Filled"),
        "Saline": user_data.get("Saline", "Not Filled"),
        "Alkaline": user_data.get("Alkaline", "Not Filled"),
        "Silty loam": user_data.get("Silty loam", "Not Filled"),
    }

    user_label = {
        "District Name": label_dicts["District_Name"].get(user_data.get("District_Name"), "Not Filled"),
        "Season": label_dicts["Season"].get(user_data.get("Season"), "Not Filled"),
        "A_C Zones": label_dicts["A_C Zones"].get(user_data.get("A_C Zones"), "Not Filled"),
        "Area (in acres)": user_data.get("Area", "Not Filled"),
        "Production (in tons)": user_data.get("Production", "Not Filled"),
        "Soil Type": user_data.get("Soil_Type", "Not Filled"),
    }
    
    df_user_input = pd.DataFrame(user_label.items(), columns=['Feature', 'Value'])
    
    # ✅ Side-by-side Layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(
            """
            <style>
                .stDataFrame {
                    width: 100% !important;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.subheader("📝 Your Information")
        st.dataframe(df_user_input, use_container_width=True)

    with col2:
        with st.container():
            st_lottie(lottie_predict_dark, speed=1, reverse=False, loop=True, quality="high", height=300, width=400, key="predict_animation")
    
    if st.button("🌾 Predict Best Crops 🌱"):
        missing_fields = [field for field in required_fields if field not in st.session_state.user_data]
        if not missing_fields:
            user_input_df = pd.DataFrame([user_input])
            input_scaled = scaler.transform(user_input_df)
            dmatrix_input = xgb.DMatrix(input_scaled)
            probabilities = xgb_model.predict(dmatrix_input)
            top2_indices = np.argsort(probabilities, axis=1)[:, -2:]
            top2_crop_numbers = le.inverse_transform(top2_indices.flatten()).reshape(top2_indices.shape)
            top2_crop_names = np.vectorize(crop_mapping.get)(top2_crop_numbers)
            
            st.success(f"🌾 **Top Recommended Crops:** {top2_crop_names[0][1]} & {top2_crop_names[0][0]}")
            st.balloons()
            
            # ✅ Additional Information for Farmers
            st.markdown("""
            ### 🌿 Importance of Agriculture in Telangana
            - Telangana's economy largely depends on agriculture, with crops like **paddy, maize, and pulses** being key contributors.
            - The state promotes **micro-irrigation** and **sustainable farming** techniques.
            
            ### 🚜 Best Practices for Cultivating Your Predicted Crops
            - **{0}**: Ensure proper irrigation and use organic fertilizers for better yield.
            - **{1}**: Suitable for {2} season; prefer well-drained soil with adequate nutrients.
            
            ✅ Follow **best farming practices** and maximize your yield! 🌾💚
            """.format(top2_crop_names[0][1], top2_crop_names[0][0], label_dicts["Season"].get(user_data.get("Season"), "Not Filled")), unsafe_allow_html=True)
        else:
            st.error(f"⚠️ Please fill in all required fields: {', '.join(missing_fields)}")

if __name__ == "__main__":
    crop_prediction()
