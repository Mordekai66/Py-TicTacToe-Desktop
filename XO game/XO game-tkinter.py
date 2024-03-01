from tkinter import *
from tkinter import messagebox
def restart_game():
    bt1.config(state=NORMAL, text="",relief=RAISED,background="whitesmoke")
    bt2.config(state=NORMAL, text="",relief=RAISED,background="whitesmoke")
    bt3.config(state=NORMAL, text="",relief=RAISED,background="whitesmoke")
    bt4.config(state=NORMAL, text="",relief=RAISED,background="whitesmoke")
    bt5.config(state=NORMAL, text="",relief=RAISED,background="whitesmoke")
    bt6.config(state=NORMAL, text="",relief=RAISED,background="whitesmoke")
    bt7.config(state=NORMAL, text="",relief=RAISED,background="whitesmoke")
    bt8.config(state=NORMAL, text="",relief=RAISED,background="whitesmoke")
    bt9.config(state=NORMAL, text="",relief=RAISED,background="whitesmoke")

sign="X"

def check_win():
    if bt1.cget("text") == "X" and bt5.cget("text") == "X" and bt9.cget("text") == "X":
        bt1.config(background="green",fg="red")
        bt5.config(background="green",fg="red")
        bt9.config(background="green",fg="red")
    elif bt7.cget("text") == "X" and bt5.cget("text") == "X" and bt3.cget("text") == "X":
        bt7.config(background="green",fg="red")
        bt5.config(background="green",fg="red")
        bt3.config(background="green",fg="red")
    elif (bt1.cget("text") == "X" and bt2.cget("text") == "X" and bt3.cget("text") == "X"):
        bt1.config(background="green",fg="red")
        bt2.config(background="green",fg="red")
        bt3.config(background="green",fg="red")
    elif (bt4.cget("text") == "X" and bt5.cget("text") == "X" and bt6.cget("text") == "X"):
        bt4.config(background="green",fg="red")
        bt5.config(background="green",fg="red")
        bt6.config(background="green",fg="red")
    elif(bt7.cget("text") == "X" and bt8.cget("text") == "X" and bt9.cget("text") == "X"):
        bt7.config(background="green",fg="red")
        bt8.config(background="green",fg="red")
        bt9.config(background="green",fg="red")
    elif (bt1.cget("text") == "X" and bt4.cget("text") == "X" and bt7.cget("text") == "X"):
        bt1.config(background="green",fg="red")
        bt4.config(background="green",fg="red")
        bt7.config(background="green",fg="red")
    elif(bt2.cget("text") == "X" and bt5.cget("text") == "X" and bt8.cget("text") == "X"):
        bt2.config(background="green",fg="red")
        bt5.config(background="green",fg="red")
        bt8.config(background="green",fg="red")
    elif(bt3.cget("text") == "X" and bt6.cget("text") == "X" and bt9.cget("text") == "X"):
        bt3.config(background="green",fg="red")
        bt6.config(background="green",fg="red")
        bt9.config(background="green",fg="red")

    if (bt1.cget("text") == "O" and bt5.cget("text") == "O" and bt9.cget("text") == "O"):
        bt1.config(background="green",fg="red")
        bt5.config(background="green",fg="red")
        bt9.config(background="green",fg="red")
    elif (bt7.cget("text") == "O" and bt5.cget("text") == "O" and bt3.cget("text") == "O"):
        bt7.config(background="green",fg="red")
        bt5.config(background="green",fg="red")
        bt3.config(background="green",fg="red")
    elif(bt1.cget("text") == "o" and bt2.cget("text") == "O" and bt3.cget("text") == "O"):
        bt1.config(background="green",fg="red")
        bt2.config(background="green",fg="red")
        bt3.config(background="green",fg="red")
    elif(bt4.cget("text") == "O" and bt5.cget("text") == "O" and bt6.cget("text") == "o"):
        bt4.config(background="green",fg="red")
        bt5.config(background="green",fg="red")
        bt6.config(background="green",fg="red")
    elif(bt7.cget("text") == "O" and bt8.cget("text") == "O" and bt9.cget("text") == "O"):
        bt7.config(background="green",fg="red")
        bt8.config(background="green",fg="red")
        bt9.config(background="green",fg="red")
    elif(bt1.cget("text") == "O" and bt4.cget("text") == "O" and bt7.cget("text") == "O"):
        bt1.config(background="green",fg="red")
        bt4.config(background="green",fg="red")
        bt7.config(background="green",fg="red")
    elif(bt2.cget("text") == "O" and bt5.cget("text") == "O" and bt8.cget("text") == "O"):
        bt2.config(background="green",fg="red")
        bt5.config(background="green",fg="red")
        bt8.config(background="green",fg="red")
    elif(bt3.cget("text") == "O" and bt6.cget("text") == "O" and bt9.cget("text") == "O"):
        bt3.config(background="green", fg="red")
        bt6.config(background="green",fg="red")
        bt9.config(background="green",fg="red")
            
            
    elif ((bt1.cget("text") != "" and bt5.cget("text") != "" and bt9.cget("text") != "")
        and (bt7.cget("text") != "" and bt5.cget("text")!= "" and bt3.cget("text") != "")
        and (bt1.cget("text") != "" and bt2.cget("text")!= "" and bt3.cget("text") != "")
        and (bt4.cget("text") != "" and bt5.cget("text") != "" and bt6.cget("text") != "")
        and (bt7.cget("text") != "" and bt8.cget("text") != "" and bt9.cget("text")!= "")
        and (bt1.cget("text") != "" and bt4.cget("text") != "" and bt7.cget("text") != "")
        and (bt2.cget("text") != "" and bt5.cget("text") != "" and bt8.cget("text") != "")
        and (bt3.cget("text") != "" and bt6.cget("text") != "" and bt9.cget("text") != "")):
        pass

def convert1(bt):
    global sign
    if sign=="X":
        bt.config(state=DISABLED,relief="sunken",text="X")
        sign="O"
        check_win()
    else:
        bt.config(state=DISABLED,text="O",relief="sunken")
        sign="X"
        check_win()

pro=Tk()
pro.config(background="#5D6D7E")
pro.geometry('324x327')
pro.resizable(False,False)

bt=Button(pro,width=1,height=1,text='Restart_game',command=restart_game)
bt.pack(fill=X)
bt1=Button(pro,width=14,height=6,command=lambda:convert1(bt1))
bt1.place(x=0,y=27)
bt2=Button(pro,width=14,height=6,command=lambda:convert1(bt2))
bt2.place(x=0,y=129)
bt3=Button(pro,width=14,height=6,command=lambda:convert1(bt3))
bt3.place(x=0,y=231)

bt4=Button(pro,width=14,height=6,command=lambda:convert1(bt4))
bt4.place(x=108,y=27)
bt5=Button(pro,width=14,height=6,command=lambda:convert1(bt5))
bt5.place(x=108,y=129)
bt6=Button(pro,width=14,height=6,command=lambda:convert1(bt6))
bt6.place(x=108,y=231)

bt7=Button(pro,width=14,height=6,command=lambda:convert1(bt7))
bt7.place(x=216,y=27)
bt8=Button(pro,width=14,height=6,command=lambda:convert1(bt8))
bt8.place(x=216,y=129)
bt9=Button(pro,width=14,height=6,command=lambda:convert1(bt9))
bt9.place(x=216,y=231)

pro.mainloop()