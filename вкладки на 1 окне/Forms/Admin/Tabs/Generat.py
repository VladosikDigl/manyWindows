from tkinter import ttk

import customtkinter as ctk

from Forms.Admin import Functions

gradeSort = False

def create_add_user_tab(self):
    frame = ctk.CTkFrame(self)

    global gradeSort
    gradeSort = False
    titleLab = ctk.CTkLabel(frame, text="Список всех оценок", font=("Times New Roman", 20))
    titleLab.place(x=500, y=5)
    scroll = ctk.CTkScrollableFrame(frame, height=600, width=650)
    scroll.place(x=225, y=50)

    def getList():
        for widget in scroll.winfo_children():
            widget.destroy()

        columns = ('ФИО', 'Предмет', 'Оценка')
        tree = ttk.Treeview(scroll, columns=columns, show='headings', height=30)

        for col in columns:
            tree.heading(col, text=col, command=lambda c=col: Functions.sort_treeview(tree, c, False))
            tree.column(col, anchor='center')

        tree.column('ФИО', width=100)
        tree.column('Предмет', width=200)
        tree.column('Оценка', width=50)


        tree.pack(pady=2, fill='both', expand=True)

    getList()
    return frame