'''
AI
'''
from playerclass import *
from barbarian import *
def minDistance(obj,player):
    #if obj.show==True:
        if len(player.playerlist)!=0:
            c=distance(obj,player.playerlist[0])
            result=player.playerlist[0]
        else:
            c=distance(obj,player.playerbuildings[0])
            result = player.playerbuildings[0]
        for i in player.playerlist+player.playerbuildings:
            if i.show==True:
                x=distance(obj,i)
                if x<c:
                    result=i
        return result
def fighting(obj,player):
    if obj.show==True:
        c=minDistance(obj,player)
        gotoGether(obj,c)
        fight(obj,c)
    else:
        for i in player.playerlist:
            i.move()
def defending(tower,player):
    if tower.show==True:
        for i in player.playerlist:
            defend(tower,i)
            fight(i,tower)
    else:
        for i in player.playerlist:
            i.move()