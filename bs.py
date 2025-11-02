
array = list(range(0,900,2))
def binary_search(array, target):
    left = 0
    right = len(array)-1

    while (left <= right):
        mid = (right + left) // 2
        # 13 /2 = 6.5 floor 6
        print(f"mid values is {mid}")
        print(f"left is {left}")
        print(f"right is {right}")
        print('------------')

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            
            # array = [7,8,9,10,11,12,13]
            # array = [7,8,9,10]
            
            left = mid + 1
            print(left)
        else:
            right = mid -1
            #array = [8,9]
    return -1

print(binary_search(array,200))

