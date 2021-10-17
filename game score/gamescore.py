#this is a simple code to save game score
#this code is applicable to games with 2 players/teams only

def score(ro):
    sc_fin_1 = 0
    sc_fin_2 = 0
    sc_lis_1 = []
    sc_lis_2 = []
    for i in range(1, ro+1):
        print("*" * 50)
        print("Round", i, "is going on")

        sc_1= int(input("enter the current score of team 1:"))
        # saving the round scores for game 1

        sc_2= int(input("enter the current score of team 2:"))
        # saving the round scores for game 2

        sc_lis_1.append(sc_1)
        sc_lis_2.append(sc_2)
        #adding up the scores to the list

        sc_fin_1 += sc_1
        sc_fin_2 += sc_2
        #finalizing and adding up the scores

    print("*" * 50)
    print ("the final score of team 1 is:", sc_fin_1)
    print ("the final score of team 2 is:", sc_fin_2)
    print ("the game scores of team 1 were:", sc_lis_1)
    print ("the game scores of team 2 were:", sc_lis_2)

    #getting out the winner's name
    if sc_fin_1 > sc_fin_2:
        print ("The winner is team_1")
    elif sc_fin_1 == sc_fin_2:
        print("There's a TIE between the teams")
    else:
        print("The winner is team_2")

ro = int(input("enter the number of rounds:"))
score(ro)