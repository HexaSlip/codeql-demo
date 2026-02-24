import subprocess

user_input = input("Enter a command: ")
subprocess.Popen(user_input, shell=True)
