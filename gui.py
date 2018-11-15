from tkinter import *
from tkinter import messagebox

from PIL import Image
from PIL import ImageTk

from random import randint
import os


class App:
    def __init__(self,master, *args):
        master.title('Tichu game')
        master.geometry("1000x600")
        master.resizable(False, False)

        self.card_list = args[0]
        self.table_cards = []

        self.containers = self.createLayout()
        (self.top, self.bot, self.left, self.mid, self.right)=self.containers

        self.init_cards = self.get_random_cards(self.card_list)
        self.player_cards, self.com_left, self.com_top, self.com_right = self.init_cards
        self.starting_cards(self.init_cards, self.containers)


        
    def createLayout(self):
        topHBox=Frame(width=1000,height=150,bg="green")
        bottomHBox=Frame(width=1000,height=150,bg="green")
        midHBox=Frame(width=1000,height=300,bg="green")

        leftVBox=Frame(master=midHBox ,width=150,height=400,bg="green")
        rightVBox=Frame(master=midHBox ,width=150,height=400,bg="green")
        midVBox=Frame(master=midHBox ,width=700,height=400,bg="green")

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

    def get_random_cards(self, list_of_cards):
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

    def starting_cards(self, cards, containers):
        player, com_left, com_top, com_right = cards
        top, bot, left, mid, right = containers
        self.refreshPlayersCards(bot, player, "you")
        self.refreshPlayersCards(top, com_top, "2")
        self.refreshPlayersCards(left, com_left, "3")
        self.refreshPlayersCards(right, com_right, "1")
        #Refresh table cards example
        self.refreshTableCards(mid, self.table_cards, "1")

    def clearFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def playCard(self,card):
        self.player_cards.remove(card)
        self.table_cards.append(card)
        self.clearFrame(self.bot)
        self.clearFrame(self.mid)
        self.refreshPlayersCards(self.bot,self.player_cards, "you")
        self.refreshTableCards(self.mid, self.table_cards, "1")
    
    def refreshPlayersCards(self,master,cards,player):
        cardCountLbl = Label(master, text="Player: {}".format(player))
        cardCountLbl.pack()
        cardCountLbl = Label(master, text="Number of cards: {}".format(len(cards)))
        cardCountLbl.pack()
        for i in range (len(cards)):
            if player in ["you", "2"]:
                if player == "2":
                    path = os.path.join(os.getcwd(),'cards','back.gif')
                else:
                    path = os.path.join(os.getcwd(),'cards',cards[i]+'.gif')
                
                img = Image.open(path)
                img = img.resize((60,80), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                cardWidth=60
                cardHeight=80
                card = Label (master, image=photoImg, width=cardWidth, height=cardHeight)
                card.photo = photoImg
                card.place(relx=0.03*i+0.3, rely=0.6, anchor=CENTER)
                card.bind("<Button-1>", lambda e,card=cards[i]:self.playCard(card))

            else:
                path = os.path.join(os.getcwd(),'cards','back.gif')
                img = Image.open(path)
                img = img.rotate(90, expand=1)
                img = img.resize((80,60), Image.ANTIALIAS)
                photoImg =  ImageTk.PhotoImage(img)
                cardWidth=80
                cardHeight=60
                card = Label (master, image=photoImg, width=cardWidth, height=cardHeight)
                card.photo = photoImg
                card.place(relx=0.5, rely=0.8-0.04*i, anchor=CENTER)

    def refreshTableCards(self,master,cards,player):
        cardCountLbl = Label(master, text="Player: {}".format(player)+" play:")
        cardCountLbl.pack()
        for i in range (len(cards)):
            path= os.path.join(os.getcwd(),'cards',cards[i]+'.gif')
            img = Image.open(path)
            img = img.resize((60,80), Image.ANTIALIAS)
            photoImg =  ImageTk.PhotoImage(img)
            cardWidth=60
            cardHeight=80
            card = Label (master, image=photoImg, width=cardWidth, height=cardHeight)
            card.photo = photoImg
            card.place(relx=0.04*i+0.2, rely=0.6, anchor=SW)


#### ΜΑΙΝ ####

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        quit()



if __name__ == "__main__":
    list_of_cards = ['10r', '10c', 'Dogs', 'qg', '2b', '7r', '2r', '3g', 'Kc', 'Jb', '10b', '7c', 'Jr', '9c', '5b', 'Mahjong', '7b', 'qr', '2c', 'Jg', '8b', '9g', '8g', '8r', 'Ab', 'Ar', '5c', 'Ag', 'Kg', '3c', '4g', '9b', '3r', '4b', '8c', '10g', 'qb', '4r', 'Kr', 'Ac', '6c', '2g', '5r', 'qc', 'Dragon', 'Phoenix', '4c', '9r', '3b', '5g', 'Kb', '6r', '6b', '6g', 'Jc', '7g']
    root = Tk()
    app = App(root, list_of_cards)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

# TODO:
#   (✓)(✗)
#   
#   (✓)(1) Create "memory" of each player cards as a list 
#   (✓)(2) Refresh the entire list each time not individual cards
#   (✓)(3) Fix Left-Right Display:
#       - Maybe a new function (?)
