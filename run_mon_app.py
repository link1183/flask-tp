"""Point de départ de l'application
Fichier : run_mon_app.py
Auteur : OM 2023.03.25

Définition et paramètres du microframework FLASK

Exemples : https://flask.palletsprojects.com/en/2.1.x/quickstart/#a-minimal-application

"""

from APP_FILMS_164 import app
from APP_FILMS_164 import SECRET_KEY_FLASK
from APP_FILMS_164 import DEBUG_FLASK
from APP_FILMS_164 import ADRESSE_SRV_FLASK
from APP_FILMS_164 import PORT_FLASK
from flask_cors import CORS

"""Pour comprendre à quoi sert CORS... et en cas de curiosité maladive...
ne PAS cliquer sur le lien ci-dessous, car c'est bien expliqué.
https://developer.mozilla.org/fr/docs/Web/HTTP/CORS
"""
CORS(app)

if __name__ == '__main__':
    # OM 2023.03.25
    # Les variables d'environnement de FLASK sont définies dans le fichier ".env"
    # Une clé est nécessaire pour crypter les "cookies" utilisés par les messages FLASH.
    app.secret_key = SECRET_KEY_FLASK
    # DEBUG_FLASK   inutile de vous dire que c'est insdipensable ... avant la version finale
    app.run(debug=DEBUG_FLASK, host=ADRESSE_SRV_FLASK, port=PORT_FLASK)
