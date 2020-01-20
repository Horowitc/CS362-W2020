# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:00:00 2020

@author: Caulin Horowitz horowitc
"""

import Dominion
import random
from collections import defaultdict


from projects.horowitc.dominion import testUtility
#Get player names
player_names = ["Annie","*Ben","*Carla"]
#number of curses and victory cards
nV = testUtility.GetVictoryCards(player_names)
nC = -10 + 10 * len(player_names)
#Define box
box = testUtility.GetBox(nV)


#Test Scenario
box["Market"] = [Dominion.Militia()] * 9


supply_order = testUtility.GetSupplyOrder()
#Pick 10 cards from box to be in the supply.
boxlist = testUtility.GetBoxList(box)
random10 = boxlist[:10]
supply = testUtility.GetSupply(box, random10, player_names, nV, nC)
#initialize the trash
trash = []
#Construct the Player objects
players = testUtility.GetPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=testUtility.GetWinners(vp, vpmax)
winstring=testUtility.GetWinString(winners)
print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)