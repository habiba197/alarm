from tkinter import *
import datetime
import time
import winsound
import threading


def alarm():
    userTime = f"{hour.get()}:{minute.get()}:{second.get()}"

    if userTime == datetime.datetime.now().strftime("%H:%M:%S"):
        state.config(text="Time to wake up!")
        winsound.PlaySound(r"C:\Users\habiba\OneDrive\Desktop\alarm\ff.Wav", winsound.SND_ALIAS)
        hour.set(hours[0])
        minute.set(minutes[0])
        second.set(seconds[0])
    else:
        state.config(text="Alarm Started", bg="green")
        master.after(1000, alarm)  # Check again in 1000 milliseconds (1 second)


# In your Threading function, call alarm directly (without threading)
def Threading():
    alarm()


master = Tk()
frame = Frame(master)
frame.pack()

master.geometry("400x250")
master.title("Alarm clock")

iconeFrame = PhotoImage(file=r"C:\Users\habiba\OneDrive\Desktop\alarm\icon.png")
master.iconphoto(False,iconeFrame)

appTitle = Label(master,text="Alarm clock",font=("century 20 bold"))
appTitle.pack()

setTimeLabel = Label(master,text="Set Time",font=("Century 15 "))
setTimeLabel.pack()

frame = Frame(master)
frame.pack()

hour = StringVar(master)
hours = []
for num in range (0,25):
    if num <= 9:
        num = '0' + str(num)
    hours.append(num)
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
hour.set(hours[0])

minute = StringVar(master)
minutes = []
for num in range (0,61):
    if num <= 9:
        num = '0' + str(num)
    minutes.append(num)
minu = OptionMenu(frame, minute, *minutes)
minu.pack(side=LEFT)
minute.set(minutes[0])


second = StringVar(master)
seconds= []

for num in range(0,61):
    if num <= 9:
        num= '0' +str(num)
    seconds.append(num)

sec= OptionMenu(frame, second, *seconds)
sec.pack(side=LEFT)
sec.config(font=('centyury 13'))

second.set(seconds[0])

btn=Button(master,text='start alarm',font=('century 14 bold'),fg='white',bg='pink',command=Threading)
btn.pack(pady=10)

state = Label(master , font =("century 10 bold"), fg = "white")
state.pack()
master.mainloop()