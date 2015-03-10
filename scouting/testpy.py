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

    def addMatch(self, matchArray):
        # Increment the number of matches a team has played
        self.numOfMatches += 1

        # Add statistics from match data file to attributes of a team
        # Auto stats:
        self.autoBallScored += matchArray[2]
        self.autoRollingGoals += matchArray[3]
        self.autoKickstands += matchArray[4]
        self.autoRamps += matchArray[5]
        self.autoCenterGoals += matchArray[6]
        #Tele stats
        self.tele30trips += matchArray[7]
        self.tele60trips += matchArray[8]
        self.tele90trips += matchArray[9]
        #End Game Stats
        self.teleCenterGoals += matchArray[10]
        self.endGameParkingZone += matchArray[11]
        self.endGameOffFloor += matchArray[12]
        #Penalties
        self.penaltyTippedGoals += matchArray[13]
        self.penaltyBlocked += matchArray[14]
        #Update team's score
        self.updateScore()

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

    def updateScore(self):
        self.autoScore = ((self.autoKickstands * 800) + (self.autoRamps * 200) + (self.autoCenterGoals * 1500) + (self.autoRollingGoals * 350)) / (4 * self.numOfMatches)
        self.teleScore = ((self.tele30trips * 200) + (self.tele60trips * 1200) + (self.tele90trips * 1200)) / (3 * self.numOfMatches)
        self.endGameScore = ((self.teleCenterGoals * 1100) + (self.endGameParkingZone * 350) + (self.endGameOffFloor * 900)) / (3 * self.numOfMatches)
        self.penaltyScore = ((self.penaltyTippedGoals * 1000) + (self.penaltyBlocked * 750)) / (2 * self.numOfMatches)
        self.score = self.autoScore + self.teleScore + self.endGameScore - self.penaltyScore

# Opens the file to read match data from
file = open("compiled-data2.csv","r")
filedata = file.read()

# Splits the opened CSV file into a usable 2D array
teamNums = []
rawData = filedata.splitlines()
matchData = []
noteList = []
for row in rawData:
    row = row.rsplit(",")
    teamNumber = row[0]
    matchNumber = row[1]
    intData = [int(col) for col in row[3:16]]
    note = row[16]
    # If a new team is found, add that team number to a list of all team numbers
    # print row
    # print "#"
    # print intData
    # print "##"
    if row[0] not in teamNums:
        teamNums.append(int(row[0]))
    intData.insert(0, int(teamNumber))
    matchData.append(intData)
    if row[16] != '':
        noteList.append([teamNumber, matchNumber, note])
    print noteList