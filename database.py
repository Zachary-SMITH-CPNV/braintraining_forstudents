import mysql.connector
from geo01 import *
from mysql.connector import errorcode
def open_dbconnection():
    """
    open connection to the database
    """
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', user='Zach', password='Pa$$w0rd', port='3306',
                                            database='projet_dbpy', buffered=True, autocommit=True)


def close_dbconnection():
    """
    close connection to the database
    """
    db_connection.close()


def insert_results(pseudo, date_hour, duration, nb_ok, nb_trials, minigame_id):
    try:
        # Connectez-vous à votre base de données avec les bons paramètres
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='Zach',
            password='Pa$$w0rd',
            database='projet_dbpy'
        )

        # Créez un objet curseur pour exécuter des requêtes SQL
        cursor = connection.cursor()

        # Définissez votre requête SQL d'insertion
        insert_query = "INSERT INTO results (pseudo, date_et_heure, temp, nb_ok, nb_trials, minigame_id) VALUES (%s, %s, %s, %s, %s, %s)"

        # Exécutez la requête en utilisant les valeurs que vous avez passées à la fonction
        cursor.execute(insert_query, (pseudo, date_hour, duration, nb_ok, nb_trials,minigame_id))

        # Validez la transaction
        connection.commit()

        # Fermez le curseur et la connexion
        cursor.close()
        connection.close()

        print("Résultats insérés avec succès dans la base de données.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Accès refusé : Veuillez vérifier vos informations d'identification.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Base de données inexistante : Veuillez vérifier le nom de votre base de données.")
        else:
            print("Erreur MySQL inattendue :", err)