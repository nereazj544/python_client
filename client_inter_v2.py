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


# TODO: Configuración de CustomTkinter
customtkinter.set_appearance_mode("System")  # "System" (pilla la configuracion por defecto del sistema), "Dark", "Light" (modo de apariencia)
customtkinter.set_default_color_theme("dark-blue")  # blue (defecto), dark-blue, green

# TODO: Area de mensaje
app = customtkinter.CTk()  # Crear la ventana principal || a 'app' se le puede llamar como quieras, pero normalmente se llama 'root'

text = customtkinter.CTkTextbox(master=app, width=298, height=100)  # Crear un cuadro de texto
text.place(relx=0.5, rely=0.59, anchor=tkinter.CENTER)  # Colocar el cuadro de texto en el centro de la ventana

text_info = customtkinter.CTkTextbox(master=app, width=298, height=100)  # Crear otro cuadro de texto para información
text_info.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)  # Colocar el cuadro de texto en la parte inferior de la ventana
text_info.insert(tkinter.END, "Información del cliente\n")  # Insertar texto en el cuadro de texto de información



app.geometry("850x650")  # Establecer el tamaño de la ventana
app.title("Interfaz de Usuario con CustomTkinter")  # Título de la ventana


# TODO: Función para conectar al servidor

def connect():
    global client_socket, ACTIVO
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crear un socket TCP/IP
        client_socket.connect((HOST, PORT))  # Conectar al servidor
        ACTIVO = True  # Cambiar el estado a activo
        text_info.insert(tkinter.END, "Conexión establecida con el servidor.\n")  # Insertar texto en el cuadro de texto
        log_info("Conexión establecida con el servidor")  # Registrar la conexión

        thread = threading.Thread(target=recibir_mensaje, daemon=True)
        thread.start()  # Iniciar un hilo para recibir mensajes del servidor


    except socket.error as e:
        text_info.insert(tkinter.END, f"Error al conectar: {e}\n")
        log_error(f"Error al conectar: {e}")


def enviar_mensaje():
    global client_socket, ACTIVO
    if not ACTIVO:
        text_info.insert(tkinter.END, "Error: No hay conexión activa.\n")
        log_warning("Intento de enviar mensaje sin conexión activa.")
        return
    msg = text.get("1.0", tkinter.END).strip()  # Obtener el mensaje del cuadro de texto
    if msg.lower() == "exit":
        text_info.insert(tkinter.END, "Cerrando conexión...\n")
        log_info("Cerrando conexión...")
        client_socket.close()
        ACTIVO = False
        return
    
    try:
        client_socket.sendall(msg.encode())  # Enviar el mensaje al servidor
        text.insert(tkinter.END, f"Mensaje enviado: {msg}\n")  # Insertar el mensaje enviado en el cuadro de texto
        log_info(f"Mensaje enviado: {msg}")  # Registrar el mensaje enviado
    except socket.error as e:
        text_info.insert(tkinter.END, f"Error al enviar mensaje: {e}\n")
        log_error(f"Error al enviar mensaje: {e}")

def recibir_mensaje():
    global client_socket, ACTIVO
    while ACTIVO:  # Mientras el cliente esté activo
        try:
            data = client_socket.recv(1024)  # Recibir datos del servidor
            if not data:  # Si no hay datos, salir del bucle
                text_info.insert(tkinter.END, "Conexión cerrada por el servidor.\n")
                log_info("Conexión cerrada por el servidor.")
                break
            text_info.insert(tkinter.END, f"Datos recibidos: {data.decode()}\n")  # Insertar los datos recibidos en el cuadro de texto
            log_info(f"Datos recibidos: {data.decode()}")  # Registrar los datos recibidos
        except socket.error as e:
            text_info.insert(tkinter.END, f"Error al recibir datos: {e}\n")
            log_error(f"Error al recibir datos: {e}")
            break

def button_function():
    global client_socket, ACTIVO  # Acceder a las variables globales
    if ACTIVO:  # Si ya hay una conexión activa
        text_info.insert(tkinter.END, "Ya hay una conexión activa.\n")  # Insertar texto en el cuadro de texto
        log_warning("Intento de conectar cuando ya hay una conexión activa.")  # Registrar la advertencia
        return
    connect()  # Llamar a la función para conectar al servidor


def button_send():
    global client_socket, ACTIVO  # Acceder a las variables globales
    if not ACTIVO:  # Si el cliente no está activo, mostrar un mensaje de error
        text_info.insert(tkinter.END, "Error: No hay conexión activa con el servidor.\n")  # Insertar texto en el cuadro de texto
        log_error("Error: No hay conexión activa con el servidor.")  # Registrar el error
        return
    messagebox.showinfo("Información", "Mensaje enviado al servidor")  # Mostrar un mensaje de información
    enviar_mensaje()  # Llamar a la función para enviar un mensaje al servidor





































button_cnt = customtkinter.CTkButton(master=app, text="conectar al servidor", command=button_function)  # Crear un botón
button_cnt.place(relx=0.23, rely=0.8, anchor=tkinter.CENTER)  # Colocar el botón en el centro de la ventana, el ultimo parámetro 'anchor' es para centrar el botón en la ventana
button_env = customtkinter.CTkButton(master=app, text="enviar mensaje", command=button_send)  # Crear otro botón
button_env.place(relx=0.77, rely=0.8, anchor=tkinter.CENTER)  # Colocar el botón en el centro de la ventana






# TODO: 
app.mainloop()  # Iniciar el bucle principal de la aplicación
log_info("Interfaz de usuario iniciada")  # Registrar el inicio de la interfaz
log_debug("Interfaz de usuario en ejecución")  # Registrar que la interfaz está en ejecución

