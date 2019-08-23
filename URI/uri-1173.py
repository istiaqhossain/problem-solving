def main():
    i = int(input())
    print('N[0] = %d'%i)
    for x in range(1,10):
        i = i + i
        print('N[%d] = %d'%(x,i))
main()
