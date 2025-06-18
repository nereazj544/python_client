import tkinter
import customtkinter
import socket
import threading
from Logs_Interfaz import log_critical, log_error, log_info, log_warning, log_debug

HOST = "localhost"  # Dirección del servidor
PORT = 8083  # Puerto del servidor



customtkinter.set_appearance_mode("System")  # "System", "Dark", "Light" (modo de apariencia)
customtkinter.set_default_color_theme("blue")  # blue, dark-blue, green, dark-green, light-blue, dark-light-blue


app = customtkinter.CTk()  # Crear la ventana principal || a 'app' se le puede llamar como quieras, pero normalmente se llama 'root'
app.geometry("800x600")  # Establecer el tamaño de la ventana




def button_function():
    print("Botón presionado")  # Acción al presionar el botón   
    customtkinter.CTkMessageBox.show_info("Información", "Conectando al servidor...")  # Mostrar un mensaje de información


def button_send():
    print("Mensaje enviado")  # Acción al presionar el botón
    customtkinter.CTkMessageBox.show_info("Información", "Mensaje enviado al servidor")  # Mostrar un mensaje de información






text = customtkinter.CTkTextbox(master=app, width=660, height=353)  # Crear un cuadro de texto
text.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)  # Colocar el cuadro de texto en el centro de la ventana

button_cnt = customtkinter.CTkButton(master=app, text="conectar al servidor", command=button_function)  # Crear un botón
button_cnt.place(relx=0.23, rely=0.8, anchor=tkinter.CENTER)  # Colocar el botón en el centro de la ventana, el ultimo parámetro 'anchor' es para centrar el botón en la ventana
button_env = customtkinter.CTkButton(master=app, text="enviar mensaje", command=button_send)  # Crear otro botón
button_env.place(relx=0.77, rely=0.8, anchor=tkinter.CENTER)  # Colocar el botón en el centro de la ventana
app.title("Interfaz de Usuario con CustomTkinter")  # Título de la ventana
app.mainloop()  # Iniciar el bucle principal de la aplicación