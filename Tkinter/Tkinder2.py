import tkinter

window = tkinter.Tk()

window.geometry('600x400')

window.title('Ventana 1')

window.iconbitmap('icono.ico')

boton1 = tkinter.Button(window, text='Clic aquí')

boton1.pack()

window.mainloop()
