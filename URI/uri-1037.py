def main():
    I = float(input())
    if I < 0 or I > 100 :
        print('Fora de intervalo')
    else :
        if I >= 0 and I <= 25 :
            print('Intervalo [0,25]')
        elif I > 25 and I <= 50 :
            print('Intervalo (25,50]')
        elif I > 50 and I <= 75 :
            print('Intervalo (50,75]')
        elif I > 75 and I <= 100 :
            print('Intervalo (75,100]')
main()
