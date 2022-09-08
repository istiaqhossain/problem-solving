def main():
    count,total = 0,0
    for x in range(6):
        n = float(input())
        if n >= 0:
            count += 1
            total += n
    avg = total / count
    print('%d valores positivos'%count)
    print('%.1f'%avg)
main()
