import numpy

def get_diag(matrix, x):
    #enum over matrix to get index and row of matrix
    #enum over row to get index and elemnt of row 
    #try to store each diagonal as different elemnt
    #multiply elemnt at end to get sum
    
    num = []
    s = 1
    for i, row in enumerate(matrix):
        for n, el in enumerate(row):
            if i == n + x:
                num.append([el])
    num[0] = numpy.prod(num)
    del num[s:]
    return num

def get_reverse_diags(matrix, b):
    #does the same thing as other function but reversed
    num2 = []
    s = 1
    for i, row in enumerate(matrix):
        for n, el in enumerate(row[::-1]):
            if i == n + b:
                num2.append([el])
    num2[0] = numpy.prod(num2)
    del num2[s:]
    return num2

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

def sum_prod_diags(matrix):
    sum1 = []
    sum2 = []
    x = len(matrix) - 1
    b = len(matrix) - 1
    #loops over the other functions to get diags in one array
    
    while len(sum1) < 2 * len(matrix) - 1:
        sum1.append(get_diag(matrix, x))
        x -= 1
    while len(sum2) < 2 * len(matrix) - 1:
        sum2.append(get_reverse_diags(matrix, b))
        b -= 1
#             n += 1
#             if i == n:
#                 sum1.append(el)
    sum1 = flatten_list(sum1)
    sum2 = flatten_list(sum2)
    return sum(sum1) - sum(sum2)
