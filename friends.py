#!/usr/bin/env python3
# Python List Examples
import random
from termcolor import colored, cprint

friends = ['Saitana', 'Urahara', 'Levi', 'Mikasa', 'Nel tu']
wish = ['cows', 'goats', 'cats', 'dogs', 'lions']
year = [1,2,3,4,5,6,7,8,9]
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])

message1 = colored(f"{friends[0]} is a best friend", "green")
cprint(message1)
print("-----------------------------")
line = colored(f" 胸 (mune) {random.choice((wish))}", "magenta")
line2 = colored(f" おっぱい (oppai)  {random.choice((wish))}", "yellow")
line3 = colored(f" 乳 (chichi) {random.choice((wish))}", "light_grey")

cprint(line)
cprint(line2)
cprint(line3)

print("-----------------------------")
message2 =f"I enjoy going to {friends[1]} house for dinner"
print(message2)
message3 =f"I miss hanging out with {friends[2]}"
print(message3)
message4 =f"{friends[3]} was jealous of my friends"
print(message4)
message5= f"{friends[4]}'s mom was a great lady"
print(message5)
print("Becca")
