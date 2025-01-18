from tkinter import messagebox, ttk

import customtkinter as ctk

from Forms.Admin import Functions


def create_add_student_tab(self, user):
    frame = ctk.CTkFrame(self)

    nameLabel = ctk.CTkLabel(frame, text="Студент:", font=("Times New Roman", 18))
    courseLabel = ctk.CTkLabel(frame, text="Курс:", font=("Times New Roman", 18))
    gradeLabel = ctk.CTkLabel(frame, text="Оценка:", font=("Times New Roman", 18))
    nameLabel.place(relx=0.05, rely=0.05)
    courseLabel.place(relx=0.6, rely=0.05)
    gradeLabel.place(relx=0.06, rely=0.1)
    courseBox = ctk.CTkComboBox(frame, command=lambda: update_students)
    studentBox = ctk.CTkComboBox(frame)
    studentBox.place(relx=0.18, rely=0.05)
    gradeEntry = ctk.CTkComboBox(frame, values=["Выбрать оценку...", "2", "3", "4", "5"])
    courseBox.place(relx=0.68, rely=0.05)
    gradeEntry.place(relx=0.18, rely=0.1)

    setButton = ctk.CTkButton(frame, text="Поставить оценку", command=lambda: set_Mark())
    setButton.place(relx=0.4, rely=0.15)

    listTitle = ctk.CTkLabel(frame, text="Список студентов и их оценки", font=("Times New Roman", 20))
    listTitle.place(relx=0.375, rely=0.25)
    listBox = ctk.CTkScrollableFrame(frame, width=470, height=400)
    listBox.place(relx=0.25, rely=0.3)
    courseBox.bind("<Key>", Functions.prevent_input)
    studentBox.bind("<Key>", Functions.prevent_input)
    gradeEntry.bind("<Key>", Functions.prevent_input)


    def update_students():
        selected_course = courseBox.get()
        studentBox = ctk.CTkComboBox(frame)
        studentBox.place(relx=0.18, rely=0.05)


    def get_enroll():
        for widget in listBox.winfo_children():
            widget.destroy()

        columns = ('ФИО', 'Предмет', 'Оценка')
        tree = ttk.Treeview(listBox, columns=columns, show='headings', height=20)

        for col in columns:
            tree.heading(col, text=col, command=lambda c=col: Functions.sort_treeview(tree, c, False))
            tree.column(col, anchor='center')

        tree.column('ФИО', width=200)
        tree.column('Предмет', width=100)
        tree.column('Оценка', width=50)


        tree.pack(pady=2, fill='both', expand=True)


    def set_Mark():
        student = studentBox.get()
        course = courseBox.get()
        grade = gradeEntry.get()
        if grade != "Выбрать оценку...":
            if grade == "2":
                grade = 2
            if grade == "3":
                grade = 3
            if grade == "4":
                grade = 4
            if grade == "5":
                grade = 5
        else:
            messagebox.showerror("Ошибка", "Выбрана неверная оценка")
        get_enroll()

    get_enroll()
    return frame