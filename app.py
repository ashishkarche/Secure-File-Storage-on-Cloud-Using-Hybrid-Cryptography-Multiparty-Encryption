import os
import tkinter as tk
from tkinter import filedialog
from threading import Thread
from IVsKeys import *
from Threads import *
from dataProcessing import *
from user import *

class FileEncryptorApp:
    def __init__(self, master):


        self.master = master
        self.master.title("File Encryptor")

        self.file_path = None
        self.iv1 = None
        self.iv2 = None
        self.key1 = None
        self.key2 = None

        # File Upload Button
        self.upload_button = tk.Button(master, text="Upload File", command=self.upload_file)
        # self.upload_button = tk.Button(master, text="Upload File", command=self.upload_file, state=tk.DISABLED)
        self.upload_button.pack(pady=20)

        # Display Selected File Label
        self.file_label = tk.Label(master, text="")
        self.file_label.pack()

        # # Signup Button
        # self.signup_button = tk.Button(master, text="Signup", command=self.signup)
        # self.signup_button.pack(pady=10)

        # # Login Button
        # self.login_button = tk.Button(master, text="Login", command=self.login)
        # self.login_button.pack(pady=10)

    def upload_file(self):
            self.file_path = filedialog.askopenfilename()
            if self.file_path:
            # Update the label with the selected file name
                self.file_label.config(text=f"Selected File: {os.path.basename(self.file_path)}")

            # Disable file upload button after file is selected
                self.upload_button.config(state=tk.DISABLED)

            # Read the file content
                with open(self.file_path, 'r') as file:
                    content = file.read()

            # Write the file content to Original.txt
                with open('Original.txt', 'w') as original_file:
                    original_file.write(content)

            # Create a new window for encryption
                encrypt_window = tk.Toplevel(self.master)
                EncryptWindow(encrypt_window, content, self)

    # def signup(self):
    #         signup_window = tk.Toplevel(self.master)
    #         SignupWindow(signup_window, self)

    # def login(self):
    #         login_window = tk.Toplevel(self.master)
    #         LoginWindow(login_window, self)

# class SignupWindow:
#     def __init__(self, master, main_app):
#         self.master = master
#         self.master.title("Signup")

#         self.main_app = main_app

#         # Username Entry
#         self.username_label = tk.Label(master, text="Username:")
#         self.username_label.pack()
#         self.username_entry = tk.Entry(master)
#         self.username_entry.pack()

#         # Password Entry
#         self.password_label = tk.Label(master, text="Password:")
#         self.password_label.pack()
#         self.password_entry = tk.Entry(master, show="*")
#         self.password_entry.pack()

#         # Signup Button
#         self.signup_button = tk.Button(master, text="Signup", command=self.signup)
#         self.signup_button.pack()

#     def signup(self):
#             username = self.username_entry.get()
#             password = self.password_entry.get()

#             # Save user information to Google Cloud Storage
#             save_user(username, password)

#             # Close the signup window
#             self.master.destroy()

# class LoginWindow:
#     def __init__(self, master, main_app):
#         self.master = master
#         self.master.title("Login")

#         self.main_app = main_app

#         # Username Entry
#         self.username_label = tk.Label(master, text="Username:")
#         self.username_label.pack()
#         self.username_entry = tk.Entry(master)
#         self.username_entry.pack()

#         # Password Entry
#         self.password_label = tk.Label(master, text="Password:")
#         self.password_label.pack()
#         self.password_entry = tk.Entry(master, show="*")
#         self.password_entry.pack()

#         # Login Button
#         self.login_button = tk.Button(master, text="Login", command=self.login)
#         self.login_button.pack()

#     def login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()

#         # Authenticate user
#         if authenticate_user(username, password):
#             # Enable the file upload button in the main app
#             self.main_app.upload_button.config(state=tk.NORMAL)
#             # Open the main app window for file upload and encryption
#             self.main_app.master.deiconify()
#             # Close the login window
#             self.master.destroy()
#         else:
#             # Display an error message or handle unsuccessful login
#             print("Invalid username or password")

class EncryptWindow:
    def __init__(self, master, file_content, main_app):
        self.master = master
        self.master.title("Encryption Progress")

        self.file_content = file_content
        self.main_app = main_app

        
        # Encryption Log Text
        self.log_text = tk.Text(master, height=20, width=50)
        self.log_text.pack(pady=20)

        # Encrypt Button
        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt_file)
        self.encrypt_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(master, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=10)

    def encrypt_file(self):
        # Display file reading information in the log
        log_message = "Reading file: Original.txt"
        self.log_text.insert(tk.END, log_message + "\n\n")

        # Display file dividing information in the log
        log_message = "Dividing file into segments"
        self.log_text.insert(tk.END, log_message + "\n\n")

        # Divide the file into segments
        Segment()

        gatherInfo()

        
        # Display encryption information in the log
        log_message = "Generating IVs and Keys"
        self.log_text.insert(tk.END, log_message + "\n\n")

        self.iv1, self.iv2 = generateIV()
        self.key1, self.key2 = generateKey()

        log_message = f"IV1: {self.iv1}\nIV2: {self.iv2}\nKey1: {self.key1}\nKey2: {self.key2}"
        self.log_text.insert(tk.END, log_message + "\n\n")

        # Save IVs and Keys to files
        save_IV_and_key(self.iv1, self.iv2, self.key1, self.key2)

        # Display encryption progress information in the log
        log_message = "Encrypting file segments"
        self.log_text.insert(tk.END, log_message + "\n\n")

        # Perform encryption using threads
        encryption_thread = Thread(target=self.perform_encryption)
        encryption_thread.start()

    def perform_encryption(self):
        # Call the encryption function
        HybridCrypt()

        # Enable the file upload button in the main app
        self.main_app.upload_button.config(state=tk.NORMAL)

        # Display completion message in the log
        self.log_text.insert(tk.END, "Encryption completed.\n")

    def exit_app(self):
        # Close the main window
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileEncryptorApp(root)
    root.mainloop()
