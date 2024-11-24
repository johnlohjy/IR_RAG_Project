import numpy as np
import math

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

def dcg_at_k(r, k):
    if k > len(r):
         k = len(r)
    dcg = 0
    for rank in range(1,k+1):
        dcg += r[rank-1]/math.log(rank+1,2)
    return dcg

def ndcg_at_k(r, k):
    r_sorted = sorted(r,reverse=True)
    dcg = dcg_at_k(r, k)
    idcg = dcg_at_k(r_sorted, k)
    if idcg==0:
        return 0
    return dcg/idcg