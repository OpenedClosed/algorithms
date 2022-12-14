"""
Метеорологическая служба вашего города решила исследовать погоду новым способом.
Под температурой воздуха в конкретный день будем понимать максимальную температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней, в которые температура строго больше,
чем в день до (если такой существует) и в день после текущего (если такой существует).
Например, если за 5 дней максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов,
то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот период.
Заметим, что если число показаний n=1, то единственный день будет хаотичным.
"""
amount_of_days = int(input())
days = list(map(int, input().split()[:amount_of_days]))
counter = 0
if (len(days) == 1):
    counter = 1
if (len(days) != 1):
    if (days[0] > days[1]):
        counter += 1
    if (days[-1] > days[-2]):
        counter += 1
i = 1
while i < len(days) - 1:
    if days[i] > days[i + 1] and days[i] > days[i - 1]:
        counter += 1
        i += 1
    i += 1
print(counter)