name = [i for i in range(1,11)]
print(name)
reversed = []
for i in range(len(name)-1,-1,-1):
    print(name[i])
    reversed.append(name[i])
print(reversed)