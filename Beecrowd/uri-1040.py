def main():
    N1,N2,N3,N4 = input().split()
    N1 = float(N1)*2
    N2 = float(N2)*3
    N3 = float(N3)*4
    N4 = float(N4)*1
    AVERAGE = (N1+N2+N3+N4)/10
    print('Media: %.1f'%AVERAGE)
    if AVERAGE >= 7 :
        print('Aluno aprovado.')
    elif AVERAGE < 5 :
        print('Aluno reprovado.')
    elif AVERAGE >= 5 and AVERAGE <= 6.9 :
        print('Aluno em exame.')
        EXAM = float(input())
        print('Nota do exame: %.1f'%EXAM)
        FINAL = (AVERAGE + EXAM)/2
        if FINAL >= 5 :
            print('Aluno aprovado.')
            print('Media final: %.1f'%FINAL)
        elif FINAL < 5 :
            print('Aluno reprovado.')
            print('Media final: %.1f'%FINAL)
main()
