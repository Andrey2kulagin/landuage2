for i in range(0,101,10):
  temp_dict = {}
  temp_dict["Температура в цельсиях = "]=float(i)
  temp_dict["Температура в фарингейтах"] = 32+1.8*i
  print(temp_dict)