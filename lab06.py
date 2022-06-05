file = open('scores.txt', 'r')
tuple_list = []
for line in file:
    line = line.split(' ')
    line = list(filter(None, line))
    tlist = []
    total = 0
    i = 0
    while(i < (len(line))):
        try:
            tlist.append(int(line[i].replace('\n', '')))
            total += tlist[i-1]
            i+=1
        except:
            tlist.append(line[i] + f" {line[i+1]}")
            i+=2
    average = total/4
    tlist.append(average)
    tuple_list.append(tuple(tlist))
sorted_tuple = tuple(sorted(tuple_list))  

print("Name                 Exam1 Exam2 Exam3 Exam4      Mean")

for i in sorted_tuple:
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(i[0],i[1],i[2],i[3],i[4],i[5]))

score_list = []
score_tuple = []
for i in range (1,5):
    for j in range (5):
        score_list.append(sorted_tuple[j][i])
    score_tuple.append(tuple(score_list))
    score_list.clear()

total = 0
average_list = []
for i in score_tuple:
    for j in i: 
        total += j
    average_score = total/5
    average_list.append(average_score)
    total = 0


print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean", average_list[0],average_list[1],average_list[2],average_list[3]))

