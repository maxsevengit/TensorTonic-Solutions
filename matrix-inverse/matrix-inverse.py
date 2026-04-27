import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    if np.linalg.det(A) != 0:
        inv = np.linalg.inv(A)
    else:
        return None

    return inv