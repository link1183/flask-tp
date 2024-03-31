"""
    Fichier : msg_erreurs.py
    Auteur : OM 2021.03.16
    Erreurs particulières (personnalisées), qui n'existent que dans mon projet à moi.
    Quand il y a une erreur on doit définir des messages "clairs" sur un affichage à destination des "personnes".
    On ne doit pas les laisser devant des erreurs incompréhensibles.

"""
from pymysql.constants import ER

msg_erreurs = {
    "ErreurConnexionBD": {
        "message": "Pas de connexion à la BD ! Il faut démarrer un serveur MySql",
        "status": 400
    },
    "ErreurDoublonValue": {
        "message": "Cette valeur existe déjà.",
        "status": 400
    },
    "ErreurDictionnaire": {
        "message": "(OM du 164) Une valeur du dictionnaire n'existe pas !!!",
        "status": 400
    },
    "ErreurStructureTable": {
        "message": "Il y a un problème dans la structure des tables",
        "status": 400
    },
    "ErreurNomBD": {
        "message": "Problème avec le nom de la base de donnée",
        "status": 400
    },
    "ErreurPyMySql": {
        "message": "Problème en relation avec la BD",
        "status": 400
    },
    "ErreurDeleteContrainte": {
        "message": "Impossible d'effacer, car cette valeur est référencée ailleurs",
        "status": 400
    },
    "ErreurDeSyntaxeMySql": {
        "message": "Une erreur de syntaxe en MySql s'est glissée dans les requêtes",
        "status": 400
    },
}

"""
    Les constantes originales sont définies (dans PyMysql) dans le fichier "ER.py"
    Répertoire : /venv/Lib/site-packages/pymysql/constants)
    Il suffit de chercher cd fichier avec PyCharm "CTRL-SHIFT-N" "all places" "ER.py"
    
    But : Personnaliser le texte des erreurs originales.
"""
error_codes = {
    ER.DUP_ENTRY: "Ben cette valeur, elle existe déjà.",
    ER.PARSE_ERROR: "Ooouh là une très vilaine erreur de syntaxe en MySql.",
    ER.BAD_FIELD_ERROR: "La colonne de la table n'existe pas.",
    ER.NO_SUCH_TABLE: "La table n'existe pas."
}
