"""
web server
为使用者提供一个类，
使用这可以快速的搭建web服务，
展示自己的网页
"""
from socket import *
from select import select

# 主体功能
class HTTPServer:
    def __init__(self,host='0.0.0.0',port=8080,dir=None):
        self.host = host
        self.port = port
        self.dir = dir

    def start(self):
        pass


if __name__ == '__main__':
    # 需要用户决定 ： 网络地址 和要发送的数据
    host = '0.0.0.0'
    port = 8000
    dir = "./static" # 数据位置

    # 实例化对象，调用方法启动服务
    httpd = HTTPServer(host=host,port=port,dir=dir)
    httpd.start() # 启动服务

