from random import randint
print '##### WELCOME TO THE GAME OF HANGMAN #####'
animals = ['tiger','lion','dog','hyena','elephant','albatross','porcupine']
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




r=1
c=0
while r==1:
	
	s=0
	k='ij'
	
	animal = animals[randint(0,6)]
	blanks=len(animal)*'_ '
	print 'Your animal is ' + len(animal)*'_ '
	print 'You have to guess the name of the animal letter by letter'
	while s<=6:
		while len(k)!=1:
			k=raw_input("your choice of letter?")
			
			if len(k)!=1:
				print'enter only one letter please'
			else:		
				k=k.lower()
		if animal.find(k)!=-1:
			print 'yes the letter '+k+' is there'
			i=0
			while i<len(animal):
				if animal[i]==k:
					blanks=blanks[:i*2]+k+' '+blanks[i*2+2:]
				i=i+1	
			print 'the new word is'
			print blanks
		else:
			print'sorry entered letter is not there'
			print'the condition of the hangman now is'
			print hngmn[s]
			s=s+1
		if blanks.find('_')==-1:
			c=1
			break
		else:
			k='ij'
			continue
	if c==0:
		print 'sry u lost'
	else: 
		print 'congo u won'
	q=raw_input("another game?")
	if q=='yes':
		c=0
		continue
	else:
		break
		
			
			
			
		
		
		
		
		
		
		
