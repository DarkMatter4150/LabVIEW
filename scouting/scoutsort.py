import operator

class Team:
    def __init__(self, teamNum):
        self.teamNumber = teamNum
        numOfMatches = 0
    def addMatch(self, matchArray):
        numOfMatches += 1
        if matchArray[0] == 1:
            autoRamps += 1
        elif matchArray[1] == 1:
            autoKickstands += 1
        elif matchArray[2] == 1:
            autoCenterGoal += 1
        elif matcArray[3] == 1:
            autoRollingGoals +=1

#file = open("compiled-data.csv","r")
#filedata = file.read()

filedata = "4150,1,0,0,1\n4324,1,0,0,1\n4150,1,0,0,1\n"
rawData = filedata.splitlines()
matchData = []
row = 0
matchData = [int(element) for row in ]
#for row in rawData:
#    data = row.rsplit(",")
#    newRow = [int(element) for element in data]
#    print "New Row"
#    print newRow
#    matchData.append(data)
print "Match Data:"
print matchData

#Start QSM
queue = "*"
nextState = "INIT"
quit = False
while (quit != True):
    if nextState == "INIT":
        print "INIT case ran"
        teamNums = [4150,4324]
        teamList = []
        for teamNumber in teamNums:  
            teamList.append(Team(teamNumber))
        for eachTeam in teamList:
            if int(matchData[teamList.index(eachTeam)][0]) == eachTeam.teamNumber:
                print "Match Found"
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
