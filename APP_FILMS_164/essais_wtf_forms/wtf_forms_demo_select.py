"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF

    But : Essayer un formulaire avec WTForms
"""
from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import SelectField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Regexp


class MonPremierWTForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(message="Il manque le mot de passe !!!")])

    nom_genre_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_wtf = StringField("Clavioter le genre ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_genre_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, d'espace à double, "
                                                                                  "de double apostrophe, "
                                                                                  "de double trait union")
                                                                   ])

    case_cocher_npc = BooleanField('Ne pas cliquer')

    submit = SubmitField('Ok !')


"""
    Dans le formulaire "templates/zzz_essais_om_104/demo_form_select_wtf.html"
    Auteur : OM 2021.04.11
    
    But : Montrer l'utilisation d'une liste déroulante (WTF) dont le contenu est basé sur la table "t_genre"
    
"""


class DemoFormSelectWTF(FlaskForm):
    genres_dropdown_wtf = SelectField('Genres (liste déroulante)',
                                      validators=[DataRequired(message="Sélectionner un genre.")],
                                      validate_choice=False
                                      )
    # Alternative qui correspond aux lignes en commentaires lignes 88 et 89 du "gestion_wtf_forms_demo_select.py"
    # genres_dropdown_wtf = SelectField('Genres (liste déroulante)',
    #                                   validators=[DataRequired(message="Sélectionner un genre.")],
    #                                   validate_choice=False,
    #                                   coerce=int
    #                                   )
    submit_btn_ok_dplist_genre = SubmitField("Choix genre")
