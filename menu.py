#############################
# Training (Menu)
# JCY oct 23
# PRO DB PY
#############################
import tkinter as tk


import database
import geo01
import info02
import info05
from tkinter import *
from database import *

# Exercises array
a_exercise = ["geo01", "info02", "info05"]
albl_image = [None, None, None]  # Label (with images) array
a_image = [None, None, None]  # Images array
a_title = [None, None, None]  # Array of title (e.g., GEO01)

dict_games = {"geo01": geo01.open_window_geo_01, "info02": info02.open_window_info_02, "info05": info05.open_window_info_05}

# Call other windows (exercises)
def exercise(event, exer):
    dict_games[exer](window)

# Main window
window = tk.Tk()
window.title("Training, entrainement cérébral")
window.geometry("1100x900")

# Color definition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color  # Translation to hexa
window.configure(bg=hex_color)
window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

# Title creation
lbl_title = tk.Label(window, text="TRAINING MENU", font=("Arial", 15))
lbl_title.grid(row=0, column=1, ipady=5, padx=40, pady=40)

# Labels creation and positioning
for ex in range(len(a_exercise)):
    a_title[ex] = tk.Label(window, text=a_exercise[ex], font=("Arial", 15))
    a_title[ex].grid(row=1 + 2 * (ex // 3), column=ex % 3, padx=40, pady=10)  # 3 labels per row

    a_image[ex] = tk.PhotoImage(file="img/" + a_exercise[ex] + ".gif")  # Image name
    albl_image[ex] = tk.Label(window, image=a_image[ex])  # Put image on label
    albl_image[ex].grid(row=2 + 2 * (ex // 3), column=ex % 3, padx=40, pady=10)  # 3 labels per row
    albl_image[ex].bind("<Button-1>", lambda event, ex=ex: exercise(event=None, exer=a_exercise[ex]))  # Link to others .py


# Buttons, display results & quit
btn_display = tk.Button(window, text="Display results", font=("Arial", 15))
btn_display.grid(row=1 + 2 * len(a_exercise) // 3, column=1)
btn_display.bind("<Button-1>", lambda e: display_result(e))

btn_finish = tk.Button(window, text="Quitter", font=("Arial", 15))
btn_finish.grid(row=2 + 2 * len(a_exercise) // 3, column=1)
btn_finish.bind("<Button-1>", quit)


# Call display_results
def display_result(event):
    # Create a new window for displaying results
    result_window = tk.Toplevel(window)
    result_window.title("Affichage braintraining")
    result_window.geometry("1100x900")

    # Color definition
    result_window.configure(bg="light blue")
    result_window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    # Frames
    filter_frame = tk.Frame(result_window, bg="white", padx=10)
    info_results_frame = tk.Frame(result_window, bg="white", padx=10)
    results_frame = tk.Frame(result_window, bg="white", padx=10)
    total_frame = tk.Frame(result_window, bg="white", padx=10)
    res_total_frame = tk.Frame(result_window, bg="white", padx=10)

    # Totals labels TODO
    lbl_trials = tk.Label(total_frame, text="NbLignes", bg="white", padx=20, font=("Arial", 10))
    lbl_time = tk.Label(total_frame, text="Temps trials", bg="white", padx=20, font=("Arial", 10))
    lbl_nbok = tk.Label(total_frame, text="Nb OK", bg="white", padx=20, font=("Arial", 10))
    lbl_nbtotal = tk.Label(total_frame, text="Nb Total", bg="white", padx=20, font=("Arial", 10))
    lbl_purcenttot = tk.Label(total_frame, text="% Total", bg="white", padx=20, font=("Arial", 10))

    # Frame total
    total_frame.grid(row=4, pady=10, columnspan=3)
    res_total_frame.grid(row=7, pady=10, columnspan=3)
    lbl_trials.grid(row=0, column=0, padx=(0, 10))
    lbl_time.grid(row=0, column=1, padx=(0, 10))
    lbl_nbok.grid(row=0, column=2, padx=(0, 10))
    lbl_nbtotal.grid(row=0, column=3, padx=(0, 10))
    lbl_purcenttot.grid(row=0, column=4, padx=(0, 10))

    # Title of the results display
    lbl_title = tk.Label(result_window, text="TOTAL: RESULTS", font=("Arial", 15))
    lbl_title.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    # Labels for filters TODO Apply filter function
    lbl_pseudo = tk.Label(filter_frame, text="Pseudo:", bg="white", padx=10, font=("Arial", 10))
    lbl_ex_name = tk.Label(filter_frame, text="Nom Exercice:", bg="white", padx=10, font=("Arial", 10))
    lbl_start_date = tk.Label(filter_frame, text="Date début:", bg="white", padx=10, font=("Arial", 10))
    lbl_end_date = tk.Label(filter_frame, text="Date fin:", bg="white", padx=10, font=("Arial", 10))

    # Results labels in columns
    lbl_column_pseudo = tk.Label(info_results_frame, text="pseudo/Élève", bg="white", padx=20, font=("Arial", 10))
    lbl_column_date_hour = tk.Label(info_results_frame, text="Date et heure", bg="white", padx=20, font=("Arial", 10))
    lbl_column_time = tk.Label(info_results_frame, text="Temps", bg="white", padx=20, font=("Arial", 10))
    lbl_column_ex = tk.Label(info_results_frame, text="Exercice", bg="white", padx=20, font=("Arial", 10))
    lbl_column_nbok = tk.Label(info_results_frame, text="nb ok", bg="white", padx=20, font=("Arial", 10))
    lbl_column_nbtrials = tk.Label(info_results_frame, text="nb essai", bg="white", padx=20, font=("Arial", 10))
    lbl_column_succes = tk.Label(info_results_frame, text="% réussi", bg="white", padx=20, font=("Arial", 10))

    # Filters Entry
    entry_user = tk.Entry(filter_frame)
    entry_ex = tk.Entry(filter_frame)
    entry_start_date = tk.Entry(filter_frame)
    entry_enddate = tk.Entry(filter_frame)

    # Buttons TODO ajouter l'application des filtre des resultats
    button_result = tk.Button(filter_frame, text="Voir résultats", font=("Arial", 11),
                              command=lambda: create_table(results_frame, (entry_user.get(), entry_ex.get()),
                                                           res_total_frame))

    # placement of filters
    filter_frame.grid(row=1, columnspan=3)
    lbl_pseudo.grid(row=0, column=0, padx=(0, 10))

    entry_user.grid(row=0, column=1)
    lbl_ex_name.grid(row=0, column=2, padx=(0, 10))

    entry_ex.grid(row=0, column=3)
    lbl_start_date.grid(row=0, column=4, padx=(0, 10))

    entry_start_date.grid(row=0, column=5)
    lbl_end_date.grid(row=0, column=6, padx=(0, 10))

    entry_enddate.grid(row=0, column=7)
    button_result.grid(row=1, column=0, pady=5)

    # Placement of results columns
    info_results_frame.grid(row=2, pady=10, columnspan=3)
    results_frame.grid(row=3, pady=10, columnspan=3)

    lbl_column_pseudo.grid(row=0, column=0, padx=(0, 10))
    lbl_column_date_hour.grid(row=0, column=1, padx=(0, 10))
    lbl_column_time.grid(row=0, column=2, padx=(0, 10))
    lbl_column_ex.grid(row=0, column=3, padx=(0, 10))
    lbl_column_nbok.grid(row=0, column=4, padx=(0, 10))
    lbl_column_nbtrials.grid(row=0, column=5, padx=(0, 10))
    lbl_column_succes.grid(row=0, column=6, padx=(0, 10))

    create_table(results_frame, ("", ""), res_total_frame)

def create_table(res_frame, variables, tot_frame):
    # Results from Heidi sql to insert in results
    for widget in res_frame.winfo_children():
        widget.destroy()
    open_dbconnection()
    dataset = data_results(variables[0], variables[1])
    i = 0
    for student in dataset:
        for j in range(len(student)):
            for data in range(len(student[j])):
                if data != 2 and data != 3:
                    # Display results data and insert in frame
                    e = tk.Label(res_frame, width=15, text=student[j][data], relief="solid", borderwidth=1)
                elif data == 2:
                    e = tk.Label(res_frame, width=15, text=f"{student[j][data]}s", relief="solid", borderwidth=1)
                elif data == 3:
                    e = tk.Label(res_frame, width=15, text=get_exercice_name(student[j][data]), relief="solid", borderwidth=1)
                e.grid(row=j + 1, column=i + data)
            try:
                # Calculate and display the percentage
                e = tk.Label(res_frame, width=15, text=f"{round(float(student[j][4]) * 100 / float(student[j][5]), 0)}%", relief="solid", borderwidth=1)
            except ZeroDivisionError:
                e = tk.Label(res_frame, width=15, text="0%", relief="solid", borderwidth=1)
            e.grid(row=j + 1, column=i + 6)
        i += 1
    dataset = total_data_results(variables[0], variables[1])
    for info in range(len(dataset)):
        e = tk.Label(tot_frame, width=15, text=dataset[info], relief="solid", borderwidth=1)
        e.grid(row=0, column=info)
    try:
        # Calculate and display the percentage
        e = tk.Label(tot_frame, width=15, text=f"{round(float(dataset[2]) * 100 / float(dataset[3]), 0)}%",
                     relief="solid", borderwidth=1)
    except ZeroDivisionError:
        e = tk.Label(tot_frame, width=15, text="0%", relief="solid", borderwidth=1)
    e.grid(row=0, column=4)
    close_dbconnection()


# Main loop
window.mainloop()