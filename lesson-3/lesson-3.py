import json
# JSON faylni o'qib olish
f = open('data.json')
data = json.load(f)

while True:
    boshlangichHolat = input(" 1 =>  Qiriduv\t 2 => Ma'lumotlarni ko'rsatish\t  3=> Ma'lumot hajmi\n")
    if boshlangichHolat == '1':
        while True:
            # Foydalanuvchi kiritishni so'raymiz
            search = input("Qidirilayotgan qiymatni kiriting: ")

            # Topilgan ma'lumotlarni ekranga chiqaramiz
            found_data = []

            for object in data:
                for value in object.values():
                    if str(search).lower() in str(value).lower():
                        found_data.append(object)

            # Topilgan ma'lumotlarni chiqarish
            if found_data:
                print("Topilgan ma'lumotlar:")
                for object in found_data:
                    # print(object)
                    print(json.dumps(object, indent=4))
                else:
                    print("Kechirasiz, topilmadi!")

            request = input("Yana qidirishni hohlaysizmi: -> 1\n Chiqish -> 0:\n>>>")
            if request == '1' :
                continue
            elif request == '0':
                break
            else:
                print("Xato buyruq")


    elif boshlangichHolat == '2':
        print(json.dumps(data, indent=4))
    elif boshlangichHolat == '3':
        print(len(data))
    else:
         print("Xato buyruq kiritdingiz")
         break