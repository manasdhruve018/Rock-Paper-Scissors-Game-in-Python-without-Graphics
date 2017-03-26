import random
words=('rock','paper','scissors')
Your_Score=0
Computer_Score=0
print('Hey, Welcome..')
print('Do you want to play a game?')
str1=input()
if str1=="YES" or str1=="yes" or str1=="Yes" or str1=="y" or str1=="Y":
	print('If you want to play a Game and have pressed Yes, then you are at a right place..')
	print('We are going to play Rock Paper Scissors Game: ')
	print('Remember the Rules: ')
	print('Rock beats Scissors..')
	print('Scissors beats Paper..')
	print('Paper beats Rock')
	while(True):
		x=random.choice(words)
		print('\n')
		print(x)
		c=input('rock, paper or scissors?')
		if x==c:
			print('Draw!')
			print('\n')
		elif x=="rock" and c=="paper":
			print('You WIN! Paper beats Rock')
			print('\n')
			Your_Score=Your_Score+1
		elif x=="rock" and c=="scissors":
			print('You LOSE! Rock beats Scissors')
			print('\n')
			Computer_Score=Computer_Score+1
		elif x=="paper" and c=="scissors":
			print('You WIN! Scissors beats Paper')
			print('\n')
			Your_Score=Your_Score+1
		elif x=="paper" and c=="rock":
			print('You LOSE! Paper beats Rock')
			print('\n')
			Computer_Score=Computer_Score+1
		elif x=="scissors" and c=="paper":
			print('You LOSE! Scissors beats Paper')
			print('\n')
			Computer_Score=Computer_Score+1
		elif x=="scissors" and c=="rock":
			print('You WIN! Rock beats Scissors')
			print('\n')
			Your_Score=Your_Score+1
		print('Scores are: ')
		print('Computer: ',Computer_Score)
		print('You: ',Your_Score)
		print('Do You want to play again?')
		temp=input();
		if temp=="No" or temp=="no" or temp=="n" or temp=="N":
			break
else:
	System.exit();
