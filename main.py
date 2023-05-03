from random import randint
countries = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                 "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье", "Сербия": "Белград"}
print(countries)
print(countries['Ирландия'])
for key in sorted(countries):
    print(key, ' - ', countries[key])
def zad2():
    alph = {
        "а": 1,
        "б": 3,
        "в": 1,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3
    }
    a= input('Слово')
    s= 0
    for i in a:
        s+= alph[i.lower()]
    print(s)
zad2()
def zad3():
    stud=['Иванов',  'Студнев', 'Сидоров', 'Петров', 'Ковалёв']
    lang={1:'русский', 2:'китайский', 3: 'французский', 4:'немецкий', 5: 'английский'}
    rasp={}
    kol= set()
    vsego=set()
    zn=list()
    kit=list()
    for i in range(5):
        for j in range(randint(1, 5)):
            kol.add(randint(1, 5))
        rasp[stud[i]] = kol
        kol=set()
    print(rasp)
    for key in rasp:
        vsego=vsego.union(rasp[key])
    for i in vsego:
        zn.append(lang[i])
    print('Студенты знают', len(vsego), 'языков:', sorted(zn))
    for key in rasp:
        if 2 in rasp[key]:
            kit.append(key)
    print('Китайский знают: ', sorted(kit))

zad3()
