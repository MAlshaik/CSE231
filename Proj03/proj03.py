###########################################################
#  Computer Project #3
#  Algorithm
#    prompt the user to answer if they wish to process a triangle
#    enter a loop while the user answers yes
#    prompt for the length of the sides of the triangle
#    evaluate wether the triangle is valid, degenerate, or not a triangle
#    if the triangle is valid, then find and display the diffrent attributes of the triangle
#    calculate the angles of the triangle in radian and degrees 
#    evaluate the area of the triangle
#    print out the sides, and angles of the triangle in both degrees and radian rounded to the correct decimal place
#    evaluate and print out the diffrent types of triangles that corrisponds to the current triangle
#    ask if they wish to process another triangle
###########################################################
from cmath import sqrt
import math

BANNER = '''

╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''

print(BANNER)
print()
valid_triangles = 0
start = input("Do you wish to process a triangle (Y or N)?  \n")
while(start.upper() == 'Y'):
    if start.upper() != 'Y':
        break
    AB = round(float(input("Enter length of side AB: \n")),1)
    BC = round(float(input("Enter length of side BC: \n")),1)
    CA = round(float(input("Enter length of side CA: \n")),1)
    #prompts for length of the sides of the triangle, floats them, sand rounds them to one decimal place

    if((AB + CA) > BC and (CA + BC) > AB and (AB + BC) > CA):
        triangle = "Valid Triangle"
        valid_triangles += 1
    elif((AB + CA) == BC or (CA + BC) == AB or (AB + BC) == CA):
        triangle = "Degenerate Triangle"
    else: 
        triangle = "Not a Triangle"
    #checks if the triangle is valid, degenerate or not a triangle and adds one to the number of valid triangles.
        
        
    print(f"\n  {triangle}\n")

    if(triangle == "Valid Triangle"):
        
        A = math.acos((AB**2 + CA**2 - BC**2)/(2*CA*AB))
        B = math.acos((BC**2 + AB**2 - CA**2)/(2*BC*AB))
        C = math.acos((BC**2 + CA**2 - AB**2)/(2*CA*BC))
        #uses the arccos formula using all sides of the triangle to find the radian value of each of the angles in the triangle.
        A_deg = A*(180/math.pi)
        B_deg = B*(180/math.pi)
        C_deg = C*(180/math.pi)
        #converts the radian angles to degrees and stores it in its respective formula

        s = 1/2*(AB + BC + CA)
        area = sqrt(s*(s-AB)*(s-BC)*(s-CA))
        #uses the Heron’s formula to find the area of the triangle

    
        print("  Triangle sides:")
        print("    Length of side AB: {:.1f}".format(AB))
        print("    Length of side BC: {:.1f}".format(BC))
        print("    Length of side CA: {:.1f}\n".format(CA))
        #prints out the length of each side rounded to one decimal place

        print("  Degree measure of interior angles:")
        print("    Angle A: {:.1f}".format(A_deg))
        print("    Angle B: {:.1f}".format(B_deg))
        print("    Angle C: {:.1f}\n".format(C_deg))
        #prints out the degree of each side rounded to one decimal place

        print("  Radian measure of interior angles:")
        print("    Angle A: {:.1f}".format(A))
        print("    Angle B: {:.1f}".format(B))
        print("    Angle C: {:.1f}\n".format(C))
        #prints out the radian measure of each side rounded to one decimal place.

        print("  Perimeter and Area of triangle:")
        print("    Perimeter of triangle: {:.1f}".format(AB + BC + CA))
        print("    Area of triangle: {:.1f}\n".format(area.real))

        print("  Types of triangle:")

        
        if(AB == BC or CA == BC or CA == AB ):
            print("    Isosceles Triangle")
        else:
            print("    Scalene Triangle")
        if(AB == BC and CA == BC ):
            print("    Equilateral Triangle")

        if(A_deg != 90 and C_deg != 90 and B_deg != 90):
            print("    Oblique Triangle")
        else:
            print("    Right Triangle")

        if(A_deg > 90 or C_deg > 90 or B_deg > 90):
            print("    Obtuse Triangle")
        # evaluate and print out the diffrent types of triangles that corrisponds to the current triangle
        
        print("")
        
    start = input("Do you wish to process another triangle? (Y or N) \n")

print(f"Number of valid triangles: {valid_triangles}")