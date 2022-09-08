def main():
    X,Y = input().split()
    X = int(X)
    Y = int(Y)
    if X == 1 :
        Z = Y*4.00
        print('Total: R$ %.2f'%Z)
    elif X == 2 :
        Z = Y*4.50
        print('Total: R$ %.2f'%Z)
    elif X == 3 :
        Z = Y*5.00
        print('Total: R$ %.2f'%Z)
    elif X == 4 :
        Z = Y*2.00
        print('Total: R$ %.2f'%Z)
    elif X == 5 :
        Z = Y*1.50
        print('Total: R$ %.2f'%Z)
main()
