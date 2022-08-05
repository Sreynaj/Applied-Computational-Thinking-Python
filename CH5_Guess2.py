import random as rand
compnumber = rand.randint(1, 100)
usernumber = int(input("Choose a number between 1 and 100. You'll get 5 guesses or you lose! "))

usernumber = 0
allowed_guess = 5
right_answer = False

while usernumber < allowed_guess and right_answer == False:
    usernumber -=1 
print("Guess time: ",usernumber)

if compnumber == usernumber:
    print("You win!")
else:
    print("You lose!")