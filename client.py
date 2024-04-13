from socket import *


#에코옵션 선택 함수
def get_echo_option():
    while True:
        print("Select an echo option:")
        print("1. Normal echo (Type 1)")
        print("2. Uppercase echo (Type 2)")
        print("3. Lowercase echo (Type 3)")
        print("4. Exit chat (Type 4)")
        option = input("Option: ")
        if option in ['1', '2', '3', '4']:
            return option
        else:
            print("Invalid option. Please select again.")


#서버에 연결하는 함수
def connect_to_server(serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_STREAM) #TCP 연결을 위한 소켓을 형성
    clientSocket.connect((serverName, serverPort)) # 서버의 IP 주소와 포트에 소켓을 연결
    return clientSocket


#메시지 패킷을 보내는 함수
def send_message(clientSocket, username, echo_option, message):
    packet = f"{username}: {echo_option}: {message}" #username echo_option message를 패킷으로 묶음
    clientSocket.send(packet.encode()) #패킷을 인코드하여 전송함


#서버로부터 처리된 응답을 받는 함수
def receive_response(clientSocket):
    response = clientSocket.recv(1024).decode() #서버로부터 받은 response를 디코드하여 처리
    return response


def main():
    serverName = '127.0.0.1' #local주소
    serverPort = 12000
    username = input("Enter your username: ")
    clientSocket = connect_to_server(serverName, serverPort)

    while True:
        echo_option = get_echo_option()
        if echo_option == '4':
            print("Exiting the chat.")
            break
        message = input("Enter your message: ")
        send_message(clientSocket, username, echo_option, message)
        response = receive_response(clientSocket)
        print("Server response:", response)
    clientSocket.close()


if __name__ == "__main__":
    main()
