from tkinter import messagebox, END

import customtkinter as ctk

import Forms.AuthForm
import HandlerMain
from HandlerMain import hash_pass

loggedUser = ""
code = ""

class StudentWindow(ctk.CTk):
    def __init__(self, user):
        super().__init__()
        global loggedUser
        loggedUser = user
        Handler.DB
        self.title("Панель студента")
        self.resizable(False, False)
        self.geometry("600x550")
        self.protocol("WM_DELETE_WINDOW", self.destroy) #При закрытии окна вызывает удаление окна на всякий случай
        self.studentName = ctk.CTkLabel(self, text=f"Студент: {loggedUser}")
        self.studentName.place(relx=0.03, rely=0.01)
        self.markLabel = ctk.CTkLabel(self,text="Мои оценки", font=("Times New Roman", 20))
        self.markLabel.place(relx=0.4,rely=0.08)

        self.markScroll = ctk.CTkScrollableFrame(self,width=450,height=375)
        self.markScroll.place(relx=0.1,rely=0.15)
        self.fillScroll()

        self.buttonExit = ctk.CTkButton(self, text="Выйти", command=lambda: self.Exit())
        self.buttonExit.place(x=450, y=510)

        self.changeOpen = ctk.CTkButton(self, text="Изменить пароль", command=lambda: self.open_change())
        self.changeOpen.place(x=430, y=10)

    def open_change(self):
        self.withdraw()
        change = ChangePassword()
        change.protocol("WM_DELETE_WINDOW", lambda:(self.deiconify(), change.destroy()))

    def Exit(self):
        self.destroy()
        auth = Forms.AuthForm.AuthWindow()
        auth.mainloop()

    def fillScroll(self):
        for widget in self.markScroll.winfo_children():
            widget.destroy()


class ChangePassword(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Смена пароля")
        self.resizable(False, False)
        self.geometry("300x300+750+400")
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self.titleLabel = ctk.CTkLabel(self, text="Смена пароля", font=("Times New Roman", 20))
        self.PasswordNewEntry = ctk.CTkEntry(self)
        self.PasswordOldEntry = ctk.CTkEntry(self)
        self.newPassLabel = ctk.CTkLabel(self,text="Новый пароль:")
        self.oldPassLabel = ctk.CTkLabel(self,text="Старый пароль:")
        self.ButtonChange = ctk.CTkButton(self,text="Сменить пароль", command=lambda: self.change_pass())

        self.codeLabel = ctk.CTkLabel(self, text="Код:")
        self.codeEntry = ctk.CTkEntry(self)
        self.buttonWithCode = ctk.CTkButton(self,text="Сменить пароль")

        self.titleLabel.place(x=60, y=10)
        self.newPassLabel.place(x=20,y=50)
        self.oldPassLabel.place(x=20,y=100)
        self.PasswordNewEntry.place(x=120,y=50)
        self.PasswordOldEntry.place(x=120,y=100)
        self.ButtonChange.place(x=60,y=150)

    def change_pass(self):
        global loggedUser
        old_password = self.PasswordOldEntry.get()
        new_password = self.PasswordNewEntry.get()

    def check_code(self, new_password):
        entry_code = int(self.codeEntry.get())
        global code

        if entry_code != "" and entry_code == code:
            messagebox.showinfo("Успешно", "Ваш пароль был изменён")
            code = ""

            self.buttonWithCode.place_forget()
            self.codeEntry.place_forget()
            self.codeLabel.place_forget()
            self.ButtonChange.place(x=60, y=150)
        else:
            messagebox.showerror("Ошибка", "Неверный код")