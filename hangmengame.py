import random
def chhose_world():
    words=["python","saloni","programming","developer","language"]
    return random.choice(words)
def display_word(word,guess_letter):
    display=""
    for letter in word:
        if letter in guess_letter:
            display+=letter
        else:
            display += "_"
    return display
def hangman():
    word_to_guess=chhose_world()
    guess_letter=[]
    attemps=6
    print("Welcome to hangman !")
    while attemps>0:
        current_display=display_word(word_to_guess,guess_letter)
        print(f"Currently world:{current_display}")
        guess=input("Guess a letter :").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Entera valid single letter.")
            continue
        if guess in guess_letter:
            print("you've already guessed that letter. Try agaimn.")
            continue
        guess_letter.append(guess)
        if guess not in word_to_guess:
            attemps-=1
            print("Worng Guess! attempts Left:{attemps}")
        if "_" not in display_word(word_to_guess,guess_letter):
            print("Congratulation! you guess the word.")
    if attemps==0:
        print(f"Sorry! you ran out of attemps. The word was :{word_to_guess}")
hangman()  




