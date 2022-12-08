import os

while True:
    enterText = input("Enter Text to Input into File:- \n")
    with open("text.txt", "a") as f:
        f.write(enterText)
    
    with open("text.txt", "r") as f:
        print(f"The text in the file is '{f.read()}'\n")

    qontinue = input("Do you want to add more text?(y/n/clear text)")
    
    if qontinue in ["y","yes","Yes","YES", "Y"]:
        continue
    
    elif qontinue in ["n","no","No","NO", "N", ""]:
        break

    elif qontinue in ["clear text", "cleartext", "clear", "Clear Text", "CLEARTEXT", "clearText", "CLEAR"]:
        file = "text.txt"
        os.remove(file)
        break

    else:
        print("Please enter y, n, clear text")
        continue