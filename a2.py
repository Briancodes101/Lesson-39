n = int(input('Enter you number of rows here : '))

for i in range(1, n+1):
    for j in range(i):
        print("#", end = " ")
    print()