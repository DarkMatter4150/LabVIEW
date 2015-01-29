import operator

class Team:
    def __init__(self, teamNum):
        self.teamNumber = teamNum
        self.numOfMatches = 0
        self.autoRamps = 0
        self.autoKickstands = 0
        self.autoCenterGoals = 0
        self.autoRollingGoals = 0
        self.score = 0

    def addMatch(self, matchArray):
        numOfMatches = 1
        if matchArray[1] == 1:
            self.autoRamps += 1
        elif matchArray[2] == 1:
            self.autoKickstands += 1
        elif matchArray[3] == 1:
            self.autoCenterGoal += 1
        elif matcArray[4] == 1:
            self.autoRollingGoals += 1
#        self.updateScore()

    def getReport(self):
        print "==# Team: " + str(teamNumber) + " #=="
        print "~ Auto Stats ~"
        print ("Drove off ramps: " + str(self.autoRamps) + "/" + str(self.numOfMatches))
        print ("Kickstands: " + str(self.autoKickstands) + "/" + str(self.numOfMatches))
        print ("Center goals: " + str(self.autoCenterGoals) + "/" + str(self.numOfMatches))
        print ("Rolling goals: " + str(self.autoRollingGoals) + "/" + str(self.numOfMatches))
        print ("~ Team Score ~")
        print self.score

#    def updateScore(self):
#        autoScore = ((self.autoKickstands * 800) + (self.autoRamps * 200) + (self.autoCenterGoals * 1000) + (self.autoRollingGoals * 350)) / (4 * self.numOfMatches)
#        teleScore = 0
#        score = autoScore + teleScore

#file = open("compiled-data.csv","r")
#filedata = file.read()

filedata = "4150,1,0,0,1\n4324,1,0,0,1\n4150,1,0,0,1\n"
rawData = filedata.splitlines()
matchData = []
for row in rawData:
    row = row.rsplit(",")
    row = [int(element) for element in row]
    matchData.append(row)
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

        testTeam = 4150

        for eachTeam in teamList:
            row = teamList.index(eachTeam)
            if int(matchData[row][0]) == eachTeam.teamNumber:
                eachTeam.addMatch(matchData[row])
            if eachTeam.teamNumber == testTeam:
                eachTeam.getReport()
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
