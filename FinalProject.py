import random

### Perhaps put this in a "while guesscounter != 0" loop, so the game can be replayed
### As is, once the guesscounter reaches zero, you are allowed to continue making guesses as the counter goes into the negatives.

word_list = ["bunny", "variable", "mountain", "vibes", "popcorn", "backpack", "rule", "patient", "beneficiary", "collect", "mess", "unpleasant", "clash", "apology", "stain", "guide", "negotiation", "standard", "childish", "forge", "angel", "node", "chief", "thick", "bulletin", "user", "safety", "appearance", "mutter", "institution", "action", "justice", "review", "partner", "origin", "occupation", "authority", "wedding", "blonde", "excavate", "ambiguity", "delicate", "government", "figure", "recycle", "harvest", "bedroom", "platform", "poison", "board", "pursuit", "excess", "business", "telephone", "absence", "revival", "calendar", "cooperative", "competition", "insight", "bucket", "dessert", "talented", "strange", "relax", "spread", "owner", "daughter", "pollution", "population"]
n = random.randint(0, len(word_list)-1)
word = word_list[n]
letters = []
dashes = []
guess_counter = []
guesses = []
def readWord(word):
    for i in range(0,len(word)):
        letters.append(word[i]) 
    for i in range(0, len(letters)):
        dashes.append("_")
    print("The word is", len(letters), "letters long")
    b = " ".join(dashes)
    print(b)
    return letters


def guess(letter):
    if letter not in letters:
        guess_counter.append(1)
        print(letter, "is not in the word, you have", str(6-len(guess_counter)), "guesses remaining")
    else:
        x=0
        while x<len(letters):
            if letter == letters[x]:
                print(letter, "is letter", x+1, "in the word")
                dashes[x] = letter
                x= x+1
            else:
                x = x+1
    guesses.append(letter)
    b = " ".join(dashes)
    print(b)
    return guess_counter     

def ask():
    print("Take a guess")
    user_input = input()
    finish = 0
    if user_input == "guesses":
        a = ",".join(guesses)
        print(a)
    elif user_input == "word":
        print("you may guess the word")
        user_word = input()
        if user_word == word:
            finish = 1
            print("You guessed it, great job!")
            return finish
        else:
            guess_counter.append(1)
            print("Not quite, you have", str(6-len(guess_counter)), "guesses left")
    else:
        guess(user_input)
    if finish == 0:
        if len(guess_counter) > 5:
            finish =1
            print("Sorry, you lost")
            print("Word was: " + str(word))
    return finish

def game():
    done = 0
    while done == 0:
        done = ask()
    
print("Welcome to hangman")
print("When you want to guess the word type 'word' and you will be prompted")
print("If you would like to see your previous guesses type 'guesses'" )
readWord(word)
game()
    



