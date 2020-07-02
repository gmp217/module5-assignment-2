l,n=[],int(input('Enter value of n:'))
print('Enter elements:')
for i in range(0,n):
	ele=input()
	l.append(ele)
t=tuple(l)
print('list:',l,'\ntuple:',t)