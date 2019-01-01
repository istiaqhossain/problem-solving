def main():
    amount = float(input())

    if amount >= 0 and amount <= 1000000.00:
    
        amount = float('%.2f'%amount)
        hundred = int(amount/100)
        amount = amount%100

        amount = float('%.2f'%amount)
        fifty = int(amount/50)
        amount = amount%50

        amount = float('%.2f'%amount)
        twenty = int(amount/20)
        amount = amount%20

        amount = float('%.2f'%amount)
        ten = int(amount/10)
        amount = amount%10

        amount = float('%.2f'%amount)
        five = int(amount/5)
        amount = amount%5

        amount = float('%.2f'%amount)
        two = int(amount/2)
        amount = amount%2

        amount = float('%.2f'%amount)
        one = int(amount/1)
        amount = amount%1

        amount = float('%.2f'%amount)
        point_fify = int(amount/0.5)
        amount = amount%0.5

        amount = float('%.2f'%amount)
        point_twenty_five = int(amount/0.25)
        amount = amount%0.25

        amount = float('%.2f'%amount)
        point_ten = int(amount/0.10)
        amount = amount%0.10

        amount = float('%.2f'%amount)
        point_zero_five = int(amount/0.05)
        amount = amount%0.05

        amount = float('%.2f'%amount)
        point_zero_one = int(amount/0.01)
        amount = amount%0.01
        
        print('NOTAS:')
        print(hundred,'nota(s) de R$ 100.00')
        print(fifty,'nota(s) de R$ 50.00')
        print(twenty,'nota(s) de R$ 20.00')
        print(ten,'nota(s) de R$ 10.00')
        print(five,'nota(s) de R$ 5.00')
        print(two,'nota(s) de R$ 2.00')
        print('MOEDAS:')
        print(one,'moeda(s) de R$ 1.00')
        print(point_fify,'moeda(s) de R$ 0.50')
        print(point_twenty_five,'moeda(s) de R$ 0.25')
        print(point_ten,'moeda(s) de R$ 0.10')
        print(point_zero_five,'moeda(s) de R$ 0.05')
        print(point_zero_one,'moeda(s) de R$ 0.01')
main()
