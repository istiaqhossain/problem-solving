def main():
    cpf = input()
    x = cpf.split('.')
    print(x[0])
    print(x[1])
    x = x[2].split('-')
    print(x[0])
    print(x[1])
main()
