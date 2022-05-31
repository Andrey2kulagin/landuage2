numbers_arr = []
numbers_arr.append(float(input("введите последовательность чисел, окончание последовательности - '0' ")))
if numbers_arr[0] == 0:
    raise Exception("Первое число не может быть нулём")

while True:
    num = float(input())
    if num == 0:
        break
    else:
        numbers_arr.append(num)
avarge = sum(numbers_arr) / len(numbers_arr)
print(avarge)