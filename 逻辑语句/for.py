## for_loop
# for i in xxx:
#     print()   for循环代码块要缩进4位
# the_count = [1, 2, 3, 4, 5]
# fruits =["apples", "oranges", "pears", "apricots"]
# change =[1, "pennies", 2, "dimes", 3, "quarters"]

# # this first kind of foe-loop goes through a list for number in the_count
# for number in the_count:
#     print("This is count %d" % number)

# #same as above
# for fruit in fruits:
#     print("A fruit of type: %s" % fruit)

# #also we can go through mixed lists too
# #notice we have to use %r since we don`t know what`s in it
# for i in change:
#     print("I got %r" % i)

# # we can also build lists, first start with an empty one
# elements = []

# #then use the range function to do 0 to 5 counts
# for i in range(0, 6):  ##range()左闭右开
#     print("Adding %d to the list." % i)
#     #append is a function that lists understand
#     elements.append(i)

# #now we can print them out too
# for i in elements:
#     print("Element was: %d" % i)

#使用range构造一个列表方法-1
element1 = list(range(1,6)) 
print(element1)

#还可创建等差序列 list(range(1,11,2))
list1 = list(range(1,11,2))
print(list1)

#使用range构造一个列表方法-2
element2 = []
for i in range(1,6):
    element2.append(i)
print(element2)

#使用range遍历列表
list2 = [1, 2, 3, 3, 5]
for i in range(len(list2)):
    val = list2[i]
    print(val)