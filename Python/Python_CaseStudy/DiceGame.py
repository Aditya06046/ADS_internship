import random
def DiceGame():
    min_val=1
    max_val=6
    #loop starts for rolling dice
    print("Welcome to dice game :")
    key=input("Enter start to start game:")
    if key=='start':
        rool_again=True
    else:
        rool_again=False
    while (rool_again==True):
        # picks random value form 1 to 6
        rand=random.randint(min_val,max_val)
        print("You Rolled Dice-",rand)
        # yes-- while loop iternate again
        # no-- while loop terminate
        rool_next=input("You want to Roll Again (yes,no) :")
        if rool_next=='yes' or rool_next=='y':
            rool_again=True
        else:
            rool_again=False
    print("Your Game is going to terminae...Successfully played the Dice Game--- Tada")
DiceGame()
    
