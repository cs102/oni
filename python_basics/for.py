total = 0
print(4 % 3)
print(5 % 3)
print(1 % 3)
print(6 % 3)
print(list(range(1,8)))
for i in range(1, 8):
    if i % 3 == 0:
        total += 1
print(total)
print("*****")
s = "demo loop - fruit loop"
print(s)
for index in range(len(s)):
    if s[index] == 'i' or s[index] =='u':
        print("there is an i or u")

for char in s:
    if char == 'i' or char =='u':
        print("there is an i or u")
