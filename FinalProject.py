import random

### Perhaps put this in a "while guesscounter != 0" loop, so the game can be replayed
### As is, once the guesscounter reaches zero, you are allowed to continue making guesses as the counter goes into the negatives.

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
            finish = 1
            print("You guessed it, great job!")
            return finish
        else:
            guess_counter.append(1)
            print("Not quite, you have", str(5-len(guess_counter)), "guesses left")
    else:
        guess(user_input)
    if finish == 0:
        if len(guess_counter) > 4:
            finish =1
            print("Sorry, you lost")
            print("Word was: " + str(word))
    return finish

def game():
    while ask() == 0:
        ask()
    

    
print("Welcome to hangman")
print("When you want to guess the word type 'word' and you will be prompted")
readWord(word)
game()
