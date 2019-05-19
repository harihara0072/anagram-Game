# anagram-Game

### Algorithm:

- First, we need to ask the user for the file name and check if it is valid. 
- We need to open and read the lines in the file.
- After creating the dictionary with each word as the key and its meaning as the value, we need to choose a key in random by using the random library.
- Then again by using the random library we need to shuffle the key.
- Then we need to print the shuffled key for the user to guess.
- The number of attepts permitted are equal to the length of the word that needs to be guessed.
- An hint will be provided (The meaning of the word) by entering '?'
- Also, we need to keep track of number of attempts the user made along with the number of times the hint(?) is taken. An attempt will be counted after one warning on the second entry of '?'.
- We need to repeat the steps if the user guess the word correctly within the given number of attepts or he exceepts the attempts by asking if the user wants to continue or not.

### Instructions for running the program:

> Run the following three cells in sequence to execute the program.

### Expected output:


> Give the name of the 'words and their meanings' file:mywords.txt

> Do you want to play:Y

> Unscramble the following letters to form a word. Type '? for the meaning of the unscrambled word: enypur

> Unscramble the following letters to form a word. Type '? for the meaning of the unscrambled word: enypur

> Enter the answer [or ? for the meaning]: ?

> The word means: extremely poor

> Enter the answer [or ? for the meaning]: penur

> Wrong, try again

> Enter the answer [or ? for the meaning]: penury

> You got it!
