try:
    flearnt = open("learnt.txt", "x") #eğer yoksa bilinen kelimeler dosyası oluşturma
except:
    pass

try:
    flearnt = open("learning.txt", "x") #eğer yoksa öğrenilen kelimeler dosyası oluşturma
except:
    pass

#yukarıdakiler de dahil olmak üzere kod genel olarak optimize değil, önerini beklerim

flearnt = open("learnt.txt", "r") #bilinen kelimeleri içeren dosyayı açma ve liste oluşturma
learnts = flearnt.read().split("\n")
flearnt.close()

fstudying = open("learning.txt", "r") #öğrenilmekte olan kelimeleri içeren dosyayı açma ve liste oluşturma
studyings = fstudying.read().split("\n")
fstudying.close()

text= None
def know(com):
    flearnt = open("learnt.txt", "a")
    flearnt.write("\n" + com) #kelimeyi bilinenlere ekleme
    flearnt.close()
    if com in studyings: #kelime eğer öğrenilenlerde ise oradan silme
        studyings.remove(com)
        fstudying = open("learning.txt", "w")
        fstudying.write('\n'.join(studyings))
        fstudying.close()

def study(com):
    fstudying = open("learning.txt", "a")
    fstudying.write("\n" + com)
    fstudying.close()

def commands(com):
    if com[:4] == "know": #bilinenlere ekleme
        know(com[5:])

    elif com[:5] == "study": #öğrenilenlere ekleme
        study(com[6:])

    elif com=="list": #tüm bilinmeyen kelimeleri listeler
        for word in wordList:
            if word not in learnts and word not in studyings:
                print(word, end="       ")
                com2 = input()
                if com2=="know" or com2=="k":
                    know(word)
                elif com2=="study" or com2=="s":
                    study(word)
                elif com2=="pass" or com2=="p":
                    pass
                else:
                    print("Error! Unknown command")

    elif com=="help": #komutlar
        print("\'know + word\' adds word to the learnt words list\n\'study + word\' adds word to the studying words list")

    else:
        global text
        text = com



commands(input("Text:"))

spChars = ['"','!','?','.','-','(',')','[',']','♪',',','...'] #özel karakterleri boşluğa çevirme
if text:
    for i in spChars:
        text = text.replace(i, " ")

    wordList = text.split() #boşluklarla ayırıp listeye çevirme
    wordList = [i.lower() for i in wordList] #hepsini küçük harfli yapma
    wordList = set(wordList) #birden fazla olan kelimeleri silme
    wordList = list(wordList)
    for i in wordList: #sayılarla başlayanları çıkarma
        if ord(i[0])>47 and ord(i[0])<58:
            wordList.remove(i)
    wordList.sort() #alfabetik sıralama

    print("")
    print("\nNot Learnt:") #bilinmeyen kelimeler
    for word in wordList:
        if word not in learnts and word not in studyings:
            print(word)

    print("\nLearning:") #bilinen kelimeler
    for word in wordList:
        if word in studyings and word not in learnts:
            print(word)

while True:
    commands(input("\nCommand:"))

input()
