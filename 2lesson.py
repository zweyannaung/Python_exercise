a=170
b=160
c=120
d=80
e=150
 
if (a<b) and (a>c) and (a>d) and (a>e):
    name='a'
    largest_number = a
elif (b>a) and (b>c) and (b>d) and (b>e):
    name='b'
    largest_number = b
elif (c>a) and (c>b) and (c>d) and (c>e):
    name='c'
    largest_number = c
elif (d>a) and (d>b) and (d>c) and (d>e):
    name='d'
    largest_number = d
else:
    name='e'
    largest_number = e
print('The largest number is {}:'.format(name),largest_number)