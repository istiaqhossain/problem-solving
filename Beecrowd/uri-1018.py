def main():
    amount = int(input())
    print(amount)

    hundred = int(amount/100)
    amount = amount%100

    fifty = int(amount/50)
    amount = amount%50

    twenty = int(amount/20)
    amount = amount%20

    ten = int(amount/10)
    amount = amount%10

    five = int(amount/5)
    amount = amount%5

    two = int(amount/2)
    amount = amount%2

    one = int(amount/1)
    amount = amount%1

    print(hundred,'nota(s) de R$ 100,00')
    print(fifty,'nota(s) de R$ 50,00')
    print(twenty,'nota(s) de R$ 20,00')
    print(ten,'nota(s) de R$ 10,00')
    print(five,'nota(s) de R$ 5,00')
    print(two,'nota(s) de R$ 2,00')
    print(one,'nota(s) de R$ 1,00')
main()
