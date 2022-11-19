import random
import random
from hangman_words import word_list
print("hello world !")

chosen_word= random.choice(word_list)
word_length = len(chosen_word)
end_game = False
lives = 6


from hangmanimg import logo
print(logo)


display = []\

for  _ in range(word_length):
    display.append("_")
print(display)


while not end_game:
    guess= input("enter the leeter theta may be present in the random word ").lower()
    if guess in display:
        print ( f"already guessed:{guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"the guessed is not in the word {guess}, ou losss a life")
        lives-=1
        if lives==0:
            end_game= True
            print("you lose")
    print(f"{''.join(display)}")

    if "_" not in display:
        end_game = True
        print("you win")
    from hangmanimg import stages
    print(stages[lives])