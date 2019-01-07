import threading as thread
import time


def action(arg):
    """
    方法一：将要执行的方法作为参数传给Thread的构造方法
    :param arg:
    :return:
    """
    time.sleep(1)
    print("the arg is:", arg)


# 创建4个线程
for i in range(4):
    t = thread.Thread(target=action, args=(i,))
    t.start()

print('main thread end!')


class MyThread(thread.Thread):
    """
    方法二：从Thread继承，并重写run()
    注意：一定要显式的调用父类的初始化函数。
    """
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    def run(self):
        """
        定义每个线程要运行的函数
        :return:
        """
        time.sleep(1)
        print('the arg is:', self.arg)


for i in range(4):
    t = MyThread(i)
    t.start()

print('main thread end!')
