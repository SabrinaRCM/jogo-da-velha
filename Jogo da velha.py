from tkinter import *
from tkinter import messagebox
from tkinter import ttk


jogador = 1
j1 = [] #armazena os cliques do jogador1 em um vetor
j2 = [] #armazena os cliques do jogador2 em um vetor

root = Tk()  #define a janela principal
root.title('Vez do jogador 1')  #define o titulo da janela
# estilo=ttk.Style()                Estilo opcional
# estilo.theme_use('clam')

titulo = ttk.Label(root, text='Jogo da Velha')  #adiciona uma label com titulo 
titulo.grid(row=0, column=1, ipady='10', )   #define a posição da label no grid


btn1 = ttk.Button(root, text='')  #adiciona um botão
btn1.grid(row=1, column=0, sticky='snew', ipadx='10', ipady='10')  #define a posição do botão no grid
btn1.config(command=lambda: clique(1))

btn2 = ttk.Button(root, text='')
btn2.grid(row=1, column=1, sticky='snew', ipadx='10', ipady='10')
btn2.config(command=lambda: clique(2))

btn3 = ttk.Button(root, text='')
btn3.grid(row=1, column=2, sticky='snew', ipadx='10', ipady='10')
btn3.config(command=lambda: clique(3))

btn4 = ttk.Button(root, text='')
btn4.grid(row=2, column=0, sticky='snew', ipadx='10', ipady='10')
btn4.config(command=lambda: clique(4))

btn5 = ttk.Button(root, text='')
btn5.grid(row=2, column=1, sticky='snew', ipadx='10', ipady='10')
btn5.config(command=lambda: clique(5))

btn6 = ttk.Button(root, text='')
btn6.grid(row=2, column=2, sticky='snew', ipadx='10', ipady='10')
btn6.config(command=lambda: clique(6))

btn7 = ttk.Button(root, text='')
btn7.grid(row=3, column=0, sticky='snew', ipadx='10', ipady='10')
btn7.config(command=lambda: clique(7))

btn8 = ttk.Button(root, text='')
btn8.grid(row=3, column=1, sticky='snew', ipadx='10', ipady='10')
btn8.config(command=lambda: clique(8))

btn9 = ttk.Button(root, text='')
btn9.grid(row=3, column=2, sticky='snew', ipadx='10', ipady='10')
btn9.config(command=lambda: clique(9))


def clique(botao):  #define qual botão esta sendo clicado
    global jogador
    global j1
    global j2
    if jogador == 1:  #alterna os turnos entre jogador 1 e jogador 2
        mudarSimbolo(botao, 'X')
        j1.append(botao)
        root.title('Vez do jogador 2')
        jogador = 2
        print("Jogador 1: ", j1)
    elif jogador == 2:
        mudarSimbolo(botao, 'O')
        j2.append(botao)
        root.title('Vez do jogador 1')
        jogador = 1
        print("Jogador 2: ", j2)
    vencedor() #checa a cada turno se algum jogador ja venceu
        


def mudarSimbolo(botao, simbolo): #alterna os simbolos entre os turnos para jogador 1 e jogador 2
    if botao == 1:
        btn1.config(text=simbolo)
        btn1.state(['disabled'])
    elif botao == 2:
        btn2.config(text=simbolo)
        btn2.state(['disabled'])
    elif botao == 3:
        btn3.config(text=simbolo)
        btn3.state(['disabled'])
    elif botao == 4:
        btn4.config(text=simbolo)
        btn4.state(['disabled'])
    elif botao == 5:
        btn5.config(text=simbolo)
        btn5.state(['disabled'])
    elif botao == 6:
        btn6.config(text=simbolo)
        btn6.state(['disabled'])
    elif botao == 7:
        btn7.config(text=simbolo)
        btn7.state(['disabled'])
    elif botao == 8:
        btn8.config(text=simbolo)
        btn8.state(['disabled'])
    elif botao == 9:
        btn9.config(text=simbolo)
        btn9.state(['disabled'])


def vencedor():     #checa quem venceu a partida
    vencedor = 0
    if 1 in j1 and 2 in j1 and 3 in j1:
        vencedor = 1
    if 1 in j2 and 2 in j2 and 3 in j2:
        vencedor = 2

    if 4 in j1 and 5 in j1 and 6 in j1:
        vencedor = 1
    if 4 in j2 and 5 in j2 and 6 in j2:
        vencedor = 2

    if 7 in j1 and 8 in j1 and 9 in j1:
        vencedor = 1
    if 7 in j2 and 8 in j2 and 9 in j2:
        vencedor = 2

    if 1 in j1 and 4 in j1 and 7 in j1:
        vencedor = 1
    if 1 in j2 and 4 in j2 and 7 in j2:
        vencedor = 2

    if 2 in j1 and 5 in j1 and 8 in j1:
        vencedor = 1
    if 2 in j2 and 5 in j2 and 8 in j2:
        vencedor = 2

    if 3 in j1 and 6 in j1 and 9 in j1:
        vencedor = 1
    if 3 in j2 and 6 in j2 and 9 in j2:
        vencedor = 2

    if 1 in j1 and 5 in j1 and 9 in j1:
        vencedor = 1
    if 1 in j2 and 5 in j2 and 9 in j2:
        vencedor = 2

    if 3 in j1 and 5 in j1 and 7 in j1:
        vencedor = 1
    if 3 in j2 and 5 in j2 and 7 in j2:
        vencedor = 2

    if vencedor == 1:  #mostra uma mensagem na tela com o vencedor da partida
        messagebox.showinfo(title='Vencedor!', message='Jogador 1 venceu!!!')

    if vencedor == 2:
        messagebox.showinfo(title='Vencedor!', message='Jogador 2 venceu!!!')

    if len(j1 + j2) == 9 and vencedor != 1 and vencedor != 2: 
        messagebox.showinfo(title='Empate!', message='Ih! Deu velha!')
        
    if vencedor == 1 or vencedor == 2 or len(j1 + j2) == 9:
        j1.clear()
        j2.clear()
        btn1.config(text='')
        btn1.state(['!disabled'])
        btn2.config(text='')
        btn2.state(['!disabled'])
        btn3.config(text='')
        btn3.state(['!disabled'])
        btn4.config(text='')
        btn4.state(['!disabled'])
        btn5.config(text='')
        btn5.state(['!disabled'])
        btn6.config(text='')
        btn6.state(['!disabled'])
        btn7.config(text='')
        btn7.state(['!disabled'])
        btn6.config(text='')
        btn6.state(['!disabled'])
        btn7.config(text='')
        btn7.state(['!disabled'])
        btn8.config(text='')
        btn8.state(['!disabled'])
        btn9.config(text='')
        btn9.state(['!disabled'])
      
        

root.mainloop()
