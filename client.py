import socket

#Socket creation
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connecting to the server
connexion.connect(('localhost',666))

#Sending a message to the server
connexion.send(b'touch zizi.txt')