filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    #print(pi_string[:52] + "...")
    #print(len(pi_string))
    birthday = input("Enter DOB, form mmddYY: ")
    if birthday in pi_string:
        print("Your birthday in the first million digits of pi ◝(ᵔᗜᵔ)◜")
    else:
        print("Your birthday is does not °՞(ᗒᗣᗕ)՞° appear in the first million of pie")
