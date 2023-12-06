import random
wordlist = ['floor','rice','afraid','baseball','heady','tidy','dark','nation','public','fluttering','chivalrous','decorous','concentrate','tough','thoughtless','narrow','popcorn','cooing','battle','expert','animated','oven','numberless','remarkable','juvenile','chickens','learn','route','approval','perfect','bumpy','women','clever','same','disagree','jelly','club','song','selection','special','seashore','fill','serious','uttermost','ball','bent','impartial','handle','kaput','alike']
word = random.choice(wordlist)
blank = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

chance8 = """
--------------------
                   |
                   |
                   |
                   |
                   |
                 -----
"""
chance7 = """
--------------------
                   |
                   |
                   |
                   |
                   |
                 -----
"""
chance6 = """
--------------------
         0         |
                   |
                   |
                   |
                   |
                 -----
"""
chance5 = """
--------------------
         0         |
         |         |
                   |
                   |
                   |
                 -----
"""
chance4 = """
--------------------
         0         |
         |         |
        /          |
                   |
                   |
                 -----
"""
chance3 = """
--------------------
         0         |
         |         |
        / \        |
                   |
                   |
                 -----
"""
chance2 = """
--------------------
         0         |
         |\        |
        / \        |
                   |
                   |
                 -----
"""
chance1 = """
--------------------
         0         |
        /|\        |
        / \        |
                   |
                   |
                 -----
"""


stages = [chance1,chance2,chance3,chance4,chance5,chance6,chance7,chance8]
score = 0
chances = 8
correctguess = []
play = True
wrongguesses = []
length = len(word)
cover = ""
for x in range(length):
    cover = cover + "-"
    
while play == True:
    print(blank)
    print(f"word has {length} letters")
    print(cover)
    print("incorrect guesses :",wrongguesses)
    print(stages[chances-1])
    guess = input("guess a letter/word:\n	")
    
    if guess in word:  
        correctguess.append(guess)
        for x in range(length):
            if word[x] == guess:
                cover = cover[:x]+guess+cover[x+1:]
                score += 1
    if guess == word:
        cover = word
        score = (length)
        
        
    elif guess in wrongguesses:
        None
    elif guess in cover:
        None
    else:
        chances -= 1
        wrongguesses.append(guess)
        
        
    if chances == 0:
        play = False

    if score == len(word):
        play = False
print(blank)
print(f"word has {length} letters")
print(cover)
print("incorrect guesses :",wrongguesses)
print(stages[chances-1])        
if chances == 0:
    print(f"You lose, the word was {word}")
if score == len(word):
    print(f"You win, the word was {word} ")

            
