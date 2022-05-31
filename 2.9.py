string = input("Введите строку")
reversed_string = ""
for i in range(len(string), 0, -1):
  reversed_string += string[i-1]
if string == reversed_string:
  print("Палиндром")
else:
  print("Не палиндром")