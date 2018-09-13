def ask_user():
        a = input() 
        if a in d.keys():
            print(d[a])
            return True
        else:
            print('попробуй спросить что-нибудь ещё?')
            return False
d = {
'Как дела?':'Хорошо',
'Что делаешь?':'Программирую'
 }

print('Спроси меня что-нибудь ?')

while True:
    if ask_user():
        break