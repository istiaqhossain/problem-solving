def main():
    l1 = [int(x) for x in input().split()]
    l2 = sorted(l1)
    for i in l2:
        print(i)
    print()
    for i in l1:
        print(i)
main()
