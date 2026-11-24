import random

guess_count=0

print('Welcome to the Cow and Bull Game...!')

number = str(random.randint(1000,9999))

while True:
    guess = input('Guess the 4 digit Number:')

    if len(guess)!=4 or not guess.isdigit():
        print('Enter a Valid 4 digit Number')
        continue

    guess_count+=1

    cow = 0
    bull = 0

    remaining_number = []
    remaining_guess = []

    for i in range(4):
        if guess[i] == number[i]:
            cow+=1
        else:
            remaining_number.append(number[i])
            remaining_guess.append(guess[i])

    for digit in remaining_guess:
        if digit in remaining_number:
            bull+=1
            remaining_number.remove(digit)

    print(f'{cow} Cow')
    print(f'{bull} Bull')

    if(guess == number):
        print('Congratulations ! You guessed the Correct Number')
        print(f'Total Guesses: {guess_count}')
        break