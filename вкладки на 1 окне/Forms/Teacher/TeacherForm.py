import customtkinter as ctk
from Forms.Admin import Functions
from Forms.Teacher.Tabs import AddMark, ChangePassword



class TeachWindow(ctk.CTk):
    def __init__(self, thisUser):
        super().__init__()
        self.title("Панель преподавателя")
        self.resizable(False, False)
        self.geometry("1000x700")
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.user = thisUser

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(padx=10, pady=10)

        self.tabs = {
            "Мои студенты": self.main_tab(),
            "Выставить оценки": AddMark.create_add_student_tab(self,self.user),
            "Сменить пароль": ChangePassword.create_add_student_tab(self,self.user),
        }

        for tab_name in self.tabs.keys():
            button = ctk.CTkButton(button_frame, text=tab_name,
                                    command=lambda name=tab_name: Functions.show_tab(self,name))
            button.pack(side="left", padx=10, pady=5)

        self.current_tab = None

        self.teacherName = ctk.CTkLabel(self, text=f"Пользователь: ")
        self.user_log = ctk.CTkLabel(self,text=f"{thisUser}")
        self.teacherName.place(relx=0.01, rely=0.01)
        self.user_log.place(relx=0.01,rely=0.04)
        Functions.show_tab(self,"Мои студенты")

    def main_tab(self):
        frame = ctk.CTkFrame(self)

        titleLabel = ctk.CTkLabel(frame, text="Мои курсы", font=("Times New Roman", 20))
        titleLabel.place(relx=0.20, rely=0.1)
        courseBox = ctk.CTkScrollableFrame(frame, width=400, height=500)
        courseBox.place(relx=0.03, rely=0.15)

        studLabel = ctk.CTkLabel(frame, text="Мои студенты", font=("Times New Roman", 20))
        studLabel.place(relx=0.7, rely=0.1)
        studentBox = ctk.CTkScrollableFrame(frame, width=400, height=500)
        studentBox.place(relx=0.55, rely=0.15)

        def get_my_students():
            for widget in courseBox.winfo_children():
                widget.destroy()


        def get_my_course():
            for widget in courseBox.winfo_children():
                widget.destroy()


        get_my_students()
        get_my_course()

        return frame