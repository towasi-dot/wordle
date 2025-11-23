import random

words = ["brisk", "flame", "crypt", "shard", "tower"]
word = random.choice(words)

print("Welcome to Wordle!")
print("C = letter is on that place, O = letter is in this word but not on that place, N = letter is not in this word \n")

for i in range(1, 7):
    letters = ["N" for k in range(5)]
    wordInput = input(f"\n{i}. ")
    while len(wordInput) != 5:
        print("Wrong input! Try again!")
        wordInput = input(f"{i}. ")
    for j in range(5):
        if wordInput[j] == word[j]:
            letters[j] = "C"
        elif wordInput[j] in word:
            letters[j] = "O"
        else:
            letters[j] = "N"

    l1, l2, l3, l4, l5 = letters
    print(l1, l2, l3, l4, l5)

    if letters == ["C" for k in range(5)]:
        print(f"\nCongrats! You guessed the word after {i} tries!")
        break