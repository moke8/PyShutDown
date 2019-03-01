from tkinter import *    #UI库
from tkinter import messagebox  #消息弹出
import os           #用于执行cmd命令
import string       #StringVar要用    字符串钩子

def text():          #判断是否是数字并将小时处理为秒
    i=time.get()     #获得字符串钩子的值
    try:              #错误抓捕     判断是否为数字
        i=str(int(float(i)*60*60))
    except ValueError:
        messagebox.showwarning(title="输入错误",message="请输入一个数字！")  #警告消息弹窗
    else:
        result=shutdown(i)
             
def shutdown(i=False):     #执行cmd语句以设置定时关机
    if i==False:
        result=os.system("shutdown -a")
        if result:
            messagebox.showwarning(title="错误",message="当前无定时关机任务")
            return 0
    else:
        result=os.system("shutdown -s -t "+i)
        if result:
            result=os.system("shutdown -a")
            if not result:
                result=os.system("shutdown -s -t "+i)

    if not result:
        messagebox.showinfo(title="状态信息",message="成功！")
    else:
        messagebox.showerror(title="错误",message="未知原因失败")
        
soft=Tk()
soft.geometry('200x90+885+465')       #初始化窗口大小信息
soft.resizable(0, 0)                  #设置窗口大小不可更改
text1=Label(soft,text="您需要几小时后关机？（支持小数）",compound="center").grid(row=0,column=0,columnspan=2,padx=0,pady=0)     #文本
time=StringVar()             #声明字符串钩子
time.set("1")                #设置初始值
text2=Entry(soft,textvariable=time).grid(row=1,column=0,columnspan=2,padx=5,pady=0)          #设置文本框    grid为设置在窗口初始化时的位置（表格方式）
button1=Button(soft,text="取消任务",command=shutdown).grid(row=2,column=0,padx=5,pady=10)
button2=Button(soft,text="设置任务",command=text).grid(row=2,column=1,padx=5,pady=10)
soft.mainloop() #运行





