def main():
    l = [float(x) for x in input().split()]
    l.sort(reverse=True)
    A , B , C = l[0] , l[1] , l[2]
    if (A >= B + C):
        print('NAO FORMA TRIANGULO')
    elif (A*A == B*B + C*C):
        print('TRIANGULO RETANGULO')
    elif (A*A > B*B + C*C):
        print('TRIANGULO OBTUSANGULO')
    elif (A*A < B*B + C*C):
        print('TRIANGULO ACUTANGULO')

    if (A == B == C):
        print('TRIANGULO EQUILATERO')
    elif (A == B or A == C or B == C):
        print('TRIANGULO ISOSCELES')
main()
