#Строки и индексация строк

example = 'Дисциплина'
print(example[0])
print(example[-1])
print(example[5:])
print(example[::-1])

#хотел вывести с первого символа с шагом 2, но не знаю считалось бы правильным,
#так как в примере со второго, поэтому вывел так
print(example[1::2])