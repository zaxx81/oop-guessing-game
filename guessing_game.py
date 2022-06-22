import random

class GuessingGame():

    def __init__(self, our_num):
        self.our_num = our_num
        self.guess_num = 0

    def guess(self, guess_num):
        self.guess_num = int(guess_num)
        if(self.guess_num < self.our_num):
            return 'low'
        elif(self.guess_num > self.our_num):
            return 'high'
        else:
            return 'correct'
    
    def solved(self):
        if(self.guess_num == self.our_num):
            return True
        else:
            return False

game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = input("Enter your guess: ")
  last_result = game.guess(last_guess)

print(f"{last_guess} was correct!")