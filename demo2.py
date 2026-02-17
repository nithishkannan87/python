# student_type=str(input("enter the student type: "))
# if student_type=="msh":
#     tuition_fee=(float(input("enter the tuition fee: ")))
#     hostel_fee=(float(input("enter the hostel fee: ")))
#     print("total fee =",tuition_fee+hostel_fee)
# elif student_type=="msds":
#     tuition_fee=(float(input("enter the tuition fee: ")))
#     day_scholarship=(float(input("enter the day scholar ship: ")))
#     print("total fee =",tuition_fee-day_scholarship)
# elif student_type=="mgsds":
#     tuition_fee=(float(input("enter the tuition fee: ")))
#     day_scholarship=(float(input("enter the day scholar ship: ")))
#     print("total fee =",tuition_fee-day_scholarship)
# elif student_type=="mgsh":
#     tuition_fee=(float(input("enter the tuition fee: ")))
#     hostel_fee=(float(input("enter the hostel fee: ")))
#     print("total fee =",tuition_fee+hostel_fee)
# else:
#     print("invalid student type")


# accountbalance=50000
# withdrawal_limit=10000
# withdrawal_amount=int(input("enter the withdrawal amount: "))
# if withdrawal_amount>accountbalance:
#     print("insufficient balance")
# elif withdrawal_amount>withdrawal_limit:
#     print(" withdrawal limit exceeded")
# else:
#     print("withdrawal cash successful")



# accountbalance=60000
# correct_pin=1234
# pin=int(input("enter the pin: "))
# if pin==correct_pin:
#     amount=int(input("enter the amount to withdraw:"))
#     print("pin is correct")
# else:
#     print("incorrect pin")


# age=int(input("enter the age: "))
# showtime=str(input("enter the show time: "))
# child=135
# adult=230
# senior=180
# if age>=18 and showtime=="evening":
#     print("ticket price is 150")
# elif age>=18 and showtime=="afternoon":
#     print("ticket price is 230")
# elif age<18 and showtime=="evening":
#     print("ticket price is 135")
# elif age<18 and showtime=="afternoon":
#     print("ticket price is 150")
    
# loop
# sum=0
# for i in range(1,100,):
#     print(i)
#     sum=sum+i
#     total=sum

# sum=0
# for i in range(1,100):
#     if i%2==0:
#       print(i)
#       sum=sum+i
#       total=sum
# print("total of even numbers is",total)


# for i in range(1,10):
#     sum=i*5
#     print(i,"*",5,"=",sum)



# for i in range(1,6):
#  print("*"*i)



# n=5
# for i in range(n,0,-1):
#     print("*"*i)


# n=5
# for i in range(1,100):
#     print(i)

# sum=0
# i=1
# while i<100:
#     if i%2==1:
#      print(i)
#     sum=i+sum
#     i=i+1
# print("total of odd numbers is",sum)

# sum=0
# i=1
# while i<100:
#     if i%2==0:
#      print(i)
#     sum=i+sum
#     i=i+1

# sum=0
# i=1
# while i<100:
#     if i%2==0:
#      print(i)
#     sum=i+sum
#     i=i+1
# print("total of even numbers is",sum)

total_seats = 10 
current_seat = 1
while current_seat <= total_seats:
    name = input("Enter passenger name: ")
    print(f"Seat {current_seat} booked for {name}\n")
    current_seat += 1
print("All seats are booked!")




