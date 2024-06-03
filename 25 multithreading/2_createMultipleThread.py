import threading


class MyThread(threading.Thread):
    def __init__(self):
        print("In Constructor")
        
    def run(self):
        for x in range(10):
            print("In run")

t1=MyThread()
t1.start()