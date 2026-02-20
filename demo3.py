#fibonacci series
# n=int(input("Enter a number: "))
# a=0
# b=1
# for i in range(1,n+1):
#     print(a)
#     c=a+b
#     a=b
#     b=c

#list
# list=[1,2,3,4,5]
# print(list[4])
#list slicing 
  #syntax[start:stop:step]
  #print(list[1:4])

#list operations

#1.concatenation operation
# a=[1,2,3]
# b=[4,5]
# print(a+b)

#2.repetition operation
# number=[1,2,3]
# print(number*3)

#3.membership operation
# fruits=["apple","banana","grapes"]
# print("apple" in fruits)
# print("banana" not in fruits)

#comparison operation
# listone=[1,2,3]
# listtwo=[1,2,3]
# print(listone==listtwo)
# print(listone<listtwo)

#list indices
# a=[1,2,3,4,5,6]
# b=[7,8,9,10,11]
# print(a[4])
#slicing(start:stop:step)
# print(a[1:4:2])
#concatenation
# print(a+b)
# print(a*4)
# print(1 in a)
# print(7 in a)
# print(a==b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# list methods

# 1.append() - adds an element to the end of the list
# num=[1,2,3]
# num.append(4)
# print(num)

# 2.insert() - adds an element at a specific index

# syntax: list.insert(index, element)
# num.insert(2,5)
# print(num)

# 3.extend() - adds all elements of an iterable to the end of the list
# a=[1,2,3]
# b=[4,5,6]
# a.extend(b)
# print(a)

# 4.remove() - removes the first occurrence of an element from the list
# num=[1,2,3,4,5]
# num.remove(3) 
# print(num)

# 5.pop(index) - removes and returns the element at a specific index (default is the last element)
# num=[10,20,30]
# num.pop(1)
# print(num)0

# 6.clear() - removes all elements from the list
# num=[1,2,3]
# num.clear() 
# print(num)

# 7.index(element) - returns the index of the first occurrence of an element in the list
# num=[1,2,3,4,5]
# print(num.index(3))

# 8.count(element)
# num=[1,2,3,2,4,2]
# print(num.count(2))

# 9.sort() - sorts the elements of the list in ascending order
# a=[4,6,34,9,23]
# a.sort() 
# print(a)

# 10.reverse() - reverses the order of the elements in the list
# a=[1,2,3,4,5]
# a.reverse() 
# print(a)

# 11.copy() - returns a shallow copy of the list
# a=[1,2,3]
# b=a.copy()
# print(b)

# def fun(x):
#     return x*2
# result=list(map(fun,[1,2,3]))
# print(result)

# #reduce-->convert into a single value--->
# #syntax
# #reduce(func,iterable)
# from functools import reduce
# num=[1,2,3,4]
# result=reduce(lambda x,y:x+y,num)
# print(result)

# from functools import reduce

# num = 1,2,3,4,5,6,7,8,9,10
# even_numbers = list(filter(lambda x: x % 2 == 0, num))
# even_sum = reduce(lambda a, b: a + b, even_numbers)
# print("Even numbers:", even_numbers)
# print("Sum of even numbers:", even_sum)
# odd_numbers = list(filter(lambda x: x % 2 != 0, num))
# odd_sum = reduce(lambda a, b: a + b, odd_numbers)
# print("Odd numbers:", odd_numbers)
# print("Sum of odd numbers:", odd_sum)

#1st method---->slicing
word=input("Enter a word: ")
if word==word[::-1]:
    print("palindrome")
else:
    print("not palindrome")






































































































































































































































































































































































































































































































































































































































































































































































































































































































