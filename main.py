# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import logging
import threading
from time import sleep, ctime
logging.basicConfig(level=logging.INFO)

def loop0():
    logging.info("start loop0 " + ctime())
    sleep(4)
    logging.info("end loop0:" + ctime())

def loop1():
    logging.info("start loop1:" + ctime())
    sleep(2)
    logging.info("end loop1:" + ctime())

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

class Person():
    def __init__(self):
        self.name = "zhangsan"

    @classmethod
    def eat(self):
        print('eating')

loops = [2, 4]
def loop(nloop, nsec):
    logging.info("start loop" + str(nloop) + "at " + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + "at " + ctime())

if __name__ == '__main__':
    #print_hi('PyCharm')
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

    sleep(6)
    logging.info("end main:" + ctime())
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
