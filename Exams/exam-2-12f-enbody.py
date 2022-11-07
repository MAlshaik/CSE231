# def fun1(List1, List2):
#     List1[1] = 'y'
#     return List2


# def fun2(a, b):
#     a += b
#     return a


# def fun3(a, b):
#     b += a


# L1 = [1, 2]
# L2 = ['x', L1, 'z']
# L3 = ['a', 'b', 'c']

# L3 = fun1(L1, L2)
# print(L1)             # Question 1 X
# print(L3)             # Question 2 X

# s = 2
# t = 3
# print(fun2(s, t))      # Question 3
# print(s, t)            # Question 4


# def reader(f):
#     D = {}
#     for x in f:
#         for c in x:
#             if c in D:
#                 D[c] += 1
#             else:
#                 D[c] = 1
#     return D


# fp = ['to be or', 'not to be']
# A = reader(fp)
# print(A['t'])   # Line 1
# print(len(A))   # Line 2 X
# # print(D['e'])   # Line 3

# # The file test1.txt contains the two lines:
# # to be or
# # not to be

# D = {'a': 2, 'b': 7, 'c': 1, 'd': 5}
# T = sorted([(v, k) for k, v in D.items()])
# print(T)  # Question 11

S1 = {2,4,6,8}
S2 = {1,2,3,4,5,6}
print(S1&S2)      # Line 12
print(S1|S2)      # Line 13
print(S2-S1)      # Line 14
print(S1<S2)      # Line 15
S1.add(6)
print(S1)         # Line 16
