import random
#number that randomly picked by system to guess
def random_system_number():
    original_number = random.randint(0,10)
    return original_number

#to get a guessing number from the user
#to calucuate the number of number of guesses completed
def User_input_number():
    user_Guess = input("Guess the number between 0 to 10 ")
    if(user_Guess.isdigit()):
        return int(user_Guess)
    else:
        User_input_number()
     

def Guess_game(number):
    result = False
    no_guesses = 0
    for i in range(3):
        Guess = User_input_number()
        no_guesses += 1
        if(number < Guess):
            print("Your Guess is Too High")
            
        elif(number > Guess):
            print("Your Guess is Too Low")
        else:
            result = True
            break

    if (result):   
        print(f"Congratulations, The correct Number Is {number}. You Gussed it Correctly")
    else:]
        print(f"You have completed {no_guesses} Guesses, Try again.")

def main():
    number = random_system_number()
    #Guess = User_input_number()
    Guess_game(number)
    

if __name__ == "__main__":
    main()