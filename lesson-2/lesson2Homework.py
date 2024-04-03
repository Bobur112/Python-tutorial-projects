mark = ['xan', 'Song Plus','c11', '01', 'Seltos', 'K5']
company = ['byd','byd', 'leap motor', 'zeekir','kia', 'kia']
status = ['yangi', 'yurgan: (0-50 km)', 'yurgan: (50-150km)','yangi','yangi','yangi']
autoDealer = ['DMC Group', 'Drivers Village', 'AutoLady','DMC Group', 'DMC Group', 'DMC Group']

listSum = [mark, company, status, autoDealer]

def MalumotKiritish():
    while True:
        nomi = input("Moshinaning markasini: ")
        zavodNomi = input("Moshinaning companiyasi nomini kiriting: ")
        holati = input("Moshinaning holatini kiriting: ")
        diller = input("Toshkentdagi avto Dillerni kiriting: ")

        mark.append(nomi)
        company.append(zavodNomi)
        status.append(holati)
        autoDealer.append(diller)
     
        sorov = input('Qoshish -> 1\n Chiqish -> 0:\n>>>')
        if sorov == '1' :
            continue
        elif sorov == '0':
            break
        else:
            print("Xato buyruq")
        
        

def PrintMessage(index):
    message = f"""
        Mark:  {mark[index]}
        Company: {company[index]}
        Status: {status[index]}
        AutoDiller: {autoDealer[index]}
    """
    print(message)

def FullMessage():
    for index in range(len(mark)):
        PrintMessage(index)

def SozniTozalash(search):
    return "".join(search.lower().split())

def mana(index, search, word):
    search = SozniTozalash(search)
    word = SozniTozalash(word)
    if search in word:
        PrintMessage(index)  

def SearchData():
        search = input("Qidirmoqchi bo'lgan ma'lumotingizni kiriting: ")
        for x in listSum:
            for index, word in enumerate(x):
               mana(index, search, word)

        # for index, word in enumerate(mark):
        #     mana(index, search, word)        
        # for index, word  in enumerate(company):
        #     mana(index, search, word)         
        # for index, word  in enumerate(status):
        #     mana(index, search, word) 
        # for index, word  in enumerate(autoDealer):
        #     mana(index, search, word)


while True:
    boshlangichHolat = input(" 1 => Ma'lumot kiritish\t 2 => Qiriduv\t  3 => Ma'lumotlarni ko'rsatish\n")
    if boshlangichHolat == '1':
        MalumotKiritish()
    elif boshlangichHolat == '2':
        while True:
            SearchData()
            sorov = input("Yana qidirishni hohlaysizmi: -> 1\n Chiqish -> 0:\n>>>")
            if sorov == '1' :
                continue
            elif sorov == '0':
                break
            else:
                print("Xato buyruq")
    elif boshlangichHolat == '3':
        FullMessage()
    else:
         print("Xato buyruq kiritdingiz")
         break