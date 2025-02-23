import socket
import threading

def listen_for_messages(peer_socket):
    while True:
        try:
            message = peer_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received message: {message}")
        except:
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