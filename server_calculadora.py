import socket

host_ip="192.168.56.1"
port=8080
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((host_ip,port))
except:
    print("Ha habido un problema")
    server_socket.close()
server_socket.listen(10)
print("Esperando conexión")
conexion, addr_cliente=server_socket.accept()
print("Conexión establecida")
while True:
    mensaje_cliente1=conexion.recv(1024).decode()
    recibido="Hemos recibido la opción"
    conexion.send(recibio).encode()
    mensaje_cliente2=conexion.recv(10240).decode()
    recibido2="Hemos recibido el número"
    conexion.send(recibido2).encode()
    if mensaje_cliente1==1:
        mensaje_cliente2=conexion.recv(1024).decode()
        suma=mensaje_cliente2[0]+mensaje_cliente2[1]+mensaje_cliente2[2]
        conexion.send(suma).encode()
    elif mensaje_cliente1==2:
        mensaje_cliente2=conexion.recv(1024).decode()
        multiplicacion=mensaje_cliente2[0]*mensaje_cliente2[1]*mensaje_cliente2[2]
        conexion.send(multiplicaion).encode()
    elif mensaje_cliente1==0:
        break
    else:
        break
server_socket.close()
