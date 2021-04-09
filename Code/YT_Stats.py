from tkinter import *
import urllib.request

import json
key="AIzaSyCLHj086Qe-4bCPp8Vyw7RFZeK6SsdMOSA"

def channel_data():
    name=e1.get()
    data=urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+name+"&key="+key).read()
    sub=json.loads(data)['items'][0]["statistics"]["subscriberCount"]
    total_view=json.loads(data)['items'][0]["statistics"]["viewCount"]
    total_videos=json.loads(data)['items'][0]["statistics"]["videoCount"]
    l2.config(text=sub)
    l4.config(text=total_view)
    l6.config(text=total_videos)
interpretor_function=Tk()
interpretor_function.geometry("500x200")
channel_name=StringVar()
e1=Entry(interpretor_function,textvariable=channel_name)
e1.grid(row=1,column=2)
b1=Button(interpretor_function,text="get",command=channel_data)
b1.grid(row=2,column=2)

l1=Label(interpretor_function,text="total number of subscribers: ",font="times 15")
l1.grid(row=4,column=1)
l2=Label(interpretor_function,font="times 15 bold")
l2.grid(row=4,column=3)

l3=Label(interpretor_function,text="total number of Views: ",font="times 15")
l3.grid(row=6,column=1)
l4=Label(interpretor_function,font="times 15 bold")
l4.grid(row=6,column=3)

l5=Label(interpretor_function,text="total number of Videos: ",font="times 15")
l5.grid(row=8,column=1)
l6=Label(interpretor_function,font="times 15 bold")
l6.grid(row=8,column=3)
print("the interpreter window is running")
interpretor_function.mainloop()
print("the interpreter window is closed")
