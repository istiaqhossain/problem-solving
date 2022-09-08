def main():
    salary = float(input())
    tax = 0
    if salary <= 2000.00:
        print('Isento')
    else:
        salary -= 2000.00
        if salary > 1000.00:
            salary -= 1000.00
            tax += 1000*.08
            if salary > 1500.00:
                salary -= 1500.00
                tax += 1500*.18
                if salary > 00.00:
                    tax += salary*.28
            else:
                tax += salary*.18
        else:
            tax += salary*.08
        print('R$ %.2f'%tax)
main()
