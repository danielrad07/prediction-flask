from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import os

app = Flask(__name__)
app.secret_key = 'vraiment-tres-secret'  # à personnaliser pour plus de sécurité

# Mot de passe simple pour accéder à l'application
PASSWORD = "D@nieL07"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            session['authenticated'] = True
            return redirect(url_for('predict'))
        else:
            return render_template('login.html', error="Mot de passe incorrect")

    # Affiche un message si l'utilisateur a été déconnecté
    logout_message = None
    if request.args.get('message') == 'logout':
        logout_message = "Vous avez été déconnecté avec succès."

    return render_template('login.html', message=logout_message)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if not session.get('logged_in'):
        return redirect('/')

    prediction_text = None  # <- corrige le crash
    if request.method == 'POST':
        try:
            cote1 = float(request.form['cote_equipe_1'])
            coteN = float(request.form['cote_nul'])
            cote2 = float(request.form['cote_equipe_2'])

            model = joblib.load('modele_cotes.pkl')
            prediction = model.predict([[cote1, coteN, cote2]])[0]
            prediction_text = f"Résultat prédit : {prediction}"
        except:
            prediction_text = "Erreur de saisie."

    return render_template('index.html', prediction_text=prediction_text)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login', message='logout'))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
