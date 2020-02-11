#!/usr/bin/env python
from __future__ import print_function
from builtins import input
from termcolor import colored
import readchar
from random import randint
import sys
import os
import time
from .data import *
import threading,time
from threading import Lock

data_dir = os.path.join(os.path.dirname(__file__),'data')

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
    def __init__(self,words,list_type):#initialisation
        print(words)
        self.animal = words[randint(0,len(words)-1)].upper()
        self.blanks=len(self.animal)*'_'
        for i,letter in enumerate(self.animal):
            if not letter.isalpha():
                self.blanks = self.blanks[:i]+letter+self.blanks[i+1:]
        os.system("clear")
        #print(hngmn[0])
        #print ('Guess the name of the '+list_type+' letter by letter')
        #print ('Your '+list_type+' is ' ,end='')
        #for letter in self.blanks:
        #    print(letter,end = ' ')
        #print()
        #time.sleep(3)
    
    def Score(self):#displayed at the end
        if self.success_stat == 1:
            Game.win = Game.win + 1 # Game.win will be shared between objects
        else:
            Game.lose = Game.lose + 1

    def Status(self): # Returns current win/lose status
        print("Score is "+colored("win = "+str(Game.win),'green')+" \\ "+colored("lose ="+ str(Game.lose),'red') )
    
    def MainGame(self):#main game method
        while True:
            os.system("clear")
            k='ij'
            print (colored(hngmn[self.s],'magenta')) # Print current state of hangman
            for i in range(len(self.blanks)):
                print(self.blanks[i],end= ' ')
            print()
            print(colored("DONE LETTERS:",'blue'),end='')
            print(*self.done_letters,sep=',')
            while True:
                k=input("Your choice of letter?")
                if len(k)!=1:
                    print('Enter only one letter please')
                    continue
                elif not k.isalpha():
                    print('Enter only alphabets')
                    continue
                elif k.upper() in self.done_letters:
                    print ('The letter entered is already done')
                    k='ij'
                    continue
                else:       
                    k=k.upper()
                    self.done_letters.append(k)
                    break
                    
            if self.animal.find(k)!=-1: # When letter is in the animal name
                #print ('yes the letter \''+colored(k,'red')+'\' is there')
                #time.sleep(2)
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

key = None
def get_key_press():
    global key
    global printing_lock
    while key!='q':
        key = readchar.readchar()
        if key == '\x03':
            raise KeyboardInterrupt

# Start Screen of game
def start_screen():
    i = 0
    global key
    global printing_key
    try:
        while key!='q':
            os.system("clear") # equivalent to typing clear on terminal
            print(colored(hngmn[i%7],'green'))
            print (colored('##### WELCOME TO THE GAME OF HANGMAN #####','yellow'))
            print (colored('####### Save the man from hanging ########','cyan'))
            if i%2 == 0:
                print (colored('       [press <Ctrl + c> to start]','red'))
            time.sleep(0.5) # Animate by giving sleep time
            i+=1
    except:
        pass

def select_type():
    os.system("clear")
    print(colored("Rules: Guess the word letter by letter to save the man from hanging",'blue'))
    print(colored("\n\n\t\tSelect word list\n\t\t1. Animals\n\t\t2. Pokemons\n\t\t3. Fruits\n\t\t4. Countries\n\t\t5. Bollywood Movies","magenta"))
    file_name = None
    lst_type = None
    while True:
        c = readchar.readchar() 
        if c == '1': 
            file_name = 'animals.txt'
            lst_type = 'animals'
            break
        elif c == '2':
            file_name = 'pokemons.txt'
            lst_type = 'pokemons'
            break
        elif c == '3':
            file_name = 'fruits.txt'
            lst_type = 'fruits'
            break
        elif c == '4':
            file_name = 'countries.txt'
            lst_type = 'fruits'
            break
        elif c == '5':
            file_name = 'bollywood movies.txt'
            lst_type = 'bollywood movies'
            break
        elif c == '\x03':
            raise KeyboardInterrupt

    # Open file containing animal names in read-only mode
    #file_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)),DATA_LOCATION,file_name)
    '''
    file_loc = os.path.join(data_dir,file_name)
    f = open(file_loc,'r')

    # Add each animal name on each line to a list 'animals'
    lst =  [x.strip() for x in f.readlines()]
    '''
    lst = word_list[lst_type]
    print(lst)
    return lst_type,lst


# Function for animation after win or lose
# Takes a Game class object as input
def hanging_man_anim(game):  
    i = 0    
    if game.success_stat == 0:
        while i <= 4:
            os.system("clear")
            if i%2 == 0:
                print(colored(hanged_man,'red'))
            else:
                print(colored(hngmn[-1],'red'))
            print(colored(":( !Man Hanged! :(\nCorrect word: ",'red')+colored(game.animal,'green'))
            game.Status()
            time.sleep(0.5)
            i+=1
    else:
        while i <= 4:
            os.system("clear")
            if i%2 == 0:
                print(colored(free_man[0],'green'))
            else:
                print(free_man[1])
            print(colored(":) !Man Saved! :)",'green'))
            game.Status()
            time.sleep(0.5)
            i+=1

def main():
    start_screen()
    list_type,words = select_type()
    print(words)

    while True:#Game loop
        
        game = Game(words,list_type)
        
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
