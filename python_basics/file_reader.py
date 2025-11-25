# reads a file
# open looks for file in same directory

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# improving 
print("\n" + "### Improved" + "\n")

filename = 'pi_digits.txt'

with open(filename) as file_object:
    pi_strings =''
    for line in file_object:
        print(line.rstrip())
        pi_strings += line.rstrip()
        # https://docs.python.org/3/library/stdtypes.html#str.rstrip
        print(len(pi_strings))
        print(pi_strings)

        
