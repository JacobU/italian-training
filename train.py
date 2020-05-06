import sys
import random

def train(diff="easy"):
    
    with open("words.txt", "r") as rf:
        if rf.mode == "r":
            print("Welcome to your training session. Your mode is: ", diff)
            print("To end your session, type: 'exit'")
            if diff == "easy":
                lives = 3
            elif diff == "medium":
                lives = 2
            elif diff == "hard":
                lives = 1
            
            lines = rf.readlines()
            # Get the number of words in the practise list
            numWords = len(lines) / 2

            random.seed()

            # Continue until the user exits: Ctrl + C
            while(True):
                guesses = 0

                # Choose a random word
                choice = random.randint(0, numWords - 1)
                
                italWord = lines[ ( choice * 2 ) ]
                engWord = lines[ ( choice * 2 ) + 1 ]

                italWord = italWord.rstrip()
                engWord = engWord.rstrip()

                # Display the word to the user
                print(italWord)
                
                # Get the users input
                while(lives - guesses > 0):
                    guess = input()
                    if guess == "exit":
                        rf.close()
                        sys.exit()
                    if(guess == engWord):
                        print("Correct!\n")
                        break
                    else: 
                        guesses += 1
                        if lives - guesses == 0:
                            print("Sorry, the english word is: ", engWord, "\n")
                            break
                        # Depending on the number of guesses, give them a hint
                        print("Hint: ", engWord[0:guesses])



if __name__ == "__main__":
    if len(sys.argv) > 2:
        raise Exception("You have entered too many arguments. Please choose either [easy] [medium] or [hard] mode.")
    
    if len(sys.argv) == 1:
        train()

    if len(sys.argv) == 2:
        # Diff = difficulty
        diff = sys.argv[1]
        if(diff != "easy" and diff != "medium" and diff != "hard"):
            raise Exception("You have entered an invalid difficulty. The options are [easy] [medium] or [hard]")
        else:
            train(diff)

    