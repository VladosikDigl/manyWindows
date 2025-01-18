from tkinter import messagebox, END

import customtkinter as ctk

code = ""

def create_add_student_tab(self, user):
    frame = ctk.CTkFrame(self)

    titleLabel = ctk.CTkLabel(frame, text="Смена пароля", font=("Times New Roman", 20))
    PasswordNewEntry = ctk.CTkEntry(frame)
    PasswordOldEntry = ctk.CTkEntry(frame)
    newPassLabel = ctk.CTkLabel(frame, text="Новый пароль:")
    oldPassLabel = ctk.CTkLabel(frame, text="Старый пароль:")
    ButtonChange = ctk.CTkButton(frame, text="Сменить пароль", command=lambda: change_pass(user))

    codeLabel = ctk.CTkLabel(frame, text="Код:")
    codeEntry = ctk.CTkEntry(frame)
    buttonWithCode = ctk.CTkButton(frame, text="Сменить пароль", command=lambda: check_code(user,PasswordNewEntry.get()))

    titleLabel.place(relx=0.45, rely=0.01)
    newPassLabel.place(relx=0.4, rely=0.07)
    oldPassLabel.place(relx=0.4, rely=0.13)
    PasswordNewEntry.place(relx=0.55, rely=0.07)
    PasswordOldEntry.place(relx=0.55, rely=0.13)
    ButtonChange.place(relx=0.45, rely=0.22)

    def change_pass(user):
        old_password = PasswordOldEntry.get()
        new_password = PasswordNewEntry.get()


    def check_code(user,new_password):
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



    return frame