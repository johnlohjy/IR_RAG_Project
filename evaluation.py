import numpy as np

def precision_at_k(r,k):
    r = r[:k]
    return np.mean(r)

def average_precision(r):
    num = 0
    den = 0
    for i in range(len(r)):
        if r[i]:
            num+=precision_at_k(r,i+1)
            den+=1
    if den==0: 
        return 0
    avg_p = num/den
    return avg_p

def mean_average_precision(rs):
    num = 0
    den = 0
    for r in rs:
        num+=average_precision(r)
        den+=1
    m_avg_p = num/den
    return m_avg_p

def reciprocal_rank(r):
    for i,v in enumerate(r):
        if v==1:
            return 1/(i+1)
    return 0

def mean_reciprocal_rank(rs):
    num = 0
    den = 0

    for r in rs:
        num+=reciprocal_rank(r)
        den+=1

    m_rec_r = num/den
    return m_rec_r