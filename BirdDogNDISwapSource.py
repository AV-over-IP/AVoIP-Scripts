import requests
import json
import time

def post_request(url, payload):
    """
    Realiza una solicitud POST a una URL con un payload dado.

    Parameters:
        url (str): La URL a la que se enviará la solicitud.
        payload (dict): El cuerpo de la solicitud.

    Returns:
        Response: Objeto de respuesta de la solicitud.
    """
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response

def change_source(ip, channel, source_name):
    """
    Cambia la fuente de un decodificador en una dirección IP específica.

    Parameters:
        ip (str): La dirección IP del decodificador.
        channel (int): El número del canal a cambiar.
        source_name (str): El nombre de la fuente a la cual cambiará.

    Returns:
        None
    """
    url = f"http://{ip}:8080/connectTo"
    payload = {"sourceName": source_name, "ChNum": str(channel)}
    
    response = post_request(url, payload)

    if response.status_code == 200:
        print(f"Fuente cambiada en el decodificador {ip} al canal {channel} para {source_name}.")
    else:
        print(f"Error al cambiar la fuente en {ip}, código de estado: {response.status_code}")

def main():
    """
    Función principal que cambia las fuentes de varios decodificadores.
    """
    # Configuración de decodificadores y fuentes
    decoders = {
        "decoder1": {"ip": "10.100.1.123", "channel": 1, "sources": ["Source 2", "Source 1"]},
        "decoder2": {"ip": "10.100.1.113", "channel": 1, "sources": ["Source 1", "Source 2"]}
    }

    # Cambio de fuentes para cada decodificador
    for name, decoder in decoders.items():
        for source in decoder["sources"]:
            change_source(decoder["ip"], decoder["channel"], source)
            time.sleep(1)

if __name__ == "__main__":
    main()
