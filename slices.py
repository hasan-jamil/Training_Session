my_list = [2, 3, 4, 2, 3, 5, 6, 8, 7]
new_list = my_list[:2]
print(new_list)


#Negative-Index Slicing
k = my_list[8:0:-1]
print(k)


#Slicing of string & tuple
string = "hello world"
print(string[0:6:2])

tup = 1, 2, 3, 4, 5
print(tup[0::3])
