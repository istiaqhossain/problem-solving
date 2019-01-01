def main():
    MaiorAB , MaiorAC = 0 , 0
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    MaiorAB = (a + b + abs(a-b))/2
    MaiorAC = (MaiorAB + c + abs(MaiorAB-c))/2
    print('%d eh o maior'%MaiorAC)
main()
