from itertools import count
import numpy as np
number = np.random.randint(1, 100)
count = 0
while True:
    count = count + 1
    predict_number = int(input('Enter a number from 1 to 100: '))
    if predict_number > number:
        print('It is less.')
    elif predict_number < number:
        print('It is bigger.')
    else:
        print(f'You got it! This number is {number}, trial number is {count}.')
        break