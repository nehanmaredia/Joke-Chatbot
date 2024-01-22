"""
File:APCSP Chatbot Hackathon
Author(s): Vishnu Guntakala , Nehan Maredia
Date:November 8th 2023
Description: This program replicates a chatbot that tells the user jokes based off of user responses
"""

#Sources: https://medium.com/artisanal-article-machine/no-the-other-side-is-not-a-metaphor-for-death-in-the-chicken-joke-357c1788de43

# -------- IMPORTS/LIBRARIES --------
#This library allows for the jokes to be randomized when the user asks for them
import random


# -------- DEFINED FUNCTIONS --------
#This function finds the user a random joke, and then deletes it from the list to make sure that it is not used again
def find_joke():
    random_joke = random.choice(joke_list)
    print(random_joke)
    joke_list.remove(random_joke)


#This function starts the jokebot and asks the user if they want to hear a joke
def intro_chat():
  #This is the introduction, and it asks for the user's name
  print("Hi! My name is Jokebot!")
  ask_user = input("What is your name? ")
  
  #This prints the users name and asks them if they want to hear a joke
  print(" ")
  ask_user_joke = input("Hi " + ask_user + ", do you want to hear a joke? Respond with Yes or No: ")
  #If they don't want to hear a joke, it will say goodbye and then quit the program
  if ask_user_joke.lower() == "no":
    print(" ")
    print("Okay, maybe next time!")
    quit()
  
  #If they do want to hear a joke, it will find a joke using the find_joke() function
  if ask_user_joke.lower() == "yes":
    print(" ")
    find_joke()

# -------- MAIN CODE / SEQUENCING --------
#This is the list from which the program gets jokes from to tell the user
joke_list = [
    "Why did the chicken cross the road? To get to the other side!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the banana go to the doctor? Because it wasn't peeling well!",
    "Why did the cookie go to the doctor? Because it was feeling crumbly!",
    "Why did the frog call his insurance company? He had a jump!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "Why don't eggs tell jokes? Because they might crack up!",
    "Why don't bicycles fall over? Because they are two-tired!",
    "Why don't oysters donate to charity? Because they are shellfish!",
    "Why don't cats play poker in the wild? Too many cheetahs!",
]


#This is the introduction to the chatbot, and it asks for the user's name and if they would like to hear a joke?
intro_chat()

#This loop tells the user jokes until it runs out of jokes or if the user says no
while len(joke_list) > 0:
  #Asks the user if they want to hear another joke
  print(" ")
  ask_joke_again = input("Do you want to hear another joke? Yes or No: ")
  #If the user says no, it will say goodbye and break
  if ask_joke_again.lower() == "no":
    print("Okay, maybe next time!")
    break
#If the user says yes, it will find a random joke and print it
  if ask_joke_again.lower() == "yes":
    print(" ")    
    find_joke()
    
#If the joke list is out of jokes, it will say goodbye and break
  if len(joke_list) == 0:
    print(" ")
    print("Sorry, I am out of jokes for now. I hope you thought the jokes were funny! Goodbye! ")
    break