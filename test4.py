import time
import threading

event = threading.Event()


def lighter():
    event.set()
    n = 0
    while True:
        if n > 2 and n < 5:
            event.clear()
            print("\033[1;41m 现在是红灯\033[0m")
        elif n > 5:
            event.set()
            n = 0
        else:
            print("\033[1;42m现在是绿灯\033[0m")
        time.sleep(1)
        n += 1


def car(name):
    while True:
        if event.is_set():
            print("%s正在开车" % name)
            time.sleep(1)
        else:
            print("%s等待绿灯" % name)
            event.wait()
            print("\033[1;42m绿灯亮了，%s继续开车\033[0m" % name)


a = threading.Thread(target=lighter)
a.start()
b = threading.Thread(target=car, args=("张三",))
b.start()
