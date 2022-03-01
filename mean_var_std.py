import numpy as np
def calculate(input):
    if len(input) != 9:
        raise ValueError("List must contain nine numbers.")
    # create numpy array & reshape to 3x3
    a = np.array(input).reshape(3,3)

    cal = dict()
    cal['mean'] = [a.mean(0).tolist(), a.mean(1).tolist(), a.mean()]
    cal['variance'] = [a.var(0).tolist(), a.var(1).tolist(), a.var()]
    cal['standard deviation'] = [a.std(0).tolist(), a.std(1).tolist(), a.std()]
    cal['max'] = [a.max(0).tolist(), a.max(1).tolist(), a.max()]
    cal['min'] = [a.min(0).tolist(), a.min(1).tolist(), a.min()]
    cal['sum'] = [a.sum(0).tolist(), a.sum(1).tolist(), a.sum()]
    return cal


#print(calculate([0,1,2,3,4,5,6,7,8]))
#print(calculate([9,1,5,3,3,3,2,9,0]))
