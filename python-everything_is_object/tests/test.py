#!/usr/bin/python3
print("------------Task 6------------")
s1 = "Best School"
s2 = s1
print(s1 == s2)

print("------------Task 7------------")
s1 = "Best"
s2 = s1
print(s1 is s2)

print("------------Task 8------------")
s1 = "Best School"
s2 = "Best School"
print(s1 == s2)

print("------------Task 9------------")
s1 = "Best School"
s2 = "Best School"
print(s1 is s2)

print("------------Task 10------------")
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)

print("------------Task 11------------")
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)

print("------------Task 12------------")
l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)

print("------------Task 13------------")
l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)

print("------------Task 14------------")
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l1 == l2)

print("------------Task 15------------")
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

print("------------Task 16------------")
def increment(n):
    n += 1
    # return n is missing
a = 1  # a is not mutable
increment(a)  # a is not changed (a = increment(a))
print(a)

print("------------Task 17------------")
def increment(n):
    n.append(4)

l = [1, 2, 3]  # l is mutable
increment(l)
print(l) # l is changed

print("------------Task 18------------")
def assign_value(n, v):
    n = v  # n is not changed (n = v) use n[:] = v instead

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

print("------------Task 20------------")
a = ()
print(type(a))

print("------------Task 21------------")
a = (1, 2)
print(type(a))

print("------------Task 22------------")
a = (1)
print(type(a))

print("------------Task 23------------")
a = (1, )
print(type(a))

print("------------Task 24------------")
a = (1)
b = (1)
a is b  # did they mean print(a is b) ? cuz it doesn't print anything
# True cuz they are the same object (singletons)

print("------------Task 25------------")
a = (1, 2)
b = (1, 2)
a is b  # false cuz they are different objects

print("------------Task 26------------")
a = ()
b = ()
a is b  # True cuz they are the same object (singletons)
