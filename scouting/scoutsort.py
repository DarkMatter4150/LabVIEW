import operator
import os

class Team:
    def __init__(self,teamNum):
        self.number = teamNum
        self.numOfMatches = 0
        self.autoRamps = 0
        self.autoBallScored = 0
        self.autoKickstands = 0
        self.autoCenterGoals = 0
        self.autoRollingGoals = 0
        self.tele30trips = 0
        self.tele60trips = 0
        self.tele90trips = 0
        self.teleCenterGoals = 0
        self.endGameParkingZone = 0
        self.endGameOffFloor = 0
        self.penaltyTippedGoals = 0
        self.penaltyBlocked = 0

        self.score = 0

    def addMatch(self, matchArray):
        self.numOfMatches += 1
        #Auto stats
        if matchArray[2] == 1:
            self.autoBallScored += 1
        if matchArray[3] == 1:
            self.autoRollingGoals += 1
        if matchArray[4] == 1:
            self.autoKickstands += 1
        if matchArray[5] == 1:
            self.autoRamps += 1
        if matchArray[6] == 1:
            self.autoCenterGoals += 1
        #Tele stats
        if matchArray[7] > 0:
            self.tele30trips += matchArray[7]
        if matchArray[8] > 0:
            self.tele60trips += matchArray[8]
        if matchArray[9] > 0:
            self.tele90trips += matchArray[9]
        #End Game Stats
        if matchArray[10] > 0:
            self.teleCenterGoals += matchArray[10]
        if matchArray[11] > 0:
            self.endGameParkingZone += matchArray[11]
        if matchArray[12] > 0:
            self.endGameOffFloor += matchArray[12]
        #Penalties
        if matchArray[13] > 0:
            self.penaltyTippedGoals += matchArray[13]
        if matchArray[14] > 0:
            self.penaltyBlocked += matchArray[14]
        #Update team's score
        self.updateScore()

    def getReport(self):
        print "==# Team: " + str(self.number) + " #=="
        print "~ Auto Stats ~"
        print "Drove off ramps: " + str(self.autoRamps) + "/" + str(self.numOfMatches)
        print "Kickstands: " + str(self.autoKickstands) + "/" + str(self.numOfMatches)
        print "Center goals: " + str(self.autoCenterGoals) + "/" + str(self.numOfMatches)
        print "Rolling goals: " + str(self.autoRollingGoals) + "/" + str(self.numOfMatches)
        print "Balls scored in Rolling goal: " + str(self.autoBallScored) + "/" + str(self.numOfMatches)
        print "~ Tele Stats ~"
        print "Avg 30cm Trips: " + str(self.tele30trips / self.numOfMatches)
        print "Avg 60cm Trips: " + str(self.tele60trips / self.numOfMatches)
        print "Avg 90cm Trips: " + str(self.tele90trips / self.numOfMatches)
        print "~ End Game Stats ~"
        print "Avg Center Goal Trips: " + str(self.teleCenterGoals / self.numOfMatches)
        print "Avg items in parking zone: " + str(self.endGameParkingZone / self.numOfMatches)
        print "Avg items off floor: " + str(self.endGameOffFloor / self.numOfMatches)
        print "~ Penalties ~"
        print "Total goals tipped over: " + str(self.penaltyTippedGoals)
        print "Total blocking penalties: " + str(self.penaltyBlocked)
        print "~ Team Score ~"
        print self.score

    def updateScore(self):
        self.autoScore = ((self.autoKickstands * 800) + (self.autoRamps * 200) + (self.autoCenterGoals * 1000) + (self.autoRollingGoals * 350)) / (4 * self.numOfMatches)
        self.teleScore = ((self.tele30trips * 200) + (self.tele60trips * 1000) + (self.tele90trips * 100)) / (3 * self.numOfMatches)
        self.endGameScore = ((self.teleCenterGoals * 800) + (self.endGameParkingZone * 350) + (self.endGameOffFloor * 900)) / (3 * self.numOfMatches)
        self.penaltyScore = ((self.penaltyTippedGoals * 1000) + (self.penaltyBlocked * 750)) / (2 * self.numOfMatches)
        self.score = self.autoScore + self.teleScore + self.endGameScore - self.penaltyScore

file = open("python-data.csv","r")
filedata = file.read()

#filedata = "4150,1,0,0,1,1\n4324,1,0,0,1,0\n4150,1,0,1,1,1\n"
rawData = filedata.splitlines()
matchData = []
for row in rawData:
    row = row.rsplit(",")
    row = [int(element) for element in row]
    matchData.append(row)

#Start QSM
os.system("clear")
queue = "*"
nextState = "INIT"
quit = False
while (quit != True):

    if nextState == "INIT":
        
        teamNums = [4150,4324]
        teamList = []
        for number in teamNums:
            team = Team(number)
            teamList.append(team)
            for row in matchData:
                if row[0] == team.number:
                    team.addMatch(row)

        queue += "IDLE*"

    elif nextState == "IDLE":
        os.system("clear")
        command = raw_input("Please enter command: ")
        if command == "report":
            queue += "REPORT*"
        elif command == "rankings":
            queue += "RANKS*"
        elif command == "refresh":
            queue += "INIT*"
        elif command == "exit":
            queue += "EXIT*"
        else:
            print "Command not found, please try again"
            queue += "IDLE*"

    elif nextState == "RANKS":
        teamList.sort(key=lambda team: team.score, reverse=True)
        reportNum = int(raw_input("Please enter the number of teams to rank: "))
        if reportNum <= len(teamList):
            for i in range(0, reportNum):
                print teamList[i].number
        else:
            print "Number of teams to report is greater than the number of teams present. Please try another command"
        raw_input("\nPress any key to continue")
        queue += "IDLE*"

    elif nextState == "REPORT":
        target = int(raw_input("Please enter the number of the team you wish to report on: "))
        for team in teamList:
            print "Searching for the target team"
            if team.number == target:
                team.getReport()
                break
        raw_input("\nPress any key to continue")
        queue += "IDLE*"

    elif nextState == "EXIT":
        queue = ""

    #Load next queue
    try:
        delimeterIndex = queue.index("*")
        nextState = queue[0:delimeterIndex]
        queue = queue[delimeterIndex+1:len(queue)]
    except ValueError:
        print "* Program will exit *"
        quit = True
