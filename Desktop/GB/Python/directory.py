def work_with_phonebook():
    choice=show_menu()

    phone_book=read_txt('phonebook.txt')

    while (choice!=8):

        if choice==1:
            print(phone_book)
            print(type(phone_book[1]))
            print_txt('phonebook.txt')
        elif choice==2:
            last_name=input('Введите фамилию: ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            change = change_number(phone_book,last_name,new_number)
            write_txt('phonebook.txt',change)
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname('phonebook.txt',lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data')
            write_txt('phonebook.txt', user_data)
        elif choice==7:
            write_from_to('phonedop.txt', 'phonebook.txt')

        choice=show_menu()


def show_menu():
    print('1. Вывести всю телефонную книгу')
    print('2. Найти контакт по фамилии')
    print('3. Изменить номер контакта')
    print('4. Удалить контак по фамилии')
    print('5. Найти по номеру телефона')
    print('6. Внести новый контакт')
    print('7. Внеси контаки из другого документа')
    print('8. Завершить работу')
    choice=int(input("введите команду"))
    return choice

def print_txt(filename):
    # gaps = lambda x,n: x + ''.join(['' for i in range(n-len(x))])
    with open(filename,'r',encoding='utf-8') as file:
        print(*list(map(lambda x: x + ''.join([' ' for i in range(15-len(x))]), ['Фамилия','Имя','Телефон','Описание'])))
        for line in file:
            contact = line.split(', ')
            print(*list(map(lambda x: x + ''.join([' ' for i in range(15-len(x))]),contact)))

def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

	

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:

            record = dict(zip(fields, line.split(',')))

			# dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
	     
            phone_book.append(record)	

    return phone_book

def write_txt(filename, new_datas):
    phone_book=read_txt('phonebook.txt')
    with open(filename,'w',encoding='utf-8') as phout:
        datas = new_datas + '\n'
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                # print(v)
                s += v + ','
                # print(s)
            datas += s[:-1]
            # print(datas)
        phout.write(datas)

def find_by_lastname(phone_book,surname):
    for element in phone_book:
        if element['Фамилия'] == surname:
            for k in element.keys():
                print(element[k], end ='')

def find_by_number(phone_book,number):
    for element in phone_book:
        if element['Телефон'] == number:
            for k in element.keys():
                print(element[k], end ='')

def change_number(phone_book,last_name,new_number):
    new_data=''
    for element in phone_book:
        if element['Фамилия'] == last_name:
            element['Телефон'] = new_number
            
            delete_by_lastname('phonebook.txt',last_name)
            for key in element.keys():
                new_data += element[key]+', '
    return(new_data[:-3])    

def delete_by_lastname(filename,lastname):
    with open(filename,'r',encoding='utf-8') as readfile:
        contacts=[]
        for line in readfile:
            if lastname not in line:
                contacts.append(line)
    with open(filename, 'w',encoding='utf-8') as writefile:
        for i in contacts:
            writefile.write(i)

        # with open(filename,'w',encoding='utf-8') as phout:
        # datas = new_datas + '\n'
        # for i in range(len(phone_book)):
        #     s = ''
        #     for v in phone_book[i].values():
        #         # print(v)
        #         s += v + ','
        #         # print(s)
        #     datas += s[:-1]
        #     # print(datas)
        # phout.write(datas)
        

    # with open(filename, 'w') as data:
    #     for i in contacs:
    #         data.write(i)


def write_from_to(filename_from, filename_to):
    with open(filename_from, 'r', encoding='utf-8') as first:
        new_contact = first.readlines()[int(input('введите номер строки для добавления в записную книгу '))-1][:-1]
    write_txt(filename_to, new_contact)   

work_with_phonebook()
