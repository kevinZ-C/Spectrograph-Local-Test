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

    def StartRecord(self, WavName='Command.wav'):
        CommandFlag = False

        RecStream = self.pyaudio_instance.open(format=pyaudio.paInt16, channels=1, rate=self.FileRate, input=True,
                                               frames_per_buffer=self.RecChunk)
        StartTime = time.time()

        self.RecFrames = []
        self.BlankFrames = []

        while True:
            AudioData = RecStream.read(self.RecChunk)
            InputFlag = self.vad_instance.is_speech(AudioData, self.FileRate)

            if InputFlag:
                self.RecFrames.append(AudioData)
                self.BlankFrames = []
            else:
                self.BlankFrames.append(AudioData)

            NowTime = time.time()

            if not CommandFlag:
                # 无语音输入判断
                if NowTime - StartTime >= self.MaxNoInputTime:
                    return False
                # 指令输入判断
                if self.RecordTimeLength() >= self.MinCommandInputTime:
                    StartTime = time.time()
                    CommandFlag = True
                    continue
            else:
                if NowTime - StartTime >= self.MaxRecInputTime:
                    break
                if self.BlankTimeLength() >= self.MaxStopInputTime:
                    break

        with wave.open(WavName, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(self.pyaudio_instance.get_sample_size(pyaudio.paInt16))
            wf.setframerate(self.FileRate)
            wf.writeframes(b''.join(self.RecFrames))

        RecStream.stop_stream()
        RecStream.close()
        return True

    """
    @FunctionName: RecordTimeLength
    @Description: 返回录音的时长
    @Input: NULL
    @Output: 录音的时长s
    @Author: Kevin
    """

    def RecordTimeLength(self):
        return (len(self.RecFrames) * self.RecChunk) / self.FileRate

    """
    @FunctionName: BlankTimeLength
    @Description: 返回空白录制的时长
    @Input: NULL
    @Output: 空白音时长s
    @Author: Kevin
    """

    def BlankTimeLength(self):
        return (len(self.BlankFrames) * self.RecChunk) / self.FileRate


if __name__ == '__main__':
    Rec_Instance = Record()
    print(Rec_Instance.StartRecord())
