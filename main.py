import streamlit as st
from streamlit_option_menu import option_menu
from views import crop_prediction, district_season, farm_soil_details
import json
from streamlit_lottie import st_lottie
import re
# --- Load Animation ---
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_home = load_lottiefile("./assets/home.json")

# --- LOGO DISPLAYED ON ALL PAGES ---
with st.sidebar:
    st.markdown("<div style='text-align: center; margin-top: -10px;'>", unsafe_allow_html=True)
    st.image("assets/gardener.png", width=60)
    st.markdown("</div>", unsafe_allow_html=True)

# Session state for page navigation
if "S" not in st.session_state:
    st.session_state.S = 1

# --- Page mapping (Keys match cleaned option names) ---
page_indices = {
    "home": 0,
    "district_season": 1,
    "farm_soil_details": 2,
    "crop_prediction": 3
}

current_page = st.session_state.get("current_page", "home")
default_index = page_indices.get(current_page, 0)

# --- NAVIGATION SETUP ---
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "District & Season", "Farm Soil Details", "Crop Prediction"],
        icons=["house-door", "cloud-sun", "droplet", "tree"],  # Updated icons
        menu_icon="cast",
        default_index=default_index,
        styles={
            "container": {"padding": "5px", "background-color": "#e6f2d9"},  # Slightly darker greenish-beige
            "icon": {"color": "#3d2c1e", "font-size": "22px"},  # Deep brown for strong contrast
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#a8c68c",  # Medium green hover
                "color": "#4d3826",  # Darker brown for better readability
            },
            "nav-link-selected": {"background-color": "#66a163", "color": "#ffffff"},  # Rich green for selected tab
        }
    )

    # Clean selected option for matching (remove & and lowercase)
    cleaned_selected = re.sub(r"_+", "_", selected.lower().replace("&", "").replace(" ", "_").strip())
    

    if cleaned_selected != st.session_state.get("current_page", "home"):
        st.session_state["current_page"] = cleaned_selected
        st.rerun()

    if st.session_state.S == 1:
        st.session_state["current_page"] = cleaned_selected
    else:
        selected = st.session_state["current_page"].replace("_", " ").title()

    st.session_state.S = 1

# --- PAGE CONTENT FUNCTIONS ---
def home():
    st.title("🌾 Welcome to Tcrop - Telangana Crop Recommendation System")

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.subheader("🌿 Empowering Farmers, Enriching Harvests")
        st.markdown(
            """
            🚜 **Tcrop** helps Telangana farmers make the best crop choices using scientific data.  
            🌍 By analyzing **soil**, **weather**, and **past trends**, we ensure **higher yields** and sustainable farming.  
            🌱 Let's cultivate prosperity together!  
            """
        )
        st.markdown(
            """
            💬 *"A farmer is not just a cultivator of land, but a cultivator of life."*  
            — **Kaloji Narayana Rao**
            """
        )
        st.write("🔍 Get started and find the best crops for your farm!")

    with col2:
        st_lottie(
            lottie_home,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=280,
            width=280,
            key="home_animation"
        )

# --- Page function mappings ---
page_functions = {
    "home": home,
    "district_season": district_season.district_season,
    "farm_soil_details": farm_soil_details.farm_soil_details,
    "crop_prediction": crop_prediction.crop_prediction
}

# --- NAVIGATION LOGIC ---
def navigate_page():
    current_page = st.session_state.get("current_page", "home")

    if current_page in page_functions:
        page_functions[current_page]()
    else:
        home()

navigate_page()
