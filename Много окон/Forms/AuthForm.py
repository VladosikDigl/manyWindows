import customtkinter as ctk
from tkinter import messagebox

import HandlerMain
from Forms import TeacherForm, StudentForm, AdminWindow


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

        #Открывает окно в зависимости от прав пользователя
        def perms():
            login = self.loginEntry.get()
            if login == "1":
                try:
                    open_admin(self)
                    return
                except Exception as e:
                    return exit("Не удалось открыть окно")

                return
            if login == "2":
                try:
                    open_teach(self)
                    return
                except Exception as e:
                    return exit("Не удалось открыть окно")
            if login == "3":
                try:
                    open_student(self)
                    return
                except Exception as e:
                    return exit("Не удалось открыть окно")
        #Открытие и создание окна Админа
        def open_admin(self):
            login = self.loginEntry.get()
            password = self.passwordEntry.get()
            isLogged = HandlerMain.auth(login, password.encode())
            if isLogged == None:
                return
            global authedUser
            authedUser = login
            #Удаляем текущее окно и делаем главным окно админа
            self.destroy()
            adminPanel = AdminWindow.AdminWindow()
            adminPanel.mainloop()

        # Открытие и создание окна Преподавателя
        def open_teach(self):
            login = self.loginEntry.get()
            password = self.passwordEntry.get()
            isLogged = HandlerMain.auth(login,password.encode())
            if isLogged == None:
                return
            global authedUser
            authedUser = login
            self.destroy()
            teachPanel = TeacherForm.TeachWindow(authedUser)
            teachPanel.mainloop()

        #Открытие и создание окна студента
        def open_student(self):
            login = self.loginEntry.get()
            password = self.passwordEntry.get()
            isLogged = HandlerMain.auth(login, password.encode())
            if isLogged == None:
                return
            global authedUser
            authedUser = login
            self.destroy()
            studentPanel = StudentForm.StudentWindow(authedUser)
            studentPanel.mainloop()