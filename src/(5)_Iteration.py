# (5)_Iteration

# result = [1,2,3]
# i = 0

# #while i <= 10:
# #   result.append(2**i)
# #    i+=1 

# # for number in range(1,11):
# #    print(number)

# # while i < len(result):
# #    print(result[i])
# #    i += 1

# for element in result:
#     print(element)


L2 = [1,2,3,4,5]
sum = 0

# for num in L2:
#     sum += num
i = 0 
smallest_so_far = L2[0]

# while i < len(L2):
#      sum += L2[i]
#      i += 1
#     if L2[i] < smallest_so_far:
#         smallest_so_far = L2[i]
#     i += 1

# largest_so_far = L2[0]

# for num in L2:
#     if num > largest_so_far:
#         largest_so_far = num

# print(largest_so_far)


x = 11
prime = True

for num in range(2,x):
    if x % num == 0:
        prime = False
print(f'{x} is prime: {prime}')