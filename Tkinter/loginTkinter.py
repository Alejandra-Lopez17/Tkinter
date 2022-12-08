import tkinter 
from tkinter import messagebox


window = tkinter.Tk()
window.geometry('300x130')
window.title('Login colstis')
window.iconbitmap('')
window.resizable(0,0)


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


usuario_etiqueta = tkinter.Label(window, text='Usuario:')
usuario_etiqueta.grid(row=0, column=0, sticky=tkinter.E, padx=5, pady=5)
usuario_entrada = tkinter.Entry(window)
usuario_entrada.grid(row=0, column=1, sticky=tkinter.W, padx=5, pady=5)


password_etiqueta = tkinter.Label(window, text='Password:')
password_etiqueta.grid(row=1, column=0, sticky=tkinter.E, padx=5, pady=5)
password_entrada = tkinter.Entry(window, show='*')
password_entrada.grid(row=1, column=1, sticky=tkinter.W, padx=5, pady=5)


def login():
    messagebox.showinfo('Datos Login',
                    f'usuario: {usuario_entrada.get()}, Password: {password_entrada.get()}')

login_boton = tkinter.Button(window, text='Login', command=login)
login_boton.grid(row=3, column=0, columnspan=2)


window.mainloop()