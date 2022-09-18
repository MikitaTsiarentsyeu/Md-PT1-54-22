import time

isRun = False

def start():
    global start_time
    global isRun
    isRun = True
    start_time = time.time()

def finish():
    global isRun
    if isRun:
        res = time.time() - start_time
        isRun = False
        return res
    else:
        return -1
