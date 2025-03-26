SymbolTable = {
    'R0': 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5, "R6": 6, "R7": 7,
    "R8": 8, "R9": 9, "R10": 10, "R11": 11, "R12": 12, "R13": 13, "R14": 14, "R15": 15,
    "SCREEN": 16384, "KBD": 24576, "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
}

def scanFileForJumpVars(textFile):
    i=0
    while i < len(textFile):
        line = textFile[i]
        if line[0] == "(":
            word = line[1:-1]
            SymbolTable[word] = i
            textFile.pop(i)
        else:
            i += 1

def replaceSymbols(textFile):
    counter = 16
    for i in range(len(textFile)):
        line = textFile[i]
        if line[0] == "@":
            word = line[1:]

            if not word.isnumeric():
                if not word in SymbolTable:
                    SymbolTable[word] = counter
                    counter += 1

                textFile[i] = "@" + str(SymbolTable[word])

def manageFile(textFile):
    scanFileForJumpVars(textFile)
    replaceSymbols(textFile)