import os
import operator as op
from functools import reduce
import random
import itertools
import sys

def Plaintext():
    print("Enter word to be encrypted:")
    Word = str(input())
    if Word == "":
        os.remove("Key_Logs.txt")
        sys.exit()
    Word = list(Word)
    return Word

def Numeric(Word):
    Numbers = []
    Code = {}
    Letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    Values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
              18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33,
              34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
              50, 51]
    for x in range(len(Letters)):
        Code[Letters[x]] = Values[x]
    for x in range(len(Word)):
        Numbers.append(Code[Word[x]])
    return Numbers


def Pascal(NumValue):
    def ncr(n, r):
            r = min(r, n-r)
            numer = reduce(op.mul, range(n, n-r, -1), 1)
            denom = reduce(op.mul, range(1, r+1), 1)
            return numer // denom
    RowValue = []
    for x in range(len(NumValue)):
        PascalRow = []
        for y in range(NumValue[x]+1):
            n = NumValue[x]
            r = y
            PascalValue = ncr(n,r)
            PascalRow.append(PascalValue)
        RowValue.append(PascalRow)
    return RowValue

def HalfPascal(RowValue):
    HalfRowValue = []
    HalfRow = []
    for y in range(len(RowValue)):
        HalfRow = []
        for x in range(len(RowValue[y]) // 2):
            HalfRow.append(RowValue[y][x])
        HalfRowValue.append(HalfRow)
    return HalfRowValue
    
def RowToLetter(HalfRowValue):
    CypherNum = []
    CypherText = []
    IndiCypher = 0
    for x in range(len(HalfRowValue)):
        CypherNum = []
        IndiCypher = HalfRowValue[x]
        for y in range(len(IndiCypher)):
            r = IndiCypher[y] % 52
            Code = {}
            Letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
            Values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                      18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32,
                      33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
                      48, 49, 50, 51]
            for x in range(len(Letters)):
                Code[Values[x]] = Letters[x]
            r = Code[Values[r]]
            CypherNum.append(r)
        CypherText.append(CypherNum)
    return CypherText

def CreateKey(CypherLetters):
    KeyLength = 0
    KeyList = [1, 1]
    KeyValue = 0
    for x in range(len(CypherLetters)):
        for y in range(len(CypherLetters[x])):
            BinaryDigit = random.randint(0, 1)
            KeyList.append(BinaryDigit)
    for x in range(len(KeyList)):
        KeyList[x] = str(KeyList[x])
    KeyList.pop(-1)
    KeyList.pop(-1)
    Key = "".join(KeyList)
    Key = str(Key)
    print(Key)
    return Key

def BinaryEncryption(Key, CypherLetters):
    CypherText = list(itertools.chain.from_iterable(CypherLetters))
    print(CypherText)
    EncryptedText = []
    Key = str(Key)
    for x in range(len(Key)):
        if Key[x] == "1":
            EncryptedText.append(CypherText[x])
    EncryptedText = "".join(EncryptedText)
    return EncryptedText

def CreateTXT(Key, EncryptedMessage):
    try:
        file = open("Key_Logs.txt", "a")
        file.write("{}\n{}\n".format(Key, EncryptedMessage))
        file.close()
    except FileNotFoundError:
        file = open("Key_Logs.txt", "w")
        file.write("{}\n{}\n".format(Key, EncryptedMessage))
        file.close()
    
while True:
    #STEP 1: ENTER WORD
    Word = Plaintext()
    #STEP 2: CONVERT INTO NUMERIC VALUES
    NumValue = Numeric(Word)
    #STEP 3: FIND PASCAL'S TRIANGLE ROW
    RowValue = Pascal(NumValue)
    HalfRowValue = HalfPascal(RowValue)
    #STEP 5: CONVERT DIGITS BACK TO LETTERS
    CypherLetters = RowToLetter(HalfRowValue)
    #STEP 6: CREATE KEY
    Key = CreateKey(CypherLetters)
    #STEP 7: USE KEY
    EncryptedMessage = BinaryEncryption(Key, CypherLetters)
    print(EncryptedMessage)
    #STEP 8: ADD TO TXT FILE
    TxtDict = CreateTXT(Key, EncryptedMessage)
