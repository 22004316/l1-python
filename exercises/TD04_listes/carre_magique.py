carre_mag = [[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
print(carre_mag)

'''carre_pas_mag = carre_mag.copy()
print(carre_pas_mag)
carre_pas_mag[3].insert(2,7)
print(carre_pas_mag)
print(carre_mag)
del carre_pas_mag[3][3]
print(carre_pas_mag)
print(carre_mag)'''

carre_pas_mag=[]
for i in range(len(carre_mag)):
    e=list(carre_mag[i])
    carre_pas_mag.append(e)
c=carre_pas_mag[3]
c.insert(3, 7)
c.remove(3)
print(carre_pas_mag)


