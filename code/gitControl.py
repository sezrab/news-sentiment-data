import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.system("cd "+dir_path) # ensure we are in the "code" directory
os.system("git pull")
os.system("git add *")