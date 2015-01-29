import operator

class Team:
    def __init__(self,teamNum):
        self.number = teamNum
        self.numOfMatches = 0
        self.autoRamps = 0
        self.autoKickstands = 0
        self.autoCenterGoals = 0
        self.autoRollingGoals = 0
        self.score = 0

    def addMatch(self, matchArray):
        self.numOfMatches += 1
        if matchArray[1] == 1:
            self.autoRamps += 1
        elif matchArray[2] == 1:
            self.autoKickstands += 1
        elif matchArray[3] == 1:
            self.autoCenterGoal += 1
        elif matchArray[4] == 1:
            self.autoRollingGoals += 1
        self.updateScore()

    def getReport(self):
        print "==# Team: " + str(self.number) + " #=="
        print "~ Auto Stats ~"
        print "Drove off ramps: " + str(self.autoRamps) + "/" + str(self.numOfMatches)
        print "Kickstands: " + str(self.autoKickstands) + "/" + str(self.numOfMatches)
        print "Center goals: " + str(self.autoCenterGoals) + "/" + str(self.numOfMatches)
        print "Rolling goals: " + str(self.autoRollingGoals) + "/" + str(self.numOfMatches)
        print "~ Team Score ~"
        print self.score

    def updateScore(self):
        self.autoScore = ((self.autoKickstands * 800) + (self.autoRamps * 200) + (self.autoCenterGoals * 1000) + (self.autoRollingGoals * 350)) / (4 * self.numOfMatches)
        self.teleScore = 0
        self.score = self.autoScore + self.teleScore

#file = open("compiled-data.csv","r")
#filedata = file.read()

filedata = "4150,1,0,0,1\n4324,1,0,0,1\n4150,1,0,1,1\n"
rawData = filedata.splitlines()
matchData = []
for row in rawData:
    row = row.rsplit(",")
    row = [int(element) for element in row]
    matchData.append(row)

#Start QSM
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
                    print "Match added to team " + str(team.number) + ":"
                    print row
            print team.getReport()
        queue += "IDLE*"

    elif nextState == "IDLE":
        command = raw_input("Please enter command: ")
        if command == "report":
            queue += "REPORT*"
        elif command == "rankings":
            queue += "RANKS*"
        elif command == "exit":
            queue += "EXIT*"
        else:
            print "Command not found, please try again"
            queue += "IDLE*"

    elif nextState == "RANKS":
        reportNum = int(raw_input("Please enter the number of teams to rank: "))
        if reportNum <= len(teamList):
            for i in range(0, reportNum):
                print teamList[i].number
        else:
            print "Number of teams to report is greater than the number of teams present. Please try another command"
        queue += "IDLE*"

    elif nextState == "REPORT":
        target = int(raw_input("Please enter the number of the team you wish to report on: "))
        for team in teamList:
            print "Searching for the target team"
            if team.number == target:
                team.getReport()
                break
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
