"""
    Fichier : exceptions.py
    Auteur : OM 2021.03.07
    Classes pour définir des erreurs particulières (personnalisées), qui n'existent que dans mon projet à moi.
    Quand il y a une erreur on doit définir des messages "clairs" sur un affichage à destination des "personnes".
    On ne doit pas les laisser devant des erreurs incompréhensibles.
    Dérivation des classes standard des "except" dans les blocs "try...except"
"""
import sys

from flask import flash, render_template
from pymysql import IntegrityError

from APP_FILMS_164 import app


class Base(Exception):
    """
    Handled in Base Handler, will result of an error page display.
    Display an base error flash message
    """

    def __init__(self, message):
        self.message = message


class ErreurFichierSqlDump(Exception):
    """Erreur qui doit être affichée lorsque le fichier DUMP à un problème"""
    pass


class ErreurFichierEnvironnement(Exception):
    """Erreur qui doit être affichée lorsque le fichier des variables d'environnement pose un problème"""
    pass


class ExceptionInitApp(Exception):
    pass


class ErreurConnectionBD(Exception):
    """Erreur qui doit être affichée lorsque la connection à la bd pose un problème"""
    pass


class ErreurExtractNameBD(Exception):
    """Erreur qui doit être affichée lorsque c'est impossible d'extraire le nom de la BD depuis le fichier DUMP """
    pass


class MaBdErreurDoublon(IntegrityError):
    """Erreur qui doit être affichée lorsqu'une valeur en "double" (doublon) veut être insérée dans une table"""
    pass


class MonErreur(Exception):
    """Erreur qui doit être affichée lors d'une expérience avec du code à OM de la 707"""
    pass


class MaBdErreurConnexion(Exception):
    """Erreur qui doit être affichée lorsque la connection à la BD à des problèmes"""
    pass


class DatabaseException(Base):
    pass


class SqlException(DatabaseException):
    pass


class SqlSyntaxError(SqlException):
    pass


class DatabaseException(Base):
    pass


class ExceptionGenresAfficher(Base):
    pass


class ExceptionGenreDeleteWtf(Base):
    pass


class ExceptionGenreUpdateWtf(Base):
    pass


class ExceptionGenresAjouterWtf(Base):
    pass


class ExceptionFilmsGenresAfficher(Base):
    pass


class ExceptionEditGenreFilmSelected(Base):
    pass


class ExceptionUpdateGenreFilmSelected(Base):
    pass


class ExceptionGenresFilmsAfficherData(Base):
    pass


class ExceptionFilmUpdateWtf(Base):
    pass


class ExceptionFilmDeleteWtf(Base):
    pass


class ExceptionInitAppFilms164(Base):
    pass


"""
    Grâce à la méthode "flash" cela permet de "raise" (remonter) les erreurs "try...execpt" dans la page "home.html"
"""


@app.errorhandler(Exception)
def om_104_exception_handler(error):
    flash(f"Erreur : {error} {error.args[0]} {sys.exc_info()[0]}", "danger")
    a, b, c = sys.exc_info()
    flash(f"Erreur générale : {a} {b} {c}", "danger")

    return render_template("home.html")


"""
    Pour définir sa propre page d'erreur 404
    Ce code est repris de la documentation FLASK
    https://flask-doc.readthedocs.io/en/latest/patterns/errorpages.html
"""


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
