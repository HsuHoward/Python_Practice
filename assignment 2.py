#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:08:38 2018

@author: howardhsu
"""
#Study Drills 

##1.Go through this program and write a comment above each line explaining it.

###set "type_of_people" as 10
types_of_people = 10
###set variable "type_of_people" which is 10 into f-string sentance x
x = f"There are {types_of_people} types of people."
 
###set binary as "binary"
binary = "binary"
###set do_not as "don't"
do_not = "don't"
###set variable "binary" which is "binary" and "do_not" which is "don't" into f-string sentance y
y = f"Those who know {binary} and those who {do_not}."

###print x
print(x)
###print y
print(y)

###print f-string sentance with variable x which is 10
print(f"I said: {x}")
###print f-string sentance with variable y which is "Those who know binary and those who don't."
print(f"I also said: '{y}'")

###set variable hilarious as False
hilarious = False

###set "joke_evaluation" with undefined variable {}
joke_evaluation = "Isn't that joke so funny?! {}" 
####use .format to define the undefined variable {}, which is hilarious 
print(joke_evaluation.format(hilarious))

###set w to a sentance
w = "This is the left side of..."
###set e to a sentance
e = "a string with a right side."

###combine sentances that w and e are represented
print(w + e)

##2.Find all the places where a string is put inside a string. There are four places.
###Line 15, 22, 30, 32, 40

##3. Are you sure there are only four places? How do you know? Maybe I like lying.
###No! There are 5 places as I mentioned in questoin 2.

###4.Explain why adding the two strings w and e with + makes a longer string.
### Since the sentaces representing by w and e are combining together.
