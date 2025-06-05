from flask import Flask, request, render_template
import joblib  # ✅ utiliser joblib à la place de pickle
import numpy as np

app = Flask(__name__)

# Charger le modèle avec joblib
model = joblib.load('modele_cotes.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        cote_equipe_1 = float(request.form['cote_equipe_1'].replace(',', '.'))
        cote_nul = float(request.form['cote_nul'].replace(',', '.'))
        cote_equipe_2 = float(request.form['cote_equipe_2'].replace(',', '.'))

        features = np.array([[cote_equipe_1, cote_nul, cote_equipe_2]])
        prediction = model.predict(features)[0]

        return render_template('index.html', prediction_text=f"Résultat prédit : {prediction}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Erreur : {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
