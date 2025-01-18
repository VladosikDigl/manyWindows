from tkinter import messagebox, ttk

import customtkinter as ctk

from Forms.Admin import Functions


def create_add_teacher_tab(self):
    frame = ctk.CTkFrame(self)

    LabelAdd = ctk.CTkLabel(frame, text="Добавление преподавателя", font=("Times New Roman", 20))
    LabelAdd.place(relx=0.05, rely=0.001)

    AddNameLabel = ctk.CTkLabel(frame, text="ФИО:")
    AddPhoneLabel = ctk.CTkLabel(frame, text="Телефон:")
    addLoginLabel = ctk.CTkLabel(frame, text="Логин:")
    addMailLabel = ctk.CTkLabel(frame, text="Почта:")
    AddNameEntry = ctk.CTkEntry(frame)
    AddPhoneEntry = ctk.CTkEntry(frame)
    AddLoginEntry = ctk.CTkEntry(frame)
    AddMailEntry = ctk.CTkEntry(frame)
    AddButton = ctk.CTkButton(frame, text="Добавить преподавателя", command=lambda: add_teacher())
    AddNameLabel.place(relx=0.038, rely=0.08)
    AddPhoneLabel.place(relx=0.01, rely=0.13)
    AddNameEntry.place(relx=0.08, rely=0.08)
    AddPhoneEntry.place(relx=0.08, rely=0.13)
    AddLoginEntry.place(relx=0.08, rely=0.18)
    AddMailEntry.place(relx=0.08, rely=0.23)
    addLoginLabel.place(relx=0.01, rely=0.18)
    addMailLabel.place(relx=0.01, rely=0.23)
    AddButton.place(relx=0.06, rely=0.28)

    LabelDelete = ctk.CTkLabel(frame, text="Удалить преподавателя", font=("Times New Roman", 20))
    LabelDeleteID = ctk.CTkLabel(frame, text="ID:")
    DeleteEntry = ctk.CTkEntry(frame)
    DeleteButton = ctk.CTkButton(frame, text="Удалить", command=lambda: del_teacher())
    LabelDelete.place(relx=0.05, rely=0.40)
    LabelDeleteID.place(relx=0.05, rely=0.45)
    DeleteEntry.place(relx=0.08, rely=0.45)
    DeleteButton.place(relx=0.08, rely=0.51)

    LabelUpdate = ctk.CTkLabel(frame, text="Обновить данные о преподавателе", font=("Times New Roman", 20))
    LabelUpdateID = ctk.CTkLabel(frame, text="ID:")
    LabelUpdateName = ctk.CTkLabel(frame, text="ФИО:")
    LabelUpdatePhone = ctk.CTkLabel(frame, text="Телефон:")
    UpdateID = ctk.CTkEntry(frame)
    UpdateName = ctk.CTkEntry(frame)
    UpdatePhone = ctk.CTkEntry(frame)
    UpdateButton = ctk.CTkButton(frame, text="Обновить данные", command=lambda: update_teacher())
    LabelUpdate.place(relx=0.03, rely=0.61)
    LabelUpdateID.place(relx=0.055, rely=0.67)
    LabelUpdateName.place(relx=0.04, rely=0.72)
    LabelUpdatePhone.place(relx=0.01, rely=0.77)
    UpdateID.place(relx=0.08, rely=0.67)
    UpdateName.place(relx=0.08, rely=0.72)
    UpdatePhone.place(relx=0.08, rely=0.77)
    UpdateButton.place(relx=0.08, rely=0.83)

    LabelList = ctk.CTkLabel(frame, text="Список преподавателей", font=("Times New Roman", 20))
    LabelList.place(relx=0.625, rely=0.001)
    scroll = ctk.CTkScrollableFrame(frame, height=600, width=425)
    scroll.place(relx=0.5, rely=0.065)
    ListButton = ctk.CTkButton(frame, text="Обновить список", command=lambda: list_teacher())
    ListButton.place(relx=0.655, rely=0.95)


    def add_teacher():
        name = AddNameEntry.get()
        phone = AddPhoneEntry.get()
        login = str(AddLoginEntry.get())
        mail = str(AddMailEntry.get())


        AddNameEntry.delete(0, ctk.END)
        AddPhoneEntry.delete(0, ctk.END)
        AddLoginEntry.delete(0, ctk.END)
        AddMailEntry.delete(0, ctk.END)


    def del_teacher():
        id = int(DeleteEntry.get())


    def update_teacher():
        id = int(UpdateID.get())
        name = UpdateName.get()
        phone = UpdatePhone.get()



    def list_teacher():
        for widget in scroll.winfo_children():
            widget.destroy()

        columns = ('ID', 'ФИО', 'Телефон', 'Логин')
        tree = ttk.Treeview(scroll, columns=columns, show='headings',height=30)

        for col in columns:
            tree.heading(col, text=col, command=lambda c=col: Functions.sort_treeview(tree, c, False))
            tree.column(col, anchor='center')

        tree.column('ID', width=30)
        tree.column('ФИО', width=200)
        tree.column('Телефон', width=90)
        tree.column('Логин', width=120)


        tree.pack(pady=2, fill='both', expand=True)

    list_teacher()
    return frame
