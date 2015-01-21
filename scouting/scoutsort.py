#!/bin/python
import operator

#file = open("compiled-data.csv","r")
#filedata = file.read()

filedata = "1234,9,8\n4324,6,27\n967,0,92\n"

a = filedata.splitlines()
#print a
b = []
row = 0
for row in a:
     b.append(row.rsplit(","))
#print b
c =[]
c = sorted(b, key=operator.itemgetter(2,1))
print c
