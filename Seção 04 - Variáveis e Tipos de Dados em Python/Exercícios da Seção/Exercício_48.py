seconds = int(input('Enter the value in seconds: '))
hours = seconds // 3600
minutes = (seconds - (hours * 3600)) // 60
seconds_1 = seconds - (hours * 3600 + minutes * 60)
print('The inserted second {} stay like {} hours {} minutes and {} seconds!'.format(seconds, hours, minutes, seconds_1))
