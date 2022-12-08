import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.geometry('600x400')
window.title('Coltis')
window.iconbitmap('icono.ico')


entrada_var1 = tkinter.StringVar(value='Valor por default')
entrada1 = tkinter.Entry(window, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)


etiqueta1 = tkinter.Label(window, text='Aquí se mostrará el contenidoo')
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():
    print(entrada1.get())
    etiqueta1.config(text=entrada_var1.get())

    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje Informativo', mensaje1 + ' Informativo')
        messagebox.showerror('Mensaje de Error', mensaje1 + ' Error')
        messagebox.showwarning('Mensaje de Alerta', mensaje1 + ' Alerta')


boton1 = tkinter.Button(window, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

window.mainloop()
