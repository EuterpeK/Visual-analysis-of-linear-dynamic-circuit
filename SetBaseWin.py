import BaseWin
import tkinter as tk


def RcZeroSt():
    import RcState


# 一阶RC零输入响应
def RcZeroIn():
    import RcInput


# 一阶RC全响应
def RcFull():
    import RcFullRes


# 一阶RL零状态响应
def RlZeroSt():
    import RlState


# 一阶RL零输入响应
def RlZeroIn():
    import RlInput


# 一阶RL全响应
def RlFull():
    import RlFull


# 二阶全响应分析
def RlcFull():
    import RlcFullRes


# 主窗口
but1 = tk.Button(BaseWin.mainwin, text='一阶RC零状态分析', width=20, height=5,
                 command=RcZeroSt)
but1.place(x=10, y=10)
but2 = tk.Button(BaseWin.mainwin, text='一阶RC零输入分析', width=20, height=5,
                 command=RcZeroIn)
but2.place(x=10, y=160)
but3 = tk.Button(BaseWin.mainwin, text='一阶RC全响应分析', width=20, height=5,
                 command=RcFull)
but3.place(x=10, y=310)
but4 = tk.Button(BaseWin.mainwin, text='一阶RL零状态分析', width=20, height=5,
                 command=RlZeroSt)
but4.place(x=160, y=10)
but5 = tk.Button(BaseWin.mainwin, text='一阶RL零输入分析', width=20, height=5,
                 command=RlZeroIn)
but5.place(x=160, y=160)
but6 = tk.Button(BaseWin.mainwin, text='一阶RL全响应分析', width=20, height=5,
                 command=RlFull)
but6.place(x=160, y=310)
but7 = tk.Button(BaseWin.mainwin, text='二阶RLC全响应分析', width=20, height=5,
                 command=RlcFull)
but7.place(x=310, y=160)

BaseWin.mainwin.mainloop()
