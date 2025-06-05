from flask import Flask, render_template, request, redirect, url_for, session
import joblib

app = Flask(__name__)
app.secret_key = 'D@nieL07'  # Remplace par une vraie clé secrète

MOT_DE_PASSE = 'D@nieL07'

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        mot_de_passe = request.form.get('password')
        if mot_de_passe == MOT_DE_PASSE:
            session['authenticated'] = True
            return redirect(url_for('predict'))
        else:
            message = 'Mot de passe incorrect.'
    return render_template('login.html', message=message)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction_text = None
    if 'logged_in' not in session:
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
    app.run(host='0.0.0.0', port=10000)
