from tkinter import messagebox

import customtkinter as ctk

from Forms.Admin.AdminForm import AdminWindow
from Forms.Student.StudentForm import StudentWindow
from Forms.Teacher.TeacherForm import TeachWindow


class AuthWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Авторизация")
        self.resizable(False,False)
        self.geometry("250x250")

        self.loginLabel = ctk.CTkLabel(self, text="Логин:")
        self.loginLabel.pack(pady=5)

        self.loginEntry = ctk.CTkEntry(self)
        self.loginEntry.pack(pady=5)

        self.passwordLabel = ctk.CTkLabel(self, text="Пароль:")
        self.passwordLabel.pack(pady=5)

        self.passwordEntry = ctk.CTkEntry(self, show="*")
        self.passwordEntry.pack(pady=5)

        self.buttonAuth = ctk.CTkButton(self, text="Авторизация", command=lambda: perms())
        self.buttonAuth.pack(pady=20)

        def perms():
            login = self.loginEntry.get()
            pwd = self.passwordEntry.get()

            if login == "1":
                try:
                    self.destroy()
                    adminPanel = AdminWindow()
                    adminPanel.mainloop()
                    return
                except Exception as e:
                    return exit(1)

            if login == "2":
                try:
                    login = self.loginEntry.get()
                    self.destroy()
                    teacherPanel = TeachWindow(login)
                    teacherPanel.mainloop()
                    return
                except Exception as e:
                    return exit(1)

            if login == "3":
                try:
                    login = self.loginEntry.get()
                    self.destroy()
                    studentPanel = StudentWindow(login)
                    studentPanel.mainloop()
                    return
                except Exception as e:
                    return exit(1)