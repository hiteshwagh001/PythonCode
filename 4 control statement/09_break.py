x=10
while(x>0):
    print(x)
    x-=1
    if(x==5):
        break


playerList=["virat",'rohit','klRahul','jadeja']
playername=input("player to be search : ")
for player in playerList:
    if(playername==player):
        print(playername,"is present in list")
        break;