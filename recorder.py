# -*- coding: utf-8 -*-
"""
@FileName: recorder.py
@Description: 录音模块文件
@Author: Kevin
@Time: 2023/6/29 11:35
"""
import pyaudio
import wave
import time
import os
import webrtcvad
import configparser

"""
@ClassName: Record
@Description: 录音类
@Author: Kevin
"""


class Record:
    def __init__(self):
        self.pyaudio_instance = pyaudio.PyAudio()
        self.vad_instance = webrtcvad.Vad(3)

        # CommandFlag = False
        if os.path.exists('config.ini'):
            config = configparser.ConfigParser()
            config.read('config.ini')
            print("已读取配置文件")
            self.MaxNoInputTime = int(config.get('Recorder_Update', 'MaxNoInputTime'))
            self.MaxRecInputTime = int(config.get('Recorder_Update', 'MaxRecInputTime'))
            self.MaxStopInputTime = int(config.get('Recorder_Update', 'MaxStopInputTime'))
            self.MinCommandInputTime = int(config.get('Recorder_Update', 'MinCommandInputTime'))
        else:
            print("配置文件不存在")
            self.MaxNoInputTime = 5
            self.MaxRecInputTime = 14
            self.MaxStopInputTime = 2
            self.MinCommandInputTime = 1

        self.FileRate = 16000
        self.RecChunk = 480

        self.RecFrames = []
        self.BlankFrames = []

    """
    @FunctionName: StartRecord
    @Description: 开始录音
    @Input: 录音文件名，默认为Command.wav
    @Output: 是否有语音输入
    @Author: Kevin
    """

    def StartRecord(self):
        pass

    """
    @FunctionName: RecordTimeLength
    @Description: 返回录音的时长
    @Input: NULL
    @Output: 录音的时长s
    @Author: Kevin
    """

    def RecordTimeLength(self):
        pass

    """
    @FunctionName: BlankTimeLength
    @Description: 返回空白录制的时长
    @Input: NULL
    @Output: 空白音时长s
    @Author: Kevin
    """

    def BlankTimeLength(self):
        pass


if __name__ == '__main__':
    Rec_Instance = Record()
    print(Rec_Instance.StartRecord())
