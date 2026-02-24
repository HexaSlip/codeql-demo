# trigger new run
import os

user_input = input("Enter a command: ")
os.system("sh -c " + user_input)
