import random

def give_instructions():
    print('''\n Wordle is a word guessing game.
    You have 5 attempts
    (✔) means the letter is in the word and in the correct position
    (:O) means the letter is in the word and in the wrong position
    (❌) means the letter is not in the word
         
         Good Luck!!!\n''')

words = ["pink","this","help","five", "meow", "help"]

hidden_word = random.choice(words)


def check_word(guess):
    if hidden_word == guess:
            print("Congrats!! You did it!")
            return True
    else:
        result = ""
        for i,j in zip(guess, hidden_word):           #Zip() pairs the iterations
            if i == j:
                result = result + "(✔)"
            elif i in hidden_word:
                result = result + "(:O)"
            else:
                result = result + "(❌)"
        print(result)
        return False
    
def main():
    give_instructions()
    attempt = 5
    while attempt > 0:
        guess = input("Enter a four letter word: ")
        if check_word(guess):
            break
        else:
            attempt -= 1
            print(f'You have {attempt} attempts left.')
    else:
        print("Game Over!!!!")
        
main()



