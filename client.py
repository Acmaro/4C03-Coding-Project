from socket import *
serverName = 'localHost'
serverPort = 12023
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Input lower case sentence: ")
clientSocket.send(bytes(sentence, 'utf-8'))
modifiedSentence = clientSocket.recv(1024)
print("From server: ", modifiedSentence)
clientSocket.close()