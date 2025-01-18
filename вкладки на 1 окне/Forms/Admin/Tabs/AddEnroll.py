from tkinter import messagebox

import customtkinter as ctk

from Forms.Admin import Functions


class EnrollStudentTab:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(self.parent)

        studentLabel = ctk.CTkLabel(self.frame, text="Студенты", font=("Times New Roman", 20))
        studentLabel.place(relx=0.1, rely=0.03)
        courseLabel = ctk.CTkLabel(self.frame, text="Предмет", font=("Times New Roman", 20))
        courseLabel.place(relx=0.7, rely=0.03)

        self.courseBox = ctk.CTkComboBox(self.frame)
        self.courseBox.place(relx=0.65, rely=0.1)

        self.studentBox = ctk.CTkScrollableFrame(self.frame, width=300, height=300)
        self.studentBox.place(relx=0.02, rely=0.1)

        addButton = ctk.CTkButton(self.frame, text="Добавить в курс", command=self.add)
        addButton.place(relx=0.65, rely=0.2)

        self.courseBox.bind("<Key>", Functions.prevent_input)

        self.checkboxes = []
        self.update_checkboxes()

    def update_checkboxes(self):
        for widget in self.studentBox.winfo_children():
            widget.destroy()


        self.checkboxes = []

    def add(self):
        selected_students = []
        for checkbox in self.checkboxes:
            if checkbox.get():
                selected_students.append(checkbox.cget("text"))

        course = self.courseBox.get()

        if not selected_students:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите хотя бы одного студента")
            return

        try:
            messagebox.showinfo("Успех", "Студенты успешно добавлены на курс")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Возникла ошибка при добавлении на курс: {str(e)}")