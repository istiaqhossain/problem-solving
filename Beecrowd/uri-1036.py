import math
def main():
    A,B,C = input().split()
    A = float(A)
    B = float(B)
    C = float(C)
    D = B**2 -(4*A*C)
    if A != 0 and D > 0:
        R1 = (-B+math.sqrt(D))/(2*A)
        R2 = (-B-math.sqrt(D))/(2*A)
        print('R1 = %.5f'%R1)
        print('R2 = %.5f'%R2)
    else:
        print('Impossivel calcular')
main()
