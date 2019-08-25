def main():
    count = 0
    for x in range(6):
        n = float(input())
        if n >= 0:
            count += 1
    print('%d valores positivos'%count)
main()
