#this is a simple code to save game score
def score(ro):
    sc_fin = 0
    sc_lis = []
    for i in range(ro):
        sc = int(input("enter the current score to be saved:"))
        sc_lis.append(sc)
        sc_fin += sc
    print ("the final score is:", sc_fin)
    print ("the game scores per round were:", sc_lis)

ro = int(input("enter the number of rounds:"))
score(ro)