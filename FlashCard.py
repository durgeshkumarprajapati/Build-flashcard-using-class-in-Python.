import random
class FlashCard:
    def __init__(self):
        self.dict={'Banana':'yellow','Grapes':'Green','Apple': 'Red','Mango': 'Yellow','Kiwi': 'Brown','Blueberry': 'Blue','Blackberry': 'Black'}
        self.fruit,self.color=random.choice(list(self.dict.items()))
        color=input(f"Enter the color of {self.fruit}")
        if color==self.color:
            print("correct")
        else:
            print("wrong")
while True:
    c=input("Do you want to play(y/n):")
    if c=='y' or c=='Y':
        f=FlashCard()
    else:
        break;
