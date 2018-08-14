import numpy as np


def convert_mins_to_decimal(time):
    """
    Convert minutes in time to decimal notation.
    
    Args: time (str): time given in hrs:mins
    Returns: decimal (float): time given in hrs.mins/60*100
    """
    time_split = time.split(':')
    hrs = time_split[0]
    mins = int(time_split[1])
    percent = int((mins/60)*100)
    decimal = float('{}.{}'.format(str(hrs),str(percent)))
    return(decimal)


def fit_exp(t, r):
    """
    Fit data to an exponential distribution
    
    Args: t (float): observed time to complete task
    Args: r (float): rate parameter, how fast a task is finished
    """
    return r * np.exp(-r * t) #this is an exponential distribution, but it could be anything
