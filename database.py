#############################
# Database
# Zachary Smith
# PROJET DBPY
# Dernière modif 05.12.2023
#############################

import mysql.connector, datetime
from geo01 import *
from mysql.connector import errorcode


def open_dbconnection():
    """
    open connection to the database
    """
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', user='Zach', password='Pa$$w0rd', port='3306',
                                            database='projet_dbpy', buffered=True, autocommit=True)
    return db_connection


def close_dbconnection():
    """
    close connection to the database
    """
    db_connection.close()


def data_results(pseudo="", exercise=""):
    infos = []
    open_dbconnection()
    cursor = db_connection.cursor()
    query = "Select pseudo, date_et_heure, temp, MiniGame_id, nb_ok, nb_trials, id from results"
    if pseudo != "" and exercise != "":
        query += " WHERE pseudo=%s and MiniGame_id=%s"
        cursor.execute(query, (pseudo, get_exercice_id(exercise)[0]))
    elif pseudo != "":
        query += " WHERE pseudo=%s"
        cursor.execute(query, (pseudo,))
    elif exercise != "":
        query += " WHERE MiniGame_id=%s"
        cursor.execute(query, (get_exercice_id(exercise)[0],))
    else:
        cursor.execute(query)
    name = cursor.fetchall()
    infos.append(name)
    cursor.close()
    return infos


def total_data_results(pseudo="", exercise=""):
    open_dbconnection()
    cursor = db_connection.cursor()
    query = "Select count(pseudo), sum(temp), sum(nb_ok), sum(nb_trials) from results"
    if pseudo != "" and exercise != "":
        query += " WHERE pseudo=%s and MiniGame_id=%s"
        cursor.execute(query, (pseudo, get_exercice_id(exercise)[0]))
    elif pseudo != "":
        query += " WHERE pseudo=%s"
        cursor.execute(query, (pseudo,))
    elif exercise != "":
        query += " WHERE MiniGame_id=%s"
        cursor.execute(query, (get_exercice_id(exercise)[0],))
    else:
        cursor.execute(query)
    results = cursor.fetchall()[0]
    data = (results[0], int(results[1]), int(results[2]), int(results[3]))
    cursor.close()
    return data


def insert_results(pseudo, date_hour, duration, nb_ok, nb_trials, minigame_id):
    open_dbconnection()
    try:
        cursor = db_connection.cursor()
        # create the query
        insert_query = "INSERT INTO results (pseudo, date_et_heure, temp, nb_trials, nb_ok, minigame_id) VALUES (%s, %s, %s, %s, %s, %s)"
        # Execute the query to insert results
        cursor.execute(insert_query, (pseudo, date_hour, duration, nb_ok, nb_trials, minigame_id))
        # commit the results
        db_connection.commit()
        # Close cursor and connection
        cursor.close()
        db_connection.close()
        print("Résultats insérés avec succès dans la base de données.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Accès refusé : Veuillez vérifier vos informations d'identification.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Base de données inexistante : Veuillez vérifier le nom de votre base de données.")
        else:
            print("Erreur MySQL inattendue :", err)
    close_dbconnection()


def modify_result(dataset, id):
    open_dbconnection()
    try:
        exercise_id = get_exercice_id(dataset[3])[0]
        date_data = dataset[1].split(" ")
        date_date_data = date_data[0].split("-")
        date_time_data = date_data[1].split(":")
        final_date = datetime.datetime(int(date_date_data[0]), int(date_date_data[1]), int(date_date_data[2]),
                                       int(date_time_data[0]), int(date_time_data[1]), int(date_time_data[2]))
        final_time = dataset[2]
        okay_tries = int(dataset[4])
        total_tries = int(dataset[5])
    except:
        return
    query = "UPDATE results SET pseudo = %s, date_et_heure = %s, temp = %s, nb_trials = %s, nb_ok = %s, minigame_id = %s WHERE id=%s"
    cursor = db_connection.cursor()
    cursor.execute(query, (dataset[0], final_date, final_time, total_tries, okay_tries, exercise_id, id))


def destroy_result(id):
    open_dbconnection()
    query = "DELETE FROM results WHERE id=%s"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))


def get_exercice_name(id):
    cursor = db_connection.cursor()
    query = "Select MiniGame_name from minigame where id=%s"
    cursor.execute(query, (id, ))
    result = cursor.fetchone()
    return result


def get_exercice_id(name):
    cursor = db_connection.cursor()
    query = "Select id from minigame where MiniGame_name=%s"
    cursor.execute(query, (name, ))
    result = cursor.fetchone()
    return result



