pi = 3
for i in range(1,16):
  if i%2==0:
    pi -= 4/(i*2*(i*2+1)*(i*2+2))
  else:
    pi += 4/(i*2*(i*2+1)*(i*2+2))
  print(pi)