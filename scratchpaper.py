# from proj07 import highest_rated_by_movie

# N = 10
# L_reviews = [[], [(2, 3), (3, 3), (6, 1), (9, 5), (10, 2)], 
#              [(3, 1), (4, 4), (5, 3), (6, 5), (7, 3), (8, 5)], 
#              [(1, 2), (4, 3), (7, 3)], [(10, 5)], [],
#              [(2, 2), (5, 2), (8, 3)], [], [],
#              [(2, 2), (10, 4)], []]
# L1 = [1,2,3,6,7]

# L_max, max_score = highest_rated_by_movie(L1,L_reviews,N)
# print("Student L_max:",L_max)
# print("Student max score:",max_score)
# assert max_score == 3.0
# assert L_max == [6, 7]
avg = [0, 2.0, 2.3333333333333335, 2.0, 0, 0, 3.0, 3.0, 0, 0, 0]
index = [j for j in range(len(avg)) if avg[j] == max(avg)]

print(index)