import threading
import time

def p():
    print("the function p is running")
    time.sleep(1)
    print("done")

tr = threading.Thread(target=p)
tr.start()
print(threading.active_count())
