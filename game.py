import random #To generate Random numbers
import time #To pause the program
import numpy as np #To do matrix operations(Here,to print)
import sys #for exit
class Player:
	
	def __init__(self,playername,superpower): #constructor to set player name
		self.name=playername #Setting typed playername
		self.health=100 #setting predefined health
		self.spower=superpower
		print "\n\nWelcome to the land of unknowns ",self.name,"\n\nYour health now is : ",self.health,"\n\nYour superpower is : ",self.spower
		
class Enemy:
	ename=['Huffy Puffy','Mist Creep','Corpse bug','Evil Pickachu','Zoombie Watermelon']
	health=['20','55','45','40','35','15']
	spower=['Laser beam','Fireball','Hypnotize','Electric Shock','Seduction',]
	def __init__(self):
		self.ename=random.choice(self.ename);
		self.health=int(random.choice(self.health))
		self.spower=random.choice(self.spower)
	def battle(self): 
		print "\n\nYour enemy is : " ,enemy.ename," with fighting capacity ",enemy.health,".","\n\nAttcking you with her superpower ",enemy.spower," !!\nGet ready to fight or die."
		p1.health=int(p1.health)-int(enemy.health) #Reducing the health of the player
		print "\n\tAUTOMATING THE ATTACK.....\n\tATTACK BEGINS.......\n"
		i=3			
		while(i>0):
			word=random.choice(['\nOuch!You got hurt','\nThe Enemy is Angry','\nSheeeesshhh!!!','\nFighting','\nDishkyuuoooo','\nYou are one slep closer to winning','\nHurrraaaaa']	)
			print word,
			time.sleep(0.5)
			print '.',
			time.sleep(0.5)
			print '.'
			i=i-1
		if p1.health>0:
			print "\n\nYour health has decreased to ",p1.health
		else:
			print "\n\n\t\tGAME OVER!\n\n\tRIP TO THE GREAT TREASURE HUNTER\n\nGOOD GAME!ADIOS!"
			sys.exit() #To exit from the program
print "\n\n\n\n\n\n\n\n\t    WELCOME TO THE GAME OF GEM :P\n\t*************************************\n\n"

#Main starts
playername=raw_input("Enter Your Name : \t")
superpower=raw_input("Enter Your Super Power (Fire ball,Sword attack etc.): \t")
print "\n\t\t  Objective of the game\n\n\t\t*************************\n\tRead all instruction\n\tUser postion is represented by '@'\n\tDead monsters are denoted by 'X'\n\tMove across the environment fighting the monsters and the evil force\n\n\tYou win when you reach the treasure.\n\n\tYou cannot go back to the path once travelled and you can only move down or right.\n\n\tThere are hidden monsters in the path.So be careful!\n\n\tTHE GEM IS MARKED AS T\n\n\n"
choice=raw_input("\tWANT TO ENTER THE LAND OF MONSTERS AND TREASURES?(PRESS Y TO CONTINUE) \t:  ")
if choice=='y' or choice=='Y':
	p1=Player(playername,superpower)
	game= [["-" for x in range(9)] for y in range(9)] #Creating a matrix
	game[8][8]='T' #Placing the treasure at bottom right
	x,y=0,0
	game[x][y]='@' #Placing the player at top left
	#Defining the position of enemies
	postionxenemy1=random.choice(range(0,8,1))
	postionxenemy2=random.choice(range(0,8,1))
	postionxenemy3=random.choice(range(0,8,1))
	postionxenemy4=random.choice(range(0,8,1))
	postionyenemy1=random.choice(range(0,8,1))
	postionyenemy2=random.choice(range(0,8,1))
	postionyenemy3=random.choice(range(0,8,1))
	postionyenemy4=random.choice(range(0,8,1))
	postionxenemy5=random.choice(range(0,8,1))
	postionyenemy5=random.choice(range(0,8,1))
	postionxenemy6=random.choice(range(0,8,1))
	postionyenemy6=random.choice(range(0,8,1))
	postionxenemy7=random.choice(range(0,8,1))
	postionyenemy7=random.choice(range(0,8,1))
	postionxenemy8=random.choice(range(0,8,1))
	postionyenemy8=random.choice(range(0,8,1))
	postionxenemy9=random.choice(range(0,8,1))
	postionyenemy9=random.choice(range(0,8,1))
	postionxenemy10=random.choice(range(0,8,1))
	postionyenemy10=random.choice(range(0,8,1))

	while True:
		print "\n\n"
		print(np.matrix(game))
		move=raw_input("\n\nWhere do you want to move?(d=down,r=right,l=left) :\t ")
		
		if (move=='d' and (x+1)<9):
			if (((x+1)==postionxenemy4)and(y==postionyenemy4)):
				enemy=Enemy()
				enemy.battle()
				x=x+1
				game[x][y]='X'
				continue
			if (((x+1)==postionxenemy3)and(y==postionyenemy3)):
				enemy=Enemy()
				enemy.battle()
				x=x+1				
				game[x][y]='X'
				continue
			if (((x+1)==postionxenemy2)and(y==postionyenemy2)):
				enemy=Enemy()
				enemy.battle()
				x=x+1
				game[x][y]='X'
				continue
			if (((x+1)==postionxenemy1)and(y==postionyenemy1)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x+1
			 	game[x][y]='X'
			 	continue
			if (((x+1)==postionxenemy5)and(y==postionyenemy5)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x+1
			 	game[x][y]='X'
			 	continue
			if (((x+1)==postionxenemy7)and(y==postionyenemy7)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x+1
			 	game[x][y]='X'
			 	continue
			if (((x+1)==postionxenemy8)and(y==postionyenemy8)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x+1
			 	game[x][y]='X'
			 	continue
			if (((x+1)==postionxenemy9)and(y==postionyenemy9)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x+1
			 	game[x][y]='X'
			 	continue
			if (((x+1)==postionxenemy10)and(y==postionyenemy10)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x+1
			 	game[x][y]='X'
			 	continue
			
			if (((x+1)==postionxenemy6)and(y==postionyenemy6)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x+1
			 	game[x][y]='X'
			 	continue
			if game[x+1][y]=='T':
				print "\n \n\n\n\t\tCongratulations!!\n\t*********************\nYOU WON\nCollect the reward from the teaching faculty :P\n"
				break
			if game[x+1][y]=='@':
				print 'A Brave warrior does not go back,move forward\n'
				continue
			x=x+1
			game[x][y] = '@'
		
			
		elif (move=='r' and (y+1)<9):
			if ((x==postionxenemy4)and((y+1)==postionyenemy4)):
				enemy=Enemy()
				enemy.battle()
				y=y+1
				game[x][y]='X'
				continue
			if ((x==postionxenemy3)and((y+1)==postionyenemy3)):
				enemy=Enemy()
				enemy.battle()
				y=y+1
				game[x][y]='X'
				continue
			if ((x==postionxenemy2)and((y+1)==postionyenemy2)):
				enemy=Enemy()
				enemy.battle()
				y=y+1
				game[x][y]='X'
				continue
			if ((x==postionxenemy1)and((y+1)==postionyenemy1)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y+1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy5)and((y+1)==postionyenemy5)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y+1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy6)and((y+1)==postionyenemy6)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y+1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy7)and((y+1)==postionyenemy7)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y+1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy8)and((y+1)==postionyenemy8)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y+1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy9)and((y+1)==postionyenemy9)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y+1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy10)and((y+1)==postionyenemy10)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y+1
			 	game[x][y]='X'
			 	continue
			
			if game[x][y+1]=='T':
				print '\n \n\n\n\t\tCongratulations!!\n\t*********************\nYOU WON\nCollect the reward from the teaching faculty :P\n'
				break
			if game[x][y+1]=='@':
				print 'A Brave warrior does not go back,move forward\n'
				continue
			y=y+1
			game[x][y]='@'


	
		elif (move=='l' and (y-1)>=0):
			if ((x==postionxenemy4)and((y-1)==postionyenemy4)):
				enemy=Enemy()
				enemy.battle()
				y=y-1
				game[x][y]='X'
				continue
			if ((x==postionxenemy3)and((y-1)==postionyenemy3)):
				enemy=Enemy()
				enemy.battle()
				y=y-1
				game[x][y]='X'
				continue
			if ((x==postionxenemy2)and((y-1)==postionyenemy2)):
				enemy=Enemy()
				enemy.battle()
				y=y-1
				game[x][y]='X'
				continue
			if ((x==postionxenemy1)and((y-1)==postionyenemy1)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y-1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy5)and((y-1)==postionyenemy5)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y-1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy6)and((y-1)==postionyenemy6)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y-1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy7)and((y-1)==postionyenemy7)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y-1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy8)and((y-1)==postionyenemy8)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y-1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy9)and((y-1)==postionyenemy9)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y-1
			 	game[x][y]='X'
			 	continue
			if (((x)==postionxenemy10)and((y-1)==postionyenemy10)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	y=y-1
			 	game[x][y]='X'
			 	continue
			
			if game[x][y-1]=='T':
				print '\n \n\n\n\t\tCongratulations!!\n\t*********************\nYOU WON\nCollect the reward from the teaching faculty :P\n'
				break
			if game[x][y-1]=='@':
				print 'A Brave warrior does not go back,move forward\n'
				continue
			y=y-1
			game[x][y]='@'

		elif (move=='u' and (x-1)>=0):
			if (((x-1)==postionxenemy4)and(y==postionyenemy4)):
				enemy=Enemy()
				enemy.battle()
				x=x-1
				game[x][y]='X'
				continue
			if (((x-1)==postionxenemy3)and(y==postionyenemy3)):
				enemy=Enemy()
				enemy.battle()
				x=x-1				
				game[x][y]='X'
				continue
			if (((x-1)==postionxenemy2)and(y==postionyenemy2)):
				enemy=Enemy()
				enemy.battle()
				x=x-1
				game[x][y]='X'
				continue
			if (((x-1)==postionxenemy1)and(y==postionyenemy1)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x-1
			 	game[x][y]='X'
			 	continue
			if (((x-1)==postionxenemy5)and(y==postionyenemy5)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x-1
			 	game[x][y]='X'
			 	continue
			if (((x-1)==postionxenemy7)and(y==postionyenemy7)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x-1
			 	game[x][y]='X'
			 	continue
			if (((x-1)==postionxenemy8)and(y==postionyenemy8)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x-1
			 	game[x][y]='X'
			 	continue
			if (((x-1)==postionxenemy9)and(y==postionyenemy9)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x-1
			 	game[x][y]='X'
			 	continue
			if (((x-1)==postionxenemy10)and(y==postionyenemy10)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x-1
			 	game[x][y]='X'
			 	continue
			
			if (((x-1)==postionxenemy6)and(y==postionyenemy6)):
			 	enemy=Enemy()
			 	enemy.battle()
			 	x=x-1
			 	game[x][y]='X'
			 	continue
			if game[x-1][y]=='T':
				print "\n \n\n\n\t\tCongratulations!!\n\t*********************\nYOU WON\nCollect the reward from the teaching faculty :P\n"
				break
			if game[x-1][y]=='@':
				print 'A Brave warrior does not go back,move forward\n'
				continue
			x=x-1
			game[x][y] = '@'
		

else:
	print "\n\nGAME TERMINATED!\nCOME BACK TO FIND THE GEM SOME OTHER DAY"			
		
		
