def compare_line(first_argue, second_argue): #на самом деле не имеет смысла,  так как всё, чиро мы получаем через input итак будет строкой, соответсвенно проверять нечего, но в задание просили сделать -  сделал
    if not isinstance(first_argue, str): 
        return 0
    elif not isinstance(second_argue, str):
        return 0
    else:
        print("Оба значения строки")

def string(first_argue, second_argue):
    if len(first_argue) == len(second_argue):
        return 1
    if second_argue == 'learn':
        return 3
    elif len(first_argue) > len(second_argue):
        return 2
    else:
        print('Второй аргумент больше перового')

first_argue = input('Введите что-нибудь      ')
second_argue = input('И ещё что-нибудь             ')
print('Вы ввели {0} и {1}'.format(first_argue, second_argue))
result1 = compare_line(first_argue, second_argue)
result2 = string(first_argue, second_argue) 
print(result1)
print(result2)
