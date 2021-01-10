def isMagicDate(date, month, year):
    dayTimesMonth = date * month
    if dayTimesMonth == year%100:
            print("True")
    else:
        print("False")
    return None
date,month,year=map(int,input().split())
isMagicDate(date,month,year)
