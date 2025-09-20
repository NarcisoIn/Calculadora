from tkinter import *

#Creacion de ventana Principal
ventana = Tk()
ventana.title("Calculadora") #Titulo de la ventana
#Cambiar icono de la app
ventana.iconbitmap('C:/Users/guzma/OneDrive/Documentos/Cursos/Python Aplicado 5 Proyectos Reales de Principio a Fin/Proyecto 1 Calculadora/calculadora.ico')

#tamaño dinamico de filas y columnas
for i in range(5):
    ventana.grid_rowconfigure(i, weight = 1)

for i in range(4):
    ventana.grid_columnconfigure(i, weight = 1)

#Cuadro de texto: Visor

visorTexto = StringVar()
visor = Entry(ventana, textvariable= visorTexto,
               font = ("Helvetica", 30, "bold"),
                bd = 10,
                insertwidth = 4,
                width = 14,
                borderwidth = 2,
                justify = 'right',
                relief = "sunken",
                bg = "#e8f0fe", 
                fg = "#333333")

visor.grid(row = 0, column = 0, columnspan = 4, sticky = "ew", padx= 10, pady = 10)

#Variable de control
mostrandoResultado = False

#Funcion Presionar Tecla
def presionar(tecla):
        global mostrandoResultado
        if tecla == "C":  # Borrar todo
            visorTexto.set("")
            mostrandoResultado = False
            return

        if mostrandoResultado:  
            if tecla in "+-*/":#Si se presiona un operador, continuar con el resultado
                visorTexto.set(visorTexto.get() + tecla)
            else:#Si se presiona un número/punto, iniciar nueva operación
                visorTexto.set(tecla)
            mostrandoResultado = False
        else:
            visorTexto.set(visorTexto.get() + tecla)

#Funcion Tecla "="
def igual():
        calcular()

#Funcion Calcular
def calcular():
    global mostrandoResultado
    try:
        resultado = eval(visorTexto.get())
        #Verifica si el resultado es un numero entero para eliminar los decimales de sobra
        if resultado == int(resultado):
            resultado = int(resultado)
        visorTexto.set(str(resultado))
        mostrandoResultado = True
    except:
        visorTexto.set("Error Sintáctico")
        mostrandoResultado = True

#Tupla de botones y sus pocisiones
botones = [
    ("7", 1, 0, "#A4C4FA", "black"), ("8", 1, 1, "#A4C4FA", "black"), ("9", 1, 2, "#A4C4FA", "black"), ("/", 1, 3, "#907BC7", "white" ),
    ("4", 2, 0, "#A4C4FA", "black"), ("5", 2, 1, "#A4C4FA", "black"), ("6", 2, 2, "#A4C4FA", "black"), ("*", 2, 3, "#907BC7", "white"),
    ("1", 3, 0, "#A4C4FA", "black"), ("2", 3, 1, "#A4C4FA", "black"), ("3", 3, 2, "#A4C4FA", "black"), ("-", 3, 3, "#907BC7", "white"),
    ("0", 4, 0, "#A4C4FA", "black"), (".", 4, 1, "#075396", "white"), ("C", 4, 2, "#075396", "white"), ("+", 4, 3, "#907BC7", "white")]

#Creacion de botones dinamicamente
for texto, fila, columna, color, colorText in botones:
    Button(ventana, text = texto, bg = color,
        font = ("Helvetica", 20, "bold"), command = lambda t=texto: presionar(t),
        bd = 1, relief = "raised",
        activebackground= "grey", activeforeground= "#ffffff",
         fg = colorText,
        padx = 20, pady = 20).grid(row = fila, column = columna, sticky = "nsew", padx = 2, pady = 2)

#Boton Igual
botonIgual = Button(ventana, text = "=", bd = 1, relief = "raised",
                padx = 20, pady = 20,
                font = ("Helvetica", 40, "bold"), command = lambda: igual(),
                fg = "black", bg = "#BAD7AC", activebackground= "grey", 
                activeforeground= "#ffffff",)
botonIgual.grid(row = 5,
                column = 0,
                columnspan = 4,
                sticky = "ew",
                padx = 2, pady = 2)

#Ejecucion de aplicacion
ventana.mainloop()
