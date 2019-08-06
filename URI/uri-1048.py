def main():
    salary = float(input())
    new_salary,increment = 0.00 , 0.00
    percentage = '15 %'
    if (salary > 0 and salary <= 400.00):
        increment = salary * 0.15
        new_salary = salary + increment
        percentage = '15 %'
    elif (salary > 400.00 and salary <= 800.00):
        increment = salary * 0.12
        new_salary = salary + increment
        percentage = '12 %'
    elif (salary > 800.00 and salary <= 1200.00):
        increment = salary * 0.10
        new_salary = salary + increment
        percentage = '10 %'
    elif (salary > 1200.00 and salary <= 2000.00):
        increment = salary * 0.07
        new_salary = salary + increment
        percentage = '7 %'
    elif (salary > 2000.00):
        increment = salary * 0.04
        new_salary = salary + increment
        percentage = '4 %'

    print('Novo salario: %.2f'%new_salary)
    print('Reajuste ganho: %.2f'%increment)
    print('Em percentual: %s'%percentage)
main()
