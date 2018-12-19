import threading

# 创建全局的ThreadLocak对象：
local_school = threading.local()

def process_thread(name):
    # 绑定ThreadLocal的student：
    local_school.student = name
    process_student()

def process_student():
    # 获取当前线程关联的student：
    std = local_school.student
    print(f'Hello, {std} (in {threading.current_thread().name})')

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()