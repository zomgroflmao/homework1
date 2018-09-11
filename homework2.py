def age_occupy(age):
    if age < 7 :
        return "Ходит в детский сад"
    elif age > 7 and age < 18:
        return "Школьник"
    elif age == 7:
        return "Школьник" 
    elif  age > 18 and age < 22:
        return "Студент"
    elif  age == 18 or age == 22:
        return "Студент"
    else:
        return "Работает"


age = int(input("Угадаю по возрасту, чем занимаешься. Напиши сколько тебе лет?"))
print(age_occupy(age))