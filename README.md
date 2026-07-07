# Schüler-Leistungs-Analyse und KI-Vorhersage #

Dieses Projekt untersucht die Einflussfaktoren auf schulische Leistungen basierend auf einem Datensatz von 25'000 Schülern. Es kombiniert klassische statistische Analysen mit modernem Machine Learning.

## Projektaufbau ##

### Teil 1: Statistische Auswertung (EDA) ###
- **Datei:** `schueler_analyse.ipynb` / `Analyse.md`
- **Inhalt:** Datenbereinigung, Verteilungsanalysen (Boxplots, Histogramme) und Korrelationsberechnungen im Rahmen des Schweizer EFZ-Moduls 375.

### Teil 2: Machine Learning Noten-Vorhersage ###
- **Datei:** `regressionsmodell_schueler_daten.ipynb`
- **Inhalt:** Ein lineares Regressionsmodell (Scikit-Learn), das mit einer Genauigkeit von **90.5%** ($R^2 = 0.905794$, MAE = 4.955555) die Gesamtpunktzahl vorhersagt.
- **Zusatz:** Enthält eine interaktive Konsolen-App zur Live-Abfrage von Schülerdaten inklusive Error-Handling und automatischem Daten-Clipping. Dazu gibt es auch eine `.py`-Datei zur Ausführung der Streamlit Web-Applikation.

### Installation und Start ###
- **Pakete installieren:** `streamlit`, `pandas` und `scikit-learn` installieren mit:
  ```bash
  pip install streamlit pandas scikit-learn joblib
- **Dateien ordnen:** `linear_regression_model.pkl` und `web_app_modell.py` im gleichen Pfad speichern.
- **Pfad definieren:** Im Terminal den Pfad angeben, wo beide Dateien sind mit:
  ```bash
  cd /pfad/zu/deinem/ordner
- **Streamlit ausführen:** Mit folgendem Command das Skript ausführen:
  ```bash
  streamlit run web_app_modell.py
