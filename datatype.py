"I'm a string"
'Me too!'
str("I'm a string")

dog_name = "Lucy"
print(f"Say hello to my dog {dog_name}")

price_1 = 3
price_2 = 2.5

print(f"Item 1 costs ${price_1:.2f}")
print(f"Item 2 costs ${price_2:.2f}")

# Integers are whole numbers, like 7
# Floats are decimal numbers, like 7.3

# Conversion

int("1")

# Integer conversion is int()

intexample1 = int(1.1)

print(intexample1)

# Will convert to 1

float("1.1")

# Will convert to 1.1

# Math operation results will turn to floats. Equivalents follow

x = 4/3
y = 4/3.0
z = float(4/3)

print(x)
print(y)
print(z)

# Lists

a = [1, 3, 400, 7]

print(a)

# Can access elements in a list through index. An index or indices start at 0

list_abc = ['a','b','c']

b = list_abc[0]

c = list_abc[1]

d = list_abc[2]

print(b)
print(c)
print(d)

# Like Javascript arrays, there are methods for Python lists

# len() measures number of elements in a list

e = len([1,3,400,7])

# sorted() puts list in numerical order

f = sorted([5,100,234,7,2])

# .pop() returns length

list_123 = [1,2,3]
g = list_123.pop()

#.remove() removes an element for list

h = list_123.remove(1)

print(e)
print(f)
print(g)
print(list_123)

# Sets are also sequences of data but data in a set are individual elements/dicts

i = set()
print(i)

j = set([3,2,3,'a','b','a'])
print(j)

s = {1,2,3}

print(s.pop())

k = s.remove(3)
print(k)

#Dictionaries are composed of key/value pairs like JavaScript

my_dict = { "key1": 1, "key2": 2 }
print(my_dict["key2"])

# the get method (.get()) will pull key as well. If key does not exist, None will be a response

my_dict1 = { "key1": "value1", "key2": "value2" }

print(my_dict1.get("key3"))

# Unlike JavaScript, dot notation does not work

# dict() method creates dictionaries

print(dict(x = 1, y = 2))

# In order to have an empty variable, you have to assign none and cannot create a variable without a value

l = None

print(l)


