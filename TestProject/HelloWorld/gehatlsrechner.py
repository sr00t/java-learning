pay_hourly = input('give your hourly pay: ') # per €
day = 8 * int(pay_hourly)
week = 5 * day
month = 20 * day
year = 12 * month
print('Your salary per day is: ' + str(day) + '€')
print('Your salary per week is:' + str(week) + '€')
print('your salary per month is:' + str(month) + '€')
print('Your salary per year is: ' + str(year) + '€')