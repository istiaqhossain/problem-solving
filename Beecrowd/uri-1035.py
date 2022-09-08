def main():
    A,B,C,D = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    message = 'Valores nao aceitos'
    if (B > C) and (D > A) and ((C + D) > (A + B)) and ((C >= 0) and (D >= 0)) and (A%2 == 0) :
        message = 'Valores aceitos'
    print(message)
main()
