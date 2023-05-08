"""Binary Serach."""
"""The goal of binary search is to search whether a given number is present in the string or not."""

area = [1, 3, 2, 4, 5]
area.sort()

print(area)
print("Length: ", len(area))

ind_first = 0
ind_last = len(area) - 1
ind_mid = (ind_first + ind_last) // 2

print("First index: ", ind_first)
print("Last index: ", ind_last)
print("Middle index: ", ind_mid)

item = int(input("Enter the number to be search: "))
print("----------------------------------------------------------------")
found = False
while ind_first <= ind_last and not found:
    ind_mid = (ind_first + ind_last) // 2
    if area[ind_mid] == item:
        print("Your number", area[ind_mid])
        print(f"Found at index: {ind_mid}")
        found = True
    else:
        if item < area[ind_mid]:
            print(f"Number {item} is less than {area[ind_mid]} at index {ind_mid}")
            ind_last = ind_mid - 1
            print(f"Index changed to: {ind_last}")
        elif item > area[ind_mid]:
            print(f"Number {item} is greater than {area[ind_mid]} at index {ind_mid}")
            ind_first = ind_mid + 1
            print(f"Index changed to: {ind_first}")

if found == False:
    print("Number not found")
