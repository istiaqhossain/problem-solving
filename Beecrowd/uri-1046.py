def main():
    s,e = input().split()
    s,e = int(s),int(e)
    if (s > e or s == e):
        e = e + 24
        h = e - s
    else:
        h = e - s
    print('O JOGO DUROU %d HORA(S)'%h)
main()
