import random

word_list = ["cat", "dog", "bunny", "variable", "mountain", "vibes", "popcorn", "hat", "backpack"]
n = random.randint(0, len(word_list)-1)
word = word_list[n]
print(word)
letters = []
guess_counter = []
def readWord(word):
    for i in range(0,len(word)):
        letters.append(word[i]) 
    print("The word is", len(letters), "letters long")
    return letters


def guess(letter):
    if letter not in letters:
        guess_counter.append(1)
        print(letter, "is not in the word, you have", str(5-len(guess_counter)), "guesses remaining")
    else:
        correct = "true"
        x=0
        while x<len(letters):
            if letter == letters[x]:
                print(letter, "is letter", x+1, "in the word")
                x= x+1
            else:
                x = x+1
    return guess_counter     

def ask():
    print("Take a guess")
    user_input = input()
    finish = 0
    if user_input == "word":
        print("you may guess the word")
        user_word = input()
        if user_word == word:
            print("You guessed it, great job!")
            finish = 1
        else:
            guess_counter.append(1)
            print("Not quite, you have", str(5-len(guess_counter)), "guesses left")
    else:
        guess(user_input)
    if len(guess_counter) == 5:
        finish =1
        print("Sorry, you lost")
    return finish

def game():
    while ask() == 0:
        ask()
        continue
    

    
print("Welcome to hangman")
print("When you want to guess the word type 'word' and you will be prompted")
readWord(word)
game()
