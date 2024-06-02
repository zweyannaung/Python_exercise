# a=10
# b=20
# while a < b :
#     print('{} hello world'.format(a))
#     a +=1

# break
# for item in 'mingalarpar' :
#     if item == 'g':
#         break
#     print(item)
# print ('end loop')

# continue
# for item in "mingalarpar":
#     if item == "g":
#         continue
#     print(item)
# print ('end loop')

ls=[12,43,24,55,23]
data = 99
found = False
x=0
while x < len(ls):
    if ls[x] == data:
        found = True
        break
    x +=1

if not found:
    ls.append(data)
print(ls)