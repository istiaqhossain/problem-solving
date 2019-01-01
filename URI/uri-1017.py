def main():
    hours = int(input())
    km_h = int(input())
    liters = (km_h / 12) * hours
    print('%.3f'%liters)
main()
