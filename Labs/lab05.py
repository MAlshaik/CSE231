
Names = []
Height = []
Weight = []
BMI = []
file = open('data.txt', 'r+')
for i in range(8):
    i+=1
    file.seek(0)
    Height.append(file.readlines()[i][12:16])
    file.seek(0)
    Weight.append(file.readlines()[i][24:29])
    file.seek(0)
    Names.append(file.readlines()[i][0:5])

for i in range(len(Names)):
    Names[i] = Names[i].replace(" ", '')

file.seek(0)
Title = file.readlines(0)[0].strip() + "  BMI        "

# print(Title)
# print(Height)
# print(Weight)
# print(Names)

maxHeight = 0
minHeight = 99999
minWeight = 99999
maxWeight = 0
avgHeight = 0
avgWeight = 0 
maxBMI = 0
minBMI = 99999
avgBMI = 0
for i in range(len(Height)):

    BMI.append(round(float(Weight[i])/float(Height[i])**2, 2))
    Height[i] = float(Height[i]) 
    Weight[i] = float(Weight[i])

    if(BMI[i] > maxBMI):
        maxBMI = BMI[i]

    if(BMI[i] < minBMI):
        minBMI = BMI[i]

    if(float(Height[i]) > maxHeight):
        maxHeight = float(Height[i])

    if(float(Height[i]) < minHeight):
        minHeight = float(Height[i])
    
    if(float(Weight[i]) < minWeight):
        minWeight = float(Weight[i])

    if(float(Weight[i]) > maxWeight):
        maxWeight = float(Weight[i])

    avgHeight += float(Height[i])
    avgWeight += float(Weight[i])
    avgBMI += float(BMI[i])

avgHeight = round(avgHeight /  len(Height), 2)
avgWeight = round(avgWeight / len(Weight), 2)
avgBMI = round(avgBMI/len(BMI), 2)



file.seek(0)




print(Title,
f"\n{Names[0]:<12s}{Height[0]:<12.2f}{Weight[0]:<12.2f}{BMI[0]:<11.2f}",
f"\n{Names[1]:<12s}{Height[1]:<12.2f}{Weight[1]:<12.2f}{BMI[1]:<11.2f}",
f"\n{Names[2]:<12s}{Height[2]:<12.2f}{Weight[2]:<12.2f}{BMI[2]:<11.2f}",
f"\n{Names[3]:<12s}{Height[3]:<12.2f}{Weight[3]:<12.2f}{BMI[3]:<11.2f}",
f"\n{Names[4]:<12s}{Height[4]:<12.2f}{Weight[4]:<12.2f}{BMI[4]:<11.2f}",
f"\n{Names[5]:<12s}{Height[5]:<12.2f}{Weight[5]:<12.2f}{BMI[5]:<11.2f}",
f"\n{Names[6]:<12s}{Height[6]:<12.2f}{Weight[6]:<12.2f}{BMI[6]:<11.2f}",
f"\n{Names[7]:<12s}{Height[7]:<12.2f}{Weight[7]:<12.2f}{BMI[7]:<12.2f}")

print(
"\n{:<12s}{:<12.2f}{:<12.2f}{:<11.2f}".format("Average",avgHeight, avgWeight, avgBMI),
"\n{:<12s}{:<12.2f}{:<12.2f}{:<11.2f}".format("Max",maxHeight, maxWeight, maxBMI), 
"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min",minHeight, minWeight, minBMI))
file.close()
