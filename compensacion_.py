import tkinter as tk
from tkinter import messagebox
from tkinter import *

# Variables
usuario = None
clave = None
saldo_usuario = None
cantidad = None
intentos = None
limite_maximo = 5000
saldo_anterior = None

def crear_login():
    global login, usuario, clave, saldo_usuario, cantidad, intentos
    login = tk.Tk()
    login.title("Caja Fuerte Virtual 🔒💪🏾")
    login.geometry("500x280")
    marco = tk.Frame(login)
    marco.place(relwidth=1, relheight=1)
    marco["bg"] = "#EBEFFF"
    Label(login, text="¡Bienvenido a tu caja fuerte de confianza🔒💪🏾!", bg="#EBEFFF", font=("Time", 14)).place(x=40, y=10)
    #img = tk.PhotoImage(file="C:\\Users\\presi\\Desktop\\compensacion\\klipartz.com.png")
    #lbl_img = tk.Label(login, image=img)
    #lbl_img.pack()

    login.iconbitmap("image.ico")
    usuario = tk.StringVar()
    clave = tk.StringVar()
    saldo_usuario = tk.DoubleVar()
    cantidad = tk.DoubleVar()
    intentos = 3
    saldo_usuario.set(4500)


    tk.Label(login, text="Usuario:", bg="#EBEFFF", font=("poppins", 12)).place(x=15, y=80)
    tk.Entry(login, textvariable=usuario, border="5px").place(x=128, y=85)
    tk.Label(login, text="Contraseña:", bg="#EBEFFF", font=("poppins", 12, )).place(x=18, y=130)
    tk.Entry(login, textvariable=clave, show='*', border="5px").place(x=128, y=135)
    tk.Button(login, text="Iniciar Sesión", command=validar_usuario, font=("poppins", 10), bg="#656ED3", fg="white", border="5px" ).place(x=140, y=180)

def validar_usuario():
    global intentos
    usuario_definido = "Maxcervantes"
    contraseña_definida = "1083"
    if usuario_definido == usuario.get() and contraseña_definida == clave.get():
        crear_menu_opciones()
    else:
        intentos -= 1
        messagebox.showerror("Inicio de Sesión Fallido", f"Nombre de usuario o contraseña inválidos. Intentos restantes: {intentos}")
        if intentos == 0:
            messagebox.showerror("Error", "Has excedido el número máximo de intentos. La caja fuerte se bloqueará.")
            bloquear_caja_fuerte()

def crear_menu_opciones():
    global menu
    menu = tk.Tk()
    menu.title("¡Opciones a realizar🔒💪🏾!")
    menu.iconbitmap("image.ico")
    menu.geometry("500x300")
    marco = tk.Frame(menu)
    marco.place(relwidth=1, relheight=1)
    marco["bg"] = "#EBEFFF"

    tk.Button(menu, text="Depositar", command=depositar, font=("poppins", 10), bg="#656ED3", fg="white", border="5px").place(x=30, y=60)
    tk.Button(menu, text="Retirar", command=retirar, font=("poppins", 10), bg="#656ED3", fg="white", border="5px").place(x=30, y=120)
    tk.Button(menu, text="Consultar Saldo", command=consultar_saldo, font=("poppins", 10), bg="#656ED3", fg="white", border="5px").place(x=150, y=60)
    tk.Button(menu, text="Salir", command=cerrar_caja_fuerte, font=("poppins", 10), bg="#656ED3", fg="white", border="5px").place(x=150, y=120)
    login.iconify()

def depositar():
    global deposito_menu, saldo_anterior
    deposito_menu = tk.Tk()
    deposito_menu.title("Depositar")
    deposito_menu.geometry("300x200")
    marco = tk.Frame(deposito_menu)
    marco.place(relwidth=1, relheight=1)
    marco["bg"] = "#EBEFFF"
    tk.Label(deposito_menu, text="Saldo Disponible", bg="#EBEFFF", font=("poppins", 12)).place(x=50, y=40)
    label = tk.Label(deposito_menu, text=f"${saldo_usuario.get()},", bg="#EBEFFF", font=("poppins", 12))
    label.place(x=200, y=40)
    entry = tk.Entry(deposito_menu, textvariable=cantidad, border="5px")
    entry.place(x=150, y=80)
    tk.Button(deposito_menu, text="Depositar", font=("poppins", 10), bg="#656ED3", fg="white", border="5px", command=lambda: [realizar_deposito(entry.get()), actualizar_etiqueta(label)]).place(x=50, y=80)
    tk.Button(deposito_menu, text="Volver", font=("poppins", 10), bg="#656ED3", fg="white", border="5px", command=lambda: volver_al_menu(deposito_menu)).place(x=200, y=150)
    menu.iconify()
    saldo_anterior = saldo_usuario.get()

def retirar():
    global retirar_menu, saldo_anterior
    retirar_menu = tk.Tk()
    retirar_menu.title("Retirar")
    retirar_menu.geometry("300x200")
    marco = tk.Frame(retirar_menu)
    marco.place(relwidth=1, relheight=1)
    marco["bg"] = "#EBEFFF"
    tk.Label(retirar_menu, text="Saldo Disponible", bg="#EBEFFF", font=("poppins", 12)).place(x=50, y=40)
    label = tk.Label(retirar_menu, text=f"${saldo_usuario.get()}", bg="#EBEFFF", font=("poppins", 12))
    label.place(x=200, y=40)
    entry = tk.Entry(retirar_menu, textvariable=cantidad, border="5px")
    entry.place(x=150, y=80)
    tk.Button(retirar_menu, text="Retirar",font=("poppins", 10), bg="#656ED3", fg="white", border="5px", command=lambda: [realizar_retiro(entry.get()), actualizar_etiqueta(label)]).place(x=50, y=80)
    tk.Button(retirar_menu, text="Volver",font=("poppins", 10), bg="#656ED3", fg="white", border="5px", command=lambda: volver_al_menu(retirar_menu)).place(x=200, y=150)
    menu.iconify()
    saldo_anterior = saldo_usuario.get()

def consultar_saldo():
    global consultar_saldo_menu
    consultar_saldo_menu = tk.Tk()
    consultar_saldo_menu.title("Consultar Saldo")
    consultar_saldo_menu.geometry("300x200")
    marco = tk.Frame(consultar_saldo_menu)
    marco.place(relwidth=1, relheight=1)
    marco["bg"] = "#EBEFFF"
    tk.Label(consultar_saldo_menu, text="Saldo Actual",bg="#EBEFFF", font=("poppins", 12)).place(x=50, y=80)
    label = tk.Label(consultar_saldo_menu, text=f"${saldo_usuario.get()}",bg="#EBEFFF", font=("poppins", 12))
    label.place(x=200, y=80)
    tk.Button(consultar_saldo_menu, text="Volver",font=("poppins", 10), bg="#656ED3", fg="white", border="5px", command=lambda: volver_al_menu(consultar_saldo_menu)).place(x=200, y=150)
    menu.iconify()

def realizar_deposito(monto):
    global saldo_usuario
    total = saldo_usuario.get()
    if total + float(monto) > limite_maximo:
        espacio_restante = limite_maximo - total
        messagebox.showerror("Error", f"No hay suficiente espacio en la caja. Operación cancelada. Te quedan {espacio_restante} disponibles. Puedes agregar esa cantidad o menos de esa cifra")
        saldo_usuario.set(saldo_anterior)
    else:
        total += float(monto)
        saldo_usuario.set(round(total, 2))
        messagebox.showinfo("Éxito", f"Depósito realizado. Nuevo saldo: ${saldo_usuario.get()}")

def realizar_retiro(monto):
    global saldo_usuario
    if saldo_usuario.get() - float(monto) < 0:
        messagebox.showerror("Error", "Saldo insuficiente")
    else:
        total = saldo_usuario.get()
        total -= float(monto)
        saldo_usuario.set(round(total, 2))
        messagebox.showinfo("Éxito", f"Retiro realizado. Nuevo saldo: ${saldo_usuario.get()}")

def volver_al_login():
    menu.iconify()
    login.deiconify()

def volver_al_menu(sub_menu):
    sub_menu.iconify()
    menu.deiconify()

def actualizar_etiqueta(etiqueta):
    etiqueta.config(text=f"${saldo_usuario.get()}")

def bloquear_caja_fuerte():
    login.destroy()

def cerrar_caja_fuerte():
    menu.destroy()
    login.destroy()

# Crear ventana de inicio de sesión
crear_login()
tk.mainloop()