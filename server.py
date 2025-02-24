import socket
import threading

def listen_for_messages(peer_socket):
    while True:
        try:
            message = peer_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received message: {message}")
        except:
            print("Connection lost")
            break


clients=[]

def broadcast(message, sender_socket):
    
    for client in clients[:]:  
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)  



def handle_client(client_socket, client_address):
    print(f"New Connection from {client_address}")
    
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received from {client_address}: {message}")
                broadcast(message, client_socket)  
        except:
            print(f"Client {client_address} disconnected.")
            clients.remove(client_socket)  
            client_socket.close()
            break

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost',12345))
    server_socket.listen(1)
    print("Server listening on port 12345...")

    while True:
        peer_socket, peer_adress = server_socket.accept()
        print(f"connected to {peer_adress}")
        threading.Thread(target=listen_for_messages,args=(peer_socket,)).start()

if __name__ == "__main__":
    server()