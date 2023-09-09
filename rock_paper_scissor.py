#      ////////////////////// ROCK PAPER SCISSOR GAME ///////////////////////////
import random 
def user():
  while True:
    user_=input("Enter your choice (rock/paper/scissors) : ").lower()
    if user_ in ["rock","paper","scissor"]:
     return user_
    else:
       print("Wrong input !! Again enter ")

def computer():
   computer_=['rock','paper','scissor']
   return random.choice(computer_)

user_input=user()
computer_input=computer()
print(f"Player 1 choice is : {user_input}")
print(f"Player 2 choice is : {computer_input}")

if(user_input==computer_input):
  print("Tie")
elif(user_input=='scissor'and computer_input=='rock'):
  print("You Loose")
elif(user_input=='paper'and computer_input=='scissor'):
  print("You Loose")
elif(user_input=='rock'and computer_input=='paper'):
  print("You Loose")
elif(user_input=='scissor'and computer_input=='paper'):
  print("You Win")
elif(user_input=='paper'and computer_input=='rock'):
  print("You Win")
elif(user_input=='rock'and computer_input=='scissor'):
  print("You Win")
