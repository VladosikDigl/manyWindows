import string

import bcrypt as bc
import re
import random
import smtplib
from tkinter import messagebox
from tkinter import END


def auth(login, password):
    login = login

    return login

def adminPanel_AddUser(login,password, role, mail):
    if login == "" or password == "":
        messagebox.showwarning("Ошибка", "Поля не должны быть пустыми")
        return

    isEng = re.match(r'^[a-zA-Z]+\Z', login) is not None
    if not isEng:
        messagebox.showerror("Ошибка", "Логин должен состоять только из английских символов")
        return

    password_len = len(password)
    upper = 0
    lower = 0
    number = 0
    isCorrect = True

    for i in range(0, len(password)):
        for x in password:
            if x.isupper() == True:
                upper += 1
            elif x.islower() == True:
                lower += 1
            elif x.isalpha() == False:
                number += 1
        if upper <= 0 or lower <= 0 or number <= 0:
            isCorrect = False

    if not isCorrect:
        messagebox.showwarning("Ошибка", f"Пароль должен содержать как минимум одну строчную и заглавную буквы и одну цифру")
        return

def check_pass(password):
    password_len = len(password)
    upper = 0
    lower = 0
    number = 0
    isCorrect = True

    for i in range(0, len(password)):
        for x in password:
            if x.isupper() == True:
                upper += 1
            elif x.islower() == True:
                lower += 1
            elif x.isalpha() == False:
                number += 1
        if upper <= 0 or lower <= 0 or number <= 0:
            isCorrect = False
        return isCorrect

def hash_pass(password):
    salt = bc.gensalt()
    hashed_pass = bc.hashpw(password, salt)
    return hashed_pass

def adminPanel_DeleteUser(login):
    if login == "":
        messagebox.showerror("Ошибка", "Поле не должно быть пустым")
        return
    messagebox.showinfo("Успех!", f"Пользователь {login} успешно удалён")

def symbolControl(entry, max_length):
    def validate_input(char):
        return char.isdigit() or char == ""

    def on_key_release(event):
        current_text = entry.get()
        if not all(validate_input(char) for char in current_text):
            entry.delete(len(current_text) - 1, END)
        if len(current_text) > max_length:
            entry.delete(len(current_text) - 1, END)  # Удаление лишнего символа

    entry.bind("<KeyRelease>", on_key_release)

def mail_validator(mail):
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    return re.match(pattern, mail)


def send_email(subject, body, receiver_email):
    sender_email = "spprtvladosik@gmail.com"
    sender_password = ""

    subject = subject
    body = body

    message = f"Subject: {subject}\n\n{body}".encode('utf-8')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
    server.close()

def generate_code():
    code = random.randint(100000,999999)
    return code

def generate_pass():
    characters = string.ascii_letters + string.digits + string.punctuation
    symbols = ''.join(random.choice(characters) for _ in range(8))
    temp = ["Kk1", symbols]
    password = ''.join(temp)
    return password



