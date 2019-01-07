import os


class TestOs:
    """
    pyhton标准库os入门
    """
    def __init__(self):
        self.file_name = "D://web-postsale-debug.log"

    def test_access(self):
        """
        查看文件的访问权限
        :return: None
        """
        exist = os.access(self.file_name, os.F_OK)
        can_read = os.access(self.file_name, os.R_OK)
        can_write = os.access(self.file_name, os.W_OK)
        can_exe = os.access(self.file_name, os.X_OK)
        print("是否存在？ ", "是" if exist else "否")
        print("是否可读？ ", "是" if can_read else "否")
        print("是否可写？ ", "是" if can_write else "否")
        print("是否可执行？ ", "是" if can_exe else "否")
        # 获取文件的大小
        print("文件大小", os.path.getsize(self.file_name))
        # 执行shell命令
        os.system(self.file_name)

    def test_path(self):
        print("系统的当前路径：", os.getcwd())
        # 修改当前路径
        os.chdir('/')
        print("系统的当前路径：", os.getcwd())
        print(os.listdir(os.getcwd()))


if __name__ == "__main__":
    test_os = TestOs()
    test_os.test_access()
