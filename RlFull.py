import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import BaseWin
from decimal import Decimal

window = tk.Toplevel(BaseWin.mainwin)
window.title('一阶RL零输入响应')
window.geometry('1000x1000')

# 等效电流的输入
label_i = tk.Label(window, text='等效电流源电流:', font=('Arial', 10), width=15, height=1)
label_i.place(x=10, y=10)
label_a = tk.Label(window, text="A", font=('Arial', 10), width=15, height=1)
label_a.place(x=210, y=10)
equ = tk.Entry(window, show=None)
equ.place(x=120, y=10)

# 等效串联电阻
label_r = tk.Label(window, text='等效并联电阻:', font=('Arial', 10), width=15, height=1)
label_r.place(x=10, y=50)
label_R = tk.Label(window, text="R", font=('Arial', 10), width=15, height=1)
label_R.place(x=210, y=50)
eqr = tk.Entry(window, show=None)
eqr.place(x=120, y=50)

# 电容值
label_c = tk.Label(window, text='电感值:', font=('Arial', 10), width=15, height=1)
label_c.place(x=10, y=90)
label_F = tk.Label(window, text="H", font=('Arial', 10), width=15, height=1)
label_F.place(x=210, y=90)
H = tk.Entry(window, show=None)
H.place(x=120, y=90)

# 电感初始电流
label_il = tk.Label(window, text='电感初始电压', font=('Arial', 10), width=15, height=1)
label_il.place(x=10, y=130)
label_ilA = tk.Label(window, text='A', font=("Arial", 10), width=15, height=1)
label_ilA.place(x=210, y=130)
LA = tk.Entry(window, show=None)
LA.place(x=120, y=130)

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
mpl.rcParams['axes.unicode_minus'] = False  # 负号显示


class From1:
    def __init__(self, a, b, c, d):
        self.root = tk.Tk()  # 创建主窗体
        self.canvas = tk.Canvas()  # 创建一块显示图形的画布
        self.figure = self.create_matplotlib(a, b, c, d)  # 返回matplotlib所画图形的figure对象
        self.create_form(self.figure)  # 将figure显示在tkinter窗体上面
        self.root.mainloop()

    def create_matplotlib(self, Is, Req, I0, L):
        # 创建绘图对象f
        f = plt.figure(num=2, figsize=(8, 8), dpi=80, facecolor="pink", edgecolor='green', frameon=True)
        # 创建一副子图
        tal = L / Req
        t = np.linspace(0.0, 100.0, 100000)
        il = float(Is) + (float(I0) - float(Is)) * np.exp(-1.0 / float(tal) * t)
        plt.plot(t, il)

        plt.xlabel("时间t/s", fontproperties='SimHei', fontsize=15, color='red')
        plt.ylabel("电流Li/A", fontproperties='SimHei', fontsize=15, color='red')
        plt.title(r"RL Full Response", fontproperties='SimHei', fontsize=20)

        plt.grid(True)
        # plt.axis([0, 100.0, 0, float(I)])
        plt.show()

        return f

    def create_form(self, figure):
        # 把绘制的图形显示到tkinter窗口上
        self.canvas = FigureCanvasTkAgg(figure, self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # 把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
        toolbar = NavigationToolbar2Tk(self.canvas,
                                       self.root)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def run():
    var1 = Decimal(equ.get())
    var2 = Decimal(eqr.get())
    var3 = Decimal(H.get())
    var4 = Decimal(LA.get())
    From1(var1, var2, var4, var3)


def clear_content():
    equ.delete(0, tk.END)
    eqr.delete(0, tk.END)
    H.delete(0, tk.END)
    LA.delete(0, tk.END)


# 运行
run_first = tk.Button(window, text="Run", width=5, height=1, command=run)
run_first.place(x=300, y=25)

# 清空
clear = tk.Button(window, text="Clear", width=5, height=1, command=clear_content)
clear.place(x=300, y=65)

# 时间
label_time = tk.Label(window, text='时间\n图像中点的横坐标', font=('Arial', 8))
label_time.place(x=380, y=25)

# 电压
label_uc = tk.Label(window, text='电感电流\n图像中点的纵坐标', font=('Arial', 8))
label_uc.place(x=380, y=65)


# 显示时间常数
def show_const_time():
    var1 = Decimal(H.get())
    var2 = Decimal(eqr.get())
    Sc.insert('insert', str(var1 / var2))


# 时间常数
button_con_time = tk.Button(window, text='时间常数(ms)', font=('Arial', 15), width=12, height=2, command=show_const_time)
button_con_time.place(x=530, y=10)
Sc = tk.Text(window, height=2, width=10)
Sc.place(x=550, y=80)


class From2:
    def __init__(self, a, b, v):
        self.root = tk.Tk()  # 创建主窗体
        self.canvas = tk.Canvas()  # 创建一块显示图形的画布
        self.figure = self.create_matplotlib(a, b, v)  # 返回matplotlib所画图形的figure对象
        self.create_form(self.figure)  # 将figure显示在tkinter窗体上面
        self.root.mainloop()

    def create_matplotlib(self, Is, I0, v):
        # 创建绘图对象f
        f = plt.figure(num=2, figsize=(8, 8), dpi=80, facecolor="pink", edgecolor='green', frameon=True)
        # 创建一副子图
        tal = v
        t = np.linspace(0.0, 100.0, 100000)
        # il = float(U) / float(Req) * (1.0 - * np.exp(-1.0 / float(tal) * t))
        il = float(Is) + (float(I0) - float(Is)) * np.exp(-1.0 / float(tal) * t)
        plt.plot(t, il)

        plt.xlabel("时间t/s", fontproperties='SimHei', fontsize=15, color='red')
        plt.ylabel("电流Li/A", fontproperties='SimHei', fontsize=15, color='red')
        plt.title(r"RL Full Response", fontproperties='SimHei', fontsize=20)

        plt.grid(True)
        plt.show()

        return f

    def create_form(self, figure):
        # 把绘制的图形显示到tkinter窗口上
        self.canvas = FigureCanvasTkAgg(figure, self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # 把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
        toolbar = NavigationToolbar2Tk(self.canvas,
                                       self.root)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def show_change(v):
    var1 = Decimal(equ.get())
    var2 = Decimal(LA.get())
    From2(var1, var2, v)


# 改变时间常数
change_time = tk.Scale(window, label='改变时间常数', from_=10, to=2000, orient=tk.HORIZONTAL,
                       length=200, showvalue=1, tickinterval=500, resolution=1, command=show_change)
change_time.place(x=750, y=20)

window.mainloop()
