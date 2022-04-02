# create by andy at 2022/4/2
# reference: https://www.programminghunter.com/article/3135281453/
import threading
import time


def add2():
    start_time = time.time()
    for i in range(100000000):
        pass
    end_time = time.time()
    use_time = end_time - start_time
    print("线程id：%s 耗时：%s" % (threading.current_thread().ident, use_time))


if __name__ == '__main__':
    print("【线程测试】")
    print("主线程：%s 主线程id：%s" % (threading.current_thread(), threading.current_thread().ident))
    t1 = threading.Thread(target=add2, args=(), name="t1-线程")
    t2 = threading.Thread(target=add2, args=(), name="t2-线程")
    t3 = threading.Thread(target=add2, args=(), name="t3-线程")

    start_time = time.time()
    t1.start()
    t2.start()
    t3.start()
    t3.join()
    t1.join()
    t2.join()
    end_time = time.time()
    use_time = end_time - start_time
    print("线程id：%s 耗时：%s  (主线程)" % (threading.current_thread().ident, use_time))

    print("====主线程单独运行一次循环耗时：=====")
    add2()
