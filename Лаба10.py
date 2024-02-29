#Крестики-нолики на tkinter с компьютером.

import tkinter
from tkinter import ttk
from tkinter import *
import random
import copy

turn = 'X'
p1 = random.choice(['X','O'])
if p1 == 'X':
    p2 = 'O'
else:
    p2 = 'X'


def click(r,c):
    global xos
    global turn
    turn = 'X'
    if p1 == 'X':
        btns[r][c].config(text='X', state=DISABLED)
        xos[r][c] = 'X'
        turn = 'O'
        if not checkwin(xos, 'X'):
            pcmove = pc()
            if pcmove:
                a, b = pcmove[0], pcmove[1]
                btns[a][b].config(text='O', state=DISABLED)
                xos[a][b] = 'O'
    elif p1 == 'O':
        btns[r][c].config(text='O', state=DISABLED)
        xos[r][c] = 'O'
        turn = 'X'
        pcmove = pc()
        a, b = pcmove[0], pcmove[1]
        btns[a][b].config(text='X', state=DISABLED)
        xos[a][b] = 'X'
        winner()

    winner()

def pc():
    posmove = []
    for row in range(3):
        for elem in range(3):
            if xos[row][elem] == '':
                posmove.append([row, elem])
    if posmove == []:
        return
    else:
        for char in ['X', 'O']:
            for i in posmove:
                xoscopy = copy.deepcopy(xos)
                xoscopy[i[0]][i[1]] = char
                if checkwin(xoscopy, char):
                    return i
        for i in posmove:
            if i == [1,1]:
                return i
        ugol = []
        for i in posmove:
            if i in [[0,0],[0,2],[2,0],[2,2]]:
                ugol.append(i)
        if ugol != []:
            move = random.randint(0, len(ugol)-1)
            return ugol[move]
        storona = []
        for i in posmove:
            if i in [[0,1],[1,0],[1,2],[2,1]]:
                storona.append(i)
        if storona != []:
            move = random.randint(0, len(storona)-1)
            return storona[move]

def checkwin(board, symv):
    for row in board:
        if row[0] == row[1] == row[2] == symv:
            return True
    if board[0][0] == board[1][0] == board[2][0] == symv or board[0][1] == board[1][1] == board[2][1] == symv or board[0][2] == board[1][2] == board[2][2] == symv:
        return True
    if board[0][0] == board[1][1] == board[2][2] == symv or board[0][2] == board[1][1] == board[2][0] == symv:
        return True
    else:
        return False

def winner():
    if checkwin(xos, 'X'):
        for i in range(3):
            for j in range(3):
                btns[i][j].config(state=DISABLED)
        player.config(text='Победили крестики!', pady=50)

    if checkwin(xos, 'O'):
        for i in range(3):
            for j in range(3):
                btns[i][j].config(state=DISABLED)
        player.config(text='Победили нолики!', pady=50)

    k=0
    for i in xos:
        if not '' in i:
            k+=1
            if k == 3:
                if not checkwin(xos, 'X') and not checkwin(xos, 'O'):
                    player.config(text='Ничья!', pady=50)



root = Tk()
root.title('Крестики-нолики')
root.geometry('480x640')
root.resizable(False, False)
canvas = Canvas(root)
canvas.pack(anchor='s', expand=True, pady=50)
player = tkinter.Label(canvas, text=f'Вы играете за {p1}', font='Arial 20')
player.pack(anchor='n', fill=X, expand=True)



btns = [
        [0,0,0],
        [0,0,0],
        [0,0,0]]

xos = [
    ['','',''],
    ['','',''],
    ['','','']]

setka = xos


for i in range(3):
    for j in range(3):
        btns[i][j] = Button(root,text='',font='20', height=7,width=16, command=lambda r = i, c = j: click(r,c))
        btns[i][j].place(x=0+160*j,y=0+140*i)

if p2 == 'X':
    pcmove = pc()
    i, j = pcmove[0], pcmove[1]
    btns[i][j].config(text='X', state=DISABLED)
    xos[i][j] = 'X'
    turn = 'O'


root.mainloop()