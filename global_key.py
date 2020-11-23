import pyautogui
import pyautogui as pag
import sys
import time
import requests

pyautogui.FAILSAFE = False  # 防止异常


def is_connected():
    try:
        html = requests.get("https://www.baidu.com", timeout=2)
    except:
        print("{}网络中断".format(time.strftime("%H:%M:%S", time.localtime())))  # 打印坐标
        return False
    print("{}网络正常".format(time.strftime("%H:%M:%S", time.localtime())))  # 打印坐标
    return True


if __name__ == '__main__':
    print("请在5秒内移动到想要点击的坐标内")
    time.sleep(5)
    x, y = pag.position()  # 返回鼠标的坐标
    print("获取位置成功位置为（{},{}）将每2分钟点击一次".format(x, y))  # 打印坐标
    while True:
        if not is_connected():
            print("{}正在拨号".format(time.strftime("%H:%M:%S", time.localtime())))  # 打印坐标
            try:
                cx, cy = pag.position()  # 返回鼠标的坐标
                pyautogui.click(x, y)
                pyautogui.moveTo(cx, cy)
                time.sleep(0.2)
                print("{2}刷新成功（{0},{1}）".format(x, y, time.strftime("%H:%M:%S", time.localtime())))  # 打印坐标
            except:
                continue
        time.sleep(2)
