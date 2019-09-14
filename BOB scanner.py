import re
import os

def isLink(string):
    if re.match("LINKS:", string.upper()) or re.match("HTTPS*://", string.upper()):
        return True
    else:
        return False

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
linkPassed = True

for line in range(0, len(lineList)-1):
    if line > 0:
        if lineList[line] in lineList[line-1] and isLink(lineList[line-1]):
            continue

    if '__________________________________________________________________' in lineList[line]:
        break

    if isLink(lineList[line]) and ' ' not in lineList[line+1]:
        lineList[line] += lineList[line+1]
        lineList[line].replace('\n', '')

    if linkPassed and not isLink(lineList[line]):
        for i in range(line, len(lineList)-1):

            if isLink(lineList[i]):
                linkPassed = True
            else:
                linkPassed = False

            if linkPassed and not isLink(lineList[i]):
                break
            elif isNew(lineList[i]):
                if isSoph(lineList[i]):
                    doPrint = True
                    break
                else:
                    doPrint = False
                    break

    if isLink(lineList[line]):
        linkPassed = True
    else:
        linkPassed = False

    if doPrint:
        print(lineList[line])
