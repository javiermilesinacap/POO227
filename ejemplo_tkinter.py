import os
import cx_Oracle
from tkinter import *

os.environ["TNS_ADMIN"]="Z:/Wallet_DB20220530152721"
conexion = cx_Oracle.connect("admin", "CAMBIALACLAVE", "db20220530152721_high")
def menu() -> None:
    print("Menu")
    ventana = Tk()
    ventana.title("Proyecto Ventas")
    ventana.geometry("700x500")
    ventana.configure(bg="white")
    ventana.mainloop()
def validarUsuario() -> None:
    global conexion
    global usuario
    global password
    global mensaje
    print(usuario.get())
    print(password.get())
    cursor = conexion.cursor()
    cursor.execute("select * from usuarios where username='"+usuario.get()+"' and clave='"+password.get()+"'")
    for fila in cursor:
            print("Usuario existe")
            mensaje.setvar("Mensaje", "Usuario existe")
            print(fila)
            menu()

ventana = Tk()
ventana.title("Proyecto Ventas")
ventana.geometry("700x500")
ventana.configure(bg="white")
etiqueta = Label(ventana, text="Ingrese Usuario", bg="white", fg="black", font=("Arial", 20))
etiqueta.place(x=250, y=50)
usuario = Entry(ventana, width=30)
usuario.place(x=250, y=100)
password = Entry(ventana, width=30)
password.place(x=250, y=150)
boton = Button(ventana, text="Ingresar", command=validarUsuario)
boton.place(x=250, y=200)
mensaje = Label(ventana, text="Mensaje", bg="white", fg="red", font=("Arial", 20), textvariable="Mensaje")
mensaje.place(x=250, y=250)


ventana.mainloop()
