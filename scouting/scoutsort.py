#!/bin/python
import operator

class Team:
    def __init__(self, teamNum):
        self.teamNumber = teamNum
    def getNumber(self):
        return self.teamNumber

#file = open("compiled-data.csv","r")
#filedata = file.read()

filedata = "1234,9,8\n4324,6,27\n967,0,92\n"

a = filedata.splitlines()
b = []
row = 0
for row in a:
     b.append(row.rsplit(","))
b = sorted(b, key=operator.itemgetter(2,1))
print b

#Start QSM
queue = "*"
nextState = "INIT"
quit = False
while (quit != True):
    if nextState == "INIT":
        print "INIT case ran"
        queue += "IDLE*"
    elif nextState == "IDLE":
        print "IDLE case ran"
        queue += "EXIT*"
    elif nextState == "EXIT":
        print "EXIT case ran"
        queue = ""
        
    #Load next queue
    try:
        delimeterIndex = queue.index("*")
        nextState = queue[0:delimeterIndex]
        queue = queue[delimeterIndex+1:len(queue)]
    except ValueError:
        print "Queue is empty"
        quit = True
