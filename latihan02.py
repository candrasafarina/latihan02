mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)

for x in mylist:
     print (x)
     
mylist = ["luke", "yoda", "udin"]
print(mylist)

thelist = ['udin', 'enok', 'mang oleh', 'neng']

print(thelist[2:3])

print(thelist[:3])

mylist = ["luke", "yoda", "udin"]
for x in mylist:
    if x == "luke":
        continue
    print(x)