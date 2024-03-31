"""
    Tous les exemples ci-dessous proviennent du site :
    https://towardsdatascience.com/exception-handling-in-python-85f49801b131

"""

from APP_FILMS_164.erreurs.exceptions import ErreurFichierSqlDump


def myfunction(a, b):
    return a + b


# try:
#     myfunction(100, "one hundred")
# except:
#     raise

try:
    myfunction(100, "one hundred")
except TypeError:
    print("Cannot sum the variables. Please pass numbers only.")

try:
    myfunction(100, "one hundred")
except TypeError as e:
    print(f"Cannot sum the variables. The exception was: {e}")

try:
    myfunction(100, a)
except (TypeError, NameError) as e:
    print(f"Cannot sum the variables. The exception was {e}")

try:
    myfunction(100, 12)
    if 12 > 34:
        print("ok")
    else:
        print("non 12 n'est pas supérieur à 34 !")
        raise ErreurFichierSqlDump("Essai raise ErreurFichierSqlDump ")
except (TypeError, NameError) as e:
    print(f"Cannot sum the variables. The exception was {e}")
except Exception as e:
    print(f"Unhandled exception: {e}")
