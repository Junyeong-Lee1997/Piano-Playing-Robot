udp_list=['W_17W_26W_28','W_20W_27W_29','W_17W_26W_28','W_20W_27W_29','W_17W_26W_28','W_20W_27W_29','W_17W_26W_28','W_20W_27W_29','W_17W_26W_28','W_20W_27W_29',
          'W_17W_26W_28','W_20W_27W_29','W_17W_26W_28','W_20W_27W_29','W_17W_26W_28','W_20W_27W_29','W_17W_26W_28','W_20W_27W_29']
import socket
import time

for i in udp_list:
    if i=='FFFFFFFFFFFF':
      print(i)
      time.sleep(3)
    else :
      sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      print(i)
      sock.sendto(i.encode(),('127.0.0.1',61557))
      time.sleep(3)

sock.close()