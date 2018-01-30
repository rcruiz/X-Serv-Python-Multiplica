#!/usr/bin/python3

print('Tablas de multiplicar')
for num1 in range(1,11):
    print('Tabla del '+ str(num1))
    for num2 in range(1,11):
        print(num1,'*',num2,'=',num1*num2)
