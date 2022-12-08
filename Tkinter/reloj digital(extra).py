# importando todo el modulo
from tkinter import *
from tkinter.ttk import *

# importando la función strftime a
# recuperar la hora del sistema
from time import strftime

# creando la ventana de tkinter
ventana = Tk()
ventana.title('Clock')

# Esta función se utiliza para
# tiempo de visualización en la etiqueta
def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

# Diseñar el widget de etiqueta para que el reloj
# se verá más atractivo
lbl = Label(ventana, font = ('calibri', 40, 'bold'),
			background = 'purple',
			foreground = 'white')

# Colocando el reloj en el centro
# de la ventana de tkinter
lbl.pack(anchor = 'center')
time()

mainloop()
