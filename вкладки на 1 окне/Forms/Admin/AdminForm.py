from symtable import Function

import customtkinter as ctk

from Forms.Admin import Functions

from Forms.Admin.Tabs import AddStudents, Generat, AddTeacher, AddCourse, AddEnroll


class AdminWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Панель администратора")
        self.resizable(False, False)
        self.geometry("1200x800")

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(padx=10, pady=10)

        #Вкладки
        self.tabs = {
            "Пользователи": self.create_users_tab(),
            "Преподаватели": AddTeacher.create_add_teacher_tab(self),
            "Студенты": AddStudents.create_add_student_tab(self),
            "Курсы": AddCourse.create_add_course_tab(self),
            "Запись на курсы": self.create_enroll_student_tab(),
            "Генерация отчёта": None,
            "Оценки": Generat.create_add_user_tab(self),
        }

        #Каждой кнопке добавлять выполнение команды при нажатии
        for tab_name in self.tabs.keys():
            if tab_name == "Генерация отчёта":
                button = ctk.CTkButton(button_frame, text=tab_name)
            else:
                button = ctk.CTkButton(button_frame, text=tab_name,
                                       command=lambda name=tab_name: Functions.show_tab(self, name))
            button.pack(side="left", padx=10, pady=5)

        self.current_tab = None
        Functions.show_tab(self, "Пользователи")


    def create_users_tab(self):
        scrollable_frame = ctk.CTkScrollableFrame(self, height=500, width=500)

        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        label = ctk.CTkLabel(scrollable_frame, text="Существующие пользователи:", font=("Times New Roman", 18))
        label.pack(pady=10)

        header_frame = ctk.CTkFrame(scrollable_frame)
        header_frame.pack(pady=10)

        labelName = ctk.CTkLabel(header_frame, text="Пользователь", font=("Times New Roman", 18))
        labelRole = ctk.CTkLabel(header_frame, text="Роль", font=("Times New Roman", 18))

        labelName.pack(side="left", padx=35)
        labelRole.pack(side="left", padx=50)

        return scrollable_frame

    def create_enroll_student_tab(self):
        enroll_tab = AddEnroll.EnrollStudentTab(self)
        return enroll_tab.frame
