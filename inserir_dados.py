import sys

assert len(sys.argv) == 3, "Digite dois valores filho"

with open("vals.txt","w") as file:
    
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])

    for i in range(n1,n2):
        file.write(str(i)+'\n')
    file.write(str(n2))