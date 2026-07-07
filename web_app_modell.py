#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import streamlit as app
import streamlit
import joblib

# 1. Modell importieren
modell = joblib.load(r"linear_regression_model.pkl")

# 2. Streamlit UI aufbauen
streamlit.title("Regressionsmodell für die Vorhersage der Gesamtpunktzahl")
streamlit.write(
    "Gib deine wöchentlichen Lernstunden und deine Anwesenheit ein, um deine Punktzahl vorherzusagen."
)

streamlit.divider()

# Eingabefelder für den Nutzer
study_hours = streamlit.number_input(
    "Lernstunden angeben (täglich):", 
    min_value=0.0, 
    max_value=24.0, 
    value=3.0, 
    step=0.5
)

attendance_percentage = streamlit.slider(
    "Anwesenheit in % angeben:", 
    min_value=70.0, 
    max_value=100.0, 
    value=90.0, 
    step=1.0
)

# Button für die Vorhersage
if streamlit.button("Punktzahl berechnen"):
    score_features = {
        "study_hours": study_hours,
        "attendance_percentage": attendance_percentage
    }
    
    # In DataFrame umwandeln
    input_df = pd.DataFrame([score_features])
    
    # Vorhersage treffen
    score_prediction = modell.predict(input_df)[0]
    
    # Grenzen abfangen (wie in deinem Code)
    if score_prediction > 100:
        score_prediction = 100.0
    elif score_prediction < 0:
        score_prediction = 0.0
        
    # Ergebnis anzeigen
    streamlit.success(f"Deine vorgesehene Punktzahl wird **{score_prediction:.2f}** sein.")
    
    streamlit.info(
        "Bitte beachte, dass es sich um ein Modell handelt. Die Antworten könnten nicht zu 100% "
        "mit der endgültigen Note übereinstimmen. Das Modell ist zu ca. 90% genau."
    )


# In[ ]:





# In[ ]:




