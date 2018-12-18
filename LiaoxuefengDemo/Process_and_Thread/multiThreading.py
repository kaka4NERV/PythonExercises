import time, threading

# 新线程执行的代码
def loop():
    print(f'Thread {threading.current_thread().name} is running..')
    n = 0
    while n < 5:
        n = n + 1
        print(f'threading {threading.current_thread().name} >>> {n}')
        time.sleep(1)
    print(f'thread {threading.current_thread().name} ended.')

print(f'thread {threading.current_thread().name} is running')
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print(f'thread {threading.current_thread().name} ended.')