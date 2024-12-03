from tkinter import *
from tkinter import messagebox
import sqlite3
import os

# Database Connection
def connection():
    conn = sqlite3.connect("rms.db")
    return conn

# Switch to Register Screen
def open_register_screen():
    login_frame.pack_forget()
    register_frame.pack()

# Switch to Login Screen
def open_login_screen():
    register_frame.pack_forget()
    forgot_password_frame.pack_forget()
    login_frame.pack()

# Switch to Forgot Password Screen
def open_forgot_password_screen():
    login_frame.pack_forget()
    forgot_password_frame.pack()

# Handle Registration
def handle_register():
    username = reg_username_entry.get()
    password = reg_password_entry.get()
    email = reg_email_entry.get()

    if not username or not password or not email:
        messagebox.showwarning("Registration Error", "All fields are required")
        return

    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT, email TEXT UNIQUE)")
        sql = "INSERT INTO users (username, password, email) VALUES (?, ?, ?)"
        cursor.execute(sql, (username, password, email))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Registration successful!")
        open_login_screen()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username or email already exists")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Handle Login
def handle_login(event=None):
    username = login_username_entry.get()
    password = login_password_entry.get()

    if not username or not password:
        messagebox.showwarning("Login Error", "Please enter both username and password")
        return

    try:
        conn = connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM users WHERE username=? AND password=?"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            login_window.destroy()
            os.system('python dashboard.py')  # Open the dashboard
        else:
            messagebox.showerror("Login Error", "Invalid username or password")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Forgot Password Functionality
def handle_forgot_password():
    email = forgot_email_entry.get()

    if not email:
        messagebox.showwarning("Forgot Password", "Please enter your email address")
        return

    try:
        conn = connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM users WHERE email=?"
        cursor.execute(sql, (email,))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Success", "Please contact the administrator for password assistance.")
            open_login_screen()
        else:
            messagebox.showerror("Error", "No account associated with this email")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# UI Setup
login_window = Tk()
login_window.title("Login System")
login_window.geometry("700x500+410+100")
login_window.configure(bg="#1e293b")

# Login Frame
login_frame = Frame(login_window, padx=130, pady=80, bg="#ffffff", bd=5, relief=RIDGE)
login_frame.pack()

Label(login_frame, text="Login", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#1e293b").pack(pady=10)

Label(login_frame, text="Username:", font=("Arial", 10), bg="#ffffff").pack(anchor=W)
login_username_entry = Entry(login_frame, width=30, font=("Arial", 10))
login_username_entry.pack(pady=5)

Label(login_frame, text="Password:", font=("Arial", 10), bg="#ffffff").pack(anchor=W)
login_password_entry = Entry(login_frame, show="*", width=30, font=("Arial", 10))
login_password_entry.pack(pady=5)

Button(login_frame, text="Login", command=handle_login, bg="#4caf50", fg="white", width=15, font=("Arial", 10, "bold")).pack(pady=10)
Button(login_frame, text="Register", command=open_register_screen, bg="#0073e6", fg="white", width=15, font=("Arial", 10, "bold")).pack(pady=5)
Button(login_frame, text="Forgot Password", command=open_forgot_password_screen, bg="#f44336", fg="white", width=15, font=("Arial", 10, "bold")).pack(pady=5)

# Register Frame
register_frame = Frame(login_window, padx=20, pady=20, bg="#ffffff", bd=5, relief=RIDGE)

Label(register_frame, text="Register", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#1e293b").pack(pady=10)

Label(register_frame, text="Username:", font=("Arial", 10), bg="#ffffff").pack(anchor=W)
reg_username_entry = Entry(register_frame, width=30, font=("Arial", 10))
reg_username_entry.pack(pady=5)

Label(register_frame, text="Password:", font=("Arial", 10), bg="#ffffff").pack(anchor=W)
reg_password_entry = Entry(register_frame, show="*", width=30, font=("Arial", 10))
reg_password_entry.pack(pady=5)

Label(register_frame, text="Email:", font=("Arial", 10), bg="#ffffff").pack(anchor=W)
reg_email_entry = Entry(register_frame, width=30, font=("Arial", 10))
reg_email_entry.pack(pady=5)

Button(register_frame, text="Register", command=handle_register, bg="#4caf50", fg="white", width=15, font=("Arial", 10, "bold")).pack(pady=10)
Button(register_frame, text="Back to Login", command=open_login_screen, bg="#f44336", fg="white", width=15, font=("Arial", 10, "bold")).pack(pady=5)

# Forgot Password Frame
forgot_password_frame = Frame(login_window, padx=20, pady=20, bg="#ffffff", bd=5, relief=RIDGE)

Label(forgot_password_frame, text="Forgot Password", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#1e293b").pack(pady=10)

Label(forgot_password_frame, text="Enter your email:", font=("Arial", 10), bg="#ffffff").pack(anchor=W)
forgot_email_entry = Entry(forgot_password_frame, width=30, font=("Arial", 10))
forgot_email_entry.pack(pady=5)

Button(forgot_password_frame, text="Send Email", command=handle_forgot_password, bg="#0073e6", fg="white", width=15, font=("Arial", 10, "bold")).pack(pady=10)
Button(forgot_password_frame, text="Back to Login", command=open_login_screen, bg="#f44336", fg="white", width=15, font=("Arial", 10, "bold")).pack(pady=5)

# Start with Login Frame
login_frame.pack()

login_window.mainloop()
