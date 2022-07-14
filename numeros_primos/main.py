# Gerador de números primos


def primos(x, y):
    num = []

    for i in range(x, y):
        if i == 1:
            continue
        if i == 2 or i == 3 or i==5 or i==7:
            num.append(i)
        if i % 2 != 0:
            if i % 3 != 0:
                if i % 5 != 0:
                    if i % 7 != 0:
                        num.append(i)

    return num


interval1 = int(input('Digite o início do intervalo: '))
interval2 = int(input('Digite o final do intevalo: '))

result = primos(interval1, interval2)

for item in result:
    print(item)



