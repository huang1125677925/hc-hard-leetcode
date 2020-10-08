#encoding=utf-8
import threading
import time


# 函数1
def doFirstThing(url):
    print("First Thing Star")
    time.sleep(2)
    print('First Thing Finished')


# 函数2
def doSecondThing(url):
    print("Second Thing Star")
    time.sleep(4)
    print('Second Thing Finished')


if __name__ == "__main__":
    # 传入threading
    thread1 = threading.Thread(target=doFirstThing, args=("",))
    thread2 = threading.Thread(target=doSecondThing, args=("",))
    start_time = time.time()
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    end = time.time()
    print('time:%s' % (end - start_time))
