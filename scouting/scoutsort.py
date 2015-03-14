#!/usr/bin/python

import operator
import os

class Team:
    def __init__(self,teamNum):
        # Initialize all variables for team attributes
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
        self.notes = []

    def addMatch(self, matchArray):
        # Increment the number of matches a team has played
        self.numOfMatches += 1

        # Add statistics from match data file to attributes of a team
        # Auto stats:
        self.autoBallScored += matchArray[1]
        self.autoRollingGoals += matchArray[2]
        self.autoKickstands += matchArray[3]
        self.autoRamps += matchArray[4]
        self.autoCenterGoals += matchArray[5]
        #Tele stats
        self.tele30trips += matchArray[6]
        self.tele60trips += matchArray[7]
        self.tele90trips += matchArray[8]
        #End Game Stats
        self.teleCenterGoals += matchArray[9]
        self.endGameParkingZone += matchArray[10]
        self.endGameOffFloor += matchArray[11]
        #Penalties
        self.penaltyTippedGoals += matchArray[12]
        self.penaltyBlocked += matchArray[13]
        #Update team's score
        self.updateScore()

    def addNote(self, note):
        self.notes.append(note)

    def getReport(self):
        print "==# Team: " + str(self.number) + " #=="
        print "\n~ Auto Stats ~"
        print "Drove off ramps: " + str(self.autoRamps) + "/" + str(self.numOfMatches)
        print "Kickstands: " + str(self.autoKickstands) + "/" + str(self.numOfMatches)
        print "Center goals: " + str(self.autoCenterGoals) + "/" + str(self.numOfMatches)
        print "Rolling goals: " + str(self.autoRollingGoals) + "/" + str(self.numOfMatches)
        print "Balls scored in Rolling goal: " + str(self.autoBallScored) + "/" + str(self.numOfMatches)
        print "\n~ Tele Stats ~"
        print "Avg 30cm Trips: " + str(float(self.tele30trips) / float(self.numOfMatches))
        print "Total 30cm Trips: " + str(self.tele30trips)
        print "Avg 60cm Trips: " + str(float(self.tele60trips) / float(self.numOfMatches))
        print "Total 60cm Trips: " + str(self.tele60trips)
        print "Avg 90cm Trips: " + str(float(self.tele90trips) / float(self.numOfMatches))
        print "Total 90cm Trips: " + str(self.tele90trips)
        print "\n~ End Game Stats ~"
        print "Avg Center Goal Trips: " + str(float(self.teleCenterGoals) / float(self.numOfMatches))
        print "Avg items in parking zone: " + str(float(self.endGameParkingZone) / float(self.numOfMatches))
        print "Avg items off floor: " + str(float(self.endGameOffFloor) / float(self.numOfMatches))
        print "\n~ Penalties ~"
        print "Total goals tipped over: " + str(self.penaltyTippedGoals)
        print "Total blocking penalties: " + str(self.penaltyBlocked)
        print "\n~ Team Score ~"
        print self.score
        print "\n~Notes~"
        self.getNotes()

    def getNotes(self):
        print "Match\t| Note"
        for note in self.notes:
            print note[1] + "\t| " + note[2]

    def updateScore(self):
        self.autoScore = ((self.autoKickstands * 800) + (self.autoRamps * 200) + (self.autoCenterGoals * 1500) + (self.autoRollingGoals * 350)) / (4 * self.numOfMatches)
        self.teleScore = ((self.tele30trips * 200) + (self.tele60trips * 1200) + (self.tele90trips * 1300)) / (3 * self.numOfMatches)
        self.endGameScore = ((self.teleCenterGoals * 1100) + (self.endGameParkingZone * 350) + (self.endGameOffFloor * 900)) / (3 * self.numOfMatches)
        self.penaltyScore = ((self.penaltyTippedGoals * 1000) + (self.penaltyBlocked * 750)) / (2 * self.numOfMatches)
        self.score = self.autoScore + self.teleScore + self.endGameScore - self.penaltyScore

# Opens the file to read match data from
<<<<<<< HEAD
file = open("compiled-data.csv","r")
=======
file = open("compiled-data2.csv","r")
>>>>>>> a444cb51be6f5f0f4f1897be0cb759335351517a
filedata = file.read()

# Splits the opened CSV file into a usable 2D array
teamNums = []
rawData = filedata.splitlines()
matchData = []
noteList = []
for row in rawData:
    row = row.rsplit(",")
    teamNumber = int(row[0])
    matchNumber = row[1]
    intData = [int(col) for col in row[3:16]]
    note = row[16]
    # If a new team is found, add that team number to a list of all team numbers
    if teamNumber not in teamNums:
        teamNums.append(teamNumber)
    intData.insert(0, teamNumber)
    matchData.append(intData)
    if note != '':
        noteList.append([teamNumber, matchNumber, note])
<<<<<<< HEAD
=======
print teamNums
>>>>>>> a444cb51be6f5f0f4f1897be0cb759335351517a

#Start QSM
queue = ["INIT"]
while (queue != []):

    # Removes and looks at the first element of the queue as the action to take
    nextState = queue.pop(0)

    if nextState == "INIT":
        # Generates a list of Team objects from the list of team numbers
        teamList = []
        blacklist = []
        for number in teamNums:
            team = Team(number)
            teamList.append(team)
        # Searches the match data for a match that belongs to the Team
        for team in teamList:
            for row in matchData:
                if row[0] == team.number:
                    team.addMatch(row)
            for note in noteList:
<<<<<<< HEAD
                if note[0] == team.number:
                    team.addNote(note)
=======
                if note[0] == str(team.number):
                    team.addNote(note)

>>>>>>> a444cb51be6f5f0f4f1897be0cb759335351517a
        queue.append("IDLE")

    elif nextState == "IDLE":

        # Waits for user input and addes the corresponding state to the end of the queue
        os.system("clear")
        command = raw_input("Please enter command: ")
        if command == "report":
            queue.append("REPORT")
        elif command == "rankings":
            queue.append("RANKS")
        elif command == "refresh":
            queue.append("INIT")
        elif command == "blacklist":
            queue.append("BLACKLIST")
        elif command == "list teams":
            queue.append("LIST")
        elif command == "help":
            queue.append("HELP")
        elif command == "exit":
            queue.append("EXIT")
        elif command == "troubleshoot":
            queue.append("TROUBLESHOOT")
        else:
            print "Command not found, please try again."
            print "Use the `help` command for information about available commands"
            raw_input("\nPress enter to continue")
            queue.append("IDLE")

    elif nextState == "RANKS":
        # Sorts the list of teams based on their score, highest score to lowest score
        teamList.sort(key=lambda team: team.score, reverse=True)
        # Requests a number of teams to rank and prints the top X teams in order
        reportNum = int(raw_input("Please enter the number of teams to rank: "))
        # Error Handling: Does not print team rank list if the number of teams requested is greater than the number of teams present
        if reportNum <= len(teamList):
            for i in range(0, reportNum):
                print "\n"
                teamList[i].getReport()
        else:
            print "Number of teams to report is greater than the number of teams present. Please try another command"
        raw_input("\nPress enter to continue")
        queue.append("IDLE")

    elif nextState == "REPORT":
        teamFound = False
        # Requests a team to print a statistical report on
        target = int(raw_input("Please enter the number of the team you wish to report on: "))
        # Finds the team requested and prints a statistical report
        for team in teamList:
            if team.number == target:
                team.getReport()
                teamFound = True
                break
        # Error Handling: If team requested does not exits in the list, no team will be reported on.
        if teamFound == False:
            print "Team Not found, please try another team."
        raw_input("\nPress enter to continue")
        queue.append("IDLE")

    elif nextState == "BLACKLIST":
        teamFound = False
        # Requests the user to type a number of a team
        blNumber = int(raw_input("Please enter the number of the team you wish to blacklist: "))
        # Searches for the team requested
        for team in teamList:
            if team.number == blNumber:
                # Removes team from the teamList and adds them to the blacklist
                teamList.remove(team)
                blacklist.append(team)
                teamFound = True
                break
        # Error Handling: If team requested does not exist, no team will be blacklisted
        if teamFound == False:
            print "Team Not found, please try another team."
            raw_input("\nPress enter to continue")
        queue.append("IDLE")


    elif nextState == "LIST":
        # Prints a list of all teams present
        print "Teams available:"
        for team in teamList:
            print team.number
        print "\nBlacklisted teams:"
        for blTeam in blacklist:
            print blTeam.number
        raw_input("\nPress enter to continue")
        queue.append("IDLE")


    elif nextState == "HELP":
        # Prints a list of available commands with their respective discriptions
        print "The following are a list of commands that can be used. (Reminder: commands are case-sensitive)"
        print "\n"
        print "rankings - Prints a list (length determined by the user) of the teams with the highest score"
        print "report - User inputs a team number, and that team's statistics are printed"
        print "list teams - Prints a list of all the teams present"
        print "exit - Exits the program"
        print ""
        raw_input("Press enter to continue")
        queue.append("IDLE")


    elif nextState == "EXIT":
        # Empties the queue so that the QSM will stop
        queue = []

    elif nextState == "TROUBLESHOOT":
        print teamNums
        raw_input("Press enter to continue")
        queue.append("IDLE")

<<<<<<< HEAD
os.system("clear")
=======
os.system("clear")
>>>>>>> a444cb51be6f5f0f4f1897be0cb759335351517a
