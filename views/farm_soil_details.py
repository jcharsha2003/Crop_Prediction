import streamlit as st
import json
from streamlit_lottie import st_lottie

# Load Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_farm = load_lottiefile("./assets/ap.json")

def farm_soil_details():
    # Session state variables to store user input
    if "user_data" not in st.session_state:
        st.session_state["user_data"] = {}

    user_data = st.session_state["user_data"]

    st.title("🌾 Farm & Soil Details")
    st.subheader("🌱 Provide your farm details for accurate crop prediction.")

    # Create columns for structured layout
    col1, col2 = st.columns([1, 1])

    with col1:
        # Retaining previous values if present
        area = st.number_input("📏 Farm Area (Hectares) ➖ Min: 1 | Max: 361169", min_value=1, max_value=361169, step=1, value=user_data.get("Area", 1))
        user_data["Area"] = area

        production = st.number_input("📊 Production (Tonnes) ➖ Min: 0 | Max: 11933140", min_value=0, max_value=11933140, step=1, value=user_data.get("Production", 0))
        user_data["Production"] = production

        # Soil type mapping (zero-based encoding)
        soil_mapping = {
            "🟥 Red Soil": 0, "⬛ Black Soil (Black Cotton Soil)": 1, "🏞️ Alluvial Soil": 2, "🏜️ Sandy Soil": 3,
            "⛰️ Laterite Soil": 4, "🌾 Sandy Clay Loam": 5, "🌿 Sandy Loam Soil": 6, "🟠 Red Loam Soil": 7,
            "⚪ Saline": 8, "🧂 Alkaline": 9, "🟤 Silty loam": 10
        }

        # Remove emojis for storage purposes
        def clean_soil_name(name):
            return " ".join(name.split()[1:])

        # User selects a soil type
        soil_type = st.selectbox("🧑‍🌾 Select Soil Type", options=list(soil_mapping.keys()))

        # Ensure previous data is retained
        soil_data = {clean_soil_name(soil): 0 for soil in soil_mapping.keys()}
        soil_data[clean_soil_name(soil_type)] = 1  # Set the selected soil type to 1

        # Merge soil type encoding with previous user data
        user_data.update(soil_data)
        user_data["Soil_Type"]=" ".join(soil_type.split()[1:])
        
        # Required fields from all pages that need to be checked
        

       # Submit button with validation and navigation
        if st.button("📨 Submit & Proceed"):

            required_fields = ["District_Name", "Season", "Area", "Production", "Soil_Type"]

            # Check if all required fields are present (without checking their values)
            missing_fields = [field for field in required_fields if field not in st.session_state.user_data]

            # Debugging output

            if not missing_fields:
                # If no fields are missing, proceed to prediction page
                st.success("✅ Information submitted! Redirecting to the next page...")
                st.session_state["current_page"] = "crop_prediction"
                st.session_state.S = 0  # Ensures sidebar update is skipped
                st.rerun()
            else:
                # Notify user about missing fields
                st.error(f"⚠️ Please fill out the following fields: {', '.join(missing_fields)}")



    with col2:
        st_lottie(
            lottie_farm,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=300,
            width=400,
            key="farm_animation"
        )

if __name__ == "__main__":
    farm_soil_details()
