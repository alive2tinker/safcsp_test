numbers = [3, 7, 1, 2, 8, 4, 5]
numbers.sort()
resultArr = []
for i in range(len(numbers)):
    try:
        if (numbers[i+1] - numbers[i]) == 2:
            resultArr.append(numbers[i])
            resultArr.append(numbers[i]+1)
        else:
            resultArr.append(numbers[i])
    except Exception:
        resultArr.append(numbers[i])

print(numbers)
print(resultArr)