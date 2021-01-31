firm_dict = {}
profit = {}
pr = {}
prof = 0
profit_average = 0
i = 0

with open('test-4.txt', 'r') as my_file:
    for line in my_file:

        line_another_split = line.split(' ')
        line_another_split[3:] = line_another_split.strip()
        profit = int(line_another_split[2:]) - int(line_another_split[3:])
        if profit >= 0:
            prof = prof + profit
            i += 1
        if i != 0:
            prof_aver = prof / i
            print(f'{prof_aver:.2f}')
        else:
            print(f'Прибыли нет - убыток')





