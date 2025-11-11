def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            return mid  # Found the target, return its index
        elif guess < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half
    
    return -1  # Target not found

def main():
    arr = list(range(1, 29))
    target = 21
    
    print(f"Searching for {target} in array: {arr}")
    
    index = binary_search(arr, target)
    
    if index != -1:
        print(f"Found {target} at index {index}.")
    else:
        print(f"{target} not found in the array.")

if __name__ == "__main__":
    main()

