"""
AVoIP-Scripts: Script para cambiar las entradas (HDMI o DP) de una controladora LED Novastar.

Este script envía comandos TCP para cambiar entre las entradas HDMI y DisplayPort en una controladora LED Novastar específica.

Uso:
    Ejecutar el script e introducir 'HDMI' para cambiar a la entrada HDMI o 'DP' para cambiar a DisplayPort.
"""

import socket

def send_tcp_command(ip, port, command):
    """
    Envía un comando TCP a una dirección IP y puerto específicos.

    Parameters:
        ip (str): La dirección IP del dispositivo.
        port (int): El puerto TCP del dispositivo.
        command (str): El comando en formato hexadecimal para enviar.

    Returns:
        None
    """

    # Convertir el comando de una cadena de dígitos hexadecimales a bytes
    command = bytes.fromhex(command)

    # Crear un socket TCP y conectar al dispositivo
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(command)
        data = sock.recv(1024)
    
    print(f"Recibido: {repr(data)}")

def main():
    IP = '10.100.1.10' # Ajustar a la dirección IP de la controladora LED
    PORT = 5200
    HDMI_COMMAND = '55 aa 00 00 fe 00 00 00 00 00 01 00 2d 00 20 02 01 00 a0 44 57 D3 15'
    DP_COMMAND = '55 aa 00 00 fe 00 00 00 00 00 01 00 2d 00 20 02 01 00 90 34 57 D3 15'
    
    # Solicitar al usuario que elija entre HDMI y DP
    entrada = input("Introduzca 'HDMI' para el comando HDMI o 'DP' para el comando DisplayPort: ").strip().lower()

    if entrada == 'hdmi':
        send_tcp_command(IP, PORT, HDMI_COMMAND)
    elif entrada == 'dp':
        send_tcp_command(IP, PORT, DP_COMMAND)
    else:
        print("Entrada no válida. Por favor, introduzca 'HDMI' o 'DP'.")

if __name__ == "__main__":
    main()