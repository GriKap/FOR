list_ = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
for i in list_:
    print('Я езжу на машине', i)

cars_count = 0
for i in list_[2]:
    j = cars_count
    for j in range(10):
        print(f'{i} x {j} = {j * i}')

