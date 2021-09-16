import torch
import numpy as np
# import scipy as sp


def dotdot_a_b_aT_for_row_in_a(a, b):
    '''function to calculate row wize dot(dot(a,b),aT) where aT==a.T as in
        tmpval=[]
        for q in range(len(a)):
            tmpval.append( np.dot(np.dot(a[q, :], b), aT[:,q]))
        return np.array(tmpval)

      '''
    if torch.is_tensor(a) and torch.is_tensor(b):
        return torch.einsum('ij,ji->i', torch.einsum('ij,jk', a, b), a.T)
    else:
        return np.einsum('ij,ji->i', np.einsum('ij,jk', a, b), np.array(a).T)
    # return np.einsum('ij,jk,ik->i', a,b,a)


def dotdot_a_b_aT(a, b):
    '''function to calculate row wize dot(dot(a,b),aT) for all combinations
        of rows in a and cols in aT as in:

        tmpval=[]
        for q in range(len(a)):
            for qq in range(len(a))
                tmpval.append( np.dot(np.dot(a[q, :], b), aT[:,qq]))
        return np.array(tmpval)

    '''
    if torch.is_tensor(a) and torch.is_tensor(b):
        return torch.einsum('ij,jk', torch.einsum('ij,jk', a, b), a.T)
    else:
        return np.einsum('ij,jk', np.einsum('ij,jk', a, b), np.array(a).T)


def AL_McKay92_idx(gp_std_at_lhs, nNew=1):
    '''Active learning by McKay 1992
    Return index of nNew point with highest standard deviation

    '''
    std = gp_std_at_lhs

    # ELD TODO: need test on size of std/lhs to be a meaningful sample size?

    idx = np.argpartition(std, -nNew)[-nNew:]
    idx = idx[np.argsort(-std[idx])]
    Timp = std[idx]

    return idx, Timp


def AL_Cohn96_idx(kernel_fn, X_train, X_lhs, nNew=1):
    '''Active learning by Cohn 1996
    Return index of nNew points which gives the largest global variance reduction

    '''

    n_train = len(X_train)
    n_lhs = len(X_lhs)

    # ELD TODO: need test on size of std/lhs to be a meaningful sample size?

    X_all = np.vstack([X_train, X_lhs])  # OK

    C_allx = kernel_fn(X_all)  # OK
    C_train = kernel_fn(X_train)  # OK
    C_lhs = kernel_fn(X_lhs)  # OK

    Cinv = np.linalg.inv(C_train)  # OK
    Cstar = C_allx[n_train:, :n_train]  # OK

    kstKkst = dotdot_a_b_aT_for_row_in_a(Cstar, C_train)  # OK

    tmpT = dotdot_a_b_aT(Cstar, Cinv) - C_lhs

    T_ALCs = np.einsum('ij,i->i', tmpT, 1/(C_lhs.diagonal()-kstKkst))

    idx = np.argpartition(T_ALCs, -nNew)[-nNew:]
    idx = idx[np.argsort(-T_ALCs[idx])]
    Timp = [(T_ALCs[q])/np.float(n_lhs) for q in idx]

    return idx, Timp  # , T_ALCs
