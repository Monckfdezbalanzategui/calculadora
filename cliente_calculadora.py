import socket

host_ip="192.168.56.1"

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.connect((host_ip,0))
except:
    print("Ha habido un problema")
    client_socket.close()
while True:
    print("Qué quieres hacer, pulsa 0 para salir, 1 para sumar, o 2 para multiplicar")
    mensaje_cliente=input(int())
    mensaje_cliente=mensaje_cliente.encode()
    client_socket.send(mensaje_cliente)
    client_socket.recv(1024).decode()
    print("Escribe tres números,separador por comas, para realizar la operación: ")
    numeros=(input(int())
    numeros=list(numeros)
    numeros=numeros.encode()
    client_socket.send(numeros).encode()
    client_socket.recv(1024).decode()

client_socket.close()
