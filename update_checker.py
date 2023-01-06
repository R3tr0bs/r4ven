"""
Author: R3tr0
Purpose: Checks for updates in the repo and asks the user if he wants
to update it, if he dose, updates, otherwise, leaves
"""

from requests import get
from os import system
from time import sleep

repo_url = "https://github.com/R3tr0bs/r4ven.git"
version = "0.0"

def check_for_update():
    get_version()
    try:
        git_ver = get("https://raw.githubusercontent.com/R3tr0bs/r4ven/main/Version.txt").text.strip()
    except Exception as e:
        append(e, error_file)
        git_ver = version
    if git_ver != "404: Not Found" and float(git_ver) > float(version):
        print(f"R4ven has a new update!\nCurrent: {version}\nAvailable: {git_ver}")
        upask=input(f"\nDo you want to update R4ven?[y/n] > ")
        if upask.lower() == "y":
            update_repo()
        elif upask.lower() == "n":
            print(f"\nUpdating cancelled. Using old version!")
            sleep(2)
        else:
            print(f"\nWrong input!\n")
            sleep(2)
            

def update_repo():
    """
    updates the repo
    """
    print("Updating R4ven")
    system(f"cd .. && rm -rf r4ven && git clone {repo_url}")
    print(f"\nR4ven has been updated successfully!! Please restart terminal!")
    exit()
    

def get_version():
    """
    gets the current version from the version file
    """
    try:
      with open("./Version.txt", r) as version_file:
        version = version_file.read(1).strip()
    except:
      pass
    
