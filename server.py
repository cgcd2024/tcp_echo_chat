from socket import *


#클라이언트로부터 받은 메시지를 처리하는 함수
def handle_echo(connectionSocket):
    while True:
        try:
            #클라이언트로부터 받은 패킷을 각각 변수로 지정
            packet = connectionSocket.recv(1024).decode()
            packet_parts = packet.split(": ")
            username = packet_parts[0]
            echo_option = packet_parts[1]
            message = packet_parts[2]

            if echo_option == '1':
                response = message
            elif echo_option == '2':
                response = message.upper()
            elif echo_option == '3':
                response = message.lower()
            elif echo_option == '4':
                response = "Chat session ended."
                connectionSocket.send(response.encode())
                break
            else:
                response = "Invalid echo option."
            connectionSocket.send(response.encode())
        except Exception as e:
            print("An error occurred:", e)
            break
    connectionSocket.close()


def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Connected to:", addr)
        handle_echo(connectionSocket)


if __name__ == "__main__":
    main()
