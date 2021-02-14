import numpy as np
from skbio.stats.composition import closure, alr_inv


def sim1(seed=0):
    np.random.seed(seed)
    p1 = np.array([1/5, 1/5, 3/5])
    p2 = np.array([1/3, 1/3, 1/3])

    x1 = np.random.multinomial(60, p1, size=1000)
    x2 = np.random.multinomial(90, p2, size=1000)
    x = np.vstack((closure(x1), closure(x2)))
    y = np.array([0] * len(x1) + [1] * len(x2))
    return x, y.astype(np.bool)

def sim1_truth(seed=0):
    np.random.seed(seed)
    p1 = np.array([1/5, 1/5, 3/5])
    p2 = np.array([1/3, 1/3, 1/3])
    x1 = np.random.multinomial(60, p1, size=1000)
    x2 = np.random.multinomial(90, p2, size=1000)
    n1, n2 = 3, 5
    x = np.vstack((closure(x1) * n1, closure(x2) * n2))
    y = np.array([0] * len(x1) + [1] * len(x2))
    return x, y.astype(np.bool)

def sim2():
    n = 100
    eps = np.random.randn(n)
    t = np.linspace(-10, 10, n)
    x1 = 0.5 - 1 * t + 0.3 * np.random.randn(n)
    x2 = 0.5 - 0.5 * t + 0.3 * np.random.randn(n)
    x = np.vstack((x2, x1)).T
    return alr_inv(x), t

