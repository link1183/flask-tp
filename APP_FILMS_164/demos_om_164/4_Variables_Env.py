"""
    Fichier : 4_Variables_Env.py
    Auteur : OM 2021.03.15 Démonstration de l'accès aux variables d'environnement

    Paramètres : Fichier nommé ".env" situé dans le répertoire principal
                Le fichier ".env" DOIT être signalé dans le ".gitignore",
                car il contient des données confidentielles (key, passwords, etc)
"""
import os
import pprint

import environs
from environs import Env

from APP_FILMS_164.erreurs.exceptions import ErreurFichierEnvironnement



try:

    os_env_var = os.environ
    print("User's Environment variable:")
    pprint.pprint(dict(os_env_var), width=1)

    """
        Démo : on accède aux variables d'environnement existantes 
    """
    obj_env = Env()
    computer_name = obj_env("COMPUTERNAME")
    print("computer_name ", computer_name)

    """
        Démo : on accède aux variables d'environnement de l'utilisateur 
    """
    try:
        """
            obj_env("PORT_MYSQL") permet de récupérer le num. du port dans le fichier ".env"
            obj_env.int("PORT_FLASK") permet de récupérer le num. du port (INTEGER) dans le fichier ".env"
        """
        obj_env.read_env()
        DEMO_PORT_MYSQL = obj_env("PORT_MYSQL")
        print("DEMO_PORT_MYSQL dans le fichier \".env\" ", DEMO_PORT_MYSQL)

        DEMO_PORT_FLASK = obj_env.int("PORT_FLASK")
        print("DEMO_PORT_FLASK dans le fichier \".env\" ", DEMO_PORT_FLASK)

    except FileNotFoundError as erreur_file_not_found:
        print(f"Erreur fichier \".env\" introuvable (nom, emplacement, etc) (variables environnement)",
              f"{erreur_file_not_found.args[0]}, "
              f"{erreur_file_not_found}")
        raise

except environs.EnvError as NameVariableEnv:
    print(f"Problème avec les variables d'environnement "
          f"{NameVariableEnv.args[0]} , "
          f"{NameVariableEnv}")

except Exception as erreur_fichier_environnement:
    print(f"Problème avec le fichier \".env\" (nom, emplacement, etc) "
          f"{erreur_fichier_environnement.args[0]} , "
          f"{erreur_fichier_environnement}")
    raise ErreurFichierEnvironnement(f"Problème avec le fichier \".env\" (nom, emplacement, etc)")