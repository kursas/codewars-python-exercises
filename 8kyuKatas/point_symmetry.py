# "Point reflection" or "point symmetry" is a basic concept in geometry
# where a given point, P, at a given position relative to a mid-point, Q has a corresponding point, P1, which is the same distance from Q but in the opposite direction.
# Task
# Given two points P and Q, output the symmetric point of point P about Q. Each argument is a two-element array of integers representing the point's X and Y coordinates.' \
# ' Output should be in the same format, giving the X and Y coordinates of point P1. You do not have to validate the input.
def symetric_point(p,q):
    diff_x=q[0]-p[0]
    x=q[0]+diff_x
    diff_y = q[1] - p[1]
    y = q[1] + diff_y
    return [x,y]
print(f'paduotos koordinates[2,6],[-2,-6],veidrodines bus:{symetric_point([2,6],[-2,-6])}')
print(f'paduotos koordinates[0,0],[1,1],veidrodines bus:{symetric_point([0,0],[1,1])}')

def symetric_point2(p,q):
    return [2*q[0]]-p[0],2*q[1]-p[1]
print(f'paduotos koordinates[2,2],[-2,-2],veidrodines bus:{symetric_point([2,2],[-2,-2])}')
print(f'paduotos koordinates[5,5],[-5,-5],veidrodines bus:{symetric_point([5,5],[-5,-5])}')

symetric_point3=lambda p,q:[2*b-a for a,b in zip(p,q)]
print(f"paduotos lambda funkc.koordinates[10,5],[-10,-5],veidrodines bus:{symetric_point3([10,5],[-10,-5])}")

def symetric_point4(p,q):
    p1x=(q[0]-p[0])+q[0]
    p1y=(q[1]-p[1])+q[1]
    return [p1x,p1y]
print(f'paduotos koordinates[10,5],[-10,-5],veidrodines bus:{symetric_point4([10,5],[-10,-5])}')

#output
paduotos koordinates[2,6],[-2,-6],veidrodines bus:[-6, -18]
paduotos koordinates[0,0],[1,1],veidrodines bus:[2, 2]
paduotos koordinates[2,2],[-2,-2],veidrodines bus:[-6, -6]
paduotos koordinates[5,5],[-5,-5],veidrodines bus:[-15, -15]
paduotos lambda funkc.koordinates[10,5],[-10,-5],veidrodines bus:[-30, -15]
paduotos koordinates[10,5],[-10,-5],veidrodines bus:[-30, -15]

Process finished with exit code 0
