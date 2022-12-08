import tkinter

ventana = tkinter.Tk()

ventana.geometry('600x400')

ventana.title('Hola Estudiantes de Coltis')

ventana.iconbitmap('icono.ico')

def evento_click():
    boton1.config(text='Botón presionado')
    print('Ejecución del evento_click')
    
    boton2 = tkinter.Button(ventana, text='Nuevo botón')
    boton2.pack()


boton1 = tkinter.Button(ventana, text='Dar click', command=evento_click)

boton1.pack()

ventana.mainloop()