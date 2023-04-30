str = input("Enter a string : ")
str = string.lower()
list = []
for i in string:
  if i not in list:
    list.append(i)
  else:
    pass:
string = (" ,").join(list)
print(string)
