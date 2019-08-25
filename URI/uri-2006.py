def main():
    count = 0
    T = int(input())
    A,B,C,D,E = [int(x) for x in input().split()]
    if T == A:
        count += 1
    if T == B:
        count += 1
    if T == C:
        count += 1
    if T == D:
        count += 1
    if T == E:
        count += 1
    print(count)
main()
