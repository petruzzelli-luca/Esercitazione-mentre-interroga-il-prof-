from flask import Flask, render_template, request, redirect, url_for
import pandas 
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/aggiungi", methods=["GET", "POST"])
def aggiungi():
    if request.method == "POST":
        nuovo_profilo = {
            "Nome": request.form["nome"],
            "Cognome": request.form["cognome"],
            "sport": request.form["sport"],
        }
        df = pandas.read_csv("profile.csv")
        df_nuovo = pandas.concat([df, pandas.DataFrame([nuovo_profilo])], ignore_index=True)
        df_nuovo.to_csv("profile.csv", index=False)
        return redirect(url_for('home'))
    
    return render_template("aggiungi.html")



if __name__ == '__main__':
    app.run(debug=True)