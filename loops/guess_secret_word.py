# Design a program that uses a while loop and continuously asks the user to 
# enter a word unless the user enters "chupacabra" as the secret exit word, in which case 
# the message "You've successfully left the loop." should be printed to the screen, 
# and the loop should terminate.

secret_word = "chupacabra"
word = input("Enter the secret word!: ")

while True:
    if word == secret_word:
        break
    word = input("Wrong word muggle, gess again!")
print("Lucky muggle! You've successfully left the loop.")