import socket
import json
localIP     = "192.168.0.241"
localPort   = 20001
bufferSize  = 1024

def start_server():
    ips = []
    serv = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    serv.bind((localIP, localPort))
    while(True):
        bytesAddressPair = serv.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        try: m = json.loads(message)
        except: m = {'type': None}
        if m['type'] == 'get':
            serv.sendto(str.encode(json.dumps(ips)), address)
        elif m['type'] == 'add':
            ips.append(address[0])
        elif m['type'] == 'remove':
            ips.remove(address[0])
        else:
            print(message)

def start_client(type=None):
    data = {'type': type}
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.sendto(str.encode(json.dumps(data)), (localIP, localPort))
    if type == 'get':
        msg = UDPClientSocket.recvfrom(bufferSize)
        print(msg[0])
        return json.loads(msg[0])

if __name__ == "__main__":
    #start_server()
    i = input()
    print(start_client(i))