# Написание функции медианы без библиотек
def median(sample):
    prep = sorted(sample)
    if len(prep) % 2 == 1:
        return prep[len(sample) // 2]
    else:
        return (prep[len(sample) // 2] + prep[len(sample) // 2 + 1]) / 2

print(median([7, 1, 5, 0, 10, 9, 14]))