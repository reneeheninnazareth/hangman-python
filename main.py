import random
import stages
words=["apple","butterfly","mango","coconut","library","potato","file","money"]
chosen_word=random.choice(words)
lives=6
game=True
word_display=[]
for i in range (len(chosen_word)):
    word_display.append('_')

print(word_display)
while(game):
    user_letter=input("Guess a letter:").lower()
    for i in range(len(chosen_word)):
        letter=chosen_word[i]
        if letter==user_letter:
            word_display[i]=letter
    print(word_display)        
    if user_letter not in chosen_word:
        lives-=1
        print('incorrect guess')
    else:
        print('correct guess')
    
    if lives==0:
        print('you lose!!')
        game=False
    if '_' not in word_display:
        print('you win')
        game=False
        break
    print(stages.stages[lives])
    