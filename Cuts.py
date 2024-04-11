cuts = 2
count = 2
number = int(input("enter number of cuts"))

for i in range(2,number+1):
    if i%2 == 0:
        cuts = cuts + count
    else:
        cuts = cuts + count
        count+=1

print('number of pieces formed ',cuts)
