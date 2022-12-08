import tkinter 

window = tkinter.Tk()
window.geometry('600x400')
window.title('Coltis')
window.iconbitmap('icono.ico')


def evento1():
    boton1.config(text='Botón 1 presionado')

def evento2():
    boton2.config(text='Botón 2 presionado')


boton1 = tkinter.Button(window, text='Botón 1', command=evento1)
boton1.grid(row=0, column=0)

boton2 = tkinter.Button(window, text='Botón 2', command=evento2)
boton2.grid(row=5,column=0)

window.mainloop()
