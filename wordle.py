import random

with open('words.txt') as f:
    lines = f.readlines()

words = []

for line in lines:
    words.append(line)

def esc(ansiCode):
    return f'\033[{ansiCode}m'

count = 0
roundCount = 1
winHistory = 0
while(True):
    
    if count == 1:
        cmd = input("start game? (y/n/rules): ")
        print("\n")
        
    else:
        cmd = input("play again? (y/n/rules): ")
        count = 0
        print("\n")

    if cmd == 'rules':
        print("\nGuess the WORDLE in six tries.")
        print("Each guess must be a valid five-letter word. Hit the enter button to submit.")
        print("After each guess, the color of the letters will change to show how close your guess was to the word.\n")
        cmd = input("start game? (y/n): ")

    if cmd == 'n':
        print("exiting...\n")
        break
    
    elif cmd == 'y':

        print("\n--------------------------ROUND " + str(roundCount) + "--------------------------")

        #repeats = int(input("how many chances do you want? (1-10): "))

        rand = random.randint(0, len(words)-1)
        word = words[rand]
        print(word)

        for i in range(6):
            attempt = input("attempt: ")

            if len(attempt) != 5:
                attempt = input("word length must be 5. enter another word: ")

            output = ""
            similar = 0

            for i in range(5):
                if attempt[i] == word[i]:
                    output = output + esc('32') + attempt[i] + esc(0)
                    similar = similar + 1
                elif attempt[i] in word:
                    output = output + esc('33') + attempt[i] + esc(0)
                else:
                    output = output + attempt[i]

            print(output + "\n")

            if similar == 5:
                count = count + 1 
                winHistory = winHistory + 1
                if count == 1:
                    print("wordle solved in 1 try!")
                else:
                    print("wordle solved in " + str(count) + " tries!")
                break

    else:
        print("invalid cmd. valid commands: y/n/rules.")

    roundCount = roundCount + 1


    
    
