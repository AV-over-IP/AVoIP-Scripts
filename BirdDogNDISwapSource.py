import requests
import json
import time

def change_source(ip, channel, source_name):
    url = f"http://{ip}:8080/connectTo"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"sourceName": source_name, "ChNum": str(channel)})
    
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print(f"Cambiado el decodificador en {ip} al canal {channel} para fuente {source_name}")
    else:
        print(f"Error al cambiar la fuente en {ip}, código de estado: {response.status_code}")

def main():
    decoder1_ip = "192.168.1.1" #cambiar por la ip del deco 1
    decoder2_ip = "192.168.1.2" #cambiar por la ip del deco 2
    
    #deco 1
    change_source(decoder1_ip, 1, "Source 2")
    time.sleep(2)
    change_source(decoder1_ip, 1, "Source 1")

    #deco 2
    change_source(decoder2_ip, 1, "Source 1")
    time.sleep(2)
    change_source(decoder2_ip, 1, "Source 2")

if __name__ == "__main__":
    main()
