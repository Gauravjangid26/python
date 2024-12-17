#why need-its is getting long and it is dry(dont repeat yourself) code
coordinates=(1,2,3)
co=coordinates[0]*coordinates[1]*coordinates[2]
print(co)
#unpacking-better approach with far less code
x,y,z=coordinates
print(x*y*z)