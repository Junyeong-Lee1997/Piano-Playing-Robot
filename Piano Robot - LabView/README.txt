pianomaster : 전체 프로젝트 파일
global variable : 글로벌 변수 선언파일

Right Arm

GripperAngle : Right Arm이 쳐야하는 음계에 따라 Gripper의 벌린 정도를 조절하는 VI
iikk : Right Arm의 Inverse Kinematics 계산 및 PWM signal로 변환

rightarm11109 : 1, 2, 3번 모터 controller와 연결하는 VI
rightarm653 : 4, 5, 6번 모터 controller와 연결하는 VI

Left Arm

udp left arm convert : right arm과 left arm의 거리 차이를 계산하는 VI
leftarmfk : Left arm의 Foward Kinematics를 적용하는 VI

leftarm11109 : 1, 2, 3번 모터 controller와 연결하는 VI
leftarm653 : 4, 5, 6번 모터 controller와 연결하는 VI

UDP

udp LA send convert : Robot Arm이 이동해야 하는 수평 위치에 대해 Linear Actuator로 값을 전송하는 VI
udp send to LA : UDP 통신으로 Linear actuator에 position값을 전송하는 VI
udp receive from python : chord인식 결과를 UDP로 수신

udp통신-LA영점설정 : Linear Actuator의 "0" position을 설정하기 위한 UDP Sender 코드

실행 순서 :; rightarm11109 rightarm653 leftarm11109 leftarm653를 제외한 모든 VI 실행 -> rightarm11109 rightarm653 leftarm11109 leftarm653 실행

Linear Actuator 영점 설정 후 Chord Detect 결과 전송