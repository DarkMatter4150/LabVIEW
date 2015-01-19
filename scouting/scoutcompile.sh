#!/bin/bash
for filename in ~/Documents/code/robotics-code/scouting/test-data/*.csv; do
    cat $filename >> compiled-data.csv
done
