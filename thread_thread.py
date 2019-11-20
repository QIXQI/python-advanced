# -*- coding: utf-8 -*-

# _thread 模块已经弃用，不推荐

import _thread
import time


#  定义线程函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f'{threadName}: {time.ctime(time.time())}')


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ('Thread-1', 2, ))
    _thread.start_new_thread(print_time, ('Thread-2', 4, ))
except:
    print('Error：无法启动线程')

while 1:
    pass