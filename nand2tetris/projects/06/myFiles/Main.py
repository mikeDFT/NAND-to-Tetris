import fnmatch
import os
import Parser
import Code
import SymbolTable

def removeWhitespaceForLine(lineStr):
    # remove spaces and new lines
    lineStr = lineStr.replace(" ", "")
    lineStr = lineStr.replace("\n", "")
    # remove comments
    return lineStr.split("//", 1)[0]

def removeWhitespace(openedFile):
    for i in range(len(openedFile)):
        openedFile[i] = removeWhitespaceForLine(openedFile[i])

    while("" in openedFile):
        openedFile.remove("")

for file in os.listdir('FilesToAssamble'):
    if fnmatch.fnmatch(file, '*.asm'):
        print(file)

        openedFile = open("FilesToAssamble/" + file).readlines()
        removeWhitespace(openedFile)
        
        SymbolTable.manageFile(openedFile)

        f = open("FilesToAssamble/" + file.split(".")[0] + ".hack", "a")

        for i in range(len(openedFile)):
            instrType, parsedLine = Parser.parseLine(openedFile[i])
            #print(instrType, parsedLine, 3)

            #print("translateInstr" + instrType)
            translateFunc = getattr(Code, "translateInstr" + instrType)
            binaryStr = translateFunc(parsedLine)
            #print(binaryStr)
            f.write(binaryStr + "\n")
            
        
        #f.write("".zfill(30).replace("0", "-") + "\n")

