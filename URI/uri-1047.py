def main():
    init_hour,init_minute,fin_hour,fin_minute = [int(x) for x in input().split()]
    hour,minute = 0,0
    
    if fin_hour <= init_hour:
        hour = (fin_hour + 24) - init_hour
    else:
        hour = fin_hour - init_hour

    if fin_minute < init_minute:
        minute = (fin_minute + 60) - init_minute
        hour -= 1
    else: 
        minute = fin_minute - init_minute
    
    print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)'%(hour,minute))
main()
