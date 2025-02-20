import socket
import threading

peers = []

def listen_for_messages():
    while True:
        try:
            message = peer_socket_recv(1024).decode('utf-8')
            if message:
                print(f"Received message: {message}")
        except:
            break
