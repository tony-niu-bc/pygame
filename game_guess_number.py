import random

print("""
Haha! 
I'm the Dread Pirate Robot, and I have a password for the treasure chest!
It is a number between 1 and 100.
I'll give you 6 tries.
""")

# Will get a Pirate's password
uiTreasurePassword = random. randint(1, 100)
# Will initialise the try times to zero
uitryTimes = 0

while uitryTimes < 6 :

    uiGuessPassword = int(input("What do you think the password is?"))
    
    if uiGuessPassword == uiTreasurePassword : 

        print("""
        Oh my God! 
        You guess my password for a treasure chest, you did!
        """)

        break
        
    elif uiGuessPassword < uiTreasurePassword:
        print("Too low, guess again!")

    elif uiGuessPassword > uiTreasurePassword:
        print("Too high, guess again!")

    uitryTimes = uitryTimes + 1
    
if  uitryTimes >= 6 :

    print("""
    No more guesses! 
    Better luck next time, guy! 
    Let me tell you the password was
    """, 
    uiTreasurePassword)
                