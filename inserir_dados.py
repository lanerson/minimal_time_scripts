import sys

assert len(sys.argv) in [3, 4], "\nUso: \n \t$ python3 inserir_dados.py n1 n2 \nou\n\t$ python3 inserir_dados.py n1 n2 n3\nObs: n1, n2 e n3 são positivos"

with open("vals.txt","w") as file:
    
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = 1 if len(sys.argv) == 3 else int(sys.argv[3])
    for i in range(n1,n2+1, n3):
        file.write(str(i)+'\n')    