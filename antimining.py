import psutil
import os
from tkinter import *
import tkinter.messagebox
import time
import sys

window = Tk()
btn1 = Label(window, text='웹채굴 방지 소프트웨어 구동중. 종료하기')
btn1.pack()
browser=['chrome.exe','iexplore.exe','firefox.exe']
while True:
    time.sleep(1)
    cpu = psutil.cpu_percent()
    process= os.popen('tasklist').read()
    if browser[0] in process:
        if cpu >= 75:
            response = tkinter.messagebox.askyesno("채굴의심","채굴이 의심됩니다. 브라우저를 종료하시겠습니까? 안심할 수 있는 웹페이지인 경우 아니오를 클릭하셔서 본 탐지SW를 종료하십시오.")
            if response==True:
                os.system('taskkill /f /im '+browser[0])
            elif response==False:
                os.system('taskkill /f /im ANTIMINER.exe')
    elif cpu>95:
        os.system('taskkill /f /im'+browser[0])
    elif browser[1] in process:
        if cpu >= 75:
            response = tkinter.messagebox.askyesno("채굴의심","채굴이 의심됩니다. 브라우저를 종료하시겠습니까? 안심할 수 있는 웹페이지인 경우 아니오를 클릭하셔서 본 탐지SW를 종료하십시오.")
            if response==True:
                os.system('taskkill /f /im '+browser[1])
            elif response==False:
                os.system('taskkill /f /im ANTIMINER.exe')
        elif cpu > 95:
            os.system('taskkill /f /im' + browser[1])

    elif browser[2] in process:
        if cpu >= 75:
            response = tkinter.messagebox.askyesno("채굴의심","채굴이 의심됩니다. 브라우저를 종료하시겠습니까? 안심할 수 있는 웹페이지인 경우 아니오를 클릭하셔서 본 탐지SW를 종료하십시오.")
            if response==True:
                os.system('taskkill /f /im '+browser[2])
            elif response==False:
                os.system('taskkill /f /im ANTIMINER.exe')
        elif cpu > 95:
            os.system('taskkill /f /im' + browser[2])