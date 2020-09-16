#u!/usr/bin/env python3

import sys, os, re

def shell(args):
    processID = os.getpid()
    rc = os.fork()

    if rc < 0: 
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1) #exit

    elif rc == 0:
        for directory in re.split(":", os.environ['PATH']): # try all paths
            pgrm = "%s/%s" % (directory, args[0])
            try:
                os.execve(pgrm, args, os.environ) # exec the program
            except FileNotFoundError:
                pass
                
        os.write(2, ("-bash: %s: command not found\n" % args[0]).encode()) # state that the command wasn't found
        sys.exit(1) # exit
    
    else:
        childprocessID = os.wait()


def main():
    while True:
        if 'PS1' in os.environ:
            os.write(1, (os.environ['PS1']).encode())
        else:
            os.write(1, ("Enter a command, \"exit\" quits the program.\n$ ").encode())

        shellInput = input() # get the input from the user using the shell
    
        args = shellInput.split() # make the input a list
    
        if shellInput == "": # continue if there is no input from the user
            continue
        elif 'cd' in args[0]: # change directory
            try: 
                if len(args) <= 1 or args[-1] == " ": # go to the parent directory
                    os.chdir("..")
                else: 
                    os.chdir(args[1])
                print(os.getcwd())
            except FileNotFoundError:
                os.write(1, ("-bash: cd: %s: No such file or directory\n" % args[1]).encode())
                pass
        elif 'exit' in shellInput: # exit shell
            sys.exit(0)
        else:
            shell(args)

if __name__ == "__main__":
    main()