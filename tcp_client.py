"""
tcp客户端
重点代码
"""

from socket import *

# 服务器地址
server_addr = ('127.0.0.1',8888)

# 创建套接字
tcp_socket = socket()  # 默认值就是tcp

# 发起链接
tcp_socket.connect(server_addr)

# 循环发送消息
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print(data.decode())

# 断开链接
tcp_socket.close()

