# data = [x for x in range(6)] 
# temp = [x for x in range(8) if x in data and x%2!=0] 
# print("1: ", end='')
# print(temp)

# L1 = [3,5]
# L2 = [2,4]
# print("2: ", end='')
# print(L1 + L2)

# L1 = list() 
# L1.append([1, [4, 5], 6]) 
# L1.extend([2, 7, 9]) 
# print("3: ", end='')
# print(L1[0][1][1] + L1[2]) 

# L1 = ['x','y']
# L2 = ['a',L1,'b']
# print("4: ", end='')
# print(L2)

# L1 = ['x','y']
# L2 = ['a',L1[:],'b']
# print("5: ", end='')
# print(L2)

# tuple = ('Cehck',)*3
# print("7: ", end='')
# print(tuple)

# my_list = list('231 Lab')
# print("9: ", end='')
# print(my_list)

# s = "Head, Shoulders, Knees and Toes"
# print("10: ", end='')
# print(s.split(', '))

# A = {3, 4, 5}		
# B = {3, 4, 3, 5}
# print("11: ", end='')
# print(A == B)


# set1 = {3, 4, 5} 
# set2 = set1.copy() 
# set2.add(6)
# print("12: ", end='')
# print(set1) 


# def boo( A = 4, B = -2 ):
#     A = A + B
#     B = 2 * A
#     return A + B

# A = 2
# B = 1
# C = boo( A, B )
# print("13: ", end='')
# print( A, B, C ) # Line 1
# A = 5
# B = 2
# C = boo( B=3 )
# print("14: ", end='')
# print( C )       # Line 2
# A = 5
# B = 3
# C = boo( B )
# print("15: ", end='')
# print( C )       # Line 3


# def f(a,b):
#       if a:
#           a.append('w')
#       b += a
#       return a
  
# w = 3
# x = 0
# y = [4,3]
# z = [5,4]
# print("16: ", end='')
# print(f(x,w))
# print("17: ", end='')    # Line 1
# print(f(y,z))
# print("18: ", end='')    # Line 2
# print(w)         # Line 3
# print("19: ", end='')
# print(z)         # Line 4



# L = []
# a_str = 'Nah nah nah nah, Nah nah nah nah, Hey Jude' # Hey Jude The Beatles (1968) 
# a_lst = a_str.split()
# for s in a_lst:
#     L.append(s.lower().strip(','))

      
# D = {}
# for item in L:
#     if item in D:
#         D[item] += 1
#     else:
#         D[item] = 1

# print("20: ", end='')
# print(len(D))      # Line 1
# print("21: ", end='')
# print(D['nah'])   # Line 2

# count = sum([v for v in D.values()])
# print("22: ", end='')
# print(count)       # Line 3

# D = {'elephant':{},'mouse':{}}
# D['elephant']['2'] = 4
# D['mouse']['1'] = 5
# D['mouse']['1'] += 6
# print("24: ", end='')
# print(D)

# d = {'Tim': 18,'Anna':12,'Zach':22,'Robert':25}
# items = sorted(d, reverse=True)
# print("25: ", end='')
# print(items)

# A = {5,6,7,8}
# B = {7,8,9,10}

# print("26: ", end='')
# print(A | B)
# print("27: ", end='')          # Line 1
# print(A & B)
# print("28: ", end='')          # Line 2
# print(A - B)
# print("29: ", end='')          # Line 3
# print(B - A)
# print("30: ", end='')          # Line 4
# print(A ^ B)          # Line 5


############
# Figure 3 #
############
D = {0:1, 2:3}                          
s = input("Input something: ")          
try:                                    
    x = float(s)
    y = int(s)      
    z = D[y]                               # Line 1
except ValueError:
    print("Oops_1")                        # Line 2                
except KeyError:
    print("Oops_3")                        # Line 3                  
else:
    print(x,y,z)      
finally:
    print("Finally Executed")
    
print('x' + 'x')              # Line 4 