from numpy import number

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