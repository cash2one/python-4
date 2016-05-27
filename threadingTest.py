import threading;
import time;
import scrapy;
from docutils.nodes import thead
import lxml;
sem = threading.Semaphore(value=1);
is_start = threading.Event();

def run():
    global chen,is_start;
    # sem.acquire();
    print(threading.current_thread().getName());
    print("before add  "+ str(chen))
    # time.sleep(0.2);
    chen = chen+1;
    print("after add  "+ str(chen))
    # time.sleep(0.2);
    chen = chen - 1;
    print("before jian  "+ str(chen))
    time.sleep(5);
    is_start.set();
    # sem.release();

def run1():
    global is_start;
    if is_start.isSet()==False:
        is_start.wait();
    print(is_start.isSet());
    print("begin");

if(__name__=="__main__"):
    chen = 0;

    t = threading.Thread(target=run);
    t1 = threading.Thread(target=run1);

    t.start();
    t1.start();