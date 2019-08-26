def main():
    count = 0
    for x in range(5):
        n = int(input())
        if n % 2 == 0:
            count += 1
    print('%d valores pares'%count)
main()
