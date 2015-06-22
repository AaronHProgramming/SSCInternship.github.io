__author__ = 'aaron'

def dot_product(v, w):
    """

    :param v:
    :param w:
    :return:
    >>> v = [1, 3]
    >>> w = [5, 1]
    >>> print(dot_product(v, w))
    8
    """

    if len(v) != len(w):
        val_str = "Size of vector 1={}, size of vector 2={}".format(len(v), len(w))
        raise ValueError(val_str)
    dot_prod = 0
    for i, val in enumerate(v):
        dot_prod += val * w[i]
    return dot_prod

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    v1 = [1, 3]
    v2 = [5, 1]
    print(dot_product(v1, v2))
