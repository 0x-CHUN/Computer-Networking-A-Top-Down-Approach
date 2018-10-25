import sys
import select
from random import random

# 设置在localhost进行测试
HOST = '127.0.0.1'

# 设置服务器端与客户端的端口号
SERVER_PORT = 5001
CLIENT_PORT = 5002

# 另开端口组实现双向通信
SERVER_PORT_EXTRA = 5003
CLIENT_PORT_EXTRA = 5004

# 单次读取的最大字节数
BUFFER_SIZE = 2048

# 窗口与包序号长度
WINDOWS_LENGTH = 8
SEQ_LENGTH = 10

# 最大延迟时间
MAX_TIME = 3


class Data(object):
    def __init__(self, msg, seq=0, state=0):
        self.msg = msg
        self.seq = str(seq % SEQ_LENGTH)
        self.state = state  # 0为未发送，1为已发送

    def __str__(self):
        return self.seq + " " + self.msg


class GBN(object):
    def __init__(self, server):
        self.server = server

    def push(self, path, port):
        # 初始化time、seq、windows
        time, seq = 0, 0
        data_windows = []
        with open(path, "r") as f:
            while True:
                # 超时
                if time > MAX_TIME:
                    for data in data_windows:
                        data.state = 0  # 全部未发送
                # windos未满，添加数据
                while len(data_windows) < WINDOWS_LENGTH:
                    info = f.readline().strip()

                    if not info:
                        break

                    data = Data(msg=info, seq=seq)
                    data_windows.append(data)
                    seq += 1
                # 无数据，退出
                if not data_windows:
                    break
                # 发送未发送成功的
                for data in data_windows:
                    if data.state == 0:
                        self.server.sendto(str(data).encode(encoding="utf-8"), (HOST, port))
                # 无阻塞socket连接监控
                readable, writeable, errors = select.select([self.server, ], [], [], 1)
                if len(readable) > 0:
                    # 收到数据则重新计时
                    time = 0
                    message, address = self.server.recvfrom(BUFFER_SIZE)
                    sys.stdout.write('ACK ' + message + '\n')
                    for i in range(len(data_windows)):
                        if message == data_windows[i].seq:
                            data_windows = data_windows[i + 1:]
                            break
                else:
                    # 未收到数据则计时器加一
                    time += 1
        self.server.close()

    def pull(self):
        # 记录上一个回执的ack的值
        last_ack = SEQ_LENGTH - 1
        data_windows = []
        while True:
            readable, writeable, errors = select.select([self.server, ], [], [], 1)
            if len(readable) > 0:
                message, address = self.server.recvfrom(BUFFER_SIZE)
                ack = int(message.split()[0])
                # 连续接收数据则反馈当前ack
                if last_ack == (ack - 1) % SEQ_LENGTH:
                    # 丢包率为0.2
                    if random() < 0.2:
                        continue
                    self.server.sendto(str(ack).encode(encoding="utf-8"), address)
                    last_ack = ack
                    # 判断数据是否重复
                    if ack not in data_windows:
                        data_windows.append(ack)
                        sys.stdout.write(message + '\n')
                    while len(data_windows) > WINDOWS_LENGTH:
                        data_windows.pop(0)
                else:
                    self.server.sendto(str(last_ack).encode(encoding="utf-8"), address)
        self.server.close()
