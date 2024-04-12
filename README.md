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
패킷 형식 설명:

클라이언트에서 서버로의 패킷: 사용자 이름, 에코 옵션, 메시지를 포함하는 텍스트 형식의 패킷
서버에서 클라이언트로의 정상 패킷: 서버에서 처리된 응답 메시지를 포함하는 텍스트 형식의 패킷
서버에서 클라이언트로의 오류 패킷: 오류 메시지를 포함하는 텍스트 형식의 패킷
패킷의 송/수신 순서 설명:

클라이언트는 먼저 사용자 이름, 에코 옵션, 메시지를 포함한 패킷을 서버로 전송합니다.
서버는 해당 패킷을 수신하고 처리한 후, 클라이언트로부터 받은 메시지에 대한 응답을 전송합니다.
클라이언트는 서버로부터의 응답을 수신하고 처리합니다.
각 패킷 송/수신 시 수행되는 동작 설명:

클라이언트에서 서버로의 패킷 송신: 사용자 이름, 에코 옵션, 메시지를 포함한 텍스트 형식의 패킷을 생성하여 서버로 전송합니다.
서버에서 클라이언트로의 정상 패킷 송신: 서버는 클라이언트로부터 받은 메시지를 처리한 후, 정상적인 경우 응답 메시지를 생성하여 클라이언트로 전송합니다. 이때, 상태 코드와 함께 정상적인 처리를 알립니다.
서버에서 클라이언트로의 오류 패킷 송신: 서버는 클라이언트로부터 받은 메시지를 처리하는 과정에서 오류가 발생한 경우, 오류 메시지를 생성하여 클라이언트로 전송합니다. 이때, 상태 코드와 함께 오류를 알립니다.
