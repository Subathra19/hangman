import time
import random
def play():
    print ("Start guessing...")
    time.sleep(0.5)
    wordbank = ["avocado", "chicken", "funds", "bankrupt", "cushion", "filming", "apartment", "radio", "detective", "vinegar", "curtains", "carpet", "addictive", "control", "raining", "sunshine", "diamond", "charcoal", "chocolate", "container", "cubes", "fan", "processor", "sunbed", "towel", "jellyfish", "meals"]
    word=random.choice(wordbank)

    guesses = ''

    #determine the number of turns
    turns = 5

    while turns > 0:        
        failed = 0                 
        for char in word:      
            if char in guesses:    
                print (char)    
            else:
                print ("_")     
                failed += 1    
        if failed == 0:        
            print ("You won")  
            break              

        guess = input("Guess a character:") 
        guesses += guess.lower()                    

        if guess not in word:  
            turns -= 1 
            if turns==4:
                print("   _____ \n"
                     "  |      \n"
                     "  |      \n"
                     "  |      \n"
                     "  |      \n"
                     "  |      \n"
                     "  |      \n"
                     "__|__\n")
                print ("Wrong")    
                print ("You have", + turns, 'more guesses')

            if turns==3:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")       
                print ("Wrong")    
                print ("You have", + turns, 'more guesses')

            if turns==2:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     | \n"
                      "  |     | \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print ("Wrong")    
                print ("You have", + turns, 'more guesses')

            if turns==1:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")

                print ("Wrong")    
                print ("You have", + turns, 'more guesses')

            if turns == 0:   
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")        
                print("You Lose")  
                print("Actual word is: {}".format(word))

def main():
    #to make the player to play again and again
    play_again = ''
    while play_again.lower() != "no":
        play()
        print ("\nDo you want to play again?")
        play_again = input("Type yes or no:")

name = input("\nWhat is your name? ")
print("\nHello, {}. Let's play hangman!".format(name))
print (" ")
main()
