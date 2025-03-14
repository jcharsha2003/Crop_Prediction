import streamlit as st
import json
from streamlit_lottie import st_lottie

# Encoding dictionaries for categorical variables
district_mapping = {
    "ADILABAD": 0, "HYDERABAD": 1, "KARIMNAGAR": 2, "KHAMMAM": 3,
    "MAHBUBNAGAR": 4, "MEDAK": 5, "NALGONDA": 6, "NIZAMABAD": 7,
    "RANGAREDDI": 8, "WARANGAL": 9
}

season_mapping = {
    "Kharif": 0, 
    "Rabi": 1, 
    "Whole Year": 2
}

zone_mapping = {
    "Northern Zone": 0, 
    "Central Zone": 1, 
    "Southern Zone": 2
}

# Load Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_location = load_lottiefile("./assets/soil.json")

def district_season():
    # Session state variables to store user input
    if "user_data" not in st.session_state:
        st.session_state["user_data"] = {}

    user_data = st.session_state["user_data"]

    # Page Title with Icon
    st.title("📍 District & Season Selection")
    st.subheader("🏡 Provide your district, season, and agricultural zone to get the best crop recommendations.")

    # Create a two-column layout
    col1, col2 = st.columns([1, 1])

    with col1:
        # District Selection
        district = st.selectbox("Select Your District:", options=list(district_mapping.keys()))
        user_data["District_Name"] = district_mapping[district]  # Store encoded value

        # Season Selection
        season = st.selectbox("Select the Current Season:", options=list(season_mapping.keys()))
        user_data["Season"] = season_mapping[season]  # Store encoded value

        # Agricultural Zone Selection
        zone = st.selectbox("Select Your Agricultural Zone:", options=list(zone_mapping.keys()))
        user_data["A_C Zones"] = zone_mapping[zone]  # Store encoded value

        # Next button to navigate to the next page
        if st.button("Next (Farm Details)"):
            st.session_state["current_page"] = "farm_soil_details"
            st.success("✅ Information saved! Proceeding to Farm Details.")
            st.rerun()

    # Display animation in the second column
    with col2:
        st_lottie(
            lottie_location,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=280,
            width=400,
            key="location_animation"
        )
    
if __name__ == "__main__":
    district_season()
