##############################
# Sign-in window
# Zachary Smith
# PROJET DBPY
# Dernière modif 16.01.2024
###############################

import tkinter as tk
import database as DB

# Define window dimensions
login_geometry = "450x120"
register_geometry = "450x170"


class Tk_Label:
    def __init__(self, origin_frame, text_info, gRow, gCol, gPadx=10):
        # Utility class for creating labeled widgets helped by brad
        label = tk.Label(origin_frame, text=text_info, font=8)
        label.grid(row=gRow, column=gCol, padx=gPadx)


def open_window():
    # Function to open the main window
    DB.open_dbconnection()
    window = tk.Tk()
    window.title("Login")
    window.geometry(login_geometry)
    window.resizable(0, 0)
    title_frame, main_frame, last_frame = add_frames(window)
    add_login_widgets([title_frame, main_frame, last_frame], window)
    window.configure(bg="light blue")
    window.mainloop()


def add_frames(window):
    # Function to create and place frames in the window
    title_frame = tk.Frame(window)
    title_frame.grid(row=0, column=0, columnspan=3)
    title_frame.configure(bg="light blue")

    main_frame = tk.Frame(window)
    main_frame.grid(row=1, column=0, columnspan=3)
    main_frame.configure(bg="light blue")

    last_frame = tk.Frame(window)
    last_frame.grid(row=2, column=0, columnspan=3)
    last_frame.configure(bg="light blue")

    return title_frame, main_frame, last_frame


def change_window_utility(frames, window):
    # Function to change between Login and Register frames
    for window_frame in frames:
        for widget in window_frame.winfo_children():
            widget.destroy()

    title_frame, main_frame, last_frame = frames

    if window.title() == "Login":
        window.title("Register")
        add_register_widgets(frames, window)
        window.geometry(register_geometry)
    else:
        window.title("Login")
        add_login_widgets(frames, window)
        window.geometry(login_geometry)


def add_login_widgets(frames, window):
    # Function to add Login widgets to the frames
    change_button = tk.Button(frames[0], text="Register", command=lambda: change_window_utility(frames, window))
    change_button.grid(row=0, column=0)
    change_button.configure(borderwidth="3px")

    Tk_Label(frames[1], "Username:", 0, 0)
    user_entry = tk.Entry(frames[1], width=40)
    user_entry.grid(row=0, column=1, padx=30)
    user_entry.configure(bg="white", highlightthickness="2px", highlightcolor="red")

    Tk_Label(frames[1], "Password:", 1, 0)
    password_entry = tk.Entry(frames[1], show="*", width=40)
    password_entry.grid(row=1, column=1, padx=30)
    password_entry.configure(bg="white", highlightthickness="2px", highlightcolor="red")

    login_button = tk.Button(frames[2], text="Login", command=lambda: login([user_entry.get(), password_entry.get()], window))
    login_button.grid(row=0, column=0)
    login_button.configure(borderwidth="3px")


def add_register_widgets(frames, window):
    # Function to add Register widgets to the frames
    change_button = tk.Button(frames[0], text="Login", command=lambda: change_window_utility(frames, window))
    change_button.grid(row=0, column=0)

    Tk_Label(frames[1], "Username:", 0, 0)
    email_entry = tk.Entry(frames[1], width=35)
    email_entry.grid(row=0, column=1, padx=30)
    email_entry.configure(bg="white", highlightthickness="2px", highlightcolor="red")

    Tk_Label(frames[1], "Prénom et Nom", 1, 0)
    user_entry = tk.Entry(frames[1], width=35)
    user_entry.grid(row=1, column=1, padx=30)
    user_entry.configure(bg="white", highlightthickness="2px", highlightcolor="red")

    Tk_Label(frames[1], "Password:", 2, 0)
    password_entry = tk.Entry(frames[1], show="*", width=35)
    password_entry.grid(row=2, column=1, padx=30)
    password_entry.configure(bg="white", highlightthickness="2px", highlightcolor="red")

    Tk_Label(frames[1], "Confirm Password:", 3, 0)
    confirm_password_entry = tk.Entry(frames[1], show="*", width=35)
    confirm_password_entry.grid(row=3, column=1, padx=30)
    confirm_password_entry.configure(bg="white", highlightthickness="2px", highlightcolor="red")

    register_button = tk.Button(frames[2], text="Register", command=lambda: register([email_entry.get(), user_entry.get(),
                                                                                     password_entry.get(), 0],
                                                                                    [password_entry.get(), confirm_password_entry.get()], window))
    register_button.grid(row=0, column=0)


def login(data, window):
    # Function to handle login functionality
    import menu
    menu.check_information(data, window)


def register(data, passwords, window):
    # Function to handle registration functionality
    if len(passwords[0]) > 3 and any(not passwords[0].isalnum() for c in passwords[0]):
        if DB.get_exercice_name(data[1]) is None and passwords[0] == passwords[1]:
            DB.insert_new_user(data)
    else:
        DB.error_box("Invalid password.", "Wrong Credentials", window)


if __name__ == "__main__":
    open_window()