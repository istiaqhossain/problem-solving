def main():
    str1 = input()
    str2 = input()
    str3 = input()
    if (str1 == 'vertebrado' and str2 == 'ave' and str3 == 'carnivoro'):
        print('aguia')
    elif (str1 == 'vertebrado' and str2 == 'ave' and str3 == 'onivoro'):
        print('pomba')
    elif (str1 == 'vertebrado' and str2 == 'mamifero' and str3 == 'onivoro'):
        print('homem')
    elif (str1 == 'vertebrado' and str2 == 'mamifero' and str3 == 'herbivoro'):
        print('vaca')
    elif (str1 == 'invertebrado' and str2 == 'inseto' and str3 == 'hematofago'):
        print('pulga')
    elif (str1 == 'invertebrado' and str2 == 'inseto' and str3 == 'herbivoro'):
        print('lagarta')
    elif (str1 == 'invertebrado' and str2 == 'anelideo' and str3 == 'hematofago'):
        print('sanguessuga')
    elif (str1 == 'invertebrado' and str2 == 'anelideo' and str3 == 'onivoro'):
        print('minhoca')
main()
