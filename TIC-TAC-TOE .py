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
    global count, clicked,winner,buttonsl
    count=0
    for j in buttonsl:
        j.config(text=" ", bg="White",state="normal")
        
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
b1=Button(window, text=" ", font=("Halvetica", 20),height=4, width=8,bg="White", command=lambda: click(b1))
b2=Button(window, text=" ", font=("Halvetica", 20),height=4, width=8,bg="White", command=lambda: click(b2))
b3=Button(window, text=" ", font=("Halvetica", 20),height=4, width=8,bg="White", command=lambda: click(b3))

#row 2

b4=Button(window, text=" ", font=("Halvetica", 20),height=4, width=8,bg="White", command=lambda: click(b4))
b5=Button(window, text=" ", font=("Halvetica", 20),height=4, width=8,bg="White", command=lambda: click(b5))
b6=Button(window, text=" ", font=("Halvetica", 20),height=4, width=8,bg="White", command=lambda: click(b6))

#row 3  

b7=Button(window, text=" ", font=("Halvetica", 20),height=4, width=8,bg="White", command=lambda: click(b7))
b8=Button(window, text=" ", font=("Halvetica", 20),height=4, width=8,bg="White", command=lambda: click(b8))
b9=Button(window, text=" ", font=("Halvetica", 20),height=4, width=8,bg="White", command=lambda: click(b9))

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

buttonsl=[b1,b2,b3,b4,b5,b6,b7,b8,b9]

#defining a function which will disable the buttons once the game is over

def disable():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    buttonsl=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for i in buttonsl:
        i.config(state="disabled")


#defining a function that check if some one wins

def checkwinner(x):
    global winner
# for  row 1
    if b1["text"] ==x and b2["text"]==x and b3["text"]==x:
        b1.config(bg="Green")
        b2.config(bg="Green")
        b3.config(bg="Green") 
        winner=True
        messagebox.showinfo("Tic Tac Toe", f"{x} is the Winner!")
        disable()
        reset()
    
#for row 2
    elif b4["text"] ==x and b5["text"]==x and b6["text"]==x:
        b4.config(bg="Green")
        b5.config(bg="Green")
        b6.config(bg="Green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", f"{x} is the Winner!")
        disable()
        reset()

#for  row 3
    elif b7["text"] ==x and b8["text"]==x and b9["text"]==x:
        b7.config(bg="Green")
        b8.config(bg="Green")
        b9.config(bg="Green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", f"{x} is the Winner!")
        disable()
        reset()
# for  column 1
    if b1["text"] ==x and b4["text"]==x and b7["text"]==x:
        b1.config(bg="Green")
        b4.config(bg="Green")
        b7.config(bg="Green") 
        winner=True
        messagebox.showinfo("Tic Tac Toe", f"{x} is the Winner!")
        disable()
        reset()
    
#for  column 2
    elif b2["text"] ==x and b5["text"]==x and b8["text"]==x:
        b2.config(bg="Green")
        b5.config(bg="Green")
        b8.config(bg="Green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", f"{x} is the Winner!")
        disable()
        reset()

#for  column 3
    elif b3["text"] ==x and b6["text"]==x and b9["text"]==x:
        b3.config(bg="Green")
        b6.config(bg="Green")
        b9.config(bg="Green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", f"{x} is the Winner!")
        disable()
        reset()

#for  diagonal left
    elif b1["text"] ==x and b5["text"]==x and b9["text"]==x:
        b1.config(bg="Green")
        b5.config(bg="Green")
        b9.config(bg="Green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", f"{x} is the Winner!")
        disable()
        reset()

#for  diagonal right
    elif b3["text"] ==x and b5["text"]==x and b7["text"]==x:
        b3.config(bg="Green")
        b5.config(bg="Green")
        b7.config(bg="Green")
        winner=True
        messagebox.showinfo("Tic Tac Toe", f"{x} is the Winner!")
        disable()
        reset()



# check for tie

    elif count==9 and not winner:
        global buttonsl
        for i in buttonsl:
            i.config(bg="Yellow")
        messagebox.showinfo("Tic Tac Toe", "It is a Tie")
        disable()
        reset()





window.mainloop()
