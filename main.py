# tkinter GUI para app
from tkinter import *
from tkinter import ttk

window = Tk()
window.iconbitmap("calc-icon.ico")  
window.title("GUI Calculator")

window.geometry("250x350")
window.resizable(False, False)
window.grid_rowconfigure(0, weight=0) 
window.grid_rowconfigure(1, weight=1) 
window.grid_columnconfigure(0, weight=1)

# display 
display = Frame(window, height=80, bg='#303338')
display.grid(row=0, column=0, sticky="ew")

# body
display_body = Frame(window, bg="#D9D9D9")
display_body.grid(row=1, column=0, sticky="nsew")

# app funcs
all_values = ""

#func input values
def values(event):
    global all_values
    all_values = all_values + str(event)
    text_value.set(all_values)

#func calculate values
def calculate():
    result = eval(all_values)
    text_value.set(str(result))

#func clear display
def clear_display():
    global all_values
    all_values = ""
    text_value.set("")

for i in range(4):
    display_body.grid_columnconfigure(i, weight=1)
for i in range(5):
    display_body.grid_rowconfigure(i, weight=0, minsize=60)

#label
text_value = StringVar()

app_label = Label(display, textvariable=text_value, width=15, height=2,padx=10, pady=10,
                  bg='#303338', fg='white', anchor='e',)
app_label.pack(expand=True, fill='both')

# line 1
b_1 = Button(display_body, command= clear_display,text="C", bg='pink', borderwidth=0,
             activebackground="#D60F6F", activeforeground='white',
             font=('Arial', 13, 'bold'))
b_1.grid(row=0, column=0, columnspan=2, sticky="nsew")

b_2 = Button(display_body, command= lambda: values('%'), text="%", bg="#578EE7", borderwidth=0,
             activebackground="#131C9A", activeforeground='white')
b_2.grid(row=0, column=2, sticky="nsew")

b_3 = Button(display_body, command= lambda: values('/'), text="/", bg="#FFFFFF", borderwidth=0,
             activebackground="#3E3E42", activeforeground='white')
b_3.grid(row=0, column=3, sticky="nsew")

# line 2
b_4 = Button(display_body, command= lambda: values('7'), text="7", bg="#D31D1D", borderwidth=0,
             activebackground="#7F0A0A", activeforeground='white')
b_4.grid(row=1, column=0, sticky="nsew")

b_5 = Button(display_body, command= lambda: values('8'), text="8", bg="#3CE73C", borderwidth=0,
             activebackground="#13621D", activeforeground='white')
b_5.grid(row=1, column=1, sticky="nsew")

b_6 = Button(display_body, command= lambda: values('9'), text="9", bg="#BBEB5D", borderwidth=0,
             activebackground="#5C6F11", activeforeground='white')
b_6.grid(row=1, column=2, sticky="nsew")

b_7 = Button(display_body, command= lambda: values('*'), text="*", bg="#D1FB01", borderwidth=0,
             activebackground="#5A592C", activeforeground='white')
b_7.grid(row=1, column=3, sticky="nsew")

# line 3
b_8 = Button(display_body, command= lambda: values('4'), text="4", bg="#D31D1D", borderwidth=0,
             activebackground="#7F0A0A", activeforeground='white')
b_8.grid(row=2, column=0, sticky="nsew")

b_9 = Button(display_body, command= lambda: values('5'), text="5", bg="#3CE73C", borderwidth=0,
             activebackground="#13621D", activeforeground='white')
b_9.grid(row=2, column=1, sticky="nsew")

b_10 = Button(display_body, command= lambda: values('6'), text="6", bg="#BBEB5D", borderwidth=0,
             activebackground="#5C6F11", activeforeground='white')
b_10.grid(row=2, column=2, sticky="nsew")

b_11 = Button(display_body, command= lambda: values('-'), text="-", bg="#D1FB01", borderwidth=0,
             activebackground="#5A592C", activeforeground='white')
b_11.grid(row=2, column=3, sticky="nsew")

# line 4
b_12 = Button(display_body, command= lambda: values('1'), text="1", bg="#D31D1D", borderwidth=0,
              activebackground="#7F0A0A", activeforeground='white')
b_12.grid(row=3, column=0, sticky="nsew")

b_13 = Button(display_body, command= lambda: values('2'), text="2", bg="#3CE73C", borderwidth=0,
              activebackground="#13621D", activeforeground='white')
b_13.grid(row=3, column=1, sticky="nsew")

b_14 = Button(display_body, command= lambda: values('3'), text="3", bg="#BBEB5D", borderwidth=0,
              activebackground="#5C6F11", activeforeground='white')
b_14.grid(row=3, column=2, sticky="nsew")

b_15 = Button(display_body, command= lambda: values('+'), text="+", bg="#D1FB01", borderwidth=0,
              activebackground="#5A592C", activeforeground='white')
b_15.grid(row=3, column=3, sticky="nsew")

# line 5
b_16 = Button(display_body, command= lambda: values('0'), text="0", bg="#D31D1D", borderwidth=0,
              activebackground="#7F0A0A", activeforeground='white')
b_16.grid(row=4, column=0, columnspan=2, sticky="nsew")

b_17 = Button(display_body, command= lambda: values('.'), text=".", bg="#3CE73C", borderwidth=0,
              activebackground="#13621D", activeforeground='white')
b_17.grid(row=4, column=2, sticky="nsew")

b_18 = Button(display_body, command= calculate, text="=", bg="#BBEB5D", borderwidth=0,
              activebackground="#5C6F11", activeforeground='white')
b_18.grid(row=4, column=3, sticky="nsew")


window.mainloop()