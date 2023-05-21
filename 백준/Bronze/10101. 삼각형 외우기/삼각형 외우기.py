tri_list = []

for _ in range(3):
    tri = int(input())
    tri_list.append(tri)
        
if sum(tri_list) == 180:
    if tri_list[0] == tri_list[1] == tri_list[2] == 60:
        print('Equilateral')
    elif tri_list[0] == tri_list[1] or tri_list[1] == tri_list[2] or tri_list[2] == tri_list[0]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')