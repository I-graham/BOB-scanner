import re
import os

def isNew(string):
    if re.match(r"ELIGIBLE", string.upper()):
        return True
    else:
        return False

def isSoph(string):
    if re.match(r"ELIGIBLE: ALL.*", string.upper()) or re.match(r"ELIGIBLE:.*SOPHOMORE", string.upper()) or re.match(r"ELIGIBLE:.*10TH GRADE", string.upper()):
        return True
    else:
        return False

directory = os.path.dirname(os.path.abspath(__file__))
fileopen = open(directory +"\\BOB.txt","r+")
lineList = fileopen.readlines()
lineList.append('')
doPrint = False

for line in range(0, len(lineList)-1):
    if isNew(lineList[line+1]):
        if isSoph(lineList[line+1]):
            doPrint=True
        else:
            doPrint=False
            print('\n\n\n\n\n')
    if doPrint:
        print(lineList[line])
