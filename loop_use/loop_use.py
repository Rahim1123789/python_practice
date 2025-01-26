lis = ['user','admin','client','hip','hop','your','tiger']

for items in lis:        #this will print the items in list
    print(items)
cnt = 0
while len(lis) > 0:      #this will remove items in list
    cnt +=1
    print(cnt)
    lis.pop()

print(lis)