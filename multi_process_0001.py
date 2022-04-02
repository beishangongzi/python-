# create by andy at 2022/4/2
# reference:   https://www.programminghunter.com/article/3135281453/

import multiprocessing
import os
import time


def add2():
    start_time = time.time()
    for i in range(100000000):
        pass
    end_time = time.time()
    use_time = end_time - start_time
    print("进程id： %s use_time： %s" % (os.getpid(), use_time))


if __name__ == '__main__':
    print("【进程测试】")
    p1 = multiprocessing.Process(target=add2, args=(), name="p1-进程")
    print("p1.name ：%s" % p1.name)
    p2 = multiprocessing.Process(target=add2, args=(), name="p2-进程")
    p3 = multiprocessing.Process(target=add2, args=(), name="p3-进程")

    start_time = time.time()
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end_time = time.time()
    use_time = end_time - start_time
    print("主进程id：%s use_time： %s" % (os.getpid(), use_time))

    print("====主进程单独运行一次循环耗时：=====")
    add2()
