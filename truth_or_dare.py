import tkinter as tk
from random import *
import datetime
now = datetime.datetime.now()
seed(now)
truths=["When was the last time you lied?",
"When was the last time you cried?",
"What's your biggest fear?",
"What's your biggest fantasy?",]
dares=["Balance a spoon on your nose for 10 second",
"Hold a cup of water over your head and jump without spilling it",
"Bite a lemon.","Spin around 10 times and try to walk a straight line",]
def dare():
    dare_out_put=choice(dares)
    print(dare_out_put)
def truth():
    truth_out_put=choice(truths)
    print(truth_out_put)
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
button=tk.Button(frame,text="Truth",fg="red",command=truth)
button.pack(side=tk.LEFT)
DareButton=tk.Button(frame,text="Dare",command=dare)
DareButton.pack(side=tk.LEFT)
root.mainloop()
