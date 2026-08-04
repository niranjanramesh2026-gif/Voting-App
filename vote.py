from tkinter import *
import customtkinter as tk
party1=0
party2=0
window=Tk()
window.title("Entry")
window.geometry("350x500+625+150")
window.configure(bg="#37C0CF")
label2 = Label(window, text="Enter your Party Names", font=("Arial", 20), bg="#37C0CF")
label2.place(x=25, y=0)
label = Label(window, text="Enter your Party(1)", font=("Arial", 15), bg="#37C0CF")
label.place(x=25, y=70)
label1 = Label(window, text="Enter your Party(2)", font=("Arial", 15), bg="#37C0CF")
label1.place(x=25, y=170)
entry = Entry(window, width=20, font=("Arial", 20))
entry.place(x=25, y=100)
entry.focus()
entry.icursor(0)
def f():
   entry1.icursor(0)
window.bind("<Tab>", lambda event: f())
entry1 = Entry(window, width=20, font=("Arial", 20))
entry1.place(x=25, y=200)
window.bind("<Return>", lambda event: submit())
def submit():
  if len(entry.get()) > 0 and len(entry1.get()) > 0 :
    window1= Toplevel()
    window1.focus_set()
    window1.title("Vote machine")
    label3 = Label(window1, text="Vote for your Party", font=("Arial", 20), bg="#37C0CF")
    label3.place(x=50, y=0)
    window1.geometry("350x500+625+150")
    window1.configure(bg="#37C0CF")
    def vote():
        global party1
        party1+=1
    def vote1():
        global party2
        party2+=1
    button = Button(window1, text=entry.get(), font=("Arial", 20), bg="white",command=vote)
    button.place(x=50, y=100)
    button1 = Button(window1   , text=entry1.get(), font=("Arial", 20), bg="white", command=vote1)
    button1.place(x=50, y=200)
    def result():
        window2= Toplevel()
        window2.title("Result")
        window2.geometry("350x500+625+150")
        window2.configure(bg="#37C0CF")
        label4 = Label(window2, text="Result", font=("Arial", 20), bg="black",relief="raised",
                       bd=10,fg="white",width=10)
        label4.place(x=90, y=0)
        label5 = Label(window2, text=f"{entry.get()} : {party1}", font=("Arial", 20), bg="#37C0CF")
        label5.place(x=25, y=100)
        label6 = Label(window2, text=f"{entry1.get()} : {party2}", font=("Arial", 20), bg="#37C0CF")
        label6.place(x=25, y=200)
        if party1 > party2:
            winner = entry.get()
            label7 = Label(window2, text=f"{winner} party won by {abs(party1 - party2)} votes", font=("Arial", 20), bg="black",
                           relief="raised",bd=10,fg="white",width=20)
            label7.place(x=0, y=300)
        elif party1==party2:
            winner = "No one"
            label7 = Label(window2, text=f"{winner} won the election", font=("Arial", 20), bg="black",relief="raised",
                           bd=10,fg="white",width=20)
            label7.place(x=0, y=300)
        else:
            winner = entry1.get()
            label7 = Label(window2, text=f"{winner} party won by {abs(party1 - party2)} votes", font=("Arial", 20), bg="black",
                           relief="raised",bd=10,fg="white",width=20)
            label7.place(x=0, y=300)
        window1.destroy()
    window1.bind("<Return>", lambda event: result())
button2 =tk.CTkButton(window, text="Submit", font=("Arial", 20),command=submit,corner_radius=35, width=70, height=70)
button2.place(x=110, y=275)
window.mainloop()