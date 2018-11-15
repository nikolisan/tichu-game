from tkinter import *
from tkinter import messagebox

from PIL import Image
from PIL import ImageTk

from random import randint
import os


class App:
    def __init__(self,master):
        master.title('Tichu game')
        master.geometry("1000x600")
        master.resizable(False, False)

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
        for i in range (len(cards)):
            print ("update card:",cards[i], "@", master)
            path= os.path.join(os.getcwd(),'cards',cards[i]+'.gif')

            img = Image.open(path)
            img = img.resize((60,80), Image.ANTIALIAS)
            photoImg =  ImageTk.PhotoImage(img)
            cardWidth=60
            cardHeight=80
            card = Label (master, image=photoImg, width=cardWidth, height=cardHeight)
            card.photo = photoImg
            card.place(relx=0.03*i+0.25, rely=1, anchor=SW)
        
        


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        quit()

def starting_cards(cards, top, bot, left, mid, right):
    player, com_left, com_top, com_right = cards
    app.refresh(bot, player)
    app.refresh(top, com_top)
    app.refresh(left, com_left)
    app.refresh(right, com_right)

def get_random_cards(list_of_cards):
    player_cards = []
    com_left = []
    com_top = []
    com_right = []
    for i in range(14):
        card_index = randint(0, len(list_of_cards)-1)
        player_cards.append(list_of_cards[card_index])
        del list_of_cards[card_index]
    
    for i in range(14):
        card_index = randint(0, len(list_of_cards)-1)
        com_left.append(list_of_cards[card_index])
        del list_of_cards[card_index]
    
    for i in range(14):
        card_index = randint(0, len(list_of_cards)-1)
        com_top.append(list_of_cards[card_index])
        del list_of_cards[card_index]

    for i in range(14):
        card_index = randint(0, len(list_of_cards)-1)
        com_right.append(list_of_cards[card_index])
        del list_of_cards[card_index]
    
    return(player_cards, com_left, com_top, com_right)


root = Tk()
app = App(root)
(top, bot, left, mid, right)=app.containers
list_of_cards = ['10r', '10c', 'Dogs', 'qg', '2b', '7r', '2r', '3g', 'Kc', 'Jb', '10b', '7c', 'Jr', '9c', '5b', 'Mahjong', '7b', 'qr', '2c', 'Jg', '8b', '9g', '8g', '8r', 'Ab', 'Ar', '5c', 'Ag', 'Kg', '3c', '4g', '9b', '3r', '4b', '8c', '10g', 'qb', '4r', 'Kr', 'Ac', '6c', '2g', '5r', 'qc', 'Dragon', 'Phoenix', '4c', '9r', '3b', '5g', 'Kb', '6r', '6b', '6g', 'Jc', '7g']
init_cards = get_random_cards(list_of_cards)
starting_cards(init_cards, top, bot, left, mid, right)
root.update()
root.protocol("WM_DELETE_WINDOW", on_closing)



while True:
    a=input("cards:")
    if a in ["0", 0, "exit"]:
        break
    else:
        cards = a.split(" ")
        print (cards)
        app.refresh(bot,cards)
        print (a)
        root.update()

# TODO:
#   (1) Create "memory" of each player cards as a list
#   (2) Refresh the entire list each time not individual cards
#   (3) Fix Left-Right Display:
#       - Maybe a new function (?)