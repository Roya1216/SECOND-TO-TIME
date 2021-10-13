print('Enter the second and convert it to times')
print("please enter your desired seconds:")
sec = int(input('seconds= '))
hour = sec // 3600
minute = (sec - 3600 * hour) // 60
second = (sec - 3600 *hour) - 60 * minute
print("time= ", hour,':', minute,':', second )