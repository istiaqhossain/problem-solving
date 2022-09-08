def main():
    days = int(input())
    years = int(days/365)
    days = days%365
    months = int(days/30)
    days = days%30
    print(years,'ano(s)')
    print(months,'mes(es)')
    print(days,'dia(s)')
main()
