from __future__ import print_function
from builtins import input

from random import randint
import sys
import os
import time

# Open file containing animal names in read-only mode
f = open('animals.txt','r')

# Add each animal name on each line to a list 'animals'
animals =  [x.strip() for x in f.readlines()]

# hangman sprites
hngmn = ['''
             
                +---+
                |   |
                    |
                    |
                    |
                    |
              =========''', '''
             
                +---+
                |   |
                O   |
                    |
                    |
                    |
              =========''', '''
             
                +---+
                |   |
                O   |
                |   |
                    |
                    |
              =========''', '''
             
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
              =========''', '''
             
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
              =========''', '''
             
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
              =========''', '''

                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
              =========''']

hanged_man = '''

                +---+
                |   |
               _O_  |
                |   |
               / \  |
                    |
              ========='''

free_man = ['''

                +---+
                    |
                    |
               _O_  |
                |   |
               | |  |
              =========''','''

                +---+
                    |
                    |
               \O/  |
                |   |
               | |  |
              =========''']



class Game:
    #fields
    win = 0
    lose = 0
    success_stat = 0
    s=0
    animal='dog'
    blanks='_'
    done_letters=['ij']
    
    
    #methods
    def __init__(self):#initialisation
        self.animal = animals[randint(0,len(animals)-1)]
        self.blanks=len(self.animal)*'_'
        os.system("clear")
        print(hngmn[0])
        print ('You have to guess the name of the animal letter by letter')
        print ('Your animal is ' + len(self.animal)*'_ ')
        time.sleep(5)
    
    def Score(self):#displayed at the end
        if self.success_stat == 1:
            Game.win = Game.win + 1 # Game.win will be shared between objects
        else:
            Game.lose = Game.lose + 1

    def Status(self): # Returns current win/lose status
        print("score is win = "+str(Game.win)+" \ lose ="+ str(Game.lose) )
    
    def MainGame(self):#main game method
        while True:
            os.system("clear")
            k='ij'
            print (hngmn[self.s]) # Print current state of hangman
            for i in range(len(self.blanks)):
                print(self.blanks[i],end= ' ')
            print()
            while len(k)!=1: #while input length is different from 1
                k=input("your choice of letter?")
                if len(k)!=1:
                    print('enter only one letter please')
                    continue
                elif k.lower() in self.done_letters:
                    print ('the letter entered is already done')
                    k='ij'
                    continue
                else:       
                    k=k.lower()
                    self.done_letters.append(k)
                    break
                    
            if self.animal.find(k)!=-1: # When letter is in the animal name
                print ('yes the letter \''+k+'\' is there')
                time.sleep(2)
                i=0
                while i<len(self.animal):
                    if self.animal[i]==k:
                        self.blanks=self.blanks[:i]+k+self.blanks[i+1:]
                    i=i+1   
            else:
                self.s=self.s+1 # wrong selection counter 
            
            if self.blanks.find('_')==-1: # No blanks found
                print('entered')
                self.success_stat=1
                break
                    
            if self.s==len(hngmn): # Hangman Complete
                self.success_stat=0
                break

# Start Screen of game
def start_screen():
    i = 0
    try:
        while True:
            os.system("clear") # equivalent to typing clear on terminal
            print(hngmn[i%7])
            print ('##### WELCOME TO THE GAME OF HANGMAN #####')
            print ('####### Save the man from hanging ########')
            if i%2 == 0:
                print ('        [press Ctrl+C to start]')
            time.sleep(0.5) # Animate by giving sleep time
            i+=1
    except KeyboardInterrupt: # Catch Keyboard interrupt error and pass
        pass


# Function for animation after win or lose
# Takes a Game class object as input
def hanging_man_anim(game):  
    i = 0    
    if game.success_stat == 0:
        while i <= 4:
            os.system("clear")
            if i%2 == 0:
                print(hanged_man)
            else:
                print(hngmn[-1])
            print(":( !Man Hanged! :(\nCorrect word: "+game.animal)
            game.Status()
            time.sleep(0.5)
            i+=1
    else:
        while i <= 4:
            os.system("clear")
            if i%2 == 0:
                print(free_man[0])
            else:
                print(free_man[1])
            print(":) !Man Saved! :)")
            game.Status()
            time.sleep(0.5)
            i+=1

start_screen()

while True:#Game loop
    
    game = Game()
    
    game.done_letters=[]
    
    game.MainGame()
    
    game.Score()
    hanging_man_anim(game)
    #game.Score()
    
    exit_question = input("another game?(y/n)")
    break_flag = 0
    while True:
        if (exit_question =='y'):
            break
        elif (exit_question == 'n'):
            break_flag =1
            break   
        else:
            exit_question = input("please type (y/n)")

    if break_flag != 0:
       break
