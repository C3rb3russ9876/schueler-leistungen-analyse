#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# In[37]:


# Datensatz öffnen und Struktur lesen

df = pd.read_csv(r"Student_Performance (1).csv") # CSV öffnen

df.info() # Informationen bekommen


# In[38]:


df.head(15) #Einblick erhalten


# In[39]:


# Regressionsmodell implementieren

# X (Features) definieren und y (Target) definieren
X = df[["study_hours", "attendance_percentage"]]
y = df["overall_score"]

# Daten aufteilen (80% trainieren und 20% testen)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=17)

# Modell definieren und trainieren
modell = LinearRegression()
modell.fit(X_train, y_train)

# Vorhersage definieren
y_prediction = modell.predict(X_test)

# Auswertung geben
# Wichtig: R^2 beschreibt wie genau das Modell ist, während der Mean Absolute Error (MAE) den durchschnittlichen Fehler angibt bzw., wie weit es vom eigentlichen Wert liegt.
print(f"R^2 (Genauigkeitsniveau: 1=Perfekt, 0=ähnlich, wie Durchschnitt, -1=Durchschnitt ist genauer): {r2_score(y_test, y_prediction)}")
print(f"Durchschnittsfehler (MAE): {mean_absolute_error(y_test, y_prediction)} Punkte")


# In[40]:


# Modell präziser machen mit One-Hot-Encoding

# String-Werte mit 0 und 1 Kodieren
df_encoded = pd.get_dummies(df, columns=["parent_education", "school_type"], drop_first=True)

df_encoded.head()


# In[41]:


# Neues Regressionsmodell implementieren

# X (Features) und y (Zielwert) definieren
X_komplex = df_encoded[
    [
        "study_hours", 
        "attendance_percentage", 
        "parent_education_graduate", 
        "parent_education_high school", 
        "parent_education_no formal", 
        "parent_education_phd", 
        "parent_education_post graduate", 
        "school_type_public"
    ]
]
y_komplex = df_encoded["overall_score"]

# Daten für das Training aufteilen
X_komplex_train, X_komplex_test, y_komplex_train, y_komplex_test = train_test_split(X_komplex, y_komplex, test_size=0.2, random_state=17)

# Modell definieren und trainieren
modell_komplex = LinearRegression()
modell_komplex.fit(X_komplex_train, y_komplex_train)

# Werte vorhersagen
y_komplex_prediction = modell_komplex.predict(X_komplex_test)

# Werte ausgeben
print(f"R^2 (Genauigkeit): {r2_score(y_komplex_prediction, y_komplex_test)}")
print(f"Standard Fehler (MAE): {mean_absolute_error(y_komplex_prediction, y_komplex_test)}")

# Das neue Modell ist ungenauer als das alte, deswegen werde ich für die Konsole den alten Modell verwenden


# In[44]:


# Einfache GUI zur Verwendung des einfacheren Modells

def main():
    print("-"*50)
    print("-"*17, "Notenvorhersage", "-"*16)
    print("-"*50)
    print("\n")

    # Features abfragen
    while True:
        try:
            study_hours = float(input("Bitte Lernstunden angeben (wöchentlich): "))
            if study_hours > 56 or study_hours < 0:
                print("Bitte deine echte Lernzeit angeben.")
            else:
                break
        except ValueError:
            print("Bitte nur Zahlen angeben.")
    while True:
        try:
            attendance_percentage = float(input("Bitte Anwesenheit in % angeben: "))
            if attendance_percentage > 100 or attendance_percentage < 70:
                    print("Bitte deine echte Anwesehneit angeben.")
            else:
                break
        except ValueError:
            print("Bitte nur Zahlen angeben.")
                

    # Alle One-Hot-Encoding Features auf 0 setzen
    score_features = {column: 0 for column in X.columns}

    # Features im Dictionary definieren
    score_features["study_hours"] = study_hours
    score_features["attendance_percentage"] = attendance_percentage

    # Neuer Datensatz mit gewünschten Features erstellen
    new_df = pd.DataFrame([score_features])

    # Preis vorhersagen
    score_prediction = modell.predict(new_df)[0]

    # Wert ausgeben und Disclaimer anzeigen
    print("\n")
    print("-"*50)
    if score_prediction > 100:
        print(f"Deine vorgesehene Punktzahl wird 100 sein")
    elif score_prediction < 0:
        print(f"Deine vorgesehene Punktzahl wird 0 sein")
    else:
        print(f"Deine vorgesehene Punktzahl wird {score_prediction:.2f} sein")
    print("-"*50)
    print("\n")
    print("Bitte beachte, dass es sich um ein Modell handelt. Die Antworten könnten nicht zu 100% mit der endgültigen Note stimmen. Das Modell ist zu 90% genau und hat einen Standard Fehler von 4.95 Punkte.")

if __name__ == "__main__":
    main()


# In[45]:


# Modell speichern
joblib.dump(modell, "linear_regression_model.pkl")


# In[ ]:




