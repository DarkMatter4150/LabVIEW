#!/bin/bash

### This file needs to be in the src folder of the Java files ###

echo "script started"

getTime() {
    date +%F" "%r
}

START=0
startTimer() {
    START=$(date +%s%N)
    echo "Clock started at: $startTime"
}

getElapsedTime() {
    END=$(date +%s%N)
    ELAPSED=($(($END - $START)) / 100000000)
    echo "Start Time: $(date +"%r")"
    echo "End Time: $(date +"%r")"
    echo "Elapsed Time (In nanoseconds): $ELAPSED"
    echo "Elapsed Time (In seconds) : $(bc <<< "scale=10; $ELAPSED / 1000000000")"
}

log() {
	if [ ! -d $FLNM ]; then
		mkdir $FLNM
	fi
	cd $FLNM
    NUMOFLOGS=$(ls -l | wc -l)
    LOGFILE=$FLNM-$NUMOFLOGS.txt
    echo "$FLNM.java" >> $LOGFILE
    getTime >> $LOGFILE
    echo "$OUTPUT" >> $LOGFILE
	echo "~=~" >> $LOGFILE
	getElapsedTime >> $LOGFILE
    echo "Log Complete"
}

#Determine name of the Java file

echo "Please type the name of the file without the file extension:"
FLNM="test"
read FLNM
SRCNAME=$FLNM.java

#Determine name of the package the working file is in, and determine bin and scr folders
echo "Enter the package the file is a part of"
read PCKGDIR
MAINDIR="$PWD"
if [ $PCKGDIR = "default" ]; then
    COMPDIR="$MAINDIR/bin"
    SRCDIR="$MAINDIR/src"
else
    COMPDIR="$MAINDIR/bin/$PCKGDIR"
    SRCDIR="$MAINDIR/src/$PCKGDIR"
fi

#Compile .java file from the src folder into the bin folder and run the .class file
echo "Directory to compile into: $COMPDIR"
cd $SRCDIR
javac -d $COMPDIR $SRCNAME
echo "Compiled Successfuly, running program"
cd $COMPDIR
startTimer
echo "###########"
OUTPUT=$(java $FLNM)
echo "$OUTPUT"
echo "###########"
getElapsedTime
echo "Program finished running"
#back to log folder
cd $MAINDIR/logFiles
log
echo "script finished"
