
def parseLine(lineStr):
    if lineStr[0] == "@": # a instruction
        lineStr = lineStr[1:]

        return "A", lineStr
    else: # c instruction
        dest, comp, jump = "null", "", "null"

        tbl1 = lineStr.split("=", 1)
        if len(tbl1)>1:
            dest = tbl1[0]
            comp = tbl1[1]
        else:
            comp = lineStr

        tbl2 = comp.split(";", 1)
        if len(tbl2)>1:
            comp = tbl2[0]
            jump = tbl2[1]

        return "C", [dest, comp, jump]


