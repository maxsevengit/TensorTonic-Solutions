import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)

    if len(x) != len(p):
        raise ValueError

    if not np.isclose(np.sum(p), 1):
        raise ValueError
        
    result =  np.sum(x*p)  
    return result
    # if(result > 1):
    #     return "ValueError"
