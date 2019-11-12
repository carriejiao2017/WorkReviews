ten_things = "Apples oranges crows telephone light sugar"
print("Wait there`s not 10 things in that list, let`s fix that.")

stuff = ten_things.split(' ')
print(stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #弹出列表中最后一个元素
    print("Adding:", next_one)
    stuff.append(next_one) #为列表增加一个元素
    print("There is %d items now." % len(stuff))


print("There we go:", stuff)

print("Let`s")

print(stuff[1])
print(stuff[-1]) #选取列表中随后一个元素
print(stuff.pop()) #删除列表中的最后一个元素
print(' '.join(stuff)) # join(' ',stuff)
print('#'.join(stuff[3:5])) # join('#', stuff)

## Dictionary {}
# create a mapping of state to abbreviation
states = {'Oregon' : 'OR', 'Florida' : 'FL','California':'CA','New York':'NY','Michigan':'MI'}
#create a basic set of states and some cities in them
cities = {'CA':'San Francisco','MI':'Detrit','FL':'Jacksonville'}
 
#add some more cities
cities['NY'] = 'New York'  #构建新的key-value对
cities['OR'] = 'Portland'

#print out some cities
print('_' * 10)
print("NY State has:", cities['NY']) #字典[key] = value
print("OR State has:", cities['OR'])

#print some states
print('_' * 10)
print("Michgan`s abbreviation is:", states['Michigan'])
print("Florida`s abbreviation is:", states['Florida'])

# do it by using the state then cities dict
print('_' * 10)
print("Michigan has:", cities[states['Michigan']]) #由内层到外层计算
print("Florida has:", cities[states['Florida']])

# print every state abbreviation
print('_' * 10)
for state, abbrev in states.items():
    print("%s has the city %s" % (state, abbrev)) #dic.items() 遍历字典中的键值对

#print every city in state
print('_' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('_' * 10)
for state, abbrev in states.items():
    print("%s satate is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('_' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None) # dic.get(key, default = None) 函数返回指定键的值，如无则返回默认值（default对应值）

if not state:
    print("Sorry, no Texas")

# get a city with a default value
city = cities.get('TX','Does not Exist')
print("The city for the state 'TX' is: %s" % city)

#dic是否可以排序？  可排序，但是根据最初设置的顺序排序，而非按照内容排序——遵循先进先出原则
# from collections import OrderedDict
#dict_1 = OrderedDict(dict)