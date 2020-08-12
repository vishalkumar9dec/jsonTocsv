"""
A program that stores the book information:
Title, Author, Year, ISBN

User can:

View all records
Search an entry
Add entry
Update Entry
Close
"""

from tkinter import *
from tkinter import filedialog
import json
import ntpath


'''Function definitions'''


def UploadAction(event=None):
    global filename
    filename = filedialog.askopenfilename()
    e1.delete(0,END)
    global fname
    fname = ntpath.basename(filename)
    e1.insert(END, fname)
    a1.delete(0, END)
    a1.insert(END,round(ntpath.getsize(filename)/1024,2))
    y1.delete(0, END)
    y1.insert(END,ntpath.dirname(filename))


def convertfile():

    c1.delete(0, END)
    if fname.split(".")[1] != "json":
        c1.insert(END, "ERROR : Input file is not in JSON format")
    else:
        with open(filename) as f:
            data = json.load(f)


        output_file = filename.split(".")[0]+"_converted.csv"

        with open(output_file, 'a') as file:
            file.write('Username,EventName,EventTime,EventSource,EventType\n')
            for i in range(len(data['Records'])):
                try:
                    uname = data['Records'][i]['userIdentity']['sessionContext']['sessionIssuer']['userName']
                except:
                    uname = ""
                try:
                    eventname = data['Records'][i]['eventName']
                except:
                    eventname = ""
                try:
                    eventtime = data['Records'][i]['eventTime']
                except:
                    eventtime = ""
                try:
                    eventsource = data['Records'][i]['eventSource']
                except:
                    eventsource = ""
                try:
                    eventtype = data['Records'][i]['eventType']
                except:
                    eventtype = ""

                file.write(uname + ',' + eventname + ',' + eventtime + ',' + eventsource + ',' + eventtype + '\n')

        if ntpath.basename(output_file):
            c1.insert(END,"Json file converted to CSV successfully !")
        else:
            c1.insert(END,"Oops! Some Error Occurred")



window = Tk()
window.wm_title("Convert Json To CSV")


l1 = Label(window, text="Filename")
l1.grid(row=0,column=0,padx=10)

l2 = Label(window,text="Size(Kb)")
l2.grid(row=0,column=2)

l3 = Label(window,text="Path")
l3.grid(row=1)

l4 = Label(window,text="INFO")
l4.grid(row=3,column=0,pady=2)

file_name = StringVar()
e1 = Entry(window,textvariable=file_name)
e1.grid(row=0,column=1,ipadx=10,pady=10)

file_size = StringVar()
a1 = Entry(window,textvariable=file_size)
a1.grid(row=0,column=3,pady=10,padx=10)

file_path = StringVar()
y1 = Entry(window,textvariable=file_path,width=63)
y1.grid(row=1,column=1,columnspan=3)

convert_result = StringVar()
c1 = Entry(window,textvariable=convert_result,width=60)
c1.grid(row=3,column=1,columnspan=3,pady=5)


b2 = Button(window,text="Import File",width=12,command=UploadAction)
b2.grid(row=2,column=1,pady=5)

b3 = Button(window,text="Convert",width=12,command=convertfile)
b3.grid(row=2,column=2,pady=5)

b6 = Button(window,text="Close",width=12, command=window.destroy)
b6.grid(row=2,column=3,pady=5)


window.mainloop()