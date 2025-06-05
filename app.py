from flask import Flask, render_template, request, redirect, session
import joblib

app = Flask(__name__)
app.secret_key = 'D@nieL07'  # change ce mot si tu veux

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['password'] == 'D@nieL07':  # 🔐 Ton mot de passe ici
            session['logged_in'] = True
            return redirect('/predict')
        else:
            return render_template('login.html', error='Mot de passe incorrect.')
    return render_template('login.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if not session.get('logged_in'):
        return redirect('/')

    prediction_text = None
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
    session.pop('logged_in', None)
    return redirect('/')
