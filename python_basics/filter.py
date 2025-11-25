# print words longer than 5 strings

def longer_than_5(string):
    return len(string) > 5

words = ["biology", "mango", "train", "octopus", "cycle"]

filtered = filter(longer_than_5, words)

print(list(filtered))

# map build in function in Python 

# using words array above checking length of each item

words_size = map(len,words)

# using list to convert words_size from a map object
# <map object at 0x10b671c90>
print(list(words_size))
