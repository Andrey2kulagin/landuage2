x = int(input("введите х "))
gues = x/2
while abs(x-gues**2)>(10**-12)  :
  gues = (gues+x/gues)/2
print(gues)