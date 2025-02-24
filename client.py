import socket
import threading

peers = []

def listen_for_messages(peer_socket):
    while True:
        try:
            message = peer_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received message: {message}")
        except:
            print("Disconnected from server.")
            break


def send_message(peer_socket):
    while True:
        try:
            message = input(": ")
            if message:
                peer_socket.send(message.encode('utf-8'))
        except:
            print("Error sending message.")
            break
def connect_to_peer(peer_address):
    peer_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    peer_socket.connect(peer_address)
    print(f"Connected to chat at {peer_address}")

    threading.Thread(target=listen_for_messages, args=(peer_socket,), daemon=True).start()
    send_message(peer_socket)


if __name__ == "__main__":
    connect_to_peer(('localhost',12345))