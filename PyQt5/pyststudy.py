from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # self.windowTitleChanged.connect(lambda x:self._my_func('Shiyanlou',666))

        #设置窗体标题
        self.setWindowTitle('My First App')

        #添加布局
        layout = QHBoxLayout()

        #创建按钮
        for i in range(5):
            button = QpushButton(str(i))
            # 将按钮按压信号与自定义函数关联
            button.pressed.connect(lambda x=i:self._my_func(x))
            # 将按钮添加到布局中
            layout.addWidget(button)

        #创建部件
        widget = QWidget()
        #将布局添加到部件
        self.setCentralWidget(widget)


        #设置标签
        label = QLabel('Welecome to Shiyanlou!')

        #设置标签显示在中央
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    # 自定义的信号处理函数
    def _my_func(self,n):
        print('click button %s' % n)

# 创建应用实例，通过sys.argv传入命令行参数
app = QApplication(sys.argv)
# 创建窗口实例
window = MainWindow()
# 显示窗口
window.show()
# 执行应用，进入事件循环
app.exec_()