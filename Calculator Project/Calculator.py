#importing package
import tkinter as tk

calculate = " "

#to take no's and calculate
def to_calculate(symbol):
    global calculate
    calculate += str(symbol)
    dp_result.delete(1.0,"end")
    dp_result.insert(1.0,calculate)


#to evaluate the problem 
def to_evaluate():
    global calculate
    print(calculate)
    try:
        calculate =str(eval(calculate))
        dp_result.delete(1.0,"end")
        dp_result.insert(1.0,calculate)
    except:
        to_clear()
        dp_result.insert(1.0,"Error")
        
    #to clear the data
def to_clear():
    global calculate
    calculate = " "
    dp_result.delete(1.0,"end")
        


#window interface

interface = tk.Tk()


#geomety of window
interface.geometry("300x275")
interface.iconphoto(False,tk.PhotoImage(file = "Calculator.png"))
interface.configure(bg = "cyan")
interface.title("SIMPLE CALCULATOR")



#max and min width and height of window
interface.maxsize(300,300)
interface.minsize(300,316)

#display result
dp_result = tk.Text(interface,height = 2,width = 16,font = ("Arial",24))
dp_result.grid(columnspan=5,padx=(0,0),pady=(25,15))

#creating buttons
btn1 = tk.Button(interface,text= "1",command=lambda:to_calculate(1),width =5 ,font =  ("Arial",14),activebackground="red",bg = "yellow")
btn1.grid(row =2,column =1)


btn2 = tk.Button(interface,text= "2",command=lambda:to_calculate(2),width = 5,font = ("Arial",14),activebackground="red",bg = "yellow")
btn2.grid(row =2,column =2)

btn3 = tk.Button(interface,text= "3",command=lambda:to_calculate(3),width = 5 , font = ("Arial",14),activebackground="red",bg = "yellow")
btn3.grid(row =2,column =3)

btn4 = tk.Button(interface,text= "4",command=lambda:to_calculate(4),width = 5 ,font = ("Arial",14),activebackground="red",bg = "yellow")
btn4.grid(row =3,column =1)

btn5 = tk.Button(interface,text= "4",command=lambda:to_calculate(4),width =5, font =  ("Arial",14),activebackground="red",bg = "yellow")
btn5.grid(row =3,column =2)

btn6 = tk.Button(interface,text= "6",command=lambda:to_calculate(6),width = 5,font = ("Arial",14),activebackground="red",bg = "yellow")
btn6.grid(row =3,column =3)

btn7 = tk.Button(interface,text= "7",command=lambda:to_calculate(7),width =5 ,font =  ("Arial",14),activebackground="red",bg = "yellow")
btn7.grid(row =4,column =1)

btn8 = tk.Button(interface,text= "8",command=lambda:to_calculate(8),width = 5,font = ("Arial",14),activebackground="red",bg = "yellow")
btn8.grid(row =4,column =2)

btn9 = tk.Button(interface,text= "9",command=lambda:to_calculate(9),width =5,font =  ("Arial",14),activebackground="red",bg = "yellow")
btn9.grid(row =4,column =3)

btn0 = tk.Button(interface,text= "0",command=lambda:to_calculate(0),width =5,font =  ("Arial",14),activebackground="red",bg = "yellow")
btn0.grid(row =5,column =2)

#add, mul, minus, sub buttons creation 
btnplus = tk.Button(interface,text= "+",command=lambda:to_calculate("+"),width =5,font =  ("Arial",14),activebackground="blue",bg = "pink")
btnplus.grid(row =2,column =4)

btnminus = tk.Button(interface,text= "-",command=lambda:to_calculate("-"),width =5,font =  ("Arial",14),activebackground="blue",bg = "pink")
btnminus.grid(row =3,column =4)

btnmul = tk.Button(interface,text= "*",command=lambda:to_calculate("*"),width =5,font =  ("Arial",14),activebackground="blue",bg = "pink")
btnmul.grid(row =4,column =4)

btndiv = tk.Button(interface,text= "/",command=lambda:to_calculate("/"),width =5,font =  ("Arial",14),activebackground="blue",bg = "pink")
btndiv.grid(row =5,column =4)


btnopen = tk.Button(interface,text= "(",command=lambda:to_calculate("("),width =5,font =  ("Arial",14),activebackground="blue",bg = "pink")
btnopen.grid(row =5,column =1)

btnclose = tk.Button(interface,text= ")",command=lambda:to_calculate(")"),width =5,font =  ("Arial",14),activebackground="blue",bg = "pink")
btnclose.grid(row =5,column =3)

#functions buttons

btnclear = tk.Button(interface,text= "C",command = to_clear,width =5,font =  ("Arial",14))
btnclear.grid(row =  6,column =1,columnspan=2)

btnequals = tk.Button(interface,text= "=",command = to_evaluate,width =5,font =  ("Arial",14))
btnequals.grid(row =  6,column =3,columnspan=2)


interface.mainloop()
