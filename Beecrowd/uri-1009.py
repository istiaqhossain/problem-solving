def main():
    SELLER = input()
    SALARY = float(input())
    SALE = float(input())
    TOTAL = SALARY + ((SALE/100)*15)
    print('TOTAL = R$ %.2f'%TOTAL)
main()
