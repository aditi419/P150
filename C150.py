from tkinter import *
import random

root = Tk()
root.title('Lucky Friend Wheel')
root.geometry('500x500')

enterName = Entry(root)
enterName.place(relx = 0.5,rely = 0.2,anchor = CENTER)

names = Label(root)
names.place(relx = 0.5,rely = 0.3,anchor = CENTER)

List = []
def addFriend():
    nameValue = enterName.get()
    List.append(nameValue)
    names['text'] = List
    
def random_number():
    randomNum = random.randint(0,len(List))
    indexValue['text'] = randomNum
    luckyFriend['text'] = 'Your Lucky Friend is: ' + List[randomNum]

btn = Button(root,text = 'Add Friend',command = addFriend)
btn.place(relx = 0.5,rely = 0.4,anchor = CENTER)

btn2 = Button(root,text = 'Whos your Lucky Friend?',command = random_number)
btn2.place(relx = 0.5,rely = 0.5,anchor = CENTER)

indexValue = Label(root)
indexValue.place(relx = 0.5,rely = 0.6,anchor = CENTER)

luckyFriend = Label(root)
luckyFriend.place(relx = 0.5,rely = 0.7,anchor = CENTER)

mainloop()