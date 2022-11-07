def fun1(List1, List2):
    List1[1] = 'y'
    return List2


def fun2(a, b):
    a += b
    return a


def fun3(a, b):
    b += a


L1 = [1, 2]
L2 = ['x', L1, 'z']
L3 = ['a', 'b', 'c']

L3 = fun1(L1, L2)
print(L1)             # Question 1 X
print(L3)             # Question 2 X

s = 2
t = 3
print(fun2(s, t))      # Question 3
print(s, t)            # Question 4


def reader(f):
    D = {}
    for x in f:
        for c in x:
            if c in D:
                D[c] += 1
            else:
                D[c] = 1
    return D


fp = ['to be or', 'not to be']
A = reader(fp)
print(A['t'])   # Line 1
print(len(A))   # Line 2 X
# print(D['e'])   # Line 3

# The file test1.txt contains the two lines:
# to be or
# not to be

D = {'a': 2, 'b': 7, 'c': 1, 'd': 5}
T = sorted([(v, k) for k, v in D.items()])
print(T)  # Question 11

S1 = {2,4,6,8}
S2 = {1,2,3,4,5,6}
print(S1&S2)      # Q 12
print(S1|S2)      # Q 13
print(S2-S1)      # Q 14
print(S1<S2)      # Q 15
S1.add(6)
print(S1)         # Q 16


import copy
L1 = ['a','b','c']
L2 = [1, 2, L1]
L3 = L2
L4 = copy.deepcopy(L3)
print(L3 is L2)  # Q 17
print(L4 is L2)  # Q 18
print(L4 == L2)  # Q 19
L1[2] = [10, 11]
print(L3)        # Q 20
print(L4)        # Q 21


def f1(fd):
    lst = []
    for line in fd:
        line = line.strip()
        lst.append(line)
    return lst
  
def f2(a_list, op='+'):
    result_list=[]
    ans = 1
    for line in a_list:
        for word in line.split():
            if word.isdigit():
                result_list.append(int(word))
    if result_list:
        if op == '+':
            ans = sum(result_list)
        elif op == '*':
            for element in result_list:
                ans *= element
        else:
            ans = -1
    return ans

file_descriptor = ['there are 6','and 4 more','but 10 is OK']
result = f1(file_descriptor)
print(len(result))           # Line 1
print(f2(result))            # Line 2
print(f2(result,'*'))        # Line 3


