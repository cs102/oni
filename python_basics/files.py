# creating files https://www.youtube.com/watch?v=1IYrmTTKOoI 
# x - writes a file if file does NOT exist
# w - write 
# a - to append new data
# r - reads 
### VIM  Ctrl + w + q Vim quit vertical split window
### VIM vs - vertical split
### VIM CTRL w(twice) change split screen
### VIM :e filename open file

txt_data = "Dropkick Murphys - Chestefields and Aftershave"

file_path = "output.txt"

try:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("\n" + txt_data)
        print(f"txt file '{file_path}' was created ^ ^ ")
except FileExistsError:
        print("File already exist ⊙﹏⊙ ")

