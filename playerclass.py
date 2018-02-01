'''
class player
'''
from barbarian import *
import random
class player:
	def __init__(self,kind,k=4):
		self.kind=kind
		self.round=round
		x=randomSelect(kind,k)
		self.playerlist=x[0]
		self.playernamelist=x[1]
		if kind=='f':
			self.playerbuildings=[building('Fhall'),building('FLeftXbow'),building('FRightXbow')]
		else:
			self.playerbuildings=[building('Dhall'),building('DLeftXbow'),building('DRightXbow')]
	def resetPlayerList(self,value):
		x=randomSelect(self.kind,value)
		self.playerlist=x[0]
		self.playernamelist=x[1]
	def SetPoslist(self,lst):
		self.poslist=lst
def randomSelect(kind,d):#select random armi for player
	objlist=[]
	nameList=['barbar','giant','archer','wizard','skeleton','prince','dragon','goblin']
	namelistF=random.choices(nameList,k=d)
	namelistD=random.choices(nameList,k=d)

	for i in range(d):
		if kind=='d':
			c=armi(random.randint(0,500),800,namelistD[i],kind)
			objlist.append(c)
		else:
			c = armi(random.randint(0,500),300, namelistF[i], kind)
			objlist.append(c)
	if kind=='f':
		return [objlist,namelistF]
	else:
		return [objlist, namelistD]