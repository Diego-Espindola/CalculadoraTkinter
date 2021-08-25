from tkinter import *
import tkinter as tk



#Operações
def somar():
    resultado = int(numero1.get())+ int(numero2.get())
    
    LabelMostraResultado["text"] = resultado

def subtrair():
    resultado = int(numero1.get()) - int(numero2.get())
    LabelMostraResultado["text"] = resultado

def mult():
    resultado = int(numero1.get()) * int(numero2.get())
    LabelMostraResultado["text"] = resultado
    
def dividir():
    resultado = int(numero1.get()) / int(numero2.get())
    LabelMostraResultado["text"] = resultado


#criando 
app = Tk()
app.title("Calculadora")
app.geometry("500x300")
app.configure(background= "#dd7")

#label número 1
Label(app, text="Número 1", background="#dde", foreground="#009").place(x=10,y=10,width=65,height=20)

#Entrada de texto atribuida a variavel numero1

numero1 = Entry(app)
numero1.place(x=80,y=10,width=100,height=20) 

#label número 2

Label(app, text="Número 2", background="#dde", foreground="#009").place(x=10,y=40,width=65,height=20)

#Entrada de texto atribuida a variavel numero2

numero2 = Entry(app)
numero2.place(x=80,y=40,width=100,height=20) 


LabelMostraResultado = Label(app, text="")
LabelMostraResultado.place(x=80,y=150,width=100,height=50)

#botoes

botaoSomar = Button(app, text='+', command=somar)
botaoSomar.pack()
botaoSomar.place(x=300,y=10,width=50,height=50)


botaoSubtrair = Button(app, text='-', command=subtrair)
botaoSubtrair.pack()
botaoSubtrair.place(x=300,y=60,width=50,height=50)

botaoMultiplicar = Button(app, text= 'x', command=mult)
botaoMultiplicar.pack()
botaoMultiplicar.place(x=300,y=110,width=50,height=50)

botaoDividir = Button(app, text= '/', command=dividir)
botaoDividir.pack()
botaoDividir.place(x=300,y=160,width=50,height=50)

app.mainloop()