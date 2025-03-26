tables = {
    "comp": {
        "0":"0101010",  "1":"0111111",
        "-1":"0111010", "D":"0001100", 
        "A":"0110000",  "!D":"0001101",
        "!A":"0110001", "-D":"0001111", 
        "-A":"0110011", "D+1":"0011111",
        "A+1":"0110111","D-1":"0001110", 
        "A-1":"0110010","D+A":"0000010",
        "D-A":"0010011","A-D":"0000111", 
        "D&A":"0000000","D|A":"0010101",
        "M":"1110000",  "!M":"1110001",
        "-M":"1110011", "M+1":"1110111",
        "M-1":"1110010","D+M":"1000010",
        "D-M":"1010011","M-D":"1000111", 
        "D&M":"1000000", "D|M":"1010101"
    },
    "dest": [
        "null", "M", "D", "MD", "A", "AM", "AD", "AMD"
    ],
    "jump": [
        "null", "JGT", "JEQ", "JGE", "JLT", "JNE", "JLE", "JMP"
    ]
}

def toBinary(nr): # there's also the bin() built-in function (for pussies)
    binStr = ""
    while nr>0:
        binStr = str(nr%2) + binStr
        nr = int(nr/2)

    return binStr

def translateInstrC(tbl):
    # a = tbl[1].find("M") and "1" or "0"
    # comp already contains a
    comp = tables["comp"][tbl[1]]

    dest = toBinary(tables["dest"].index(tbl[0])).zfill(3)
    jump = toBinary(tables["jump"].index(tbl[2])).zfill(3)

    return "111" + comp + dest + jump

def translateInstrA(decimalStr):
    binaryStr = toBinary(int(decimalStr))

    return binaryStr.zfill(16)