a1 = 7
a2 = 10
a3 = 4
N = int(input('Введіть значення N:  '))
if N%a1==0 and N%a2==0 and N%a3==0:
    print("N - є спільним кратним для цих чисел")
else:
    print("N - не є спільним кратним для цих чисел")
