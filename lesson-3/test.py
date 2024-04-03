
data = [
    {'id': 991, 'last_name': 'Cattroll', 'age': 29.5, 'address': 'PO Box 58046', 'gender': 'M', 'phone_number': '310-884-2743', 'job': 'Recruiter', 'date_time': '7/21/2023'},
    {'id': 992, 'last_name': 'Gallon', 'age': 29.1, 'address': '15th Floor', 'gender': 'M', 'phone_number': '818-604-6378', 'job': 'Nurse', 'date_time': '10/8/2023'},
    {'id': 993, 'last_name': 'Cattroll', 'age': 91.2, 'address': '3rd Floor', 'gender': 'M', 'phone_number': '270-887-9717', 'job': 'Nurse', 'date_time': '3/21/2024'},
    {'id': 994, 'last_name': 'Sagg', 'age': 77.8, 'address': 'Apt 652', 'gender': 'F', 'phone_number': '405-125-4124', 'job': 'Tax Accountant', 'date_time': '6/7/2023'},
    {'id': 995, 'last_name': 'Gulland', 'age': 35.1, 'address': 'PO Box 22715', 'gender': 'M', 'phone_number': '572-738-9285', 'job': 'Human Resources Assistant I', 'date_time': '3/21/2024'},
    {'id': 996, 'last_name': 'Kintish', 'age': 98.0, 'address': 'PO Box 57950', 'gender': 'M', 'phone_number': '696-542-6964', 'job': 'Data Coordinator', 'date_time': '8/20/2023'},
    {'id': 997, 'last_name': 'Meas', 'age': 10.7, 'address': 'PO Box 39935', 'gender': 'M', 'phone_number': '166-257-3879', 'job': 'Marketing Manager', 'date_time': '1/21/2024'},
    {'id': 998, 'last_name': 'Wheaton', 'age': 4.2, 'address': '19th Floor', 'gender': 'M', 'phone_number': '489-171-5366', 'job': 'Financial Analyst', 'date_time': '1/21/2024'},
    {'id': 999, 'last_name': 'Curgenven', 'age': 43.2, 'address': 'Room 1908', 'gender': 'F', 'phone_number': '192-905-2704', 'job': 'Compensation Analyst', 'date_time': '2/17/2024'},
    {'id': 1000, 'last_name': 'Demeter', 'age': 25.4, 'address': 'Room 1838', 'gender': 'F', 'phone_number': '402-912-7457', 'job': 'Business Systems Development Analyst', 'date_time': '2/19/2024'}
]

# Foydalanuvchi kiritishni so'raymiz
qidirilayotgan_qiymat = input("Qidirilayotgan qiymatni kiriting: ")

# Topilgan ma'lumotlarni ekranga chiqaramiz
topilgan_malumotlar = []

for malumot in data:
    for qiymat in malumot.values():
        if str(qidirilayotgan_qiymat).lower() in str(qiymat).lower():
            topilgan_malumotlar.append(malumot)

# Topilgan ma'lumotlarni chiqarish
if topilgan_malumotlar:
    print("Topilgan ma'lumotlar:")
    for malumot in topilgan_malumotlar:
        print(malumot)
else:
    print("Kechirasiz, topilmadi!")
