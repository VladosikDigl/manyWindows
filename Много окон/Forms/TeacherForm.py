import tkinter

import customtkinter as ctk

import HandlerMain
from tkinter import messagebox
import Forms.AuthForm
from HandlerMain import hash_pass, check_pass

user = ""
code = ""

class TeachWindow(ctk.CTk):
    def __init__(self, thisUser):
        super().__init__()
        self.title("Панель преподавателя")
        self.resizable(False, False)
        self.geometry("1000x700")
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        global user
        user = thisUser

        name = thisUser

        self.teacherName = ctk.CTkLabel(self, text=f"Пользователь: {name}")
        self.teacherName.place(relx=0.01, rely=0.01)
        self.titleLabel = ctk.CTkLabel(self, text="Мои курсы", font=("Times New Roman", 20))
        self.titleLabel.place(relx=0.20,rely=0.08)
        self.courseBox = ctk.CTkScrollableFrame(self, width=400, height=500)
        self.courseBox.place(relx=0.03, rely=0.13)
        self.getMyCourse()

        self.changeOpen = ctk.CTkButton(self,text="Изменить пароль", command=lambda: self.open_change())
        self.changeOpen.place(x=825,y=10)

        self.studLabel = ctk.CTkLabel(self,text="Мои студенты", font=("Times New Roman", 20))
        self.studLabel.place(relx=0.7, rely=0.08)
        self.studentBox = ctk.CTkScrollableFrame(self, width=400, height=500)
        self.studentBox.place(relx=0.55, rely=0.13)
        self.getMyStudents()

        self.markButton = ctk.CTkButton(self,text="Выставление оценок", font=("Times New Roman", 16), command=lambda:self.open_mark())
        self.markButton.place(relx=0.43,rely=0.9)

        self.buttonExit = ctk.CTkButton(self, text="Выйти", command=lambda: self.Exit())
        self.buttonExit.place(x=850, y=650)

    def Exit(self):
        self.destroy()
        auth = Forms.AuthForm.AuthWindow()
        auth.mainloop()

    def open_change(self):
        self.withdraw()
        change = ChangePassword()
        change.protocol("WM_DELETE_WINDOW", lambda:(self.deiconify(), change.destroy()))

    def open_mark(self):
        self.withdraw()
        mark = MarkControl_Teacher()
        mark.protocol("WM_DELETE_WINDOW", lambda:(self.deiconify(), mark.destroy()))

    def getMyCourse(self):
        for widget in self.courseBox.winfo_children():
            widget.destroy()


    def getMyStudents(self):
        for widget in self.studentBox.winfo_children():
            widget.destroy()

class MarkControl_Teacher(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Панель выставления оценок")
        self.resizable(False, False)
        self.geometry("600x800+750+400")
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self.nameLabel = ctk.CTkLabel(self, text="Студент:", font=("Times New Roman", 18))
        self.courseLabel = ctk.CTkLabel(self,text="Курс:", font=("Times New Roman", 18))
        self.gradeLabel = ctk.CTkLabel(self, text="Оценка:", font=("Times New Roman", 18))
        self.nameLabel.place(relx=0.05,rely=0.05)
        self.courseLabel.place(relx=0.6,rely=0.05)
        self.gradeLabel.place(relx=0.06,rely=0.1)
        self.courseBox = ctk.CTkComboBox(self , command=self.update_student)
        self.studentBox = ctk.CTkComboBox(self)
        self.studentBox.place(relx=0.18, rely=0.05)
        self.gradeEntry = ctk.CTkComboBox(self, values=["Выбрать оценку...","2","3","4","5"])
        self.courseBox.place(relx=0.68, rely=0.05)
        self.gradeEntry.place(relx=0.18,rely=0.1)

        self.setButton = ctk.CTkButton(self,text="Поставить оценку", command=lambda: self.set_Mark())
        self.setButton.place(relx=0.4,rely=0.15)

        self.listTitle = ctk.CTkLabel(self,text="Список студентов и их оценки", font=("Times New Roman", 20))
        self.listTitle.place(relx=0.3,rely=0.25)
        self.listBox = ctk.CTkScrollableFrame(self, width=470,height=480)
        self.listBox.place(relx=0.1,rely=0.3)
        self.get_enroll()
        self.courseBox.bind("<Key>", self.prevent_input)
        self.studentBox.bind("<Key>", self.prevent_input)
        self.gradeEntry.bind("<Key>", self.prevent_input)

    def update_student(self, event):
        selected_course = self.courseBox.get()
        self.studentBox = ctk.CTkComboBox(self)
        self.studentBox.place(relx=0.18, rely=0.05)

    def get_enroll(self):
        for widget in self.listBox.winfo_children():
            widget.destroy()


    def set_Mark(self):
        student = self.studentBox.get()
        course = self.courseBox.get()
        grade = self.gradeEntry.get()
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
            messagebox.showerror("Ошибка","Выбрана неверная оценка")
        self.get_enroll()

    def prevent_input(self, event):
        return "break"

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
        self.ButtonChange = ctk.CTkButton(self,text="Сменить пароль")

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
        global user
        return messagebox.showinfo('чётко','круто')

    def check_code(self, new_password):
        entry_code = self.codeEntry.get()
        global code

        if entry_code != "" and entry_code == code:
            messagebox.showinfo("Успешно", "Ваш пароль был изменён")
            code = ""

            self.buttonWithCode.place_forget()
            self.codeEntry.place_forget()
            self.codeLabel.place_forget()
            self.ButtonChange.place(x=60, y=150)