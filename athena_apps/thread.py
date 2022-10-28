"""
from time import sleep
from threading import Thread

def task(sleep_time, message):
    sleep(sleep_time)
    print(message)

# create a thread
thread = Thread(target=task, args=(1.5, 'New message from another thread'))

thread.start()
print('Waiting for the thread...')

#join waits/o7tputs the result then contines
#if thread.join was commententted out it would
#print hey before the threqds out put

thread.join()
print("hey")
"""
from time import sleep
from threading import Thread
x = []
def amount():
    print("adding")
    x.append(1)
    print(len(x))

def counting():
    print("counting")
    print(len(x))

thread = Thread(target=counting)
thread.start()
amount()
thread.join()
print("done")
#output
"""
counting
0
adding
1
done

"""
