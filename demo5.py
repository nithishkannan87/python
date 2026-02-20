#217.contains duplicate
# def containsDuplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False
# nums = [1, 2, 3, 1]
# print(containsDuplicate(nums))

# #loop
# def func(a, b):
#     return a+b
# result = func(5, 8)
# print(result)

# #syntax
# class classname:
#     def methodname(self):
#         print("message")

# #class student:
# def details(self,name,marks):
#     result="pass"
#     if marks>=40:
#         result="pass"
#         print(result)
#     else:
#         result="fail"
#         print(result)
#     s1=student()
#     s1.details("john", 35)
#     s2=student()
#     s2.details("jane", 45)


#oops
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show_result(self):
        if self.marks>=40:
            result="pass"
        else:
            result="fail"
            print(f"\nStudent {self.name} result: {result}")
            print("marks",self.marks)
            print("result",result)
        
name=input("enter name")
marks=int(input("enter marks"))
s1=student(name, marks)
s1.show_result()

#encapsulation



