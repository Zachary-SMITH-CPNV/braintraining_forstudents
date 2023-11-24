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

def data_results():
    infos = []
    cursor = db_connection.cursor()
    query = "Select pseudo, date_et_heure, temp, MiniGame_id, nb_ok, nb_trials, MiniGame_id from results"
    cursor.execute(query)
    name = cursor.fetchall()
    infos.append(name)
    cursor.close()
    return infos

def insert_results(pseudo, date_hour, duration, nb_ok, nb_trials, minigame_id):
    try:
        # Connection to database
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='Zach',
            password='Pa$$w0rd',
            database='projet_dbpy'
        )
        cursor = connection.cursor()
        # create the query
        insert_query = "INSERT INTO results (pseudo, date_et_heure, temp, nb_trials, nb_ok, minigame_id) VALUES (%s, %s, %s, %s, %s, %s)"
        # Execute the query to insert results
        cursor.execute(insert_query, (pseudo, date_hour, duration, nb_ok, nb_trials,minigame_id))
        # commit the results
        connection.commit()
        # Close cursor and connection
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

def get_exercice_name(id):
    cursor = db_connection.cursor()
    query = "Select MiniGame_name from minigame where id=%s"
    cursor.execute(query, (id, ))
    result = cursor.fetchone()
    return result