#Создать окно входа и регистрации.


import tkinter
from tkinter import *
from tkinter import ttk



def click_button():
    k=0
    login = input_login.get()
    password = input_password.get()
    if not login or not password:
        k+=1
        oshibka2 = Tk()
        oshibka2.title('ОШИБКА')
        oshibka2.geometry('240x120')
        osh2 = Canvas(oshibka2, bg='#ff9494')
        osh2.pack(fill=BOTH, anchor='nw', expand=True)
        osh2.create_text(120, 60, text='Остались пустые поля', font='Arial 11')
        oshibka2.resizable(width=False, height=False)

        oshibka2.mainloop()
    with open('logpass.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            savedusername, savedpassword = line.strip().split('|')
            if savedusername == login and savedpassword == password:
                k+=1
                canvas.destroy()
                canvas2 = Canvas(root, bg='#fff0f5')
                canvas2.pack(fill=BOTH, anchor='nw', expand=True)
                canvas2.create_rectangle(0, 0, 480, 107, fill='#ffffff')
                canvas2.create_rectangle(0, 107, 480, 214, fill='blue')
                canvas2.create_rectangle(0, 214, 480, 321, fill='red')
                root.title('Верификация пройдена')
        if k < 1:
            oshibka = Tk()
            oshibka.title('ОШИБКА')
            oshibka.geometry('240x120')
            canvas3 = Canvas(oshibka, bg='#ff9494')
            canvas3.pack(fill=BOTH, anchor='nw', expand=True)
            canvas3.create_text(120, 60, text='Неверный логин или пароль', font='Arial 11')
            oshibka.resizable(width=False, height=False)

            oshibka.mainloop()


def click_button3():
    k=0
    newlogin = input_login.get()
    newpass = input_password.get()
    if '|' in newlogin or '|' in newpass:
        k+=1
        oshibka2 = Tk()
        oshibka2.title('ОШИБКА')
        oshibka2.geometry('240x120')
        osh2 = Canvas(oshibka2, bg='#ff9494')
        osh2.pack(fill=BOTH, anchor='nw', expand=True)
        osh2.create_text(120, 60, text='Запрещённый символ " | "', font='Arial 11')
        oshibka2.resizable(width=False, height=False)

        oshibka2.mainloop()
    if not newlogin or not newpass:
        k+=1
        oshibka2 = Tk()
        oshibka2.title('ОШИБКА')
        oshibka2.geometry('240x120')
        osh2 = Canvas(oshibka2, bg='#ff9494')
        osh2.pack(fill=BOTH, anchor='nw', expand=True)
        osh2.create_text(120, 60, text='Остались пустые поля', font='Arial 11')
        oshibka2.resizable(width=False, height=False)

        oshibka2.mainloop()

    with open('logpass.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            savedlogin, _ = line.strip().split('|')
            if newlogin == savedlogin:
                k+=1
                oshibka2 = Tk()
                oshibka2.title('ОШИБКА')
                oshibka2.geometry('240x120')
                osh2 = Canvas(oshibka2, bg='#ff9494')
                osh2.pack(fill=BOTH, anchor='nw', expand=True)
                osh2.create_text(120, 60, text='Такой логин уже существует', font='Arial 11')
                oshibka2.resizable(width=False, height=False)

                oshibka2.mainloop()

    if k < 1:
        if len(newpass) < 8 or len(newpass) > 16 or len(newlogin) < 8 or len(newlogin) > 16:
            oshibka3 = Tk()
            oshibka3.title('ОШИБКА')
            oshibka3.geometry('480x120')
            osh3 = Canvas(oshibka3, bg='#ff9494')
            osh3.pack(fill=BOTH, anchor='nw', expand=True)
            osh3.create_text(240, 60, text='Длина логина или пароля не соотвествует рамкам программы', font='Arial 11')
            oshibka3.resizable(width=False, height=False)

            oshibka3.mainloop()

        else:
            f = open('logpass.txt', 'a')
            f.write(f'{newlogin}|{newpass}\n')
            f.close()
            sucs = Tk()
            sucs.geometry('240x120')
            cansucs = Canvas(sucs, bg='#80ff80')
            cansucs.pack(fill=BOTH, anchor='nw', expand=True)
            cansucs.create_text(120, 60, text='Успешная регистрация', font='Arial 11')
            sucs.resizable(width=False, height=False)

            sucs.mainloop()



root = Tk()
root.geometry('480x321')
root.title('Вход и регистрация')
root.resizable(width=False, height=False)

canvas = Canvas(root, bg='#fff0f5')
canvas.pack(fill=BOTH, anchor='nw', expand=True)

canvas.create_text(240, 30, text='Введите логин и пароль', font='Arial 13')
vhod = tkinter.Button(canvas, text='Вход', command=click_button)
canvas.create_window(240, 170, window=vhod, height='30', width='100')

canvas.create_text(100,70, text='Логин(от 8 до 16 символов)\nсимвол " | " - запрещён',font='Arial 8')
canvas.create_text(100,120, text='Пароль(от 8 до 16 символов)\nсимвол " | " - запрещён',font='Arial 8')


input_login = StringVar()
login = tkinter.Entry(canvas, textvariable=input_login)
canvas.create_window(240, 70, window=login, height='30', width='120')

input_password = StringVar()
password = tkinter.Entry(canvas, textvariable=input_password)
canvas.create_window(240, 120, window=password, height='30', width='120')

regbtn = tkinter.Button(canvas, text='Регистрация', command=click_button3)
canvas.create_window(240, 230, window=regbtn, height='30', width='120')


root.mainloop()
