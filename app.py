import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model=pickle.load(open("C:/Users/Jessica/Desktop/Multiple disease pred/saved models/diabetes_model.sav", 'rb'))
heart_disease_model=pickle.load(open("C:/Users/Jessica/Desktop/Multiple disease pred/saved models/heart_disease_model.sav", 'rb'))
parkinsons_model=pickle.load(open("C:/Users/Jessica/Desktop/Multiple disease pred/saved models/parkinsons_model.sav", 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           default_index=0)
    
    # Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')
    
    # Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')
    
    # Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")
