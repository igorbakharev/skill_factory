import numpy as np

def random_predict(number:int = 1) -> int:
    """ A function that returns the number of attempts to guess a number from 1 to 100

    Args:
        number (int, optional): given number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    predict_number = 50
    lower_bound = 0
    upper_bound = 100

    while True:
        count = count + 1
        if number == predict_number:
            break
        if number < predict_number:
            upper_bound = predict_number
        if number > predict_number:
            lower_bound = predict_number
        predict_number = int(round((lower_bound + upper_bound) / 2))
    
    return count


def score_game(random_predict) -> int:
    """Average number of guesses in 1000 attempts 

    Args:
        random_predict (_type_): function that guesses the number and return the number of attempts

    Returns:
        int: anerage number of attempts
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