a=[1,2,3,4]
print("befor chaging ",a)
b=a
print(b)
b[3]=7
print("a :",a)
print("b :",b)

print("_________________________________________________\n")
c=a[:]
print("c:",c)
c[0]="000"
print("a:",a)
print("b :",b)
print("c :",c)
