import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    # Connexion à la base de données
    conn = sqlite3.connect('base de données/vraie_base.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Ici on pourra ajouter l'authentification avec mot de passe
        return redirect(url_for('statistique'))
    return render_template('connectio.html')

@app.route('/controle', methods=['GET', 'POST'])
def controle():
    conn = get_db_connection()
    etudiants = conn.execute('SELECT * FROM etudiant ORDER BY nom, prenom').fetchall()
    conn.close()
            
    if request.method == 'POST':
        # On récupère les requêtes (présent/absent) dans request.form
        # L'insertion dans la table présence se fera ici
        return redirect(url_for('statistique'))

    return render_template('controle.html', etudiants=etudiants)

@app.route('/statistique')
def statistique():
    # Tableau de bord
    return render_template('statistique.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
