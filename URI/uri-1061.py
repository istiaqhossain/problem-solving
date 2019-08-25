def main():
    day, hour, minute, second = 0,0,0,0
    start_date = int(input().split()[1])
    start_time = [int(x) for x in input().split(' : ')]
    end_date = int(input().split()[1])
    end_time = [int(x) for x in input().split(' : ')]

    if end_time[2] < start_time[2]:
       end_time[2] += 60
       if end_time[1] > 1:
           end_time[1] -= 1

    second =  end_time[2] - start_time[2]

    
    if end_time[1] < start_time[1]:
       end_time[1] += 60
       if end_time[0] > 1:
           end_time[0] -= 1

    minute =  end_time[1] - start_time[1]

    if end_time[0] < start_time[0]:
       end_time[0] += 24
       if end_date > 1:
           end_date -= 1

    hour =  end_time[0] - start_time[0]

    if end_date < start_date:
       end_date += 30

    day =  end_date - start_date
    
    print('%d dia(s)'%day)
    print('%d hora(s)'%hour)
    print('%d minuto(s)'%minute)
    print('%d segundo(s)'%second)
main()
