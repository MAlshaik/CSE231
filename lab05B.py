
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
Title = file.readlines(0)[0].strip() 

print(Title)
print(Height)
print(Weight)
print(Names)

maxHeight = 0
minHeight = 99999
minWeight = 99999
maxWeight = 0
avgHeight = 0
avgWeight = 0 
for i in range(len(Height)):

    BMI.append(round(float(Weight[i])/float(Height[i])**2, 2))
    Height[i] = float(Height[i]) 
    Weight[i] = float(Weight[i])
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

avgHeight = round(avgHeight /  len(Height), 2)
avgWeight = round(avgWeight / len(Weight), 2)
maxBMI = round((maxWeight)/(maxHeight)**2,2)
minBMI = round(minWeight/minHeight**2,2)
avgBMI = round(avgWeight/avgHeight**2, 2)

print(BMI)
print(f" max height: {maxHeight}\n min Height: {minHeight} \n max Weight: {maxWeight}\n min Weight: {minWeight}")
print(f"min BMI {minBMI} max BMI {maxBMI}")
print(f"avg BMI {avgBMI}")

file.seek(0)
file.close()

newfile = open('output.txt', 'w')
newfile.writelines([Title,"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(Names[0], Height[0], Weight[0], BMI[0]),
"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(Names[1], Height[1], Weight[1], BMI[1]),
"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(Names[2], Height[2], Weight[2], BMI[2]),
"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(Names[3], Height[3], Weight[3], BMI[3]),
"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(Names[4], Height[4], Weight[4], BMI[4]),
"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(Names[5], Height[5], Weight[5], BMI[5]),
"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(Names[6], Height[6], Weight[6], BMI[6]),
"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(Names[7], Height[7], Weight[7], BMI[7]),
"\n",
"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average",avgHeight, avgWeight, avgBMI),
"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max",maxHeight, maxWeight, maxBMI), 
"\n{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min",minHeight, minWeight, minBMI)])
newfile.close()

