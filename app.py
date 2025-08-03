import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np



option_menu_styles = {
    "container": {
        "padding": "5px",
        "background-color": "#1c1e21",
        "border-radius": "10px",
    },
    "icon": {"color": "#f1c40f", "font-size": "25px"},
    "nav-link": {
        "font-size": "18px",
        "text-align": "left",
        "margin": "0px",
        "color": "#ffffff"
    },
    "nav-link-selected": {
        "background-color": "#02ab21",
        "color": "white"
    },
}

# Page configuration
st.set_page_config(page_title="Disease Prediction System", layout="centered")

# Load the models
load_diabetes_model = pickle.load(open('Saved Models/calibrated_svc_model.sav', 'rb'))
load_heart_model = pickle.load(open('Saved Models/heart_disease_model.sav', 'rb'))
load_parkinsons = pickle.load(open('Saved Models/parkinsons_disease_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction",
        ["Heart Disease", "Diabetes Prediction", "Parkinsons Disease"],
        icons=["heart-pulse", "activity", "person-walking"],
        menu_icon="hospital",
        default_index=1,
        styles=option_menu_styles
    )



# =================== DIABETES PAGE ===================
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    with col2:
        Age = st.text_input("Age")

    diab_diagnosis = ""

    if st.button("Diabetes Test Result"):
        try:
            input_data = np.array([float(Pregnancies), float(Glucose), float(BloodPressure),
                                   float(SkinThickness), float(Insulin), float(BMI),
                                   float(DiabetesPedigreeFunction), float(Age)]).reshape(1, -1)
            diab_prediction = load_diabetes_model.predict(input_data)
            if diab_prediction[0] == 1:
                diab_diagnosis = "🔴 The person is Diabetic"
            else:
                diab_diagnosis = "🟢 The person is not Diabetic"
        except:
            diab_diagnosis = "⚠️ Please enter valid numeric inputs only!"

    st.success(diab_diagnosis)

# =================== HEART DISEASE PAGE ===================
if selected == 'Heart Disease':
    st.title("Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
        trestbps = st.text_input("Resting Blood Pressure")
        chol = st.text_input("Serum Cholestoral in mg/dl")
        restecg = st.text_input("Resting Electrocardiographic Results (0,1,2)")
        oldpeak = st.text_input("ST depression")
    with col2:
        sex = st.text_input("Sex (1 = male, 0 = female)")
        cp = st.text_input("Chest Pain types (0-3)")
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)")
        thalach = st.text_input("Maximum Heart Rate Achieved")
        slope = st.text_input("Slope of the peak exercise ST segment (0-2)")
    with col3:
        exang = st.text_input("Exercise induced angina (1 = yes; 0 = no)")
        ca = st.text_input("Number of major vessels (0-3)")
        thal = st.text_input("Thal (1 = normal; 2 = fixed defect; 3 = reversible defect)")

    heart_diagnosis = ""

    if st.button("Heart Disease Test Result"):
        try:
            input_data = np.array([float(age), float(sex), float(cp), float(trestbps), float(chol),
                                   float(fbs), float(restecg), float(thalach), float(exang),
                                   float(oldpeak), float(slope), float(ca), float(thal)]).reshape(1, -1)
            heart_prediction = load_heart_model.predict(input_data)
            if heart_prediction[0] == 1:
                heart_diagnosis = "🔴 The person has Heart Disease"
            else:
                heart_diagnosis = "🟢 The person does not have Heart Disease"
        except:
            heart_diagnosis = "⚠️ Please enter valid numeric inputs only!"

    st.success(heart_diagnosis)

# =================== PARKINSON'S DISEASE PAGE ===================
if selected == 'Parkinsons Disease':
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
        fhi = st.text_input("MDVP:Fhi(Hz)")
        flo = st.text_input("MDVP:Flo(Hz)")
        jitter_percent = st.text_input("MDVP:Jitter(%)")
        rap = st.text_input("MDVP:RAP")
        shimmer = st.text_input("MDVP:Shimmer")
        apq = st.text_input("MDVP:APQ")
        hnrs = st.text_input("HNR")
    with col2:
        jitter_abs = st.text_input("MDVP:Jitter(Abs)")
        ppq = st.text_input("MDVP:PPQ")
        ddp = st.text_input("Jitter:DDP")
        shimmer_db = st.text_input("MDVP:Shimmer(dB)")
        apq3 = st.text_input("Shimmer:APQ3")
        apq5 = st.text_input("Shimmer:APQ5")
        dda = st.text_input("Shimmer:DDA")
        nhr = st.text_input("NHR")
    with col3:
        rpde = st.text_input("RPDE")
        dfa = st.text_input("DFA")
        spread1 = st.text_input("spread1")
        spread2 = st.text_input("spread2")
        d2 = st.text_input("D2")
        ppe = st.text_input("PPE")

    parkinsons_diagnosis = ""

    if st.button("Parkinson's Test Result"):
        try:
            input_data = np.array([float(fo), float(fhi), float(flo), float(jitter_percent), float(jitter_abs),
                                   float(rap), float(ppq), float(ddp), float(shimmer), float(shimmer_db),
                                   float(apq3), float(apq5), float(apq), float(dda), float(nhr),
                                   float(hnrs), float(rpde), float(dfa), float(spread1),
                                   float(spread2), float(d2), float(ppe)]).reshape(1, -1)

            parkinsons_prediction = load_parkinsons.predict(input_data)
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "🔴 The person has Parkinson's Disease"
            else:
                parkinsons_diagnosis = "🟢 The person does not have Parkinson's Disease"
        except:
            parkinsons_diagnosis = "⚠️ Please enter valid numeric inputs only!"

    st.success(parkinsons_diagnosis)
