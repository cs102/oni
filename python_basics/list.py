#!/usr/bin/env python

names = ["cash","dash" , "max"]
new_names =[]

for n in names:
    if n.islower():
        n = n.capitalize()
    else:
        n = "Relax " + n.capitalize()
    new_names.append(n)

names = new_names

print(names)
print("----------------------")

fruits = ["apples", 'bananas', 'mango', 'anonas']
for fruit in fruits:
    print(fruit.title())

print(sorted(fruits))
print(len(fruits))

print("----------------------")
print(" List Comprehension")
print("----------------------")

gundams = ["exia", "x105", "x109", "freedom"]

gundams = [gundam.upper() for gundam in gundams]

print(gundams)

print("X105",'x105' in gundams)

print("----------------------")
print("x to the 2 power" )
print("----------------------")

squares = []
for x in range(10):
    squares.append(x**2)
squares
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

print("----------------------")
print("For Loops ")
print("----------------------")

names = ['Echo', 'Fives', 'Cody', 'Rex']
for name in names:
    print(name)

print(names[0])
print("----------------------")


for item in range(10):
    print(item)
print("----------------------")


for i in range(4):
    print(i)
print("----------------------")

for letter in range(2):
    print('hello')
    print('another hello')

print("----------------------")


movie = "StarWars:AttackOfTheClones"
my_movie = "".join(
        [i if i.islower() else " " 
         + i for i in movie
         ])[1:]
print(movie)
print(my_movie)
