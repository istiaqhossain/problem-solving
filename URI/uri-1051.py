def main():
    salary = float(input())
    if salary <= 2000.00:
        print('Isento')
    else:
        salary -= 2000.00
        print(salary)
main()
