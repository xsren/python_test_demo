# encoding: utf-8
"""
@author: xsren 
@contact: bestrenxs@gmail.com
@site: xsren.me

@version: 1.0
@license: Apache Licence
@file: test_tkinter.py
@time: 2017/5/26 下午5:38

"""

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    # def createWidgets(self):
    #     self.helloLabel = Label(self, text='Hello, world!')
    #     self.helloLabel.pack()
    #     self.quitButton = Button(self, text='Quit', command=self.quit)
    #     self.quitButton.pack()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)


def run():
    app = Application()
    # 设置窗口标题:
    app.master.title('Hello World')
    # 主消息循环:
    app.mainloop()


if __name__ == '__main__':
    run()
