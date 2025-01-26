intg = 100             # integer initalization
flot = 10.5            # float initalization
chr = 'R'              # char initalization
str = 'A. Rahim'       # string initalization
A = [1,2,3,4]          # List initalization can be read and writable
A.pop()                # It will delete last variable in the list
print(A.count(3))      # It will take data and return the number of occrance of data in the list
print(A.index(3))      # It will take data and return the index of that data
K=A.copy()             # It is used to copy list
A.append(0)            # this will add one variable at the last of list
A.sort()               # this will be arrange the list
A.extend('o')          #this will add one variable 'char' at the last of list
A.insert(2,90) #this will insert the data at the mention index
A.reverse()            #this will reverse the list
A.remove(2)            # this will take index and remove the data at that index
A.clear()              # this will clear the list
B = (4,5,6)            # tuple one time initalization readonly
print(B.index(5))      # It will take data and return the index of that data
print(B.count(5))      # It will take data and return the number of occrance of data in the tuple
dic = {"key" : 44,"name" : 54}     # Directory initalization
dicq = dic.copy()      # It is used to copy directory
dic.update(key=23)     # this will take key and updated value to update value at that key
print(dic.values())    # this will print only value in dict
print(dic.items())     # this will print all keys and value in dict
print(dic)             # this will print all keys and value in dict
#print(dicq)
#print(A)
#print(intg,flot,chr,str)