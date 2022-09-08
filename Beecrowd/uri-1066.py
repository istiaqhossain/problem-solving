def main():
    even,odd,positive,negetive = 0,0,0,0
    for x in range(5):
        n = int(input())

        if n % 2 == 0:
            even += 1
        else:
            odd += 1

        if n > 0:
            positive += 1

        if n < 0:
            negetive += 1
    print('%d valor(es) par(es)'%even)
    print('%d valor(es) impar(es)'%odd)
    print('%d valor(es) positivo(s)'%positive)
    print('%d valor(es) negativo(s)'%negetive)
main()
