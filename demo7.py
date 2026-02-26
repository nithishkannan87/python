# numrow=int(input("enter the number:"))
# triangle=[]
# for i in range(numrow):
#     row=[1]*(i+1)
#     for j in range(1,i):
#         row[j]=triangle[i-1][j-1]+triangle[i-1][j]
#     triangle.append(row)
# print(triangle)

#maximum product of three numbers
def maximum_product(nums):
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1] * nums[-1] * nums[-2] * nums[-3])
print(maximum_product([-10, -10, 5, 2]))







