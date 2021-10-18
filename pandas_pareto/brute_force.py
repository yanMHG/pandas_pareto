import pandas as pd

def _df_i_dominates_j(df, i, j, comp_better, comp_worse):
    """
    Verifies if the row with index `i` dominates the row with index `j` in the
    `pandas.DataFrame` object `df` using a brute-force method.

    Parameters
    ----------
    df : `pandas.DataFrame`

    i : integer row index

    j : integer row index

    comp_better : callable
        In a minimization problem, `comp_better(x,y) <=> x < y`. In a
        maximization problem, `comp_better(x,y) <=> x > y`.

    comp_worse : callable
        In a minimization problem, `comp_better(x,y) <=> x > y`. In a
        maximization problem, `comp_better(x,y) <=> x < y`.

    Returns
    -------
    True or False.
    """
    row_i = df.iloc[i]
    row_j = df.iloc[j]
    equal = True
    for f_ki, f_kj in zip(row_i, row_j):
        if comp_worse(f_ki, f_kj):
            return False
        if equal and comp_better(f_ki, f_kj):
            equal = False
    return not(equal)


def pareto(df, comp_better, comp_worse):
    """
    Returns the indexes of a `pandas.DataFrame` that are Pareto optimal in terms
    of minimizing/maximizing the columns using the brute-force method.

    The data entries must be of a type that implements the `__lt__` and `__gt__`
    operations (`<` and `>`, respectively). A pair of entries is assumed to be equal
    if the first is neither less than nor greater than the second.


    Parameters
    ----------
    df : `pandas.DataFrame`

    comp_better : callable
        In a minimization problem, `comp_better(x,y) <=> x < y`. In a
        maximization problem, `comp_better(x,y) <=> x > y`.

    comp_worse : callable
        In a minimization problem, `comp_better(x,y) <=> x > y`. In a
        maximization problem, `comp_better(x,y) <=> x < y`.

    Returns
    -------
    List of index entries corresponding to the rows that are Pareto
    optimal.
    """
    index_list = []
    nrows = len(df.index)
    for i in range(nrows):
        nondominated = True
        for j in range(nrows):
            # Note that i and j are swapped in the arguments; we want to verify
            # whether j dominates i.
            if _df_i_dominates_j(df, j, i, comp_better, comp_worse):
                nondominated = False
                break
        if nondominated:
            index_list.append(df.index[i])
    return index_list
