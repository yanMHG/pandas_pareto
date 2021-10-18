import pandas as pd
import sys
from .brute_force import pareto as bf_pareto

def compute_pareto(df, method='brute_force', opt_type='minimization'):
    """
    Returns the indexes of a `pandas.DataFrame` that are Pareto optimal in terms
    of minimizing/maximizing the columns.

    The data entries must be of a type that implements the `__lt__` and `__gt__`
    operations (`<` and `>`, respectively). A pair of entries is assumed to be equal
    if the first is neither less than nor greater than the second.

    Parameters
    ----------
    df : `pandas.DataFrame`

    method : {'brute_force'}, default: 'brute_force'
        Method used to estimate the Pareto front. So far, only 'brute_force' is
        supported.

    opt_type: {'minimization', 'maximization'}, default: 'minimization'
        Type of optimization problem.

    Returns
    -------
    List of index entries corresponding to the rows that are Pareto
    optimal.
    """
    ...
    if opt_type == 'minimization':
        comp_better = lambda x, y: x < y
        comp_worse  = lambda x, y: x > y
    elif opt_type == 'maximization':
        comp_better = lambda x, y: x > y
        comp_worse  = lambda x, y: x < y
    else:
        sys.exit(f"Unknow optimization type \"{opt_type}\".")

    if method == 'brute_force':
        print("Starting brute-force Pareto... This may take a while.")
        return bf_pareto(df, comp_better, comp_worse)
    else:
        sys.exit(f"Unknow method \"{method}\".")

