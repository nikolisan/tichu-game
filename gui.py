from tkinter import *
from tkinter import messagebox

from PIL import Image
from PIL import ImageTk
import os


class App:
    def __init__(self,master):
        master.title('Tichu game')
        master.geometry("1000x600")

        self.containers = self.createLayout()
        (top, bot, left, mid, right)=self.containers
        
    def createLayout(self):
        topHBox=Frame(width=1000,height=100,bg="red")
        bottomHBox=Frame(width=1000,height=100,bg="yellow")
        midHBox=Frame(width=1000,height=400,bg="blue")

        leftVBox=Frame(master=midHBox ,width=100,height=400,bg="cyan")
        rightVBox=Frame(master=midHBox ,width=100,height=400,bg="black")
        midVBox=Frame(master=midHBox ,width=800,height=400,bg="green")

        topHBox.pack_propagate(False)
        midHBox.pack_propagate(False)
        bottomHBox.pack_propagate(False)
        leftVBox.pack_propagate(False)
        midVBox.pack_propagate(False)
        rightVBox.pack_propagate(False)
        
        topHBox.pack()
        midHBox.pack()
        bottomHBox.pack()
        leftVBox.pack(side=LEFT)
        midVBox.pack(side=LEFT)
        rightVBox.pack(side=LEFT)

        return(topHBox,bottomHBox,leftVBox,midVBox,rightVBox)
        
    def refresh(self,master,cards):
        cardCountLbl = Label(master, text="Number of cards: {}".format(len(cards)))
        cardCountLbl.pack()
        print(master)
        for i in range (len(cards)):
            print ("update card:",cards[i], "@", master)
            p1= os.path.join(os.getcwd(),'cards')
            p3= ".gif"
            path=p1+'/'+cards[i]+p3

            img = Image.open(path)
            img = img.resize((60,80), Image.ANTIALIAS)
            photoImg =  ImageTk.PhotoImage(img)
            cardWidth=60
            cardHeight=80
            card = Label (master, image=photoImg, width=cardWidth, height=cardHeight)
            card.photo = photoImg
            card.place(relx=0.03*i, rely=1, anchor=SW)
        

root = Tk()
app = App(root)
(top, bot, left, mid, right)=app.containers
root.update()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        quit()

root.protocol("WM_DELETE_WINDOW", on_closing)


while True:
    test_cards = ["5g","6r","Mahjong","Phoenix","Dogs", "Dragon","6r","7b","10r","Jb", "5g","6r","7b","10r"]
    a=input("cards:")
    if a in ["0", 0, "exit"]:
        break
    else:
        if not test_cards:
            cards = a.split(" ")
            print (cards)
        else:
            cards = test_cards

        app.refresh(bot,cards)
        app.refresh(top, ["back" for i in range(14)])
        app.refresh(left, ["back" for i in range(14)])
        app.refresh(right, ["back" for i in range(14)])
        print (a)
        root.update()