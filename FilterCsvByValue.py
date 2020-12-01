import sys
import re
import os

if (len(sys.argv)<=2):
    print ("Usage:")
    print ("    py {} <file> <condition1> <condition2> ...".format(os.path.basename(__file__)))
    print ("    conditions: <fldno>=<val>")
    sys.exit()

class Condition:
    ind: int
    oper: str
    val: str
    def __init__(self, i0, e0, s0):
        self.ind = i0
        self.oper = e0
        self.val = s0

strInFile = sys.argv[1]

rgCondition = []
for i in range(2, len(sys.argv)):
    arg = sys.argv[i]
    mo = re.match(r"(\d+)([<>=!]+)(\w+)", arg)
    if(mo):
        ind = int(mo.group(1))
        oper = mo.group(2)
        val = mo.group(3)
        cond = Condition(ind, oper, val)
        rgCondition.append(cond)

with open(strInFile) as fIn:
    for i,line in enumerate(fIn):
        line1 = line[:-1]
        tokens = line1.split(',')
        bMatchAll = True
        for cond in rgCondition:
            bMatchOne = False
            if(False):
                pass
            elif(cond.oper == '=' and tokens[cond.ind] == cond.val):
                bMatchOne = True
            elif(cond.oper == '!=' and tokens[cond.ind] != cond.val):
                bMatchOne = True
            elif(cond.oper == '>' and int(tokens[cond.ind]) > int(cond.val)):
                bMatchOne = True
            elif(cond.oper == '<' and int(tokens[cond.ind]) < int(cond.val)):
                bMatchOne = True
            elif(cond.oper == '>=' and int(tokens[cond.ind]) >= int(cond.val)):
                bMatchOne = True
            elif(cond.oper == '<=' and int(tokens[cond.ind]) <= int(cond.val)):
                bMatchOne = True
            bMatchAll = bMatchAll and bMatchOne
        if(bMatchAll):
            print(line, end="")


