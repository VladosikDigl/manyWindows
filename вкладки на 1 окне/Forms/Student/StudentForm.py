from tkinter import ttk

import customtkinter as ctk
from Forms.Admin import Functions
from Forms.Teacher.Tabs import  ChangePassword


class StudentWindow(ctk.CTk):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.title("Панель студента")
        self.resizable(False, False)
        self.geometry("800x550")
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(padx=10, pady=10)

        self.tabs = {
            "Мои оценки": self.main_tab(),
            "Сменить пароль": ChangePassword.create_add_student_tab(self, self.user),
        }

        for tab_name in self.tabs.keys():
            button = ctk.CTkButton(button_frame, text=tab_name,
                                   command=lambda name=tab_name: Functions.show_tab(self, name))
            button.pack(side="left", padx=10, pady=5)

        self.current_tab = None

        self.studentName = ctk.CTkLabel(self, text=f"Пользователь: ")
        self.user_log = ctk.CTkLabel(self, text=f"{user}")
        self.studentName.place(relx=0.01, rely=0.01)
        self.user_log.place(relx=0.01, rely=0.05)
        Functions.show_tab(self,"Мои оценки")

    def main_tab(self):
        frame = ctk.CTkFrame(self)

        markLabel = ctk.CTkLabel(frame,text="Мои оценки", font=("Times New Roman", 20))
        markLabel.place(relx=0.45,rely=0.08)
        markScroll = ctk.CTkScrollableFrame(frame,width=450,height=375)
        markScroll.place(relx=0.2,rely=0.15)

        def fill_scroll():
            for widget in markScroll.winfo_children():
                widget.destroy()


            columns = ('Предмет', 'Оценка')
            tree = ttk.Treeview(markScroll, columns=columns, show='headings', height=30)

            for col in columns:
                tree.heading(col, text=col, command=lambda c=col: Functions.sort_treeview(tree, c, False))
                tree.column(col, anchor='center')

            tree.column('Предмет', width=200)
            tree.column('Оценка', width=50)

            tree.pack(pady=2, fill='both', expand=True)

        fill_scroll()
        return frame
