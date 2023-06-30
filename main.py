# -*- coding: utf-8 -*-
"""
@FileName: main.py
@Description: main
@Author: Kevin
@Time: 2023/6/29 11:34
"""
import client
import recorder
import msvcrt


def main():
    rec = recorder.Record()
    while True:
        print("按下‘q’键以退出程序，按其他任意键开始程序")
        if input() == 'q':
            print("测试程序结束")
            del rec
            break
        else:
            print("测试程序开始\n \
                  开始录音")
            if rec.StartRecord():
                cli = client.Client()
                if cli.Connect():
                    if cli.SendWAV():
                        if cli.SendStatus():
                            recogRes = cli.RecvResult()
                            if recogRes is not None:
                                print("识别匹配结果为：" + recogRes)
                                del cli
                                continue
                            else:
                                print("出现错误，无返回结果")
                                del cli
                                continue
                        else:
                            del cli
                            continue
                    else:
                        del cli
                        continue
                else:
                    del cli
                    continue
            else:
                print("无有效的音频输入")
                continue


if __name__ == '__main__':
    main()
