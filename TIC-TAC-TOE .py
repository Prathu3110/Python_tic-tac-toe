from tkinter import *
from tkinter import messagebox
#making windows
window=Tk()
window.title("prathyumna's TIC TAC TOE" )
window.geometry("414x448")


# defining a function for when button clicked

clicked=True
count=0
winner=False

#defining a reset function which resets the game once its over
def reset():
    global count, clicked,winner
    count=0
    b1.config(text=" ", bg="#FAE392",state="normal")
    b2.config(text=" ", bg="#FAE392",state="normal")
    b3.config(text=" ", bg="#FAE392",state="normal")
    b4.config(text=" ", bg="#FAE392",state="normal")
    b5.config(text=" ", bg="#FAE392",state="normal")
    b6.config(text=" ", bg="#FAE392",state="normal")
    b7.config(text=" ", bg="#FAE392",state="normal")
    b8.config(text=" ", bg="#FAE392",state="normal")
    b9.config(text=" ", bg="#FAE392",state="normal")

# defining a function for when button clicked
def click(b):
    global clicked, count
    if b["text"]==" " and clicked==True:
        b["text"] = "X"
        clicked=False
        count+=1
        checkwinner("X")
    elif b["text"]==" " and clicked==False:
        b["text"] = "O"
        clicked=True
        count+=1
        checkwinner("O")
    else:
        messagebox.showerror("Wrong move", "This box is already chosen")

# making buttons
#row 1
b1=Button(window, text=" ", font=("calming", 20),height=4, width=8,bg="#FAE392", command=lambda: click(b1))
b2=Button(window, text=" ", font=("calming", 20),height=4, width=8,bg="#FAE392", command=lambda: click(b2))
b3=Button(window, text=" ", font=("calming", 20),height=4, width=8,bg="#FAE392", command=lambda: click(b3))

#row 2

b4=Button(window, text=" ", font=("calming", 20),height=4, width=8,bg="#FAE392", command=lambda: click(b4))
b5=Button(window, text=" ", font=("calming", 20),height=4, width=8,bg="#FAE392", command=lambda: click(b5))
b6=Button(window, text=" ", font=("calming", 20),height=4, width=8,bg="#FAE392", command=lambda: click(b6))

#row 3  

b7=Button(window, text=" ", font=("calming", 20),height=4, width=8,bg="#FAE392", command=lambda: click(b7))
b8=Button(window, text=" ", font=("calming", 20),height=4, width=8,bg="#FAE392", command=lambda: click(b8))
b9=Button(window, text=" ", font=("calming", 20),height=4, width=8,bg="#FAE392", command=lambda: click(b9))

# creating grid for the buttons

b1.grid(column=0 , row=0)
b2.grid(column=1 , row=0)
b3.grid(column=2 , row=0)


b4.grid(column=0 , row=1)
b5.grid(column=1 , row=1)
b6.grid(column=2 , row=1)


b7.grid(column=0 , row=2)
b8.grid(column=1 , row=2)
b9.grid(column=2 , row=2)



#defining a function which will disable the buttons once the game is over

def disable():
    b1.configure(state='disabled')
    b2.configure(state='disabled')
    b3.configure(state='disabled')

    b4.configure(state='disabled')
    b5.configure(state='disabled')
    b6.configure(state='disabled')

    b7.configure(state='disabled')
    b8.configure(state='disabled')
    b9.configure(state='disabled')


#defining a function that check if some one wins

def checkwinner(player):
    global winner
# for x and row 1
    if b1["text"] ==player and b2["text"]==player and b3["text"]==player:
        b1.config(bg="#1A5D1A")
        b2.config(bg="#1A5D1A")
        b3.config(bg="#1A5D1A") 
        winner=True
        messagebox.showinfo("Tic Tac Toe", "X is the Winner!")
        disable()
        reset()
    
#for x and row 2
    elif b4["text"] ==player and b5["text"]==player and b6["text"]==player:
        b4.config(bg="#1A5D1A")
        b5.config(bg="#1A5D1A")
        b6.config(bg="#1A5D1A")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "X is the Winner!")
        disable()
        reset()

#for x and row 3
    elif b7["text"] ==player and b8["text"]==player and b9["text"]==player:
        b7.config(bg="#1A5D1A")
        b8.config(bg="#1A5D1A")
        b9.config(bg="#1A5D1A")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "X is the Winner!")
        disable()
        reset()
# for x and column 1
    if b1["text"] ==player and b4["text"]==player and b7["text"]==player:
        b1.config(bg="#1A5D1A")
        b4.config(bg="#1A5D1A")
        b7.config(bg="#1A5D1A") 
        winner=True
        messagebox.showinfo("Tic Tac Toe", "X is the Winner!")
        disable()
        reset()
    
#for x and column 2
    elif b2["text"] ==player and b5["text"]==player and b8["text"]==player:
        b2.config(bg="#1A5D1A")
        b5.config(bg="#1A5D1A")
        b8.config(bg="#1A5D1A")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "X is the Winner!")
        disable()
        reset()

#for x and column 3
    elif b3["text"] ==player and b6["text"]==player and b9["text"]==player:
        b3.config(bg="#1A5D1A")
        b6.config(bg="#1A5D1A")
        b9.config(bg="#1A5D1A")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "X is the Winner!")
        disable()
        reset()

#for x diagonal left
    elif b1["text"] ==player and b5["text"]==player and b9["text"]==player:
        b1.config(bg="#1A5D1A")
        b5.config(bg="#1A5D1A")
        b9.config(bg="#1A5D1A")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "X is the Winner!")
        disable()
        reset()

#for x diagonal right
    elif b3["text"] ==player and b5["text"]==player and b7["text"]==player:
        b3.config(bg="#1A5D1A")
        b5.config(bg="#1A5D1A")
        b7.config(bg="#1A5D1A")
        winner=True
        messagebox.showinfo("Tic Tac Toe", "X is the Winner!")
        disable()
        reset()

# check for tie

    elif count==9 and winner == False:
        b1.config(bg="#F1C93B")
        b2.config(bg="#F1C93B")
        b3.config(bg="#F1C93B")
        b4.config(bg="#F1C93B")
        b5.config(bg="#F1C93B")
        b6.config(bg="#F1C93B")
        b7.config(bg="#F1C93B")
        b8.config(bg="#F1C93B")
        b9.config(bg="#F1C93B")
        messagebox.showinfo("Tic Tac Toe", "It is a Tie")
        disable()
        reset()



checkwinner('X')
checkwinner('O')

window.mainloop()
