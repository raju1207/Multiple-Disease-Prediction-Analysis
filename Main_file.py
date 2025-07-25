import pandas as pd
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Function to load models
def load_model(file_name):
    with open(file_name, 'rb') as file:
        return pickle.load(file)

# Load models
Kidney_model = load_model("Kidney_Disease.pkl")
liver_model = load_model("Liver_Disease.pkl")
parkinson_model = load_model("Parkinsons_Disease.pkl")

# Sidebar
with st.sidebar:
    st.markdown("""
        <h2 style='font-size: 28px; font-weight: bold; color: #333;'>
            🩺🏥 Multiple Disease Prediction System
        </h2>
    """, unsafe_allow_html=True)

    selected_model = option_menu(
        menu_title=None,
        options=["Kidney Prediction", "Liver Prediction", "Parkinsons Prediction"],
        icons=['activity', 'heart', 'person'],
        menu_icon="hospital",
        default_index=1
    )

# Load image 
st.image("Image.jpeg")

# Sidebar styling
st.sidebar.markdown("""
    <style>
    .stSidebar {
        background-color: #ADD8E6;
    }
    </style>
""", unsafe_allow_html=True)

# Function to display results
def display_result(condition_name, prediction, advice):
    if prediction == 1:
        st.error(f"I'm so sorry about that! You have {condition_name}. 😔")
        st.write(f"💡 **Advice**: {advice}")
    else:
        st.success(f"Congrats! You don't have {condition_name}. 🤝🎉")
        st.write(f"💡 **Advice**: {advice}")


# Liver Disease Prediction
if selected_model == 'Kidney Prediction':
    st.title("Kidney's Disease Prediction")

    # Input fields
    age = st.number_input('Age', min_value=1, max_value=120)
    bp = st.number_input('Blood Pressure (bp)', min_value=0, max_value=180)
    sg = st.number_input('Specific Gravity (sg)', min_value=1.000, max_value=1.050, step=0.001, format="%.3f")
    al = st.number_input('Albumin (al)', min_value=0)
    su = st.number_input('Sugar (su)', min_value=0)
    rbc = st.selectbox('Red Blood Cells (rbc)', ['Normal', 'Abnormal'])
    pc = st.selectbox('Pus Cell (pc)', ['Normal', 'Abnormal'])
    pcc = st.selectbox('Pus Cell Clumps (pcc)', ['Present', 'Not Present'])
    ba = st.selectbox('Bacteria (ba)', ['Present', 'Not Present'])
    bgr = st.number_input('Blood Glucose Random (bgr)', min_value=0.0)
    bu = st.number_input('Blood Urea (bu)', min_value=0.0)
    sc = st.number_input('Serum Creatinine (sc)', min_value=0.0)
    sod = st.number_input('Sodium (sod)', min_value=0.0)
    pot = st.number_input('Potassium (pot)', min_value=0.0)
    hemo = st.number_input('Hemoglobin (hemo)', min_value=0.0)
    pcv = st.number_input('Packed Cell Volume (pcv)', min_value=0)
    wc = st.number_input('White Blood Cell Count (wc)', min_value=0)
    rc = st.number_input('Red Blood Cell Count (rc)', min_value=0.0)
    htn = st.selectbox('Hypertension (htn)', ['Yes', 'No'])
    dm = st.selectbox('Diabetes Mellitus (dm)', ['Yes', 'No'])
    cad = st.selectbox('Coronary Artery Disease (cad)', ['Yes', 'No'])
    appet = st.selectbox('Appetite (appet)', ['Good', 'Poor'])
    pe = st.selectbox('Pedal Edema (pe)', ['Yes', 'No'])
    ane = st.selectbox('Anemia (ane)', ['Yes', 'No'])

    # Encoding inputs
    rbc_encoded = 1 if rbc == "Normal" else 0
    pc_encoded = 1 if pc == "Normal" else 0
    pcc_encoded = 1 if pcc == "Present" else 0
    ba_encoded = 1 if ba == "Present" else 0
    htn_encoded = 1 if htn == "Yes" else 0
    dm_encoded = 1 if dm == "Yes" else 0
    cad_encoded = 1 if cad == "Yes" else 0
    appet_encoded = 1 if appet == "Good" else 0
    pe_encoded = 1 if pe == "Yes" else 0
    ane_encoded = 1 if ane == "Yes" else 0

    input_data = np.array([
        age, rbc_encoded, pc_encoded, pcc_encoded, ba_encoded, htn_encoded,
        dm_encoded, cad_encoded, appet_encoded, pe_encoded, ane_encoded,
        bp, sg, al, su, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc
    ]).reshape(1, -1)

   # Prediction button
    if st.button("Results"):
        try:
            prediction = Kidney_model.predict(input_data)
            advice = "Make physical activity part of your routine!🏃🏻‍♂️‍➡️💪🏻🏋🏻‍♂️."
            display_result("Kidney Disease", prediction[0], advice)
        except ValueError:
            st.error(f"Please ensure all inputs are numeric and valid.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")        

# Kidney Disease Prediction
elif selected_model == 'Liver Prediction':
    st.title("Liver's Disease Prediction")
    
    # Input fields
    Age = st.number_input('Age', min_value=1)
    Gender_select = st.selectbox('Gender', ['Male', 'Female'])
    Gender_map = {'Male': 1, 'Female': 0}
    Gender = Gender_map.get(Gender_select)
    Total_Bilirubin = st.number_input('Total_Bilirubin', min_value=0.0)
    Direct_Bilirubin = st.number_input('Direct_Bilirubin', min_value=0.0)
    Alkaline_Phosphotase = st.number_input('Alkaline_Phosphotase', min_value=0)
    Alamine_Aminotransferase = st.number_input('Alamine_Aminotransferase', min_value=0)
    Aspartate_Aminotransferase = st.number_input('Aspartate_Aminotransferase', min_value=0)
    Total_Protiens = st.number_input('Total_Protiens', min_value=0.0)
    Albumin = st.number_input('Albumin', min_value=0.0)
    Albumin_and_Globulin_Ratio = st.number_input('Albumin_and_Globulin_Ratio', min_value=0.0)
    
    # Prediction button
    if st.button('Results'):
        data = {
            "Age": Age, "Gender": Gender, "Total_Bilirubin": Total_Bilirubin,
            "Direct_Bilirubin": Direct_Bilirubin, "Alkaline_Phosphotase": Alkaline_Phosphotase,
            "Alamine_Aminotransferase": Alamine_Aminotransferase,
            "Aspartate_Aminotransferase": Aspartate_Aminotransferase, "Total_Protiens": Total_Protiens,
            "Albumin": Albumin, "Albumin_and_Globulin_Ratio": Albumin_and_Globulin_Ratio
        }
        input_data = pd.DataFrame([data])
        prediction = liver_model.predict(input_data)
        advice = "Reduce the amount of saturated fats, transfats and hydrogenated fats in your diet.!"
        display_result("Liver Disease", prediction[0], advice)

# Parkinson Disease Prediction
elif selected_model == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction")

    # Input fields
    MDVP_Fo_Hz = st.number_input('MDVP:Fo(Hz)', min_value=0.0, step=0.1, format="%.2f")
    MDVP_Fhi_Hz = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, step=0.1, format="%.2f")
    MDVP_Flo_Hz = st.number_input('MDVP:Flo(Hz)', min_value=0.0, step=0.1, format="%.2f")
    MDVP_Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, step=0.01, format="%.4f")
    MDVP_Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, step=0.0001, format="%.5f")
    MDVP_RAP = st.number_input('MDVP:RAP', min_value=0.0, step=0.0001, format="%.5f")
    MDVP_PPQ = st.number_input('MDVP:PPQ', min_value=0.0, step=0.0001, format="%.5f")
    Jitter_DDP = st.number_input('Jitter:DDP', min_value=0.0, step=0.0001, format="%.5f")
    MDVP_Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, step=0.0001, format="%.5f")
    MDVP_Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, step=0.01, format="%.3f")
    Shimmer_APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, step=0.0001, format="%.5f")
    Shimmer_APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, step=0.0001, format="%.5f")
    MDVP_APQ = st.number_input('MDVP:APQ', min_value=0.0, step=0.0001, format="%.5f")
    Shimmer_DDA = st.number_input('Shimmer:DDA', min_value=0.0, step=0.0001, format="%.5f")
    NHR = st.number_input('NHR', min_value=0.0, step=0.0001, format="%.5f")
    HNR = st.number_input('HNR', min_value=0.0, step=0.1, format="%.2f")
    RPDE = st.number_input('RPDE', min_value=0.0, max_value=1.0, step=0.01, format="%.3f")
    DFA = st.number_input('DFA', min_value=0.0, max_value=2.0, step=0.01, format="%.3f")
    spread1 = st.number_input('spread1', min_value=-100.0, max_value=100.0, step=0.01, format="%.3f")
    spread2 = st.number_input('spread2', min_value=0.0, step=0.01, format="%.3f")
    D2 = st.number_input('D2', min_value=0.0, step=0.01, format="%.3f")
    PPE = st.number_input('PPE', min_value=0.0, step=0.01, format="%.3f")


    # Prediction button
    if st.button('Results'):
        input_data = pd.DataFrame([{
            'MDVP:Fo(Hz)': MDVP_Fo_Hz, 'MDVP:Fhi(Hz)': MDVP_Fhi_Hz,
            'MDVP:Flo(Hz)': MDVP_Flo_Hz, 'MDVP:Jitter(%)': MDVP_Jitter_percent,
            'MDVP:Jitter(Abs)': MDVP_Jitter_Abs, 'MDVP:RAP': MDVP_RAP,
            'MDVP:PPQ': MDVP_PPQ, 'Jitter:DDP': Jitter_DDP, 'MDVP:Shimmer': MDVP_Shimmer,
            'MDVP:Shimmer(dB)': MDVP_Shimmer_dB, 'Shimmer:APQ3': Shimmer_APQ3,
            'Shimmer:APQ5': Shimmer_APQ5, 'MDVP:APQ': MDVP_APQ, 'Shimmer:DDA': Shimmer_DDA,
            'NHR': NHR, 'HNR': HNR, 'RPDE': RPDE, 'DFA': DFA, 'spread1': spread1,
            'spread2': spread2, 'D2': D2, 'PPE': PPE
        }])
        prediction = parkinson_model.predict(input_data)
        advice = "Drinking plenty of fluids and exercising and Medications that treat Parkinson's disease can dry you out."
        display_result("Parkinson Disease", prediction[0], advice)
