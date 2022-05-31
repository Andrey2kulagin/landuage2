import math
first_x = int(input("Введите первую координату Х "))
first_y = int(input("Введите первую координату Y "))
last_x = first_x
last_y = first_y
cure_x = input("Введите следующую координату Х(Enter для окончания ввода) ")
cure_y = input("Введите следующую координату Y ")
len_ = 0
while cure_x!="":
  cure_x = int(cure_x)
  cure_y = int(cure_y)
  cure_len = math.sqrt((cure_x-last_x)**2+(cure_y-last_y)**2)
  len_ +=cure_len
  last_x = cure_x
  last_y = cure_y
  cure_x = input("Введите следующую координату Х(Enter для окончания ввода) ")
  if cure_x=="": break
  cure_y = input("Введите следующую координату Y ")
cure_len = math.sqrt((last_x-first_x)**2+(last_y-first_y)**2)
len_ +=cure_len
print(len_)