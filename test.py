ss=['e','h','b','s','l','p']
for i in range(len(ss)):
  print(max(ss),end=",")
  ss.remove(max(ss))