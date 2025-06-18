import tkinter
from tkinter import messagebox
import customtkinter 
import socket
import threading
from Logs_Interfaz import log_critical, log_error, log_info, log_warning, log_debug

HOST = "localhost"  # Dirección del servidor
PORT = 8083  # Puerto del servidor

# TODO: Configuración GLOBAL socket del cliente
client_socket = None  # Variable para el socket del cliente, se inicializa como None
ACTIVO = False  # Variable para indicar si el cliente está activo, se inicializa como False




customtkinter.set_appearance_mode("System")  # "System", "Dark", "Light" (modo de apariencia)
customtkinter.set_default_color_theme("dark-blue")  # blue (defecto), dark-blue, green


app = customtkinter.CTk()  # Crear la ventana principal || a 'app' se le puede llamar como quieras, pero normalmente se llama 'root'
app.geometry("800x600")  # Establecer el tamaño de la ventana




def button_function():
    print("Botón presionado: CONECTAR")  # Acción al presionar el botón
    messagebox.showinfo("Información", "Conectando al servidor...")  # Mostrar un mensaje de información
    connect()  # Llamar a la función de conexión al servidor


def button_send():
    print("Botón presionado: ENVIAR MENSAJE")  # Acción al presionar el botón
    messagebox.showinfo("Información", "Mensaje enviado al servidor")  # Mostrar un mensaje de información


def recibir():
    global client_socket, ACTIVO  # Acceder a las variables globales
    while ACTIVO:  # Mientras el cliente esté activo
        try:
            data = client_socket.recv(1024)  # Recibir datos del servidor
            if not data:  # Si no hay datos, salir del bucle
                break
            text.insert(tkinter.END, f"Datos recibidos: {data.decode()}\n")  # Insertar los datos recibidos en el cuadro de texto
            log_info(f"Datos recibidos: {data.decode()}")  # Registrar los datos recibidos
        except Exception as e:
            text.insert(tkinter.END, f"Error al recibir datos: {e}\n")
            log_error(f"Error al recibir datos: {e}")  # Registrar el error
            break


def connect():
    global client_socket, ACTIVO  # Acceder a las variables globales
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crear un socket
        client_socket.connect((HOST, PORT))  # Conectar al servidor
        ACTIVO = True  # Cambiar el estado a activo
        log_info("Conexión establecida con el servidor")  # Registrar la conexión exitosa
        text.insert(tkinter.END, "Conectado al servidor\n")  # Insertar texto en el cuadro de texto
        log_info("Conectado al servidor")  # Registrar la conexión exitosa
    except Exception as e:
        text.insert(tkinter.END, f"Error al conectar: {e}\n")
        messagebox.showerror("Error", f"Error al conectar: {e}")
        log_error(f"Error al conectar: {e}")  # Registrar el error






# TODO ==================================================================



# TODO: Area de mensaje
text = customtkinter.CTkTextbox(master=app, width=298, height=353)  # Crear un cuadro de texto
text.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)  # Colocar el cuadro de texto en el centro de la ventana

text_info = customtkinter.CTkTextbox(master=app, width=298, height=100)  # Crear otro cuadro de texto para información
text_info.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)  # Colocar el cuadro de texto en la parte inferior de la ventana
text_info.insert(tkinter.END, "Información del cliente\n")  # Insertar texto en el cuadro de texto de información

button_cnt = customtkinter.CTkButton(master=app, text="conectar al servidor", command=button_function)  # Crear un botón
button_cnt.place(relx=0.23, rely=0.8, anchor=tkinter.CENTER)  # Colocar el botón en el centro de la ventana, el ultimo parámetro 'anchor' es para centrar el botón en la ventana
button_env = customtkinter.CTkButton(master=app, text="enviar mensaje", command=button_send)  # Crear otro botón
button_env.place(relx=0.77, rely=0.8, anchor=tkinter.CENTER)  # Colocar el botón en el centro de la ventana
app.title("Interfaz de Usuario con CustomTkinter")  # Título de la ventana
app.mainloop()  # Iniciar el bucle principal de la aplicación
log_info("Interfaz de usuario iniciada")  # Registrar el inicio de la interfaz
log_debug("Interfaz de usuario en ejecución")  # Registrar que la interfaz está en ejecución