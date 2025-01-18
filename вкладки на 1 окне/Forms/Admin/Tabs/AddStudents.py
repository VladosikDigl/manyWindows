from tkinter import messagebox, ttk

import customtkinter as ctk

from Forms.Admin import Functions



def create_add_student_tab(self):
    frame = ctk.CTkFrame(self)

    addLabel = ctk.CTkLabel(frame, text="Добавление нового студента", font=("Times New Roman", 20))
    addLabel.place(relx=0.05, rely=0.001)

    studNameLabel = ctk.CTkLabel(frame, text="ФИО:")
    studAgeLabel = ctk.CTkLabel(frame, text="Возраст:")
    studPhoneLabel = ctk.CTkLabel(frame, text="Телефон:")
    studLoginLabel = ctk.CTkLabel(frame, text="Логин:")
    studMailLabel = ctk.CTkLabel(frame, text="Почта:")
    studNameLabel.place(relx=0.07, rely=0.05)
    studAgeLabel.place(relx=0.05, rely=0.1)
    studPhoneLabel.place(relx=0.047, rely=0.15)
    studLoginLabel.place(relx=0.065, rely=0.2)
    studMailLabel.place(relx=0.065, rely=0.25)
    nameEntry = ctk.CTkEntry(frame)
    ageEntry = ctk.CTkEntry(frame)
    phoneEntry = ctk.CTkEntry(frame)
    loginEntry = ctk.CTkEntry(frame)
    mailEntry = ctk.CTkEntry(frame)
    nameEntry.place(relx=0.12, rely=0.05)
    ageEntry.place(relx=0.12, rely=0.1)
    phoneEntry.place(relx=0.12, rely=0.15)
    loginEntry.place(relx=0.12, rely=0.2)
    mailEntry.place(relx=0.12, rely=0.25)
    addButton = ctk.CTkButton(frame, text="Добавить студента", command=lambda: add_student())
    addButton.place(relx=0.12, rely=0.3)

    delLabel = ctk.CTkLabel(frame, text="Удалить студента", font=("Times New Roman", 20))
    delLabel.place(relx=0.11, rely=0.35)
    studId = ctk.CTkLabel(frame, text="ID студента:")
    studId.place(relx=0.03, rely=0.42)
    studIdEntry = ctk.CTkEntry(frame)
    studIdEntry.place(relx=0.12, rely=0.42)
    delButton = ctk.CTkButton(frame, text="Удалить студента", command=lambda: del_student())
    delButton.place(relx=0.12, rely=0.48)

    updateLabel = ctk.CTkLabel(frame, text="Обновить данные о студенте", font=("Times New Roman", 20))
    updateLabel.place(relx=0.05, rely=0.55)
    updateId = ctk.CTkLabel(frame, text="ID студента:")
    newNameLab = ctk.CTkLabel(frame, text="ФИО:")
    newAgeLab = ctk.CTkLabel(frame, text="Возраст:")
    newPhoneLab = ctk.CTkLabel(frame, text="Телефон:")
    updateId.place(relx=0.03, rely=0.62)
    newNameLab.place(relx=0.07, rely=0.67)
    newAgeLab.place(relx=0.05, rely=0.72)
    newPhoneLab.place(relx=0.047, rely=0.77)
    updateIdEntry = ctk.CTkEntry(frame)
    updateName = ctk.CTkEntry(frame)
    updateAge = ctk.CTkEntry(frame)
    updatePhone = ctk.CTkEntry(frame)
    updateIdEntry.place(relx=0.12, rely=0.62)
    updateName.place(relx=0.12, rely=0.67)
    updateAge.place(relx=0.12, rely=0.72)
    updatePhone.place(relx=0.12, rely=0.77)
    updateButt = ctk.CTkButton(frame, text="Обновить данные", command=lambda: update_student())
    updateButt.place(relx=0.12, rely=0.82)

    listLabel = ctk.CTkLabel(frame, text="Список студентов", font=("Times New Roman", 20))
    listLabel.place(relx=0.65, rely=0.001)
    scroll = ctk.CTkScrollableFrame(frame, height=600, width=500)
    scroll.place(relx=0.45, rely=0.05)
    reloadButton = ctk.CTkButton(frame, text="Обновить список", command=lambda: get_students())
    reloadButton.place(relx=0.65, rely=0.94)

    def add_student():
        name = str(nameEntry.get())
        age = int(ageEntry.get())
        phone = phoneEntry.get()
        login = str(loginEntry.get())
        mail = str(mailEntry.get())

        nameEntry.delete(0, ctk.END)
        ageEntry.delete(0, ctk.END)
        phoneEntry.delete(0, ctk.END)
        loginEntry.delete(0, ctk.END)
        mailEntry.delete(0, ctk.END)
        get_students()

    def get_students():
        for widget in scroll.winfo_children():
            widget.destroy()

        columns = ('ID', 'ФИО', 'Возраст', 'Телефон', 'Логин')
        tree = ttk.Treeview(scroll, columns=columns, show='headings',height=30)

        for col in columns:
            tree.heading(col, text=col, command=lambda c=col: Functions.sort_treeview(tree, c, False))
            tree.column(col, anchor='center')

        tree.column('ID', width=30)
        tree.column('ФИО', width=200)
        tree.column('Возраст', width=50)
        tree.column('Телефон', width=90)
        tree.column('Логин', width=100)

    def del_student():
        InputId = int(studIdEntry.get())
        if InputId != "":
            get_students()
        else:
            messagebox.showerror("Ошибка", "Поле должно быть числом и не должно быть пустым")
            return

    def update_student():
        InputId = int(updateIdEntry.get())
        name = updateName.get()
        age = updateAge.get()
        phone = updatePhone.get()
        if InputId != "":
            get_students()

    get_students()

    return frame