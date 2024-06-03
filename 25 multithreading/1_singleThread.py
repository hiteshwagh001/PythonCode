import os
import threading


def fun():
    for x in range(10):
        print(x)
    print(threading.current_thread().name)
    print(threading.currentThread)
    # print(os)

fun()