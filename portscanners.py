import socket

ip = input("Ingrese la direccion ip para escanear: ")

for puerto in range(1, 65535):

    sock = socket.socket(socket.AF_INET, socket.SOCK)
    sock.settimeout(5)

    result = sock.connect_ex((ip, puerto))

    if result == 0:
        print('Puerto Abierto: ' + str(puerto))
        sock.close()
    else:
        print('Puerto Cerrado: ' + str(puerto))