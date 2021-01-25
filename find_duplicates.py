numbers = [10,30,30,69,10,10,10,30,50,69,70,100,101,100,101,3,0,40,21,45,14,60,100,101,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numbers.sort()
unique_numbers = []
for index in range(len(numbers)):
    if numbers[index] in unique_numbers:
        continue
    else:
        nextIndex = index + 1
        if numbers[index] == numbers[nextIndex]:
            unique_numbers.append(numbers[index])
print(numbers)
print("=============================================================================")
print(unique_numbers)