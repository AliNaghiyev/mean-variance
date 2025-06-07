import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    array = np.array(list).reshape(3, 3)
    
    calculations = {
        'mean': [list(array.mean(axis=0)), list(array.mean(axis=1)), array.mean().item()],
        'variance': [list(array.var(axis=0)), list(array.var(axis=1)), array.var().item()],
        'standard deviation': [list(array.std(axis=0)), list(array.std(axis=1)), array.std().item()],
        'max': [list(array.max(axis=0)), list(array.max(axis=1)), array.max().item()],
        'min': [list(array.min(axis=0)), list(array.min(axis=1)), array.min().item()],
        'sum': [list(array.sum(axis=0)), list(array.sum(axis=1)), array.sum().item()]
    }

    return calculations
