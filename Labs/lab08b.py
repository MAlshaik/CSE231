file1 = open('data1.txt')
file2 = open('data2.txt')
file1.readline()
file2.readline()

data_dict = {}
new_dict = {}
lines1 = file1.readlines()
lines2 = file2.readlines()
Names = []
for line in lines1:
    line = line.strip().split(' ')
    data_dict[line[0]] = int(line[-1])
    Names.append(line[0])
    Names.sort()

    

for line in lines2:
    line = line.strip().split(' ')
    if line[0] in data_dict:
        data_dict[line[0]] += int(line[-1])
    else:
        Names.append(line[0])
        data_dict[line[0]] = int(line[-1])

Names.sort()

for name in Names:
    new_dict[name] = data_dict[name]
print( "{:10s} {:<10s}".format("Name", "Total"))
for i in new_dict:
     print("{:10s} {:<10d}".format(i, new_dict[i]))

