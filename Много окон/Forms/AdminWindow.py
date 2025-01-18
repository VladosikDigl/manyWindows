import tkinter
from tkinter import messagebox

import customtkinter as ctk
import HandlerMain
import Forms.AuthForm


class AdminWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Панель администратора")
        self.resizable(False, False)
        self.geometry("700x700")
        self.namedLabel = ctk.CTkLabel(self, text="Список пользователей", font=("Times New Roman", 20))
        self.namedLabel.place(relx=0.3, rely=0.03, anchor=tkinter.CENTER)
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=400, height=550)
        self.scrollable_frame.place(relx=0.03, rely=0.065)
        self.load_user()

        self.listLabel = ctk.CTkLabel(self, text="Вкладки управления", font=("Times New Roman", 20))
        self.listLabel.place(x=500,y=5)
        self.buttonStudent = ctk.CTkButton(self, text="Студенты", command=lambda: self.open_studList(), width=170)
        self.buttonTeachers = ctk.CTkButton(self, text="Преподаватели", command=lambda: self.open_teachList(), width=170)
        self.buttonCourses = ctk.CTkButton(self, text="Курсы", command=lambda: self.open_courseControl(), width=170)
        self.buttonAddCourses = ctk.CTkButton(self,text="Запись на курсы", command=lambda: self.open_addCourse(), width=170)
        self.buttonEnrolls = ctk.CTkButton(self, text="Оценки студентов", command=lambda: self.open_enroll(), width=170)
        self.buttonGener = ctk.CTkButton(self, text="Генерация отчёта", width=170)
        self.buttonStudent.place(x=510, y=40)
        self.buttonTeachers.place(x=510, y=80)
        self.buttonCourses.place(x=510, y=120)
        self.buttonAddCourses.place(x=510,y=160)
        self.buttonEnrolls.place(x=510, y=200)
        self.buttonGener.place(x=510,y=240)

        self.buttonExit = ctk.CTkButton(self, text="Выйти", command=lambda: self.Exit())
        self.buttonExit.place(x=550,y=650)

        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def Exit(self):
        self.destroy()
        auth = Forms.AuthForm.AuthWindow()
        auth.mainloop()

    def open_enroll(self):
        self.withdraw()
        list = EnrollList()
        list.protocol("WM_DELETE_WINDOW", lambda : (self.deiconify(), list.destroy()))

    def update_user(self):
        old_login = self.oldLoginEntry.get()
        new_login = self.newLoginEntry.get()
        new_password = self.newPasswordEntry.get()
        new_role = self.newRoleEnrty.get()
        if new_role == "Студент":
            new_role = 3
        elif new_role == "Преподаватель":
            new_role = 2
        elif new_role == "Администратор":
            new_role = 1
        else:
            new_role = 3
        isCorrect = HandlerMain.check_pass(new_password)
        self.oldLoginEntry.delete(0,ctk.END)
        self.newLoginEntry.delete(0,ctk.END)
        self.newPasswordEntry.delete(0,ctk.END)

    def delete_user(self):
        login = self.entryDeleteLogin.get()
        HandlerMain.adminPanel_DeleteUser(login)

    def add_user(self):
        login = self.entryLogin.get()
        password = self.entryPassword.get()
        role = self.combobox.get()
        HandlerMain.adminPanel_AddUser(login, password, role)
        self.entryLogin.delete(0,ctk.END)
        self.entryPassword.delete(0,ctk.END)

    def load_user(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()


    def open_studList(self):
        self.withdraw()
        StudientControl = StudentList_Admin()
        StudientControl.get_students()
        StudientControl.protocol("WM_DELETE_WINDOW", lambda : (self.deiconify(), StudientControl.destroy(), self.load_user()))

    def open_courseControl(self):
        self.withdraw()
        CourseControl = CourseControl_Admin()
        CourseControl.protocol("WM_DELETE_WINDOW", lambda: (self.deiconify(), CourseControl.destroy()))

    def open_teachList(self):
        self.withdraw()
        TeacherControl = TeacherControl_Admin()
        TeacherControl.protocol("WM_DELETE_WINDOW", lambda : (self.deiconify(), TeacherControl.destroy(), self.load_user()))

    def open_addCourse(self):
        self.withdraw()
        Courses = CourseAdd()
        Courses.protocol("WM_DELETE_WINDOW", lambda: (self.deiconify(), Courses.destroy()))



#Вкладка студенты в админ панели
class StudentList_Admin(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Панель управления студентами")
        self.resizable(False, False)
        self.geometry("1000x700")
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self.addLabel = ctk.CTkLabel(self, text="Добавление нового студента", font=("Times New Roman", 20))
        self.addLabel.place(relx=0.05, rely=0.001)

        self.studNameLabel = ctk.CTkLabel(self, text="ФИО:")
        self.studAgeLabel = ctk.CTkLabel(self, text="Возраст:")
        self.studPhoneLabel = ctk.CTkLabel(self, text="Телефон:")
        self.studLoginLabel = ctk.CTkLabel(self, text="Логин:")
        self.studMailLabel = ctk.CTkLabel(self, text="Почта:")
        self.studNameLabel.place(relx=0.07, rely=0.05)
        self.studAgeLabel.place(relx=0.05, rely=0.1)
        self.studPhoneLabel.place(relx=0.047,rely=0.15)
        self.studLoginLabel.place(relx=0.065,rely=0.2)
        self.studMailLabel.place(relx=0.065,rely=0.25)
        self.nameEntry = ctk.CTkEntry(self)
        self.ageEntry = ctk.CTkEntry(self)
        self.phoneEntry = ctk.CTkEntry(self)
        self.loginEntry = ctk.CTkEntry(self)
        self.mailEntry = ctk.CTkEntry(self)
        HandlerMain.symbolControl(self.phoneEntry, 11)
        HandlerMain.symbolControl(self.ageEntry, 2)
        self.nameEntry.place(relx=0.12, rely=0.05)
        self.ageEntry.place(relx=0.12, rely=0.1)
        self.phoneEntry.place(relx=0.12, rely=0.15)
        self.loginEntry.place(relx=0.12, rely=0.2)
        self.mailEntry.place(relx=0.12, rely=0.25)
        self.addButton = ctk.CTkButton(self, text="Добавить студента", command=lambda: self.add_student())
        self.addButton.place(relx=0.12,rely=0.3)

        self.delLabel = ctk.CTkLabel(self, text="Удалить студента", font=("Times New Roman", 20))
        self.delLabel.place(relx=0.11, rely=0.35)
        self.studId = ctk.CTkLabel(self, text="ID студента:")
        self.studId.place(relx=0.03, rely=0.42)
        self.studIdEntry = ctk.CTkEntry(self)
        HandlerMain.symbolControl(self.studIdEntry, 100)
        self.studIdEntry.place(relx=0.12, rely=0.42)
        self.delButton = ctk.CTkButton(self, text="Удалить студента", command=lambda: self.del_student())
        self.delButton.place(relx=0.12,rely=0.48)

        self.updateLabel = ctk.CTkLabel(self, text="Обновить данные о студенте", font=("Times New Roman", 20))
        self.updateLabel.place(relx=0.05, rely=0.55)
        self.updateId = ctk.CTkLabel(self,text="ID студента:")
        self.newNameLab = ctk.CTkLabel(self,text="ФИО:")
        self.newAgeLab = ctk.CTkLabel(self,text="Возраст:")
        self.newPhoneLab = ctk.CTkLabel(self,text="Телефон:")
        self.updateId.place(relx=0.03,rely=0.62)
        self.newNameLab.place(relx=0.07,rely=0.67)
        self.newAgeLab.place(relx=0.05,rely=0.72)
        self.newPhoneLab.place(relx=0.047,rely=0.77)
        self.updateIdEntry = ctk.CTkEntry(self)
        self.updateName = ctk.CTkEntry(self)
        self.updateAge = ctk.CTkEntry(self)
        self.updatePhone = ctk.CTkEntry(self)
        HandlerMain.symbolControl(self.updatePhone, 11)
        HandlerMain.symbolControl(self.updateAge, 2)
        HandlerMain.symbolControl(self.updateIdEntry, 100)
        self.updateIdEntry.place(relx=0.12,rely=0.62)
        self.updateName.place(relx=0.12,rely=0.67)
        self.updateAge.place(relx=0.12,rely=0.72)
        self.updatePhone.place(relx=0.12,rely=0.77)
        self.updateButt = ctk.CTkButton(self, text="Обновить данные", command=lambda: self.update_student())
        self.updateButt.place(relx=0.12,rely=0.82)

        self.listLabel = ctk.CTkLabel(self, text="Список студентов", font=("Times New Roman", 20))
        self.listLabel.place(relx=0.65, rely=0.001)
        self.scroll = ctk.CTkScrollableFrame(self, height=600, width=500)
        self.scroll.place(relx=0.45,rely=0.05)
        self.reloadButton = ctk.CTkButton(self,text="Обновить список", command=lambda: self.get_students())
        self.reloadButton.place(relx=0.65, rely=0.94)

    def add_student(self):
        name = str(self.nameEntry.get())
        age = int(self.ageEntry.get())
        phone = self.phoneEntry.get()
        login = str(self.loginEntry.get())
        mail = str(self.mailEntry.get())

        if HandlerMain.mail_validator(mail) is None:
            messagebox.showerror("Ошибка", "Неверная почта")
            return

        self.nameEntry.delete(0,ctk.END)
        self.ageEntry.delete(0,ctk.END)
        self.phoneEntry.delete(0,ctk.END)
        self.loginEntry.delete(0,ctk.END)
        self.mailEntry.delete(0,ctk.END)
        self.get_students()

    def del_student(self):
        id = int(self.studIdEntry.get())
        if id != "":
            self.get_students()
        else:
            messagebox.showerror("Ошибка", "Поле должно быть числом и не должно быть пустым")
            return
    def update_student(self):
        id = int(self.updateIdEntry.get())
        name = self.updateName.get()
        age = self.updateAge.get()
        phone = self.updatePhone.get()
        if id != "":
            self.get_students()

    def get_students(self):
        for widget in self.scroll.winfo_children():
            widget.destroy()

        name_label = ctk.CTkLabel(self.scroll, text="ID    |    ФИО    |    Возраст     |    Телефон   |     Логин  ",
                                  font=("Times New Roman", 12))
        name_label.pack(pady=2)




#Вкладка управления преподавателями у админа
class TeacherControl_Admin(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Панель управления преподавателями")
        self.resizable(False, False)
        self.geometry("950x700")
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self.LabelAdd = ctk.CTkLabel(self,text="Добавление преподавателя", font=("Times New Roman",20))
        self.LabelAdd.place(relx=0.05,rely=0.001)

        self.AddNameLabel = ctk.CTkLabel(self, text="ФИО:")
        self.AddPhoneLabel = ctk.CTkLabel(self, text="Телефон:")
        self.addLoginLabel = ctk.CTkLabel(self,text="Логин:")
        self.addMailLabel = ctk.CTkLabel(self,text="Почта:")
        self.AddNameEntry = ctk.CTkEntry(self)
        self.AddPhoneEntry = ctk.CTkEntry(self)
        self.AddLoginEntry = ctk.CTkEntry(self)
        self.AddMailEntry = ctk.CTkEntry(self)
        HandlerMain.symbolControl(self.AddPhoneEntry, 12)
        self.AddButton = ctk.CTkButton(self,text="Добавить преподавателя",command=lambda: self.add_teacher())
        self.AddNameLabel.place(relx=0.038,rely=0.08)
        self.AddPhoneLabel.place(relx=0.01,rely=0.13)
        self.AddNameEntry.place(relx=0.08,rely=0.08)
        self.AddPhoneEntry.place(relx=0.08,rely=0.13)
        self.AddLoginEntry.place(relx=0.08,rely=0.18)
        self.AddMailEntry.place(relx=0.08,rely=0.23)
        self.addLoginLabel.place(relx=0.01,rely=0.18)
        self.addMailLabel.place(relx=0.01,rely=0.23)
        self.AddButton.place(relx=0.06, rely=0.28)


        self.LabelDelete = ctk.CTkLabel(self, text="Удалить преподавателя", font=("Times New Roman",20))
        self.LabelDeleteID = ctk.CTkLabel(self, text="ID:")
        self.DeleteEntry = ctk.CTkEntry(self)
        HandlerMain.symbolControl(self.DeleteEntry, 100)
        self.DeleteButton = ctk.CTkButton(self,text="Удалить",command=lambda: self.del_teacher())
        self.LabelDelete.place(relx=0.05,rely=0.40)
        self.LabelDeleteID.place(relx=0.05,rely=0.45)
        self.DeleteEntry.place(relx=0.08,rely=0.45)
        self.DeleteButton.place(relx=0.08,rely=0.51)

        self.LabelUpdate = ctk.CTkLabel(self,text="Обновить данные о преподавателе",font=("Times New Roman", 20))
        self.LabelUpdateID = ctk.CTkLabel(self, text="ID:")
        self.LabelUpdateName = ctk.CTkLabel(self, text="ФИО:")
        self.LabelUpdatePhone = ctk.CTkLabel(self, text="Телефон:")
        self.UpdateID = ctk.CTkEntry(self)
        self.UpdateName = ctk.CTkEntry(self)
        self.UpdatePhone = ctk.CTkEntry(self)
        HandlerMain.symbolControl(self.UpdatePhone, 12)
        HandlerMain.symbolControl(self.UpdateID, 100)
        self.UpdateButton = ctk.CTkButton(self,text="Обновить данные", command=lambda: self.update_teacher())
        self.LabelUpdate.place(relx=0.03,rely=0.61)
        self.LabelUpdateID.place(relx=0.055,rely=0.67)
        self.LabelUpdateName.place(relx=0.04,rely=0.72)
        self.LabelUpdatePhone.place(relx=0.01,rely=0.77)
        self.UpdateID.place(relx=0.08,rely=0.67)
        self.UpdateName.place(relx=0.08,rely=0.72)
        self.UpdatePhone.place(relx=0.08,rely=0.77)
        self.UpdateButton.place(relx=0.08,rely=0.83)

        self.LabelList = ctk.CTkLabel(self,text="Список преподавателей", font=("Times New Roman",20))
        self.LabelList.place(relx=0.625,rely=0.001)
        self.scroll = ctk.CTkScrollableFrame(self, height=600, width=425)
        self.scroll.place(relx=0.5,rely=0.065)
        self.list_teacher()
        self.ListButton = ctk.CTkButton(self,text="Обновить список",command=lambda: self.list_teacher())
        self.ListButton.place(relx=0.655,rely=0.95)

    def add_teacher(self):
        name = self.AddNameEntry.get()
        phone = self.AddPhoneEntry.get()
        login = str(self.AddLoginEntry.get())
        mail = str(self.AddMailEntry.get())

        if HandlerMain.mail_validator(mail) is None:
            messagebox.showerror("Ошибка", "Неверная почта")
            return


        self.list_teacher()
        self.AddNameEntry.delete(0, ctk.END)
        self.AddPhoneEntry.delete(0, ctk.END)
        self.AddLoginEntry.delete(0, ctk.END)
        self.AddMailEntry.delete(0,ctk.END)

    def del_teacher(self):
        id = int(self.DeleteEntry.get())

    def update_teacher(self):
        id = int(self.UpdateID.get())
        name = self.UpdateName.get()
        phone = self.UpdatePhone.get()


    def list_teacher(self):
        for widget in self.scroll.winfo_children():
            widget.destroy()

        name_label = ctk.CTkLabel(self.scroll, text="ID    |    ФИО    |     Телефон   |     Логин  ",
                                  font=("Times New Roman", 12))
        name_label.pack(pady=2)




#Вкладка управления курсами у админа
class CourseControl_Admin(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Панель управления курсами")
        self.resizable(False, False)
        self.geometry("1200x700")

        self.LabelYo = ctk.CTkLabel(self, text="Добавление нового курса", font=("Times New Roman",20))
        self.LabelYo.place(relx=0.05, rely=0.002)
        self.labelTitle = ctk.CTkLabel(self,text="Название:")
        self.labelDescription = ctk.CTkLabel(self,text="Описание:")
        self.teacherLabel = ctk.CTkLabel(self, text="Преподаватель:")
        self.labelTitle.place(relx=0.01, rely=0.08)
        self.labelDescription.place(relx=0.01,rely=0.13)
        self.teacherLabel.place(relx=0.24, rely=0.08)
        teachers = self.get_teachers()
        self.teacherBox = ctk.CTkComboBox(self, values=teachers, width=250)
        self.teacherBox.place(relx=0.23,rely=0.125)
        self.teacherBox.bind("<Key>", self.prevent_input)

        self.entryName = ctk.CTkEntry(self)
        self.entryDescript = ctk.CTkEntry(self)
        self.entryName.place(relx=0.09,rely=0.08)
        self.entryDescript.place(relx=0.09,rely=0.13)
        self.addButton = ctk.CTkButton(self, text="Добавить курс", command=lambda: self.add_course())
        self.addButton.place(relx=0.2, rely=0.19)

        self.LabelDel = ctk.CTkLabel(self, text="Удаление курса", font=("Times New Roman", 20))
        self.LabelDel.place(relx=0.09, rely=0.3)
        self.LabelDelName = ctk.CTkLabel(self, text="ID курса:")
        self.LabelDelName.place(relx=0.055, rely=0.35)
        self.entryDelName = ctk.CTkEntry(self)
        HandlerMain.symbolControl(self.entryDelName, 100)
        self.entryDelName.place(relx=0.13, rely=0.35)
        self.delButton = ctk.CTkButton(self,text="Удалить курс", command=lambda: self.del_courses())
        self.delButton.place(relx=0.1,rely=0.42)

        self.scrollLabel = ctk.CTkLabel(self,text="Список курсов", font=("Times New Roman", 20))
        self.scrollLabel.place(relx=0.75,rely=0.009)
        self.scroll = ctk.CTkScrollableFrame(self,height=600, width=500)
        self.scroll.place(relx=0.55,rely=0.06)
        self.updateButton = ctk.CTkButton(self,text="Обновить список", command=lambda: self.get_courses())
        self.updateButton.place(relx=0.75,rely=0.9465)
        self.get_courses()

    def prevent_input(self, event):
        return "break"

    def add_course(self):
        title = self.entryName.get()
        description = self.entryDescript.get()
        teacher = self.teacherBox.get()
        self.get_courses()

    def del_courses(self):
        name = int(self.entryDelName.get())
        if name != "":
            self.get_courses()
            return
        else:
            messagebox.showerror("Ошибка", "Поле ID не должно быть пустым")

    def get_courses(self):
        for widget in self.scroll.winfo_children():
            widget.destroy()


    def get_teachers(self):
        return



#Список пользователей в админ панеле
class UserList(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Список пользователей")
        self.resizable(False, False)
        self.geometry("300x300+1500+200")

        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True)

        self.load_user()
        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def load_user(self):
        return
class CourseAdd(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Запись на курс")
        self.resizable(False, False)
        self.geometry("600x500")
        self.studentLabel = ctk.CTkLabel(self, text="Студенты", font=("Times New Roman", 20))
        self.studentLabel.place(relx=0.1, rely=0.03)
        self.courseLabel = ctk.CTkLabel(self, text="Предмет", font=("Times New Roman", 20))
        self.courseLabel.place(relx=0.7, rely=0.03)
        self.studentBox = ctk.CTkScrollableFrame(self, width=300, height=300)
        self.courseBox = ctk.CTkComboBox(self)
        self.studentBox.place(relx=0.02,rely=0.1)
        self.courseBox.place(relx=0.65,rely=0.1)
        self.addButton = ctk.CTkButton(self,text="Добавить в курс", command=lambda: self.add())
        self.addButton.place(relx=0.65,rely=0.2)
        self.checkbox()
        self.courseBox.bind("<Key>", self.prevent_input)

        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def prevent_input(self, event):
        return "break"

    def checkbox(self):
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


class EnrollList(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Все оценки")
        self.resizable(False, False)
        self.geometry("500x500")
        self.gradeSort = False
        self.titleLab = ctk.CTkLabel(self, text="Список всех оценок", font=("Times New Roman", 20))
        self.titleLab.place(x=175, y=5)
        self.scroll = ctk.CTkScrollableFrame(self, height=400, width=450)
        self.scroll.place(x=15, y=80)
        self.NameButton = ctk.CTkButton(self, text="ФИО", width=100, command=lambda: self.toName())
        self.CourseButton = ctk.CTkButton(self, text="Предмет", width=100, command=lambda: self.toCourse())
        self.GradeButton = ctk.CTkButton(self, text="Оценка", width=100, command=lambda: self.toGrade())
        self.NameButton.place(x=20, y=40)
        self.CourseButton.place(x=210, y=40)
        self.GradeButton.place(x=380, y=40)
        self.getList()

    def toName(self):
        for widget in self.scroll.winfo_children():
            widget.destroy()
        sort_list = sorted(list, key=lambda x: x[0])

        for name, course, mark in sort_list:
            if mark == None:
                mark = 0
            course_label = ctk.CTkLabel(self.scroll, text=f"{name}   |   {course}  |   {mark}",
                                        font=("Times New Roman", 12))
            course_label.pack(pady=2)

    def toCourse(self):
        for widget in self.scroll.winfo_children():
            widget.destroy()
        sort_list = sorted(list, key=lambda x: x[1])

        for name, course, mark in sort_list:
            if mark == None:
                mark = 0
            course_label = ctk.CTkLabel(self.scroll, text=f"{name}   |   {course}  |   {mark}",
                                        font=("Times New Roman", 12))
            course_label.pack(pady=2)

    def toGrade(self):
        for widget in self.scroll.winfo_children():
            widget.destroy()


        if self.gradeSort is False:
            sort_list = sorted(list, key=lambda x: (x[2] is None, -x[2] if x[2] is not None else float('inf')))
            self.gradeSort = True
        else:
            sort_list = sorted(list, key=lambda x: (x[2] if x[2] is not None else float('-inf')))
            self.gradeSort = False

        for name, course, mark in sort_list:
            if mark == None:
                mark = 0
            course_label = ctk.CTkLabel(self.scroll, text=f"{name}   |   {course}  |   {mark}",
                                        font=("Times New Roman", 12))
            course_label.pack(pady=2)

    def getList(self):
        for widget in self.scroll.winfo_children():
            widget.destroy()

