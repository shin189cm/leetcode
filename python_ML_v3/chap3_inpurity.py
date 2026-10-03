import matplotlib.pyplot as plt
import numpy as np

def gini_impurity(y: np.ndarray) -> float:
    if len(y) == 0:
        return 0.0
    
    _, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    return 1.0 - np.sum(probs ** 2)

def entropy(y: np.ndarray) -> float:
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    # 0は対数をとるとマイナス無限大に発散するため防ぐ
    probs = probs[probs > 0]
    return -np.sum(probs * np.log2(probs))
    
def best_split(
    x: np.ndarray, 
    y: np.ndarray, 
    criterion = entropy
    ):
    n = len(y)
    if n <= 1:
        return None, 0.0
    
    current_impurity = criterion(y)
    order = np.argsort(x)
    x_sort, y_sort = x[order], y[order]
    
    best_gain  = 0.0
    best_threshold = None
    
    for i in range(1, n):
        if x_sort[i] == x_sort[i-1]:
            continue
        
        threshold = (x_sort[i] + x_sort[i-1]) / 2.0
        y_left, y_right = y_sort[:i], y_sort[i:]
        
        w_left = i / n
        w_right = (n - i) / n
        gain = (
            current_impurity
            - (w_left * criterion(y_left)
            + w_right * criterion(y_right))
        )
        
        if gain > best_gain:
            best_gain = gain
            best_threshold = threshold
            
    return best_threshold, best_gain

# 配列を生成
x = np.arange(0.0, 1.0, 0.01)
y = np.digitize(x, [0.25, 0.5, 0.75])

res1, res2 = best_split(x, y)
print("best_threshold is: ", res1, "\nbest_gain is: ", res2)