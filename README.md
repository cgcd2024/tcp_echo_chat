## 환경설정
* PYTHON 3.12
  * SOCKET
* INTELLIJ IDE
  * python server.py
  * python client.py
  * **본 과제는 INTELLIJ IDE를 통해 독립된 두개의 인스턴스를 생성하여 수행하였음**
 
## 실행화면
Run server


<img width="579" alt="스크린샷 2024-04-12 오후 12 52 12" src="https://github.com/cgcd2024/tcp_echo_chat/assets/113968344/f94f3361-fd99-49d1-97b0-ed3f0d1da9be">

***
Run client and enter username


<img width="382" alt="스크린샷 2024-04-12 오후 12 52 31" src="https://github.com/cgcd2024/tcp_echo_chat/assets/113968344/da704245-8c8f-43b2-ba00-014a20b39133">

***
Echo 1


<img width="345" alt="스크린샷 2024-04-12 오후 12 53 01" src="https://github.com/cgcd2024/tcp_echo_chat/assets/113968344/2208aa1a-2985-450a-9951-0b8179ec9719">


***
Echo 2


<img width="328" alt="스크린샷 2024-04-12 오후 12 53 36" src="https://github.com/cgcd2024/tcp_echo_chat/assets/113968344/56ab3e45-238c-4a0a-8b90-1a6578237881">

***
Echo 3


<img width="307" alt="스크린샷 2024-04-12 오후 12 53 53" src="https://github.com/cgcd2024/tcp_echo_chat/assets/113968344/96181810-6583-4591-a1ab-4a9eb0663f3c">


***
Echo 4


<img width="321" alt="스크린샷 2024-04-12 오후 12 54 26" src="https://github.com/cgcd2024/tcp_echo_chat/assets/113968344/6f71508a-4215-477e-b348-2f9dc5c03c36">

***
Exception


<img width="352" alt="스크린샷 2024-04-12 오후 12 54 14" src="https://github.com/cgcd2024/tcp_echo_chat/assets/113968344/2eb4dad3-c9ac-4f00-9e9a-3cf8f1a2658f">



## 프로토콜 설계

송/수신 순서와 동작


1. 클라이언트는 사용자 이름, 에코옵션, 메시지를 포함한 패킷을 서버로 전송합니다.
2. 서버는 해당 패킷을 수신하고 처리합니다.
   * 정상 패킷 송신 : 정상적인 경우의 응답 메시지를 생성하여 클라이언트로 전송합니다.
   * 오류 패킷 송신 : 오류 메시지를 생성하여 클라이언트로 전송합니다.
3. 클라이언트는 서버로부터의 응답을 수신하고 처리합니다. 


***
패킷 형식


client to server


* username, echo_option, message로 구성된 텍스트 형식의 패킷

server to client


* response message 패킷



