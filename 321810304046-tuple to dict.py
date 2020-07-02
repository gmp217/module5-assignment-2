t1=1,2,3
t2='a','b','c'
d={}
for i in range(0,len(t1)):
	key=t1[i]
	value=t2[i]
	d[key]=value
print(d)