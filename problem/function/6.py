# quiz 3

def check_date(month,d,year):
  if 1 <= month <= 12 and year > 0:
    if month==4 or month==6 or month==9 or month==11:
        days=30
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12: 
        days=31 
    elif month==2 and (year%4==0 and (year%100)!=0) or year%400==0: 
        days=29 
    elif month==2 and ((year%400)!=0 or (year%100==0 and year%4!=0)): 
        days=28
  else: 
    days = 0

  return 0<d<=days

valid = check_date(2,30,2024)
print(valid)
