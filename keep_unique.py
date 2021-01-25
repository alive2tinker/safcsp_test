numbers = [10,30,30,69,10,10,10,30,50,69,70,100,101,100,101,3,0,40,21,45,14,60,100,101,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

cleanNumbers = []
for number in numbers:
    if number not in cleanNumbers:
        cleanNumbers.append(number)

print(numbers)
print("all numbers are: {}".format(len(numbers)))
print(cleanNumbers)
print("all clean numbers are: {}".format(len(cleanNumbers)))