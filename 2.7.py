alfabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
num = int(input("введите число для раскодирования "))
word = str.lower(input("введите слово для раскодирования "))
out_word = ""
for i in word:
  if i not in alfabet:
    out_word+=i
    continue
  index = alfabet.find(i)
  out_word+=alfabet[(index+num)%len(alfabet)]
print(out_word)