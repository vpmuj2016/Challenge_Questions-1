# Student grade based on the percentage

Sub1 = 90
Sub2 = 82
Sub3 = 78
Sub4 = 66
Sub5 = 95

Total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
perc1 = (Total/500*100)
perc = round(perc1, 2)
print('Percentage :', perc, '%')
print('Total Marks :', Total, '/500')

if perc >= 90 and perc <= 100:
    print('Grade :', 'A+')
elif perc >= 80 and perc <= 89:
    print('Grade :', 'A')
elif perc >= 70 and perc <= 79:
    print('Grade :', 'B')
elif perc >= 60 and perc <= 69:
    print('Grade :', 'C')
elif perc >= 50 and perc <= 59:
    print('Grade :', 'C')
else:
    print('Grade :', 'F')


