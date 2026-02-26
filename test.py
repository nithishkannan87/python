# Tribonacci Series

n = int(input("Enter number of terms: "))
t1, t2, t3 = 0, 1, 1
if n >= 1:
    print(t1, end=" ")
if n >= 2:
    print(t2, end=" ")
if n >= 3:
    print(t3, end=" ")
for i in range(3, n):
    next_term = t1 + t2 + t3
    print(next_term, end=" ")
    t1, t2, t3 = t2, t3, next_term

#Anagram

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")

#number palindrome
# num = input("Enter a number: ")
# if num == num[::-1]:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

