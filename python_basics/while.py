i = 1

while i < 5:
    print(i)
    i += 1
print('the end')
print('----------------------------------')

name = 'kylie'
for letter in name:
    print(letter)


print('----------------------------------')

gundams = ['x105', 'x109', 'justice', 'freedom']
for gundam in gundams:
    print(gundam)


print('----------------------------------')
numbers = [1998,2000,2002,2007,2008,2016]
for number in numbers:
    print(number)

colors = ['orange', 'green', 'purple', 4]
fruits = ['mango', 'banana', 'coconut', 2]

for color in colors:
    for fruit in fruits:
        print(color, fruit)

word_list = ['Ed', 'Rex', 'Becca', 'Kylie Ying']
for word in word_list:
    print(word)
    if word =='Becca':
        break
print('the end')
print('----------------------------------')

i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
print('the end')
print('----------------------------------')


word_list = ['Ed', 'Rex', 'Becca', 'Kylie Ying']
for word in word_list:
    if word =='Becca':
        continue
    print(word)
print('the end')

