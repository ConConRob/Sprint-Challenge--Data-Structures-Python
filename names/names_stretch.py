import time


def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty
    if arr[0] > target:
        return -1  # item looking for is too low
    if arr[len(arr) - 1] < target:
        return -1  # item looking for is too high
    low = 0
    high = len(arr)-1
    middle = int((high-low)/2 + low)
    # TO-DO: add missing code
    while high > low:

        middle = int((high + low)/2)
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            # item is less than current middle
            high = middle
        else:
            # item is greater than current middle
            low = middle + 1

    return -1  # not found


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# STRETCH
# sort one list
names_1.sort()

# Do a bi check on every name 2
for name_2 in names_2:
    if binary_search(names_1, name_2) != -1:
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
