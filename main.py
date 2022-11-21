# Класс Post
# Класс описывает публикацию от пользователя в сети:
# – никнейм пользователя,
# – время публикации,
# – количество лайков,
# – текст сообщения,
# – список комментариев.
# Конструктор класса получает автора, устанавливает время, зануляет количество
# ругательств, а для комментариев создает списочный массив.
# Добавить метод, позволяющий поставить лайк сообщению


# import datetime
#
# class Post:
#     def __init__(self, author, text, arr=[], laiks = 0):
#         self.author = author
#         self.time = datetime.datetime.now()
#         self.laiks = laiks
#         self.text = text
#         self.arr = arr
#
#     def laik(self):
#         laik = input("добавить лайк? да/нет")
#         if laik == 'да':
#             self.laiks += 1
#
#     def add_post(self):
#         wolds = ['блин', 'хрен']
#         self.text = input("Введите текст сообщения").split()
#         for i in self.text:
#             print(i)
#             if i in wolds:
#                 self.text = self.text.replace(i, '***')
#
#     def add_comments(self):
#         self.arr = []
#         coment =  input('добавить комметнарий. 0-для отмены')
#         while coment !='0':
#             self.arr.append(coment)
#             coment = input('добавить комметнарий. 0-для отмены')
#
#     def print_coments(self):
#         for arr in self.arr:
#             print(arr)
#
#     def post(self):
#         print('Автор-', self.author)
#         print('время публикации-', self.time)
#         print('текст сообщения-', self.text)
#         print('количество лайков-', self.laiks)
#         # print('список комментариев-', self.arr)
#
# post = Post('','','')
# post.add_post()
# post.laik()
# post.add_comments()
# post.post()
# post.print_coments()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Класс «Клиент» содержит поля: код клиента, ФИО, дата открытия вклада, размер
# вклада, процент по вкладу.
# Класс «Банк» (class Bank) содержит поле clientBase представляющем собой список
# клиентов и методами:
# – addClient(client) — принимает обьект клиента и помещает его в base.
# – showByMoney(money) — принимает количество денег и выводит информацию о всех
# клиентах у которых размер вклада больше
# – showByCode(cod) — принимает код и выводит всю информацию клиенте с данным
# кодом.
# – showByProc(proc) — принимает процент и выводит информацию о всех клиентах у
# которых процент по вкладу больше данного.

class Client():
    def __init__(self, base={}):
        self.base = base

    def read_file(self):
        with open('D:\Курс Python226\модуль_44 12.10.22 python ООП-3\pythonProject\class\clients.txt', 'r',
                  encoding='utf-8') as file:
            text = file.read()
            if not text:
                # print("text not")
                self.base = {}
                count = 0
            else:
                # print(text)
                # self.base = text
                text = text.replace('}{', ', ')
                text = text.replace('{', '')
                text = text.replace('}', '')
                text = text.replace(']', ']]')
                tx = text.split('], ')
                # print(text, '|||')
                self.base = {}
                # print(type(self.base), "r|||")
                for i in tx:
                    # print(i)
                    i = i.split(':')
                    # print(i)
                    arg = i[1]
                    arg = arg.replace("[",'')
                    arg = arg.replace("]", '')
                    arg = arg.replace("'", '')

                    # print(arg)
                    arg = arg.split(",")
                    fio = arg[0]
                    date_open = arg[1]
                    summ = int(arg[2])
                    procent = int(arg[3])

                    self.base[int(i[0])] = [fio, date_open, summ, procent]
                # print(self.base)

                # print(type(self.base))
                # print(tx)
                count = len(self.base)
                # print(count)
                return count

    def addClient(self):
        count = self.read_file()
        adds = input('Хотите ввести клиента? да/нет')

        while adds != 'нет':
            count += 1
            cod = count
            fio = input('введите фио клиента:')
            date_open = input('введите дату через точку (.):')
            summ = int(input('введите сумму вклада:'))
            procent = int(input('введите процент:'))
            adds = input('Хотите ввести клиента? да/нет')
            self.base[cod] = [fio, date_open, summ, procent]

        with open('D:\Курс Python226\модуль_44 12.10.22 python ООП-3\pythonProject\class\clients.txt', 'w+',
                  encoding='utf-8') as file:
            file.write(str(self.base))

    def showByMoney(self):
        self.read_file()
        summa = int(input('Введите сумму:'))
        for price in self.base.values():
            num = price[2]
            if num > summa:
                fio = price[0]
                print(fio, '-', num)

    def showByCode(self):
        self.read_file()
        codes = int(input('Выедите код клиента:'))
        if codes in self.base.keys():
            print(self.base[codes],'\n')
        else:
            print('Клиента с таким кодом не существует')

    def showByProc(self):
        self.read_file()
        proc = int(input('Введите размер процента:'))
        for pricent in self.base.values():
            nums = pricent[3]
            if nums > proc:
                fio = pricent[0]
                print(fio, '-', nums)


print('ВАС ПРИВЕТСТВУЕТСИСТЕМА БАНКА\n')
print('Выберете меню:\n')
total = int(input('1. Ввести клиента\n' \
                  '2. Запросить минимальную сумму вклада\n' \
                  '3. Вывести клиента по коду\n' \
                  '4. Запросить сумму процента\n'))

obj = Client()
while True:
    if total == 1:
        obj.addClient()
    elif total == 2:
        obj.showByMoney()
    elif total == 3:
        obj.showByCode()
    elif total == 4:
        obj.showByProc()
    else:
        print('Такого пунка нет')

    total = int(input('1. Ввести клиента\n' \
                      '2. Запросить сумму вклада\n' \
                      '3. Вывести клиента по коду\n' \
                      '4. Запросить сумму процента\n'))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
### Рабочий вариант


Класс «Клиент» содержит поля: код клиента, ФИО, дата открытия вклада, размер
вклада, процент по вкладу.
Класс «Банк» (class Bank) содержит поле clientBase представляющем собой список
клиентов и методами:
– addClient(client) — принимает обьект клиента и помещает его в base.
– showByMoney(money) — принимает количество денег и выводит информацию о всех
клиентах у которых размер вклада больше
– showByCode(cod) — принимает код и выводит всю информацию клиенте с данным
кодом.
– showByProc(proc) — принимает процент и выводит информацию о всех клиентах у
которых процент по вкладу больше данного.


class Client():
    def _init_(self, base = {}):
        self.base = base

    def addClient(self):
        self.base = {}
        adds = input('Хотите ввести клиента? да/нет')
        count = 0
        while adds != 'нет':
            count += 1
            cod = count
            fio = input("Введите ФИО клиента: ")
            data = int(input("Введите дату: "))
            vklad = int(input("Введите вклад: "))
            procent = int(input("Введите процент вклада: "))
            adds = input('Хотите ввести клиента? да/нет')
            self.base[cod] = [fio, data, vklad, procent]

    def showByMoney(self):
        summa = int(input("Введите сумму: "))
        for price in self.base.values():
            num = price[2]
            if num > summa:
                fio = price[0]
                print(fio, '-', num)

    def showByCode(self):
        codes = int(input("Введите код клиента: "))
        if codes in self.base.keys():
            print(self.base[codes])
        else:
            print("Клиента с таким кодом не существует")

    def showByProc(self):
        proc = int(input("Введите размер процента: "))
        for pricent in self.base.values():
            nums = pricent[3]
            if nums > proc:
                fio = pricent[0]
                print(fio, '-', nums)

print("ВАС ПРИВЕТСВУЕТ СИСТЕМА БАНКА \n")
print("Выберете меню: ")
total = int(input("1. Ввести клиента\n2. Запросить сумму вклада\n3. Вывести клиента по коду\n4. ЗАпросить сумму процента\n"))
obj = Client()
while True:
    if total == 1:
        obj.addClient()
    elif total == 2:
        obj.showByMoney()
    elif total == 3:
        obj.showByCode()
    elif total == 4:
        obj.showByProc()
    else:
        print("Такого пункта нет")

    total = int(input("1. Ввести клиента\n 2. Запросить сумму вклада\n 3. Вывести клиента по коду\n 4. ЗАпросить сумму процента\n"))

fdsfdsfdf f rgerg
gfdgerg erg er
fdsfdsf
