import random

nameList = []
cityList = ["istanbul","ankara","giresun","izmir","antalya","muğla","ordu","trabzon","gaziantep",
             "şanlıurfa","yalova","kocaeli","bolu","adana","hakkari","bursa",]
animalList=["zürafa","ayı","arı","köpek"
    ,"kedi","kuzu","keçi","kuş","koyun","tavuk","kertenkele","yılan","salyangoz", "balık"]

def hello():
    name = input("Adınızı Giriniz: ").capitalize()
    if name:
        print(f"{name} Adam Asmacaya Hoşgeldin...")
        gameMode()
    else:
        hello()

def gameMode():
    gamemode = input("Oyun Modunu Seçiniz:\n1. İsim Listesi\n2. Şehir Listesi\n3. Rasgele Liste Seçimi\n=> ")
    if gamemode == "1":
        createRandomKey(nameList)
    if gamemode == "2":
        createRandomKey(cityList)
    if gamemode == "3":
        randomSelect = [nameList,cityList]
        idx = random.randint(0,1)
        createRandomKey(randomSelect[idx])

def createRandomKey(keyword):
    idx = random.randint(0,len(keyword)-1)
    selectedKey = keyword[idx]
    startGame(selectedKey)

def findIdx(keyword,word):
    idx= []
    for i in range(len(keyword)):
        if keyword[i] == word:
            idx.append(i)
    return idx

def printWrongKey(findKey):
    print("Kullandığınız Harfler: ")
    for i in findKey:
        print(i,end=" ")
    print("\n")

def startGame(selectedKey):
    counter = 0
    findKey = []
    sentence = "_" * len(selectedKey)
    print()
    print(sentence)
    while True:
        inputChar = input("Harf Giriniz: ")
        if inputChar in findKey:
            print("Aynı Harfi Yazamazsın!")
        else:
            findList = findIdx(selectedKey,inputChar)
            if len(inputChar) == 1:
                findKey.append(inputChar)
                if findList:
                    for i in findList:
                        x = sentence[i].replace("_",inputChar)
                        sentence = sentence[:i] + x + sentence[i+1:]
                    print(sentence,"\n")
                    if sentence == selectedKey:
                        print("Tebrikler Kazandınız...")
                        break
                else:
                    print("Yanlış Harf\n")
                    printWrongKey(findKey)
                    counter+=1
                    print(sentence)
                    print("\n")
                    if counter == 1:
                        print("|\n"*6)
                    if counter == 2:
                        print("|","-"*10)
                        print("|\n"*5)
                    if counter == 3:
                        print("|","-"*10,"|")
                        print("|\n"*5)
                    if counter == 4:
                        print("|","-"*10,"|")
                        print("|"," "*10,"0")
                        print("|\n"*4)
                    if counter == 5:
                        print("|","-"*10,"|")
                        print("|"," "*10,"0")
                        print("|"," "*10,"|")
                        print("|"," "*10,"|")
                        print("|\n"*2)
                    if counter == 6:
                        print("|","-"*10,"|")
                        print("|"," "*10,"0")
                        print("|"," "*8,"/","|")
                        print("|"," "*10,"|")
                        print("|\n"*2)
                    if counter == 7:
                        print("|","-"*10,"|")
                        print("|"," "*10,"0")
                        print("|"," "*8,"/","|","\\")
                        print("|"," "*10,"|")
                        print("|\n"*2)
                    if counter == 8:
                        print("|","-"*10,"|")
                        print("|"," "*10,"0")
                        print("|"," "*8,"/","|","\\")
                        print("|"," "*10,"|")
                        print("|"," "*8,"/")
                        print("|")
                    if counter == 9:
                        print("|","-"*10,"|")
                        print("|"," "*10,"0")
                        print("|"," "*8,"/","|","\\")
                        print("|"," "*10,"|")
                        print("|"," "*8,"/"," ","\\")
                        print("|")
                        print(f"Adam Asıldı Tekrar Dene. Kelime: {selectedKey}")
                        break
            else:
                print("Tek Harf Giriniz...")

def fileOperation():
    file = open("trName.txt","r",encoding="utf-8")
    for line in file:
        line = line.strip().split(",")

    print(len(line))
    file.close()
    for i in line:
        nameList.append(i)

fileOperation()
hello()
