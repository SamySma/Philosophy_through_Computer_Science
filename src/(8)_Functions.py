# (8)_Functions
import math


# def greet(n):
#     print(f'Hi {n}, how are you?')

# m = 'Sam'
# def greet2():
#     print(f'Hi {m}!')

# greet2()

# def respond(n):
#     print(f'')

# def volume(r):
#     return math.pi*(r**3)*(4/3)

# print(volume(3))
def count(S,c):
    x = 0
    num_cs = 0
    while x < len(S):
        if S[x] == c:
            num_cs +=1
        x += 1
    return num_cs


print(count('sssssa','a'))
