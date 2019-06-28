#11 Euclidean distcance
import math

x1 = int(input("Enter Co-Ordinate For x1 :"))
x2 = int(input("Enter Co-Ordinate For x2 :"))
y1 = int(input("Enter Co-Ordinate For y1 :"))
y2 = int(input("Enter Co-Ordinate For y2 :"))

distance = math.sqrt( ((x1-y1)**2)+((x2-y2)**2) )

print(distance)