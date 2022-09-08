def main():
    x , y = input().split()
    x , y = int(x) , int(y)
    if (x % y == 0 or y % x == 0):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
main()
