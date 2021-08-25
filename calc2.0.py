from tkinter import *
import tkinter as tk

def calculo(numero, numero2):
    resultado = numero + numero2
    print (resultado)

calculo()




#Operações
def somar():
    global Oresultado
    Oresultado = int(numero1.get())+ int(numero2.get())
    return (Oresultado)

def subtrair():
    global Oresultado
    Oresultado = int(numero1.get()) - int(numero2.get())
    return (Oresultado)

def mult():
    global Oresultado
    Oresultado = int(numero1.get()) * int(numero2.get())
    return (Oresultado)
def dividir():
    global Oresultado
    Oresultado = int(numero1.get()) / int(numero2.get())
    return (Oresultado)

#printar resultado
def resultado():

    print(Oresultado)

app = tk.Tk()
app.title("Calculadora")
app.geometry("500x300")
app.configure(background= "#dd7")

Label(app, text="Número 1", background="#dde", foreground="#009", anchor=W).place(x=10,y=10,width=50,height=20)
numero1 = Entry(app)
numero1.place(x=80,y=10,width=100,height=20) 

Label(app, text="Número 2", background="#dde", foreground="#009", anchor=W).place(x=10,y=40,width=50,height=20)
numero2 = Entry(app)
numero2.place(x=80,y=40,width=100,height=20) 



botaoSomar = tk.Button(app, text='+', command=somar)
botaoSomar.pack()
botaoSomar.place(x=300,y=10,width=50,height=50)

botaoSubtrair = tk.Button(app, text='-', command=subtrair)
botaoSubtrair.pack()
botaoSubtrair.place(x=300,y=60,width=50,height=50)

botaoMultiplicar = tk.Button(app, text= 'x', command=mult)
botaoMultiplicar.pack()
botaoMultiplicar.place(x=300,y=110,width=50,height=50)

botaoDividir = tk.Button(app, text= '/', command=dividir)
botaoDividir.pack()
botaoDividir.place(x=300,y=160,width=50,height=50)

botaoResultado = tk.Button(app, text= 'Calcular', command=resultado)
botaoResultado.pack()
botaoResultado.place(x=150,y=250,width=100,height=50)

app.mainloop()
