import random
rndm_number = random.randrange(100)
chances = 7
guess_counter = 0
while guess_counter< chances:
    guess = int(input('Guess the number'))
    guess_counter+=1
    if guess == rndm_number:
        print(f'The number you guess is correct in the {guess_counter} attempt')
        break
    elif guess!= rndm_number and guess_counter >= chances:
        print('oops you have reached max no of chances better luck next time')
    elif guess > rndm_number:
        print('Your guess is greater than guess number')
    elif guess < rndm_number:
        print('your guess is smaller than guess number')
