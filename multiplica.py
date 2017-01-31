#!-/usr/bin/python3

for i in range(1, 11):
    Titulo = "Tabla del " + str(i)
    print(Titulo + '\n' + '-' * len(Titulo))
    for j in range(1, 11):
        print(str(i) + ' por ' + str(j) + ' es ' + str(i*j))
