import operator as op
from functools import reduce
import random
import itertools
import sys

def KeyCollection():
    Key = str(input("What is the key"))
    return Key

def CipherTextCollection():
    CipherText = str(input("What is the ciphertext"))
    return CipherText

def KeyToLetters(Key, CipherText):
    KTL = []
    CipherPos = 0
    for x in range(len(Key)):
        if Key[x] == "0":
            KTL.append("_")
        elif Key[x] == "1":
            KTL.append(CipherText[CipherPos])
            CipherPos += 1
    return KTL

def NTL():
    Code = {}
    Letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
               19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34,
               35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
               51]
    for x in range(len(Letters)):
        Code[Numbers[x]] = Letters[x]

    return Code

def FindRemainingCipher(AllTrueRows):
    #print("TRC", AllTrueRows)
    KTL = KeyToLetters(Keys[0], Ciphers[0])
    #print("KTL RC", KTL)
    RemainingCipher = AllTrueRows[1]
    #print("RC", RemainingCipher)
    FinalCipher = []
    for x in range(len(RemainingCipher)):
        #print("KTL[X]", KTL[x])
        FinalCipher.append(KTL[x])
        #print(FinalCipher)
    return FinalCipher

def CreateCode():
    Code = {}
    Letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
               19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34,
               35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
               51]
    for x in range(len(Letters)):
        Code[Letters[x]] = Numbers[x]
    return Code

def FindLastValues(KTL, Code):
    LastValues = []
    for x in range((len(KTL) - 1), 0, -1):
        if KTL[x] != "_" and KTL[x] == str(KTL[x]):
            LastValues.append(int(Code[KTL[x]]))
        if len(LastValues) == 2:
            break
    return LastValues

def FindLastPos(KTL, Code):
    LastPos = []
    for x in range((len(KTL) - 1), -1, -1):
        if KTL[x] != "_":
            LastPos.append(int(x))
        if len(LastPos) == 2:
            break
    #print(LastPos)
    LastPos = int(LastPos[1]) - int(LastPos[0])
    return LastPos

def FindRowValue(LastValues, LastPos):
    def Pascal(NumValue):
        def ncr(n, r):
                r = min(r, n-r)
                numer = reduce(op.mul, range(n, n-r, -1), 1)
                denom = reduce(op.mul, range(1, r+1), 1)
                return numer // denom
        RowValue = []
        for y in range(NumValue+1):
            n = NumValue
            r = y
            PascalValue = ncr(n,r)
            RowValue.append(PascalValue)
        return RowValue
    RowNumber = []
    for x in range(53):
        RowValue = 0
        RowValue = Pascal(x)
        #print(RowValue)
        try:
            for i in range(len(RowValue) - 1):
                #print("I                          ", i)
                #print("LastValues[1]              ", (RowValue[i]) % 52)
                #print("RowValues[0]               ", (RowValue[i + LastPos]) % 52)
                if int(RowValue[i]) % 52 == int(LastValues[1]):
                    if int(RowValue[i + LastPos]) % 52 == int(LastValues[0]):
                        RowNumber.append(RowValue)
        except IndexError:
            pass
    return RowNumber


def FindTrueRow(RowValue, KTL, Code):
    AllPKTL = []
    AllRowTest = []
    for x in range(len(RowValue)):
        if FirstSearch == True:
            KTL = KeyToLetters(Keys[0], Ciphers[0])
            PotentialKTL = []
            PotentialKTL = KTL
            RowTestPos = -1
            RowTest = RowValue[x]
            RowTest = RowTest[0:int(len(RowTest)) // 2]
            CorrectRowCount = 0
            #print("PotentialKTL     ", PotentialKTL)
        elif FirstSearch == False:
            KTL = FindRemainingCipher(TrueRow)
            #print("KTL FRC", KTL)
            PotentialKTL = []
            PotentialKTL = KTL
            RowTestPos = -1
            RowTest = RowValue[x]
            RowTest = RowTest[0:int(len(RowTest)) // 2]
            CorrectRowCount = 0
            #print("PotentialKTL     ", PotentialKTL)
        try:
            for i in range(len(PotentialKTL)):
                if PotentialKTL[len(PotentialKTL) - i - 1] != "_":
                    if int(RowTest[RowTestPos]) % 52 == int(Code[PotentialKTL[len(PotentialKTL) - i - 1]]):
                        PotentialKTL[len(PotentialKTL) - i - 1] = RowTest[RowTestPos]
                        CorrectRowCount += 1
                        #print("PotentialKTL     ", PotentialKTL)
                    else:
                        break
                elif PotentialKTL[len(PotentialKTL) - i - 1] == "_":
                    PotentialKTL[len(PotentialKTL) - i - 1] = RowTest[RowTestPos]
                    CorrectRowCount += 1
                    #print("PotentialKTL     ", PotentialKTL)
                RowTestPos -= 1
                PotentialKTL = KTL
                if CorrectRowCount == len(RowTest):
                    for x in range(len(RowTest)):
                        #print("PKTL", PotentialKTL)
                        #print("ktl, ", KTL)
                        PotentialKTL.pop(-1)
                    AllPKTL = PotentialKTL
                    AllRowTest.append(RowTest)
        except IndexError:
            pass
                        
    return AllRowTest, AllPKTL
    
def RemoveDuplicate(TrueRow):
    NonDupeNum = []
    NonDupeLetter = TrueRow[1]
    print(TrueRow)
    for y in range(len(TrueRow)):
        for x in range(len(TrueRow[y])):
            [NonDupeNum.append(x) for x in TrueRow[0][x] if x not in NonDupeNum]
    return NonDupeNum, NonDupeLetter



Keys = []
Ciphers = []
global FinalNum
FinalNum = []

for x in range(len(Keys)):
    #STEP 1: KEY TO LETTERS
    KTL = KeyToLetters(Keys[x], Ciphers[x])
    #STEP 2: CREATE CODE FOR LETTERS TO NUMBERS
    Code = CreateCode()
    FirstSearch = True
    #STEP 3: COLLECT LAST 2 VALUES
    LastValues = FindLastValues(KTL, Code)
    #STEP 4: FIND DISTANCE BETWEEN THE VALUES
    LastPos = FindLastPos(KTL, Code)
    #STEP 5: FIND PASCAL'S ROW
    RowValue = FindRowValue(LastValues, LastPos)
    print("RV", RowValue)
    #STEP 6: CALCULATE THE ROWS WHICH FIT WITH THE CIPHERTEXT
    TrueRow = FindTrueRow(RowValue, KTL, Code)
    print("TR", TrueRow)
    #STEP 7: REMOVE DUPLICATE VALUES
    TrueRow = RemoveDuplicate(TrueRow)
    FinalNum.append(TrueRow[0])
    print("NDTR", TrueRow)
    while True:
        FirstSearch = False
        if TrueRow[1] == []:
            break
        else:
            LastValues = FindLastValues(TrueRow[1], Code)
            LastPos = FindLastPos(TrueRow[1], Code)
            RowValue = FindRowValue(LastValues, LastPos)
            TrueRow = FindTrueRow(RowValue, TrueRow[1], Code)
            TrueRow = RemoveDuplicate(TrueRow)
            FinalNum.append(TrueRow[0])
Message = []
print("Done", FinalNum)
for x in range(len(FinalNum)):
    FinalCode = NTL()
    Message.append(FinalCode[FinalNum[x][1]])
print("".join(Message[::-1]))
    
import operator as op
from functools import reduce
import random
import itertools
import sys

def KeyCollection():
    Key = str(input("What is the key"))
    return Key

def CipherTextCollection():
    CipherText = str(input("What is the ciphertext"))
    return CipherText

def KeyToLetters(Key, CipherText):
    KTL = []
    CipherPos = 0
    for x in range(len(Key)):
        if Key[x] == "0":
            KTL.append("_")
        elif Key[x] == "1":
            KTL.append(CipherText[CipherPos])
            CipherPos += 1
    return KTL

def NTL():
    Code = {}
    Letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
               19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34,
               35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
               51]
    for x in range(len(Letters)):
        Code[Numbers[x]] = Letters[x]

    return Code

def FindRemainingCipher(AllTrueRows):
    #print("TRC", AllTrueRows)
    KTL = KeyToLetters(Keys[0], Ciphers[0])
    #print("KTL RC", KTL)
    RemainingCipher = AllTrueRows[1]
    #print("RC", RemainingCipher)
    FinalCipher = []
    for x in range(len(RemainingCipher)):
        #print("KTL[X]", KTL[x])
        FinalCipher.append(KTL[x])
        #print(FinalCipher)
    return FinalCipher

def CreateCode():
    Code = {}
    Letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
               19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34,
               35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
               51]
    for x in range(len(Letters)):
        Code[Letters[x]] = Numbers[x]
    return Code

def FindLastValues(KTL, Code):
    LastValues = []
    for x in range((len(KTL) - 1), 0, -1):
        if KTL[x] != "_" and KTL[x] == str(KTL[x]):
            LastValues.append(int(Code[KTL[x]]))
        if len(LastValues) == 2:
            break
    return LastValues

def FindLastPos(KTL, Code):
    LastPos = []
    for x in range((len(KTL) - 1), -1, -1):
        if KTL[x] != "_":
            LastPos.append(int(x))
        if len(LastPos) == 2:
            break
    #print(LastPos)
    LastPos = int(LastPos[1]) - int(LastPos[0])
    return LastPos

def FindRowValue(LastValues, LastPos):
    def Pascal(NumValue):
        def ncr(n, r):
                r = min(r, n-r)
                numer = reduce(op.mul, range(n, n-r, -1), 1)
                denom = reduce(op.mul, range(1, r+1), 1)
                return numer // denom
        RowValue = []
        for y in range(NumValue+1):
            n = NumValue
            r = y
            PascalValue = ncr(n,r)
            RowValue.append(PascalValue)
        return RowValue
    RowNumber = []
    for x in range(53):
        RowValue = 0
        RowValue = Pascal(x)
        #print(RowValue)
        try:
            for i in range(len(RowValue) - 1):
                #print("I                          ", i)
                #print("LastValues[1]              ", (RowValue[i]) % 52)
                #print("RowValues[0]               ", (RowValue[i + LastPos]) % 52)
                if int(RowValue[i]) % 52 == int(LastValues[1]):
                    if int(RowValue[i + LastPos]) % 52 == int(LastValues[0]):
                        RowNumber.append(RowValue)
        except IndexError:
            pass
    return RowNumber


def FindTrueRow(RowValue, KTL, Code):
    AllPKTL = []
    AllRowTest = []
    for x in range(len(RowValue)):
        if FirstSearch == True:
            KTL = KeyToLetters(Keys[0], Ciphers[0])
            PotentialKTL = []
            PotentialKTL = KTL
            RowTestPos = -1
            RowTest = RowValue[x]
            RowTest = RowTest[0:int(len(RowTest)) // 2]
            CorrectRowCount = 0
            #print("PotentialKTL     ", PotentialKTL)
        elif FirstSearch == False:
            KTL = FindRemainingCipher(TrueRow)
            #print("KTL FRC", KTL)
            PotentialKTL = []
            PotentialKTL = KTL
            RowTestPos = -1
            RowTest = RowValue[x]
            RowTest = RowTest[0:int(len(RowTest)) // 2]
            CorrectRowCount = 0
            #print("PotentialKTL     ", PotentialKTL)
        try:
            for i in range(len(PotentialKTL)):
                if PotentialKTL[len(PotentialKTL) - i - 1] != "_":
                    if int(RowTest[RowTestPos]) % 52 == int(Code[PotentialKTL[len(PotentialKTL) - i - 1]]):
                        PotentialKTL[len(PotentialKTL) - i - 1] = RowTest[RowTestPos]
                        CorrectRowCount += 1
                        #print("PotentialKTL     ", PotentialKTL)
                    else:
                        break
                elif PotentialKTL[len(PotentialKTL) - i - 1] == "_":
                    PotentialKTL[len(PotentialKTL) - i - 1] = RowTest[RowTestPos]
                    CorrectRowCount += 1
                    #print("PotentialKTL     ", PotentialKTL)
                RowTestPos -= 1
                PotentialKTL = KTL
                if CorrectRowCount == len(RowTest):
                    for x in range(len(RowTest)):
                        #print("PKTL", PotentialKTL)
                        #print("ktl, ", KTL)
                        PotentialKTL.pop(-1)
                    AllPKTL = PotentialKTL
                    AllRowTest.append(RowTest)
        except IndexError:
            pass
                        
    return AllRowTest, AllPKTL
    
def RemoveDuplicate(TrueRow):
    NonDupeNum = []
    NonDupeLetter = TrueRow[1]
    print(TrueRow)
    for y in range(len(TrueRow)):
        for x in range(len(TrueRow[y])):
            [NonDupeNum.append(x) for x in TrueRow[0][x] if x not in NonDupeNum]
    return NonDupeNum, NonDupeLetter



Keys = []
Ciphers = []
global FinalNum
FinalNum = []

for x in range(len(Keys)):
    #STEP 1: KEY TO LETTERS
    KTL = KeyToLetters(Keys[x], Ciphers[x])
    #STEP 2: CREATE CODE FOR LETTERS TO NUMBERS
    Code = CreateCode()
    FirstSearch = True
    #STEP 3: COLLECT LAST 2 VALUES
    LastValues = FindLastValues(KTL, Code)
    #STEP 4: FIND DISTANCE BETWEEN THE VALUES
    LastPos = FindLastPos(KTL, Code)
    #STEP 5: FIND PASCAL'S ROW
    RowValue = FindRowValue(LastValues, LastPos)
    print("RV", RowValue)
    #STEP 6: CALCULATE THE ROWS WHICH FIT WITH THE CIPHERTEXT
    TrueRow = FindTrueRow(RowValue, KTL, Code)
    print("TR", TrueRow)
    #STEP 7: REMOVE DUPLICATE VALUES
    TrueRow = RemoveDuplicate(TrueRow)
    FinalNum.append(TrueRow[0])
    print("NDTR", TrueRow)
    while True:
        FirstSearch = False
        if TrueRow[1] == []:
            break
        else:
            LastValues = FindLastValues(TrueRow[1], Code)
            LastPos = FindLastPos(TrueRow[1], Code)
            RowValue = FindRowValue(LastValues, LastPos)
            TrueRow = FindTrueRow(RowValue, TrueRow[1], Code)
            TrueRow = RemoveDuplicate(TrueRow)
            FinalNum.append(TrueRow[0])
Message = []
print("Done", FinalNum)
for x in range(len(FinalNum)):
    FinalCode = NTL()
    Message.append(FinalCode[FinalNum[x][1]])
print("".join(Message[::-1]))
    
