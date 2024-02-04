from tkinter import *
import math
PINK="#e2979c"
RED="#e7305b"
GREEN="#9bdeac"
YELLOW="#f7f5dd"
FONT_NAME="Courier"
WORK_MIN=25
SHORT_BREAK_MIN=5
LONG_BREAK_MIN=20
reps=0
window=Tk()
window.title("Pomodoro")
def starttimer():
    global reps
    reps+=1
    work_sec=63
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN
    timer=None

    if reps%8==0:
        l1=Label(text="Break",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
        l1.grid(column=1,row=0)
        countdown(long_break_sec)
    elif reps%2==0:
        l1=Label(text="Break",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
        l1.grid(column=1,row=0)
        countdown(short_break_sec)
    else:
        l1=Label(text="Work",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
        l1.grid(column=1,row=0)
        countdown(work_sec)
def reset_timer():
    window.after_cancel(timer)
    l1=Label(text="Timer",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
    l1.grid(column=1,row=0)
    canvas.itemconfig(time,text="00:00")
    checkmark.config(text="")
def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(time,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer= window.after(1000,countdown,count-1)
    else:
        starttimer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
            checkmark.config(text=marks)
        

window.configure(width=200,height=200)
window.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="/Users/HP/Desktop/python/pomodoro/images.png")
canvas.create_image(100,112,image=tomato_img)
time=canvas.create_text(100,120,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
b1=Button(text="Start",command=starttimer)
b1.grid(column=0,row=2)
b2=Button(text="Reset",command=reset_timer)
b2.grid(column=2,row=2)
checkmark=Label(fg=GREEN)
checkmark.grid(column=1,row=2)
window.mainloop()
