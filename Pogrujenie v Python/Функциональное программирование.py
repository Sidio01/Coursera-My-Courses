#def int_to_str(list):
#    return list(map(str, list))


#x = int_to_str(range(10))
#print(x)


a = list(zip(
  filter(bool, range(3)),
  [x for x in range(3) if x]
))
print(a)
