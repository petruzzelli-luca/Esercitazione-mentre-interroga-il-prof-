from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from datetime import datetime
current_dateTime = datetime.now()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/aggiungi", methods=["GET", "POST"])
def aggiungi():
    if request.method == "POST":
        nuovo_profilo = {
            "nome": request.form["nome"],
            "cognome": request.form["cognome"],
            "sport": request.form["sport"],
            "data e ora": datetime.now(),
            "note opzionali": request.form["note opzionali"],
        }
        
        df = pd.read_csv("profile.csv")
        # Aggiungi il nuovo profilo
        df_nuovo = pd.concat([df, pd.DataFrame([nuovo_profilo])], ignore_index=True)
        
        # Salva il file CSV
        df_nuovo.to_csv("profile.csv", index=False)
        
        return redirect(url_for('home'))
    
    return render_template("aggiungi_prenotazione.html")

@app.route("/visualizza")
def visualizza():
    # Leggi il file CSV
    df = pd.read_csv("profile.csv")
    # Converti i dati in un dizionario per passarli al template
    prenotazioni = df.to_dict(orient="records")
    return render_template("visualizza_prenotazione.html", prenotazioni=prenotazioni)


if __name__ == '__main__':
    app.run(debug=True)