from tkinter import *
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

        for i in range (len(cards)):
            
            print ("update card:",cards[i])
            p1= os.path.join(os.getcwd(),'cards')
            p3= ".gif"
            path=p1+'/'+cards[i]+p3
            print (path)

            img = Image.open(path)
            img = img.resize((60,80), Image.ANTIALIAS)
            photoImg =  ImageTk.PhotoImage(img)
            cardWidth=60
            cardHeight=80
            card = Label (master, image=photoImg, width=cardWidth, height=cardHeight)
            card.photo = photoImg
            
            card.pack(side=LEFT, expand=YES)
        

root = Tk()
app = App(root)
(top, bot, left, mid, right)=app.containers
root.update()

while True:
    a=input("cards:")
    cards = a.split(" ")
    print (cards)
    
    app.refresh(top,cards)
    print (a)
    root.update()