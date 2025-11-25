file_path = "output.txt"
import ast 

print("\n"+ "###" + "\n")
with open(file_path) as infile:
    words = ast.literal_eval(infile.read())
    print(words)
    print("\n"+ "###" + "\n")
    print("total words in this list : ", len(words))
    
    print("\n"+ "###" + "\n")
    words.sort()
    print(words)

    print("\n"+ "###" + "\n")
    print("Longest word in set : " + max(words, key=len)+ "\n")
    print("Shortest word in set : " + min(words, key=len)+ "\n")


#strings = ["Hello!!!", "I", "am", "Cherry"]

#print(max(strings, key=len)) # prints "Hello!!!"

#print(min(strings, key=len)) # prints "I"
