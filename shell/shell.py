#u!/usr/bin/env python3

import sys, os, re


while True:
    os.write(1, ('Enter a command, "exit" quits the program.\n$ ').encode())

    shellInput = input() # get the input from the user using the shell
    
    args = shellInput.split() # make the input a list
    
    if shellInput == "": # continue if there is no input from the user
        continue
    elif 'exit' in shellInput: # exit shell
        break