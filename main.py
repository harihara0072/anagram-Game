# Importing the random library
import random

#Asking the user to enter the file name

file_name = input("Give the name of the 'words and their meanings' file:")

#Using the try catch to check if the file is valid or not

try:
    
    #Opening the file and reading the lines of the file
    file = open(file_name)
    file_data = file.readlines()
    
    #Creating a dictionary to save the words os the keys and meanings as the values
    words ={}
    
    #Reading the lines of teh file and striping the newline charecter and spliting the line with delimiter ','
    for line in file_data:
        line = line.rstrip('\n').split(',')
        words[line[0]] = line[1]
    
    #Randomly choosing the number between 0 and num of the words in the file and using that number to choose that word for guessing
    random_key = random.choice(list(words.keys())).lower()
    random_key_list = list(random_key)
    
    #shuffling the chosen word using the random library
    random.shuffle(random_key_list)
    scrambled_key = "".join(random_key_list).lower()

    
    #Using the count variable to count the number of attempts user made
    count = 0 
    
    #Using the infinite While loop to ask if the user wants to play or not
    while True:
        temp = input("Do you want to play:" )
        
        #If user chooses N it will break the infinite whle loop.
        if temp.lower() == "n":
            break
        elif temp.lower() == "y":
            count = 0
            
            #Counting the number of time the help is taken
            question_count = 0
            
            #Printing the user to guess the word
            print("Unscramble the following letters to form a word. Type '? for the meaning of the unscrambled word: " + scrambled_key)
            
            #If the attempts are remaining
            while count < len(scrambled_key): 
                entered_text =input("Enter the answer [or ? for the meaning]: ").lower()
                
                #If the user enters the right word
                if entered_text == random_key:
                    print("You got it!")
                    break
                    
                #If the user takes the help for the first time
                elif entered_text == "?" and question_count == 0:
                    print("The word means: " + words[random_key])
                    question_count = 1
                    
                #If the user asks for the help second time a warning will be given
                elif entered_text == "?" and question_count == 1:
                    print("You have been given the meaning before. Next time you ask for the meaning it will count as an attempt!")
                    question_count = 2
                
                #An attempt will be counted if the user asks for the help more than twice after a warning
                elif entered_text == "?" and question_count > 1:
                    print("Meaning has already been given and attempt counted")
                    count += 1            
                
                #If the user makes a wrong guess
                else:
                    print("Wrong, try again")
                    count += 1
                    
        #If the user entered any other value apart from Y or N 
        else:
            print("Please enter a valid choice")

#Printing the error message if the file name is wrong.            
except:
    print("Enter a valid filename")
