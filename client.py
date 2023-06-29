# -*- coding: utf-8 -*-
"""
@FileName: client.py
@Description: 客户端操作文件
@Author: Kevin
@Time: 2023/6/29 11:47
"""

"""
@ClassName: Client
@Description: 客户端类 
@Author: Kevin
"""


class Client:
    def __init__(self, ):
        pass

    """
    @FunctionName: Connect
    @Description: 连接服务端
    @Input: NULL
    @Output: 连接状态  
    @Author: Kevin
    """

    def Connect(self):
        pass

    """
    @FunctionName: SendWAV
    @Description: 发送wav文件
    @Input: 待发送的wav文件的名称，默认为Command.wav
    @Output: 发送状态
    @Author: Kevin
    """

    def SendWAV(self, wavname='Command.wav'):
        pass

    """
    @FunctionName: SendStatus
    @Description: 返回工作状态
    @Input: NULL
    @Output: 返回的工作状态
    @Author: Kevin
    """

    def SendStatus(self):
        pass

    """
    @FunctionName: RecvResult
    @Description: 接受识别结果
    @Input: NULL
    @Output: 识别结果
    @Author: Kevin
    """

    def RecvResult(self):
        pass
