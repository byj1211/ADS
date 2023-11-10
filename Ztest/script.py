data = []

with open('usbdata.txt', 'r') as file:
    s = ''
    for line in file:
        number = int(line.strip())
        if number == 200:
            if s != '':
                data.append(s)
                s = ''
        else:
            s = s + str(number)[-1]


result = ''
for d in data:
    d = int(d, 4)
    d = chr(d)
    result = result + d

print(result)
