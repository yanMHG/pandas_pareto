# About

`pandas_pareto` is a small package to estimate a Pareto front based on
discrete samples of a multidimensional objective function. The
objective function is represented as a pandas.DataFrame object with
samples as rows and the values of each component of the function as
columns.

The central module of the package is `pandas_pareto.pareto`, and the
central function therein is `compute_pareto`. It receives the
DataFrame of function samples as input and returns a list of index
entries of the rows representing samples that are Pareto optimal. The
function usage is documented in the source files.

# Usage

To use `pandas_pareto`, copy the package directory into your project
and use:

	from pandas_pareto.pareto import compute_pareto


# Tips

- The list of index entries returned by
  `pandas_pareto.pareto.compute_pareto` can be used to filter the
  original data as the argument of `loc`.
