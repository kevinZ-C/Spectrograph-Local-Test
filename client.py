# -*- coding: utf-8 -*-
"""
@FileName: client.py
@Description: 客户端操作文件
@Author: Kevin
@Time: 2023/6/29 11:47
"""
import socket

"""
@ClassName: Client
@Description: 客户端类 
@Author: Kevin
"""


class Client:
    def __init__(self, ):
        self.connectStatus = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVERHOST = '127.0.0.1'
        self.SERVERPORT = 12345

    """
    @FunctionName: Connect
    @Description: 连接服务端
    @Input: NULL
    @Output: 连接状态  
    @Author: Kevin
    """

    def Connect(self):
        try:
            print("正在连接服务端")
            self.client.connect((self.SERVERHOST, self.SERVERPORT))
            self.connectStatus = True
            return True
        except Exception as e:
            print(f"连接服务端时发生错误：{e}")
            self.connectStatus = False
            return False

    """
    @FunctionName: SendWAV
    @Description: 发送wav文件
    @Input: 待发送的wav文件的名称，默认为Command.wav
    @Output: 发送状态
    @Author: Kevin
    """

    def SendWAV(self, wavName='Command.wav'):
        try:
            with open(wavName, 'rb') as testfile:
                data = testfile.read()

            self.client.sendall(data)
            return True
        except Exception as e:
            print(f"发送wav文件时发生错误：{e}")
            return False

    """
    @FunctionName: SendStatus
    @Description: 返回工作状态
    @Input: NULL
    @Output: 返回的工作状态
    @Author: Kevin
    """

    def SendStatus(self):
        try:
            queryCmd = self.client.recv(1024)
            if not queryCmd:
                print("接收查询时连接已断开")
                self.connectStatus = False
                return None
            queryCmd = str(queryCmd.encode("utf-8"))
            print("收到来自客户端的消息:" + queryCmd)
        except Exception as e:
            print(f"接收查询工作指令发生错误：{e}")
            self.connectStatus = False
            return None

        workStatus = input("工作状态：SA,RTSA,BASIC,WCDMA,CDMA2K,EDGEGSM,PNOISE,CDMA1XEV,CWLAN,CWIMAXOFDM,VSA,LTE,IDEN,WIMAXFIXED,LTETDD,TDSCDMA,NFIGURE,ADEMOD,DVB,DTMB,ISDBT,CMMB,RLC,AUDIO,PULSE,TA,MREC,WLAN,MCGD,NR5G,NR4G,OFDM,RESV,RESV_1,RESV_2,RESV_3,RESV_4,RESV_5,RESV_6,RESV_7,RESV_8,RESV_9\n \
                           请输入工作状态： ")

        try:
            self.client.send(workStatus.encode('utf-8'))
            return workStatus
        except Exception as e:
            print(f"发送工作状态时发送错误：{e}")
            self.connectStatus = False
            return None

    """
    @FunctionName: RecvResult
    @Description: 接受识别结果
    @Input: NULL
    @Output: 识别结果
    @Author: Kevin
    """

    def RecvResult(self):
        result = self.client.recv(1024)
        if not result:
            print("接收识别结果时连接断开")
            self.connectStatus = False
            return None
        result = str(result.encode("utf-8"))
        self.client.close()
        return result

