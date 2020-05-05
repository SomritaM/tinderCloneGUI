import threading
import time
mylist=[1,2,3,4,5]

def sq(list_arg):
    for i in list_arg:
        time.sleep(0.5)
        print("Current:",i*i)
def cube(list_arg):
    for i in list_arg:
        time.sleep(0.5)
        print("Current:",i*i*i)
t=time.time()
thread1=threading.Thread(target=sq,args=(mylist,))
thread2=threading.Thread(target=cube,args=(mylist,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Time taken:",time.time()-t)

