import re
from tkinter import messagebox



def add_user(login,password, role, mail):
    if login == "" or password == "":
        messagebox.showwarning("Ошибка", "Поля не должны быть пустыми")
        return

    isEng = re.match(r'^[a-zA-Z]+\Z', login) is not None
    if not isEng:
        messagebox.showerror("Ошибка", "Логин должен состоять только из английских символов")
        return


def delete_user(login):
    if login == "":
        messagebox.showerror("Ошибка", "Поле не должно быть пустым")
        return

    messagebox.showinfo("Успех!", f"Пользователь {login} успешно удалён")

def show_tab(self, tab_name):
    if self.current_tab:
        self.current_tab.pack_forget()
    self.current_tab = self.tabs[tab_name]
    self.current_tab.pack(fill="both", expand=True)

def update_tab(self):
    self.tabs["Пользователи"] = self.create_users_tab()
    self.tabs["Запись на курсы"] = self.create_enroll_student_tab()


def prevent_input(event):
    return "break"

def sort_treeview(tree, col, reverse):
    data = [(tree.set(child, col), child) for child in tree.get_children('')]

    if col == "Оценка" or col == "ID":
        data.sort(key=lambda x: float(x[0]) if x[0] else 0, reverse=reverse)
    elif col == "Возраст":
        data.sort(key=lambda x: int(x[0]) if x[0] else 0, reverse=reverse)
    else:
        data.sort(reverse=reverse)


    for index, (_, child) in enumerate(data):
        tree.move(child, '', index)

    tree.heading(col, command=lambda: sort_treeview(tree, col, not reverse))