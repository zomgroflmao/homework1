def ask_user(a):
	while True:
		if a == 'Хорошо':
			break
		elif a is not 'Хорошо':
			a = input('Как дела?') 

a = input('Как дела?')
result = ask_user(a)
print(result)

