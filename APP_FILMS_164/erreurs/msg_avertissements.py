"""
    Fichier : msg_avertissements.py
    Auteur : OM 2021.05.02

    Messages d'avertissement. Souvent à caractère informatif.
    Certains peuvent sembler être abrupts.

"""
from flask import render_template
from APP_FILMS_164 import app


@app.route("/avertissement_sympa_pour_geeks")
def avertissement_sympa_pour_geeks():
    # Envoie la page "HTML" au serveur.
    return render_template("films_genres/avertissement_projet.html")