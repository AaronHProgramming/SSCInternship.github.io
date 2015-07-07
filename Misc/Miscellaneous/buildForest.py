__author__ = 'a-aron'

def random_clump_matrix(size, time):
    """

    :param size: size of the plane the clump will grow on
    :param time: number of iterations of clump growth
    :return: matrix where ones represent where the clump is and zeros where it is not
    """
    def create_growth(matrix):
        lst = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0),(-1, -1), (0, -1), (1, -1),]
        growth_matrix = np.full((size+2, size+2), 0)
        for row in range(1, size+1):
            for col in range(1, size+1):
                num = 0
                if matrix[row][col] == 0:
                    for tup in lst:
                        if matrix[row+tup[0]][col+tup[1]] == 1:
                            num += 1
                    if np.random.uniform(0, 1, 1) < num * .07:
                        growth_matrix[row][col] = 1
        # Add the manipulated array to the old one to get the new clump
        return growth_matrix

    # matrix of zeros
    matrix = np.full((size+2, size+2), 0)
    # randomize where clump originates
    # What if start is outside the boundary?
    rand_row = np.random.choice(range(1, size))
    rand_col = np.random.choice(range(1, size))
    # If want to test with start in center
    rand_row = rand_col = size / 2
    matrix[rand_row][rand_col] = 1
    # simulate growth
    for x in xrange(20):
        mini_matrix = np.full((size+2, size+2), 0)
        mini_matrix[rand_row][rand_col] = 1
        # pool = Pool()
        # mini_matrix = pool.map(create_growth, mini_matrix).get(60)
        # print mini_matrix

        for time_unit in xrange(time):
            # Add the manipulated array to the old one to get the new clump
            mini_matrix += create_growth(mini_matrix)
            # print matrix

        matrix += mini_matrix
    matrix[rand_row][rand_col] = 0
    return matrix

if __name__ == "__main__":
    from multiprocessing import Pool
    import numpy as np
    #%matplotlib inline
    import matplotlib.pyplot as plt
    graph_dim, growth_time = 20, 24
    plt.matshow(random_clump_matrix(graph_dim, growth_time)[1:-1, 1:-1], cmap='Greens')
    plt.show()
    # print random_clump_matrix(graph_dim, growth_time)[1:-1, 1:-1] # eliminate the edges
    map(lambda x: x, [1])