import numpy as np

def random_predict(number:int = 1) -> int:
    """ Trying to guess a number

    Args:
        number (int, optional): given number. Defaults to 1.

    Returns:
        int: Trial number
    """
    count = 0
    while True:
        count = count + 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
        
    return count

def score_game(random_predict) -> int:
    """Average number of right guesses in 1000 trials 

    Args:
        random_predict (_type_): function to guess the number

    Returns:
        int: anerage number of trials
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = (1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Your algorithm finds the right number in {score} trials in average.')
    return score

if __name__ == '__main__':
    score_game(random_predict)