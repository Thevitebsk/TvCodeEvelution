import random
enemyhp=glebovskyhp=1000
bro=0
name=input("\nname for the enemy that Glebovsky will be fighting:")
print(f"----------{name} VS Glebovsky----------")
while True:
    print(f"""
Glebovsky's (aka you) HP:{glebovskyhp}
Enemy's HP:{enemyhp}
Move set:
    1: Hammer
    2: Power punch
    3: Heal potion
what do you do:""")
    i=int(input())
    #game loop
    if 1<i>3:bro=1
    else:bro=0
    if bro:print("that ain't a move")
    else:
        #your turn
        if i==1:
            enemyhp-=75
            print(
            f"\n\"YOUCH!!\" {name} said as they were hitten with a hammer",
            "Took 75 HP!",
            sep="\n"
            )
        elif i==2:
            enemyhp-=200
            print(
            f"\n\"GAAAAAAAAAARGHHHH!!!!\" {name} said as they were hitten with a powerfull punch",
            "Took 200 HP!",
            sep="\n"
            )
        elif i==3:
            glebovskyhp+=100
            print(
            f"\n\"Oooh, health potion!\" Glebovsky said",
            "Heal 100 HP!",
            sep="\n"
            )

        #enemy's turn
        j=random.randint(1,3)
        if j==1:
            glebovskyhp-=75
            print(
            f"\n\"AAAAAARGHH!!! MY HEAD!!!\" Glebovsky said as they were hitten with a hammer",
            "Took 75 HP!",
            sep="\n"
            )
        elif j==2:
            glebovskyhp-=200
            print(
            f"\n\"WOAAaaaahhh...\" Glebovsky said as they were hitten with a powerfull punch to the point he flew off the earth and came back... somehow",
            "Took 200 HP!",
            sep="\n"
            )
        elif j==3:
            enemyhp+=100
            print(
            f"\n\"yummy potion\" {name} said",
            "Heal 100 HP!",
            sep="\n"
            )
    if enemyhp<=0:print("\nGlebovsky wins!");break
    elif glebovskyhp<=0:print(f"\n{name} wins...?");break