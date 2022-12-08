import tkinter 

ventana = tkinter.Tk()
ventana.geometry('600x400')
ventana.title('Coltis')
ventana.iconbitmap('icono.ico')


ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)


def evento1():
    boton1.config(text='Botón 1 presionado')

def evento2():
    boton2.config(text='Botón 2 presionado')

def evento4():
    boton4.config(text='Botón 4 presionado', fg='blue', relief=tkinter.GROOVE, bg='yellow')

boton1 = tkinter.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE')


boton2 = tkinter.Button(ventana, text='Botón 2', command=evento2)
boton2.grid(row=1,column=0, sticky='NSWE')


boton3 = tkinter.Button(ventana, text='Botón 3')
boton3.grid(row=0, column=1, sticky='NSWE')


boton4= tkinter.Button(ventana,text='Botón 4', command=evento4)
boton4.grid(row=1, column=1, sticky='NSWE')

ventana.mainloop()
