# 🌾 Telangana Crop Prediction Project

**Live App**: [Coming Soon](#)  
**GitHub Repo**: [GitHub Link](#)

> A machine learning-powered web application to help predict the most suitable **crops for cultivation** based on regional and seasonal attributes in **Telangana, India**.

---

## 📌 Project Overview

The **Telangana Crop Prediction** project utilizes machine learning to recommend the top two crops with the **highest expected production** based on user input including season, soil type, district, and other agricultural attributes. The goal is to assist **farmers, researchers, and policymakers** in making informed crop decisions.

It is developed using **Streamlit** for the interactive frontend and employs clustering and classification algorithms like **KMeans** and **XGBoost** to deliver high-accuracy predictions.

---

## 🌱 What Our App Does

- 📍 Predicts the **top 2 high-yield crops** based on user-specified inputs:
  - State, District, Crop Year
  - Season & Soil Type
  - Agro-Climatic Zone, Area, and more
- ⚙️ Uses a **KMeans Clustering model** to enhance feature grouping
- 🤖 Applies **XGBoost classification** for highly accurate predictions
- 📊 Designed to support decision-making in agriculture planning
- 💬 Interactive and simple **Streamlit-based UI** for easy usage

---

## 🛠️ Technologies Used

| Component        | Stack                                    |
|------------------|-------------------------------------------|
| 🖥 Frontend       | Streamlit (Python Web App Framework)      |
| 🤖 ML Models      | XGBoost, KMeans                           |
| 📦 Data Handling  | Pandas, NumPy                             |
| 📊 Visualization  | Matplotlib, Seaborn (if needed)           |
| 📁 Deployment     | Streamlit Sharing (Community Cloud)       |

---

## 📁 Folder Structure

```
telangana-crop-prediction/
│
├── data/                  # Cleaned and preprocessed dataset
├── models/                # Saved model files (KMeans, XGBoost)
├── main.py                # Streamlit app entry point
├── utils.py               # Helper functions for preprocessing
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation
```

---

## 🔧 Installation & Running the App

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the Application

```bash
streamlit run main.py
```

Once started, the app will open in your browser, ready for input and crop prediction.

---

## 📅 Project Duration

- **Start Date**: June 2024  
- **End Date**: August 2024  
- **Location**: Telangana, India  
- **Status**: ✅ Functional (MVP Phase Complete)

---

## 🌾 Future Enhancements

- 🗺️ GIS Map integration to visualize district-wise predictions  
- 🌐 Multilingual support (Telugu, Hindi, English)  
- 📈 Add support for rainfall, temperature, and humidity trends  
- 🤝 Farmer feedback & validation loop integration  

---

## 🙌 Final Note

This project is built with the vision to **support sustainable agriculture** by empowering farmers and agronomists with AI-driven tools. It not only helps optimize crop planning but also contributes to food security and smart farming initiatives.

> 🌿 *Sow smart. Reap smarter.*

---

**👨‍💻 Developed by**: [Your Name Here]  
**📚 License**: MIT (optional)  
**🔗 Contact**: [your-email@example.com]
