from tkinter import messagebox, ttk

import customtkinter as ctk

from Forms.Admin import Functions

def create_add_course_tab(self):
    def prevent_input(event):
        return "break"

    frame = ctk.CTkFrame(self)
    LabelYo = ctk.CTkLabel(frame, text="Добавление нового курса", font=("Times New Roman", 20))
    LabelYo.place(relx=0.05, rely=0.002)
    labelTitle = ctk.CTkLabel(frame, text="Название:")
    labelDescription = ctk.CTkLabel(frame, text="Описание:")
    teacherLabel = ctk.CTkLabel(frame, text="Преподаватель:")
    labelTitle.place(relx=0.01, rely=0.08)
    labelDescription.place(relx=0.01, rely=0.13)
    teacherLabel.place(relx=0.24, rely=0.08)
    teacherBox = ctk.CTkComboBox(frame, width=250)
    teacherBox.place(relx=0.24, rely=0.128)
    teacherBox.bind("<Key>", prevent_input("<Key>"))

    entryName = ctk.CTkEntry(frame)
    entryDescript = ctk.CTkEntry(frame)
    entryName.place(relx=0.09, rely=0.08)
    entryDescript.place(relx=0.09, rely=0.13)
    addButton = ctk.CTkButton(frame, text="Добавить курс", command=lambda: add())
    addButton.place(relx=0.2, rely=0.19)

    LabelDel = ctk.CTkLabel(frame, text="Удаление курса", font=("Times New Roman", 20))
    LabelDel.place(relx=0.09, rely=0.3)
    LabelDelName = ctk.CTkLabel(frame, text="ID курса:")
    LabelDelName.place(relx=0.055, rely=0.35)
    entryDelName = ctk.CTkEntry(frame)
    entryDelName.place(relx=0.13, rely=0.35)
    delButton = ctk.CTkButton(frame, text="Удалить курс", command=lambda: del_courses())
    delButton.place(relx=0.1, rely=0.42)

    scrollLabel = ctk.CTkLabel(frame, text="Список курсов", font=("Times New Roman", 20))
    scrollLabel.place(relx=0.75, rely=0.009)
    scroll = ctk.CTkScrollableFrame(frame, height=600, width=500)
    scroll.place(relx=0.55, rely=0.06)
    updateButton = ctk.CTkButton(frame, text="Обновить список", command=lambda: get_course())
    updateButton.place(relx=0.75, rely=0.9465)




    def add():
        title = entryName.get()
        description = entryDescript.get()
        teacher = teacherBox.get()
        if title != "" and teacher != "":
            if description == "":
                description = "Без описания"
            else:
                description = "ЧЁ"
            Functions.update_tab(self)
        else:
            messagebox.showerror("Ошибка", "Поля названия и преподавателя должны быть заполнены")
        get_course()


    def del_courses():
        name = int(entryDelName.get())
        if name != "":
            get_course()
            return
        else:
            messagebox.showerror("Ошибка", "Поле ID не должно быть пустым")


    def get_course():
        for widget in scroll.winfo_children():
            widget.destroy()


        columns = ('ID', 'Название', 'Описание', 'Преподаватель')
        tree = ttk.Treeview(scroll, columns=columns, show='headings',height=30)

        for col in columns:
            tree.heading(col, text=col, command=lambda c=col: Functions.sort_treeview(tree, c, False))
            tree.column(col, anchor='center')

        tree.column('ID', width=5)
        tree.column('Название', width=120)
        tree.column('Описание', width=100)
        tree.column('Преподаватель', width=140)

        tree.pack(pady=2, fill='both', expand=True)

    get_course()

    return frame