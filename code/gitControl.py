import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def update():
    os.system("cd "+dir_path)  # ensure we are in the "code" directory
    os.system("git pull")  # ensure the local repo is up to date
    os.system("git add .")  # stage changes
    os.system("git commit -m \"Automatic update (gitControl.py)\"")  # commit
    os.system("git push")  # push changes
    