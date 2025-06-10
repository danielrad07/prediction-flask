from flask import Flask, render_template, request, redirect, url_for, session
import joblib

import datetime
model = joblib.load('modele_cotes.pkl')
print("🕒 Modèle chargé à", datetime.datetime.now())

app = Flask(__name__)
app.secret_key = 'D@nieL07'  # Tu peux remplacer ça plus tard par une variable d’environnement

# Mot de passe simple (à sécuriser plus tard)
MOT_DE_PASSE = 'D@nieL07'

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        mot_de_passe = request.form.get('password')
        if mot_de_passe == MOT_DE_PASSE:
            session['authenticated'] = True  # Correction ici
            return redirect(url_for('predict'))
        else:
            message = 'Mot de passe incorrect.'
    return render_template('login.html', message=message)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction_text = None
    # Correction ici — on vérifie bien la bonne clé de session
    if 'authenticated' not in session:
        return redirect('/')
    
    if request.method == 'POST':
        try:
            cote1 = float(request.form['cote_equipe_1'])
            coteN = float(request.form['cote_nul'])
            cote2 = float(request.form['cote_equipe_2'])
            model = joblib.load('modele_cotes.pkl')
            prediction = model.predict([[cote1, coteN, cote2]])[0]
            prediction_text = f"Résultat prédit : {prediction}"
        except Exception as e:
            prediction_text = f"Erreur : {e}"
    
    return render_template('index.html', prediction_text=prediction_text)

@app.route('/logout')
def logout():
    session.pop('authenticated', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)

