import os
import cx_Oracle
from tkinter import *

os.environ["TNS_ADMIN"]="Z:/Wallet_DB20220530152721"
conexion = cx_Oracle.connect("admin", ".Inacap2022.", "db20220530152721_high")
ventana = Tk()

def menu() -> None:
    print("Menu")
    ventana.title("Proyecto Ventas")
    ventana.geometry("700x500")
    ventana.configure(bg="white")
    ventana.mainloop()
def menuUsuario() -> None:
    ventana1 = Tk()
    ventana1.title("Agregar un usuario")
    ventana1.geometry("700x500")
    ventana1.configure(bg="white")
    etiqueta1 = Label(ventana1, text="Ingrese Usuario", bg="white", fg="black", font=("Arial", 20))
    etiqueta1.place(x=250, y=50)
    usuario1 = Entry(ventana1, width=30)
    usuario1.place(x=250, y=100)
    password1 = Entry(ventana1, width=30)
    password1.place(x=250, y=150)
    boton1 = Button(ventana1, text="Agregar Usuario", command=lambda: addUsuario(usuario1.get(),password1.get()))
    boton1.place(x=250, y=200)
    ventana1.mainloop()
def addUsuario(usuarioAdd,passwordAdd) -> None:
    global conexion
    cursor = conexion.cursor()
    cursor.execute("insert into usuarios(username,clave) values('"+usuarioAdd+"','"+passwordAdd+"')")
    conexion.commit()
    print("Usuario agregado")
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
            menuUsuario()

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
