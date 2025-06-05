
# ! Bibliotecas
import socket
from Logs import log_critical, log_error, log_info, log_warning, log_debug

# TODO: CONFIGURACIONES DE CONEXIÓN

HOST = 'localhost'  # Dirección IP del servidor
PORT = 8080

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        log_info("Conexión establecida con el servidor.")
        print("Conexión establecida con el servidor.")

        while True:
            data = s.recv(1024)
            print(f"Datos recibidos: {data.decode()}")
            log_info(f"Datos recibidos: {data.decode()}")
            msg = input("> ")
            if msg.lower() == 'exit':
                    log_info("Cerrando conexión.")
                    print("Cerrando conexión.")
                    break
            s.sendall(msg.encode())
            log_info(f"Mensaje enviado: {msg}")

    except Exception as e:
        log_error(f"Error en el cliente: {e}")
        print(f"Error en el cliente: {e}")
