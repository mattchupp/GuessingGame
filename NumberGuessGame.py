"""
    *Guessing Game

    *Matt Chupp

    *Last Edited - 5/4/14

This program takes an input, does some multiplication/division/etc. to the
number and then the user has ten tries to guess the number 

"""

#User Input

number = float(raw_input("Enter Any Number -> "))
new_number = 0


# taking number and changing it based on the value

if number > 400:
    new_number = number / 30

if number >= 100 and number < 400:
    new_number = (number + 10) / 4

if number < 100 and number > 50:
    new_number = (number / 3) + 7

if number > 0 and number <= 50:
    new_number = number - 6

if number <= 0:
    new_number = number + 200

#start the guessing


guess_count = 0  #set the guess count = 0 to start 


while guess_count < 10:
    guess = float(raw_input("Guess what your new number is --> "))

    if guess == new_number:
        print "You win! Your number was %s." %(new_number)
        break
    
    else:
        guess_count = guess_count + 1
        
        if guess > new_number:
            print "Your guess is too high!"
        elif guess < new_number:
            print "Your guess is too low!"
                  
        guess_left = 10 - guess_count # set num of guesses left
        
        if guess_left > 0:
            print "Number of guesses left: %s" %(guess_left)
        
        elif guess_left == 0:     
            print "You are out of guesses! Your number was %s." %(new_number)

    
    




